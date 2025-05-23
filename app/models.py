from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Packet(db.Model):
    __tablename__= 'packet'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    source_ip = db.Column(db.String(64))
    destination_ip = db.Column(db.String(64))
    protocol = db.Column(db.String(16))
    length = db.Column(db.Integer)
    info = db.Column(db.Text)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))