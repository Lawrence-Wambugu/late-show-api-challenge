from flask import Blueprint, request, jsonify
from server.models.user import User
from server.app import db
from flask_jwt_extended import create_access_token

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate request data
    if not data or not data.get("username") or not data.get("password"):
        return {"error": "Username and password required"}, 400

    # Check if username already exists
    if User.query.filter_by(username=data["username"]).first():
        return {"error": "Username already exists"}, 409

    # Create and save new user
    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()

    return {"message": "User registered successfully"}, 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate request data
    if not data or not data.get("username") or not data.get("password"):
        return {"error": "Username and password required"}, 400

    # Look up user
    user = User.query.filter_by(username=data.get("username")).first()

    # Check password and generate JWT
    if not user or not user.check_password(data.get("password")):
        return {"error": "Invalid credentials"}, 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
