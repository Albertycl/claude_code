"""
Flask application runner with database initialization.
"""
import os
import sys
sys.path.append('.')

from app import create_app, db
from app.models import User

# Create application instance
app = create_app(os.environ.get('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Make database models available in shell context."""
    return {'db': db, 'User': User}

@app.cli.command()
def init_db():
    """Initialize the database."""
    db.create_all()
    print("Database initialized!")

@app.cli.command()
def seed_db():
    """Seed the database with sample data."""
    # Create sample users
    users = [
        User(username='john_doe', email='john@example.com'),
        User(username='jane_smith', email='jane@example.com'),
        User(username='admin', email='admin@example.com')
    ]
    
    for user in users:
        db.session.add(user)
    
    try:
        db.session.commit()
        print("Database seeded with sample data!")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {e}")

if __name__ == '__main__':
    with app.app_context():
        # Initialize database tables
        db.create_all()
        print("Database tables created!")
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=58991)