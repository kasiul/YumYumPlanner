from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Fix the typo here
db.init_app(app)
migrate = Migrate(app, db)

RECIPE_API_KEY = 'd5e264fbe514448ba9d2bfa327803d60'

def get_recipe_data(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': RECIPE_API_KEY,
        'query': query,
        'number' : 10,
        'addRecipeInformation': True,  # Fix the typo here
        'instructionsRequired': True,
        'addRecipeInformation' : True,  # Fix the typo here
    }

if __name__ =='__main__':
    app.run(debug=True)
