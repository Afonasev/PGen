# make config.py with your parameters
import os


_basedir = os.path.abspath(os.path.dirname(__file__))

STATIC_PATH = os.path.join(_basedir, './pgen/static/')
TEMPLATE_PATH = os.path.join(_basedir, './pgen/templates/')

DEBUG = True
SECRET_KEY = 'VERY SECRET KEY'
