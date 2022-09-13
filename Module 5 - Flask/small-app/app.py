from flask import Flask, render_template
from dict import recipes

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/recipes/')
def recipe_list():
    return render_template('recipe_page.html', recipe_id = recipes)

