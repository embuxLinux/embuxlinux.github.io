# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Embux BusyBox/Linux'
copyright = '2023, Embux Project'
author = 'Embux Project'
release = '24.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_rtd_theme", "sphinx_external_toc", "sphinx_design"]
myst_enable_extensions = ["colon_fence"]
external_toc_path = "_index.yaml"  # optional, default: _toc.yml
external_toc_exclude_missing = True  # optional, default: False

templates_path = ['_templates']
exclude_patterns = []

html_context = {
  'display_github': True,
  'github_user': 'embuxLinux',
  'github_repo': 'embuxlinux.github.io',
  'github_version': 'main',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
