# PURPOSE OF THIS __init__.py :
    # 
from flask import Flask
from .site.routes import site

app = Flask(__name__)

app.register_blueprint(site)