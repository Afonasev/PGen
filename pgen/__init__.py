from flask import Flask

app = Flask(__name__)
app.jinja_env.cache = {}
app.jinja_env.line_statement_prefix = '%'

try:
    import config
except ImportError:
    import example_config as config

app.config.from_object(config)

from .views import *
from .utils import *
