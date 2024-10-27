from flask import Flask
from os import environ
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.secret_key = "dev-secret-key"  # For development only
    
    # Register blueprints
    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    return app
