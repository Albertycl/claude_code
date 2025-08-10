from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

api_bp = Blueprint('api', __name__)


@api_bp.route('/hello', methods=['GET'])
def hello_world():
    """Simple hello world endpoint."""
    return jsonify({
        'message': 'Hello World!',
        'status': 'success'
    })


@api_bp.route('/users', methods=['GET'])
def get_users():
    """Get all users."""
    from app import db, User
    try:
        users = User.query.all()
        return jsonify({
            'users': [user.to_dict() for user in users],
            'count': len(users),
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
    from app import db, User
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'error': 'No data provided',
                'status': 'error'
            }), 400
        
        username = data.get('username')
        email = data.get('email')
        
        if not username or not email:
            return jsonify({
                'error': 'Username and email are required',
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
    from app import User
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


@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    from app import db
    try:
        # Simple database connectivity check
        db.session.execute(db.text('SELECT 1'))
        db_status = 'connected'
    except Exception:
        db_status = 'disconnected'
    
    return jsonify({
        'status': 'healthy',
        'message': 'Flask API is running',
        'database': db_status
    })