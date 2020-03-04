# -*- coding: utf-8 -*-

import json
import os
import sys
import urllib.request
import cgi
import csv
import shutil
import pandas as pd
from nikola.plugin_categories import Task
from nikola.utils import LOGGER

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from mako.template import Template
from pylatexenc.latexencode import utf8tolatex

plugin_path = os.path.dirname(os.path.realpath("__file__"))
base_path = plugin_path.split("plugins")[0]
pages_path = os.path.join(base_path, "pages", "reports")
