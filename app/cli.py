import click
from app.models import User

def register_commands(app):
    """Register custom CLI commands with the Flask app"""
    
    @app.cli.command('init-db')
    def init_db():
        """Initialize the database"""
        with app.app_context():
            from app import db
            db.create_all()
            click.echo('Database initialized')
    
    @app.cli.command('create-admin')
    @click.argument('username')
    @click.argument('password')
    def create_admin(username, password):
        """Create an admin user"""
        with app.app_context():
            from app import db
            user = User(
                username=username,
                email=f'{username}@admin.com',
                is_admin=True
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            click.echo(f'Admin user {username} created')