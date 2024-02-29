from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from extensions import db  # Adjust this import according to your project structure
from routes import api_blueprint  # Adjust this import according to your project structure

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
    CORS(app)
    app.register_blueprint(api_blueprint, url_prefix='/api')  # All API routes will now be prefixed with /api

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

