import os
import sys
sys.path.insert(0, os.path.abspath('.'))

#from recommonmark.parser import CommonMarkParser

# source_parsers = {
#     '.md': CommonMarkParser,
# }

# .rst와 .md를 모두 인식
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

project = 'doc_test'
copyright = '2025, jacksmith'
author = 'jacksmith'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
]

templates_path = ['_templates']
exclude_patterns = []
master_doc = "index"

language = 'ko'



# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
