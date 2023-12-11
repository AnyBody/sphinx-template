# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys
from typing import Any, Dict

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = "sphinx-anybody-template"
copyright = "2022, AnyBody Technology"
author = "AnyBody Technology"
release = '0.1'

# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_needs",
    "sphinx_simplepdf",
]
templates_path = ["_templates"]

exclude_patterns = ['_build', 'Thumbs.db']


# -- Sphinx Needs configuration -----------------------------------------------

# MEL: Not sure what this does
# needs_include_needs = False

# Length of the ID field for the id numbers
needs_id_length = 5


# Need types:  These are the default
needs_types = [
    dict(
        directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"
    ),
    dict(
        directive="spec",
        title="Specification",
        prefix="S_",
        color="#FEDCD2",
        style="node",
    ),
    dict(
        directive="impl",
        title="Implementation",
        prefix="I_",
        color="#DF744A",
        style="node",
    ),
    dict(
        directive="test", title="Test Case", prefix="T_", color="#DCB239", style="node"
    ),
    dict(
        directive="unit", title="Unit", prefix="U_", color="#AAB239", style="node"
    ),
]

# Extra optional fields on the need objects:
needs_extra_options = ["introduced", "updated", "impacts"]


# Builds a json file with the need data while also building the HTML
needs_build_json = True
needs_reproducible_json = True
# Build a json file for every need object
needs_build_json_per_id = False



# -- Options for extlinks ----------------------------------------------------
#

extlinks = {
    "pypi": ("https://pypi.org/project/%s/", "%s"),
}

# -- Options for intersphinx -------------------------------------------------
#

intersphinx_mapping = {
    "ammr": ("https://anyscript.org/ammr-doc", None),
    "tutorials": ("https://anyscript.org/tutorials/",None),
}

# -- Options for TODOs -------------------------------------------------------
#

todo_include_todos = True

# -- Options for Markdown files ----------------------------------------------
#

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
    "html_image",
    "substitution",
    "linkify"
]
myst_heading_anchors = 3


myst_html_meta = {
"robots":"noindex"
}

# -- Options for HTML output -------------------------------------------------
#
# html_sidebars = {
#     "**": [
#         "sbt-sidebar-nav.html",
#     ]
# }


html_theme = "sphinx_book_theme"
html_title = "Sphinx AnyBody Template"
language = "en"

html_static_path = ["_static"]
html_css_files = []

html_theme_options: Dict[str, Any] = {
    "repository_url": "https://github.com/AnyBody/sphinx-template",
    "repository_branch": "main",
    "logo": {
      "image_light": "logo.svg",
      "image_dark": "logo.svg",
   },
   # "extra_navbar": 'Create by <a href="https://anybodytech.com">AnyBody Technology</a>',

}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = "logo.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

html_js_files = [
    'js/custom.js',
]

# -- Options for theme development -------------------------------------------
# Make sure these are all set to the default values.


# FONT_AWESOME_TESTING = False
# if FONT_AWESOME_TESTING:
#     html_css_files += [
#         "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
#         "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
#         "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
#     ]

#     html_theme_options["footer_icons"] = [
#         {
#             "name": "GitHub",
#             "url": "https://github.com/pradyunsg/furo",
#             "html": "",
#             "class": "fa-solid fa-github fa-2x",
#         },
#     ]
