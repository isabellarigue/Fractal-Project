import matplotlib.pyplot as plt
import numpy as np
import numba


@numba.jit(nopython=True)
def suite(z,c)-> complex:
    """
    Générateur des éléments de la suite z_{n+1} = z_n^2 + c.

    Parameters
    ----------
    z : complex
        Le point complexe initial.
    c : complex
        La constante utilisée pour générer la suite.

    Yields
    ------
    complex
        Les éléments successifs de la suite.
    """
    while True:
        yield z
        z = z ** 2 + c

@numba.jit(nopython=True)
def suite_mandelbrot(c, z=0)-> complex:
    """
    Renvoie la suite de Mandelbrot.

    Parameters
    ----------
    c : complex
        Le paramètre complexe utilisé pour générer la suite de Mandelbrot.
    z : complex, optional
        Le point complexe initial, par défaut 0.

    Returns
    -------
    generator
        Un générateur d'éléments de la suite de Mandelbrot.
    """
    return suite(z,c)

@numba.jit(nopython=True)
def suite_julia(z, c)-> complex:
    """
    Renvoie la suite de Julia pour un candidat et un paramètre donnés.

    Parameters
    ----------
    z : complex
        Le point complexe initial.
    c : complex
        Le paramètre complexe utilisé pour générer la suite de Julia.

    Returns
    -------
    generator
        Un générateur d'éléments de la suite de Julia.
    """
    return suite(z,c)


@numba.jit(nopython=True)
def is_in_Mandelbrot(c, max_iter) -> bool:
    """
    Teste si le point `c` est dans l'ensemble de Mandelbrot.

    Parameters
    ----------
    c : complex
        Le point complexe à tester.
    max_iter : int
        Le nombre maximum d'itérations à effectuer.

    Returns
    -------
    bool
        `True` si le point est dans l'ensemble de Mandelbrot, sinon `False`.
    """
    i = 0
    for z in suite_mandelbrot(c=c):
        if abs(z) > 2: # l’ensemble de Mandelbrot est contenu dans le cercle complexe de rayon 2
            return False 
        i += 1
        if i > max_iter:
            break
    return True


@numba.jit(nopython=True)
def is_in_Julia(z, c, max_iter) -> bool:
    """
    Teste si le point `z` est dans l'ensemble de Julia pour le paramètre `c`.

    Parameters
    ----------
    z : complex
        Le point complexe à tester.
    c : complex
        Le paramètre complexe pour l'ensemble de Julia.
    max_iter : int
        Le nombre maximum d'itérations à effectuer.

    Returns
    -------
    bool
        `True` si le point est dans l'ensemble de Julia, sinon `False`.
    """
    i = 0
    for z in suite_julia(z=z, c=c):
        if abs(z) > 2: # l’ensemble de Mandelbrot est contenu dans le cercle complexe de rayon 2
            return False 
        i += 1
        if i > max_iter:
            break
    return True


@numba.jit(nopython=True, parallel=True)
def create_matrix_mandelbrot(zmin, zmax, max_iter, width, height) -> list[list[bool]]:
    """
    Crée une matrice représentant l'ensemble de Mandelbrot.

    Parameters
    ----------
    zmin : complex
        La limite inférieure dans le plan complexe (coin inférieur gauche).
    zmax : complex
        La limite supérieure dans le plan complexe (coin supérieur droit).
    max_iter : int
        Le nombre maximum d'itérations pour déterminer l'appartenance à l'ensemble.
    width : int
        La largeur de la matrice (nombre de points dans la direction réelle).
    height : int
        La hauteur de la matrice (nombre de points dans la direction imaginaire).

    Returns
    -------
    list of list of bool
        Une matrice booléenne indiquant si chaque point est dans l'ensemble de Mandelbrot.
    """
    x = np.linspace(zmin.real, zmax.real, width)
    y = np.linspace(zmin.imag, zmax.imag, height)

    result = np.zeros((height, width), dtype=np.bool_)
    for j in numba.prange(height):
        for i in numba.prange(width):
            result[j, i] = is_in_Mandelbrot(complex(x[i], y[j]),max_iter=max_iter)
    
    return result


