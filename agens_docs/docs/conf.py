# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'SKAI Worldwide Documentation'
copyright = '2024, SKAI Worldwide'
author = 'SKAI Worldwide'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'myst_parser',  # For Markdown support
]

# Add any paths that contain templates here
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The theme to use for HTML and HTML Help pages
html_theme = 'sphinx_rtd_theme'

# Theme options
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_position': 'both',
    'style_external_links': True,
    'style_nav_header_background': '#003366',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files
html_static_path = ['_static']

# Custom CSS
html_css_files = ['custom.css']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/skai-logo.png'

# The name of an image file (relative to this directory) to use as a favicon
html_favicon = '_static/favicon.ico'

# Enable Markdown support
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Syntax highlighting ---------------------------------------------------

highlight_language = 'python'
pygments_style = 'sphinx'

# Add SQL syntax highlighting
from sphinx.highlighting import lexers
from pygments.lexers.sql import SqlLexer
lexers['sql'] = SqlLexer()
