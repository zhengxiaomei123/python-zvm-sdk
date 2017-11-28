# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# This file is execfile()d with the current directory set to
# its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import subprocess
import sys
import warnings

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../../'))
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('./'))

extensions = [
    'sphinx.ext.autodoc',
    'ext.restapi_parameters',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.viewcode',
]

# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Cloud Connector for zVM'
copyright = u'2017 IBM'
author = u'IBM z/VM cloud team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.

def package_version(filename, varname):
    """Return package version string by reading `filename` and retrieving its
       module-global variable `varnam`."""
    _locals = {}
    with open(filename) as fp:
        exec(fp.read(), None, _locals)
    return _locals[varname]

# The short X.Y version.
# Note: We use the full version in both cases (e.g. 'M.N.U' or 'M.N.U.dev0').
version = package_version('../../zvmsdk/version.py', '__version__')

# The short X.Y version.
version = '0.3'

release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# The reST default role (used for this markup: `text`) to use
# for all documents.
# default_role = None


exclude_patterns = ["tests", ".tox", ".git", "attic", "dist",
                    "build_doc", ".egg-info", ".eggs"]

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Enable support for Google style docstrings. Defaults to True.
napoleon_google_docstring = True

# Enable support for NumPy style docstrings. Defaults to True.
napoleon_numpy_docstring = False

# Include private members (like _membername). False to fall back to Sphinxâ# default behavior. Defaults to False.
napoleon_include_private_with_doc = False

# Include special members (like __membername__). False to fall back to Sphinxâ# default behavior. Defaults to True.
napoleon_include_special_with_doc = True

# Use the .. admonition:: directive for the Example and Examples sections,
# instead of the .. rubric:: directive. Defaults to False.
napoleon_use_admonition_for_examples = False

# Use the .. admonition:: directive for Notes sections, instead of the
# .. rubric:: directive. Defaults to False.
napoleon_use_admonition_for_notes = False

# Use the .. admonition:: directive for References sections, instead of the
# .. rubric:: directive. Defaults to False.
napoleon_use_admonition_for_references = False

# Use the :ivar: role for instance variables, instead of the .. attribute::
# directive. Defaults to False.
napoleon_use_ivar = True

# Use a :param: role for each function parameter, instead of a single
# :parameters: role for all the parameters. Defaults to True.
napoleon_use_param = True

# Use the :rtype: role for the return type, instead of inlining it with the
# description. Defaults to True.
napoleon_use_rtype = True


# -- Options for viewcode extension ---------------------------------------

# Follow alias objects that are imported from another module such as functions
# classes and attributes. As side effects, this option ... ???
# If false, ... ???.
# The default is True.
viewcode_import = True

# -- Options for man page output ----------------------------------------------

# Grouping the document tree for man pages.
# List of tuples 'sourcefile', 'target', u'title', u'Authors name', 'manual'


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme_path = ["."]
# html_theme = '_theme'
html_theme = 'classic'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'
git_cmd = ["git", "log", "--pretty=format:'%ad, commit %h'", "--date=local",
    "-n1"]
try:
    html_last_updated_fmt = subprocess.Popen(
        git_cmd, stdout=subprocess.PIPE).communicate()[0].decode()
except Exception:
    warnings.warn('Cannot get last updated time from git repository. '
                  'Not setting "html_last_updated_fmt".')

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''


# Output file base name for HTML help builder.


# -- Options for LaTeX output -------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    (master_doc, project+'.tex', u'Cloud Connector for zVM',
     u'IBM', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True

# -- Options for autodoc extension ----------------------------------------
# For documentation, see
# http://www.sphinx-doc.org/en/stable/ext/autodoc.html

# Selects what content will be inserted into a class description.
# The possible values are:
#   "class" - Only the classâocstring is inserted. This is the default.
#   "both"  - Both the classând the __init__ methodâdocstring are
#             concatenated and inserted.
#   "init"  - Only the __init__ methodâdocstring is inserted.
# In all cases, the __init__ method is still independently rendered as a
# special method, e.g. when the :special-members: option is set.
autoclass_content = "both"

# Selects if automatically documented members are sorted alphabetically
# (value 'alphabetical'), by member type (value 'groupwise') or by source
# order (value 'bysource'). The default is alphabetical.
autodoc_member_order = "bysource"

# This value is a list of autodoc directive flags that should be automatically
# applied to all autodoc directives. The supported flags are:
# 'members', 'undoc-members', 'private-members', 'special-members',
# 'inherited-members' and 'show-inheritance'.
# If you set one of these flags in this config value, you can use a negated
# form, 'no-flag', in an autodoc directive, to disable it once.
autodoc_default_flags = []

# Functions imported from C modules cannot be introspected, and therefore the
# signature for such functions cannot be automatically determined. However, it
# is an often-used convention to put the signature into the first line of the
# functionâdocstring.
# If this boolean value is set to True (which is the default), autodoc will
# look at the first line of the docstring for functions and methods, and if it
# looks like a signature, use the line as the signature and remove it from the
# docstring content.
autodoc_docstring_signature = True

# -- Options for intersphinx extension ------------------------------------
# For documentation, see
# http://www.sphinx-doc.org/en/stable/ext/intersphinx.html

# Defines the prefixes for intersphinx links, and the targets they resolve to.
# Example RST source for 'py2' prefix:
#     :func:`py2:platform.dist`
#
# Note: The URLs apparently cannot be the same for two different IDs; otherwise
#       the links for one of them are not being created. A small difference
#       such as adding a trailing backslash is already sufficient to work
#       around the problem.
#
# Note: This mapping does not control how links to datatypes of function
#       parameters are generated.
# TODO: Find out how the targeted Python version for auto-generated links
#       to datatypes of function parameters can be controlled.
#
intersphinx_mapping = {
  'py': ('https://docs.python.org/2/', None), # agnostic to Python version
  'py2': ('https://docs.python.org/2', None), # specific to Python 2
  'py3': ('https://docs.python.org/3', None), # specific to Python 3
}

intersphinx_cache_limit = 5

