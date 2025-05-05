from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from config import Config

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)
    
    # Register blueprints (import here to avoid circular imports)
    from app.routes import main_bp
    from app.auth import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    
    return app