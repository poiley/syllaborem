##########
# Reader #
##########

import os

'''import all python files in the reader folder'''
from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

'''importing PDF reading library'''
import textract

FILETYPES = ['pdf']

from . import core