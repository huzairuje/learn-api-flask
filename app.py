from flask import Flask
from core.router import routers

app = Flask(__name__)
routers.Router.run(app)
