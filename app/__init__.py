from flask import Flask
from .pentrazy import Pentrazy

app = Flask(__name__)
pentrazy_ai = Pentrazy()

from app import routes