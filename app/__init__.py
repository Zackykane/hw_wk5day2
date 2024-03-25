from flask import Flask

app = Flask(__name__)

from resources.sale_receipt import routes
from resources.car import routes