# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.

import os
import sys
import sphinx_rtd_theme

# Updating path
sys.path.insert(0, os.path.abspath('..//..'))
sys.setrecursionlimit(1500)

from pyonfx import __version__

# -- Project information -----------------------------------------------------

project = 'PyonFX'
copyright = '2019, Antonio Strippoli'
author = 'Antonio Strippoli (CoffeeStraw/YellowFlash)'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = __version__ 

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_logo = "_static/PyonFX Logo.png"

# The theme to use for HTML and HTML Help pages.  See the documentation for 
# a list of builtin themes. 
html_theme = 'sphinx_rtd_theme' 
htm_theme_path = [sphinx_rtd_theme.get_html_theme_path()]   

 # Theme options are theme-specific and customize the look and feel of a theme  
# further.  
html_theme_options = {  
    'canonical_url': '',    
    'logo_only': True,  
    'display_version': True,    
    'prev_next_buttons_location': 'bottom', 
    'style_external_links': True,   
    'collapse_navigation': True,    
    'sticky_navigation': True,  
    'navigation_depth': 4,  
    'includehidden': True,  
    'titles_only': False    
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyonFXdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
    'extraclassoptions': 'openany,oneside'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'PyonFX.tex', 'PyonFX Documentation',
     'Antonio Strippoli (CoffeeStraw/YellowFlash)', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pyonfx', 'PyonFX Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'PyonFX', 'PyonFX Documentation',
     author, 'PyonFX', 'An easy way to do KFX and complex typesetting based on subtitle format ASS (Advanced Substation Alpha).',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
extensions = ['sphinx.ext.napoleon']
napoleon_google_docstring = True
napoleon_use_admonition_for_examples = True

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
