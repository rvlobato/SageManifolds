# -*- coding: utf-8 -*-
#
# Sage documentation build configuration file
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
from sage.env import SAGE_DOC
sys.path.append(SAGE_DOC)
from common.conf import *

# settings for the intersphinx extension:

ref_src = os.path.join(SAGE_DOC, 'en', 'sagemanifolds')
ref_out = os.path.join(SAGE_DOC, 'output', 'html', 'en', 'sagemanifolds')
#/home/michal/sage-5.12/devel/sage/doc/output/html/en/sagemanifolds

#intersphinx_mapping[ref_out] = None

for doc in os.listdir(ref_src):
    if os.path.exists(os.path.join(ref_src, doc, 'index.rst')):
        intersphinx_mapping[os.path.join(ref_out, doc)] = None

# General information about the project.
project = u"SageManifolds Reference Manual"
name = 'sagemanifolds_ref'
release = "0.3"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + " v" + release
html_short_title = u'SageManifolds v' + release
copyright = u"2013, Michał Bejger and Éric Gourgoulhon"

# Output file base name for HTML help builder.
htmlhelp_basename = name

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', name+'.tex', u'SageManifolds Reference Manual',
   u'Michał Bejger and Éric Gourgoulhon', 'manual'),
]

# This is to make the verbatim font smaller; 
# Verbatim environment is not breaking long lines 
from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"

PygmentsBridge.latex_formatter = CustomLatexFormatter

latex_elements['preamble'] += r'''
% One-column index
\makeatletter
\renewenvironment{theindex}{
  \chapter*{\indexname}
  \markboth{\MakeUppercase\indexname}{\MakeUppercase\indexname}
  \setlength{\parskip}{0.1em}
  \relax
  \let\item\@idxitem
}{}
\makeatother
\renewcommand{\ttdefault}{txtt}
'''

#Ignore all .rst in the _sage subdirectory
exclude_trees = exclude_trees + ['_sage']

multidocs_is_master = True

# Sorted list of subdocs. Include all subdirectories of ref_src except
# for 'static' and 'templates', and to deal with upgrades: 'sage',
# 'sagenb', 'media', and 'other'.
bad_directories = ['static', 'templates', 'sage', 'sagenb', 'media', 'other']
multidocs_subdoc_list = sorted([x for x in os.listdir(ref_src)
                                if os.path.isdir(os.path.join(ref_src, x))
                                and x not in bad_directories])

# List of directories, relative to source directory, that shouldn't be
# searched for source files.
exclude_trees += multidocs_subdoc_list + [
    'sage', 'sagenb', 'options'
    ]
