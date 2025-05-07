# Configuration file for the Sphinx documentation builder.
# Para más detalles, consulta la documentación oficial:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Agregar la ruta de src/ si es necesario para la documentación automática
sys.path.insert(0, os.path.abspath('../src'))  # Ajusta si es necesario

# -- Información del proyecto -----------------------------------------------------
project = 'Articles Analysis Grobid'
copyright = '2025, Sergio Gonzalez'
author = 'Sergio Gonzalez'
release = '1.0.0'

# -- Extensiones de Sphinx ------------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",       # Documentación automática de código Python
    "sphinx.ext.napoleon",      # Soporte para docstrings estilo Google/Numpy
    "sphinx.ext.viewcode",      # Añade enlaces al código fuente en la documentación
    "autoapi.extension"         # Generación automática de documentación de src/
]

# Configuración de autoapi para extraer documentación de src/
autoapi_dirs = ["../src"]  # Asegúrate de que esta ruta es correcta

# -- Configuración general ---------------------------------------------------
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Configurar idioma en español
language = 'es'

# -- Configuración para salida en HTML ----------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
