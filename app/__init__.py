import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from app.routes.category_route import category_blueprint
from app.routes.product_route import product_blueprint
from app.routes.product_properties import product_properties_bp_blueprint
from app.routes.property_category_route import property_category_blueprint
from app.routes.property_route import property_blueprint
from app.routes.gender_route import gender_blueprint
from app.routes.gender_category_route import gender_category_blueprint

load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
CORS(app, origins=[
    'https://luxelend-client-side.vercel.app',
    'http://localhost:5000', 
    'http://localhost:3000'
], supports_credentials=True)

@app.route("/")
def helloWorld():
    return "welcome to Luxelend!"

app.register_blueprint(category_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(product_properties_bp_blueprint)
app.register_blueprint(property_category_blueprint)
app.register_blueprint(property_blueprint)
app.register_blueprint(gender_blueprint)
app.register_blueprint(gender_category_blueprint)

if __name__ == "__main__":
    app.run()