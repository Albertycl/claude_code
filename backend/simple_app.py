"""
Simple Flask application with all components in one file for learning purposes.
This demonstrates Flask best practices in a clear, understandable way.
"""
from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import os

# Configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///flask_learning.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = True

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    """User model for demonstration purposes."""
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
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

# Create API Blueprint
api_bp = Blueprint('api', __name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    """Simple hello world endpoint."""
    return jsonify({
        'message': 'Hello World from Flask!',
        'status': 'success',
        'framework': 'Flask with SQLAlchemy'
    })

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    try:
        # Test database connectivity
        db.session.execute(db.text('SELECT 1'))
        db_status = 'connected'
    except Exception:
        db_status = 'disconnected'
    
    return jsonify({
        'status': 'healthy',
        'message': 'Flask API is running',
        'database': db_status,
        'version': '1.0.0'
    })

@api_bp.route('/users', methods=['GET'])
def get_users():
    """Get all users with pagination support."""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        users = User.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'users': [user.to_dict() for user in users.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': users.total,
                'pages': users.pages,
                'has_next': users.has_next,
                'has_prev': users.has_prev
            },
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': 'Failed to fetch users',
            'message': str(e),
            'status': 'error'
        }), 500

@api_bp.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'error': 'No data provided',
                'status': 'error'
            }), 400
        
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        
        if not username or not email:
            return jsonify({
                'error': 'Username and email are required',
                'status': 'error'
            }), 400
        
        # Basic email validation
        if '@' not in email:
            return jsonify({
                'error': 'Invalid email format',
                'status': 'error'
            }), 400
        
        # Create user
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            'user': user.to_dict(),
            'message': 'User created successfully',
            'status': 'success'
        }), 201
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            'error': 'Username or email already exists',
            'status': 'error'
        }), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Failed to create user',
            'message': str(e),
            'status': 'error'
        }), 500

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID."""
    try:
        user = User.query.get_or_404(user_id)
        return jsonify({
            'user': user.to_dict(),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': 'User not found',
            'status': 'error'
        }), 404

@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user."""
    try:
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        
        if not data:
            return jsonify({
                'error': 'No data provided',
                'status': 'error'
            }), 400
        
        # Update fields if provided
        if 'username' in data:
            user.username = data['username'].strip()
        if 'email' in data:
            user.email = data['email'].strip()
        if 'is_active' in data:
            user.is_active = bool(data['is_active'])
        
        db.session.commit()
        
        return jsonify({
            'user': user.to_dict(),
            'message': 'User updated successfully',
            'status': 'success'
        })
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            'error': 'Username or email already exists',
            'status': 'error'
        }), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Failed to update user',
            'message': str(e),
            'status': 'error'
        }), 500

@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user."""
    try:
        user = User.query.get_or_404(user_id)
        username = user.username
        
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({
            'message': f'User {username} deleted successfully',
            'status': 'success'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Failed to delete user',
            'message': str(e),
            'status': 'error'
        }), 500

# Register Blueprint
app.register_blueprint(api_bp, url_prefix='/api')

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not found',
        'message': 'The requested resource was not found',
        'status': 'error'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'message': 'Something went wrong on the server',
        'status': 'error'
    }), 500

# CLI Commands (for database management)
@app.cli.command()
def init_db():
    """Initialize the database."""
    db.create_all()
    print("Database initialized!")

@app.cli.command()
def seed_db():
    """Seed the database with sample data."""
    users = [
        User(username='john_doe', email='john@example.com'),
        User(username='jane_smith', email='jane@example.com'),
        User(username='admin_user', email='admin@example.com'),
        User(username='test_user', email='test@example.com')
    ]
    
    for user in users:
        try:
            db.session.add(user)
            db.session.commit()
            print(f"Created user: {user.username}")
        except IntegrityError:
            db.session.rollback()
            print(f"User {user.username} already exists, skipping...")

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
        print("Database tables created!")
        
        # Create some sample data if the database is empty
        if User.query.count() == 0:
            sample_users = [
                User(username='demo_user', email='demo@example.com'),
                User(username='api_tester', email='tester@example.com')
            ]
            
            for user in sample_users:
                db.session.add(user)
            
            db.session.commit()
            print(f"Created {len(sample_users)} sample users")
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5491)