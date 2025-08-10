from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
import os

app = Flask(__name__)

# Load configuration
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

# Initialize database
db = SQLAlchemy(app)

# Import models after db initialization
class User(db.Model):
    """User model for demonstration purposes."""
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        """Convert user to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_active': self.is_active
        }

# Import API routes
from app.api import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    return {'error': 'Internal server error'}, 500


if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
        print("Database tables created!")
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=58991)