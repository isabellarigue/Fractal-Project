import argparse
import sys, os
from fractals.helper import plot_mandelbrot, plot_julia

def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description='Générer des ensembles de Mandelbrot ou de Julia.')

    script_name = sys.argv[0]

    if 'MandelbrotPlot' in script_name:
        parser.add_argument('--zmin', type=complex, default=-2-2j,
                            help='La limite inférieure dans le plan complexe (par défaut pour Mandelbrot: -2-2j).')
        parser.add_argument('--zmax', type=complex, default=2+2j,
                            help='La limite supérieure dans le plan complexe (par défaut pour Mandelbrot: 2+2j).')
        parser.add_argument('--pixel_size', type=float, default=1e-3,
                            help='La taille d\'un pixel dans le plan complexe (par défaut pour Mandelbrot: 1e-3).')
        parser.add_argument('--max_iter', type=int, default=100,
                            help='Le nombre maximum d\'itérations (par défaut pour Mandelbrot: 100).')
        parser.add_argument('-o', '--output', type=str, default="Mandelbrot.png",
                            help='Le nom du fichier de sortie pour l\'image générée.')
        
    elif 'JuliaPlot' in script_name:
        # Define os parâmetros para Julia
        parser.add_argument('--zmin', type=complex, default=-2-1j,
                            help='La limite inférieure dans le plan complexe (par défaut pour Julia: -2-1j).')
        parser.add_argument('--zmax', type=complex, default=2+1j,
                            help='La limite supérieure dans le plan complexe (par défaut pour Julia: 2+1j).')
        parser.add_argument('--pixel_size', type=float, default=5e-4,
                            help='La taille d\'un pixel dans le plan complexe (par défaut pour Julia: 5e-4).')
        parser.add_argument('--max_iter', type=int, default=100,
                            help='Le nombre maximum d\'itérations (par défaut pour Julia: 100).')
        parser.add_argument('--c', type=complex, default=-0.8+0.156j,
                            help='Le paramètre complexe pour l\'ensemble de Julia (par défaut: -0.8 + 0.156j).')
        parser.add_argument('-o', '--output', type=str, default="Julia.png",
                            help='Le nom du fichier de sortie pour l\'image générée.')
        
    else:
        print("Nom de script non reconnu. Utilisez 'MandelbrotPlot' ou 'JuliaPlot'.")
        return
    
    if not os.path.exists("Figures_fractals"):
        os.makedirs("Figures_fractals")  # Dossier pour stocker les figures

    args = parser.parse_args()

    if 'MandelbrotPlot' in script_name:
        plot_mandelbrot(zmin=args.zmin, zmax=args.zmax,
                         pixel_size=args.pixel_size, max_iter=args.max_iter, figname=args.output)
    elif 'JuliaPlot' in script_name:
        plot_julia(c=args.c, zmin=args.zmin, zmax=args.zmax,
                    pixel_size=args.pixel_size, max_iter=args.max_iter, figname=args.output)

if __name__ == "__main__":
    main()

