# Projet de Fractales / Fractal Project

## Description

Ce projet est une implémentation de visualisation des ensembles de Mandelbrot et de Julia en utilisant Python. Il utilise les bibliothèques `NumPy`, `Matplotlib` et `Numba` pour générer et afficher des fractales complexes.

This project is an implementation for visualizing the Mandelbrot and Julia sets using Python. It utilizes the `NumPy`, `Matplotlib`, and `Numba` libraries to generate and display complex fractals.

## Fonctionnalités / Features

- Génération des ensembles de Mandelbrot et de Julia.
- Visualisation des fractales en utilisant des images.
- Performances améliorées grâce à l'utilisation de Numba pour la compilation JIT (Just-In-Time).
- Options pour personnaliser les paramètres des fractales, tels que la taille de l'image, le nombre maximum d'itérations et les limites du plan complexe.

- Generation of the Mandelbrot and Julia sets.
- Visualization of fractals using images.
- Improved performance through the use of Numba for Just-In-Time (JIT) compilation.
- Options to customize fractal parameters, such as image size, maximum number of iterations, and limits of the complex plane.

## Prérequis / Prerequisites

Assurez-vous d'avoir une version de Python supérieure à 3.8 mais inférieure à version 13.0 installé sur votre machine. Vous aurez également besoin des bibliothèques suivantes :

Make sure you have a version of Python greater than 3.8 but inferior than 13.0 installed on your machine. You will also need the following libraries:

- `numpy`
- `matplotlib`
- `numba`

Vous pouvez les installer avec pip :

You can install them using pip:

```bash
pip install numpy matplotlib numba
```

## Installation
```bash
cd chemin/des/sources
pip install .
```

## Utilisation / Usage

### Exemple d'utilisation de la bibliothèque

La bibliothèque peut être utilisée soit via la ligne de commande (CLI), soit en appelant directement les fonctions dans le script pour des détails personnalisés.

The library can be used either through the command line interface (CLI) or by directly calling the functions in the script for customized details.

#### Utilisation en CLI

Pour produire une version par défaut de l'un des deux ensembles, vous pouvez utiliser les commandes suivantes :

To produce a default version of either set, you can use the following commands:

```bash
$ MandelbrotPlot -o mandelbrot.png
$ JuliaPlot -o julia.png
```

Pour produire une visualisation avec des détails choisis, comme dans l'API, vous pouvez utiliser les options suivantes :

To produce a visualization with selected details, as in the API, you can use the following options:

```bash
$ MandelbrotPlot --zmin=-0.7440+0.1305j \
--zmax=-0.7425+0.1320j \
--pixel_size=5e-7 \
--max_iter=50 \
-o "Mandelbrot_tentacle_lowiter.png"
```

```bash
$ JuliaPlot --c=-0.8+0.156j \
--zmin=-2-1j \
--zmax=2+1j \
--pixel_size=5e-4 \
--max_iter=100 \
-o "Julia_-0.8+0.156j.png"
```

### Description des paramètres / Parameter Description

- `--c`: Le paramètre complexe pour le ensemble de Julia. / The complex parameter for the Julia set.
- `--zmin`: La limite inférieure dans le plan complexe (coin inférieur gauche). / The lower limit in the complex plane (bottom left corner).
- `--zmax`: La limite supérieure dans le plan complexe (coin supérieur droit). / The upper limit in the complex plane (top right corner).
- `--pixel_size`: La taille d'un pixel dans le plan complexe. / The size of a pixel in the complex plane.
- `--max_iter`: Le nombre maximum d'itérations. / The maximum number of iterations.
- `-o`: Le nom du fichier de sortie pour l'image générée. / The name of the output file for the generated image.


## Licence / License

Ce projet est sous la licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Numba](https://numba.pydata.org/)