def plot_mandelbrot(zmin=-2-2j, zmax=2+2j, pixel_size=1e-3, max_iter=100, figname="Mandelbrot_ensemble.png"):
    """
    Trace l'ensemble de Mandelbrot.

    Parameters
    ----------
    zmin : complex, optional
        La limite inférieure dans le plan complexe (coin inférieur gauche), par défaut -2-2j.
    zmax : complex, optional
        La limite supérieure dans le plan complexe (coin supérieur droit), par défaut 2+2j.
    pixel_size : float, optional
        La taille d'un pixel dans le plan complexe, par défaut 1e-3.
    max_iter : int, optional
        Le nombre maximum d'itérations, par défaut 100.
    figname : str, optional
        Le nom du fichier de sortie pour l'image, par défaut "Mandelbrot_ensemble.png".

    Returns
    -------
    None
    """
    width_pixels = int((zmax.real - zmin.real) / pixel_size)
    height_pixels = int((zmax.imag - zmin.imag) / pixel_size)
    width_inches = 10  # Définir la largeur de la figure en pouces
    height_inches = width_inches * (height_pixels / width_pixels) # Calculer la hauteur de la figure en fonction du rapport d'aspect

    data = create_matrix_mandelbrot(zmin, zmax, max_iter, width_pixels, height_pixels)

    plt.figure(figsize=(width_inches, height_inches)) 
    plt.imshow(data, cmap='binary', extent=[zmin.real,zmax.real,zmin.imag,zmax.imag])
    plt.gca().set_axis_off()
    plt.savefig("Figures_fractals/"+figname, dpi=(width_pixels / width_inches))
    print("Figure enregistrée")


@numba.jit(nopython=True, parallel=True) 
def create_matrix_julia(c, zmin, zmax, max_iter, width, height) -> list[list[bool]]:
    """
    Crée une matrice représentant l'ensemble de Julia.

    Parameters
    ----------
    c : complex
        Le paramètre complexe pour l'ensemble de Julia.
    zmin : complex
        La limite inférieure dans le plan complexe (coin inférieur gauche).
    zmax : complex
        La limite supérieure dans le plan complexe (coin supérieur droit).
    max_iter : int
        Le nombre maximum d'itérations pour déterminer l'appartenance à l'ensemble.
    width : int
        La largeur de la matrice (nombre de points dans la direction réelle).
    height : int
        La hauteur de la matrice (nombre de points dans la direction imaginaire).

    Returns
    -------
    list of list of bool
        Une matrice booléenne indiquant si chaque point est dans l'ensemble de Julia.
    """
    x = np.linspace(zmin.real, zmax.real, width)
    y = np.linspace(zmin.imag, zmax.imag, height)

    result = np.zeros((height, width), dtype=np.bool_)
    for j in numba.prange(height):
        for i in numba.prange(width):
            result[j, i] = is_in_Julia(complex(x[i], y[j]), c, max_iter)

    return result


def plot_julia(c=-0.8 + 0.156j, zmin=-2-1j, zmax=2+1j, pixel_size=5e-4, max_iter=100, figname="Julia_-0.8+0.156j.png"):
    """
    Trace l'ensemble de Julia.

    Parameters
    ----------
    c : complex, optional
        Le paramètre complexe pour l'ensemble de Julia, par défaut -0.8 + 0.156j.
    zmin : complex, optional
        La limite inférieure dans le plan complexe (coin inférieur gauche), par défaut -2-1j.
    zmax : complex, optional
        La limite supérieure dans le plan complexe (coin supérieur droit), par défaut 2+1j.
    pixel_size : float, optional
        La taille d'un pixel dans le plan complexe, par défaut 5e-4.
    max_iter : int, optional
        Le nombre maximum d'itérations, par défaut 100.
    figname : str, optional
        Le nom du fichier de sortie pour l'image, par défaut "Julia_-0.8+0.156j.png".

    Returns
    -------
    None
    """
    width_pixels = int((zmax.real - zmin.real) / pixel_size)
    height_pixels = int((zmax.imag - zmin.imag) / pixel_size)
    width_inches = 10  # Définir la largeur de la figure en pouces
    height_inches = width_inches * (height_pixels / width_pixels) # Calculer la hauteur de la figure en fonction du rapport d'aspect
    
    data = create_matrix_julia(c, zmin, zmax, max_iter, width_pixels, height_pixels)

    plt.figure(figsize=(width_inches, height_inches))
    plt.imshow(data, cmap='binary', extent=[zmin.real,zmax.real,zmin.imag,zmax.imag])
    plt.gca().set_axis_off()
    plt.savefig("Figures_fractals/"+figname, dpi=(width_pixels / width_inches))
    print("Figure enregistrée")

