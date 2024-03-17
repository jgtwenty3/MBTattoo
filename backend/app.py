from flask import Flask, request, session, redirect, url_for, render_template, jsonify
from flask_bcrypt import Bcrypt
from sqlalchemy import desc

from config import app, db, migrate, api, bcrypt

from models import db, User, Client, ConsentForm

@app.route('/')
def home():
    return ''

@app.route('/signup', methods=['POST'])
def signup():
    json_data = request.get_json()

    # Validate required fields
    required_fields = ['username', 'password', 'email', 'usertype', 'phone', 'address']
    for field in required_fields:
        if field not in json_data:
            return {'error': f'Missing required field: {field}'}, 400

    # Validate usertype
    valid_usertypes = ['artist', 'admin']
    if json_data['usertype'] not in valid_usertypes:
        return {'error': f'Invalid usertype. Must be one of: {", ".join(valid_usertypes)}'}, 400
    
    

    # Create a new user instance
    new_user = User(
        username=json_data['username'],
        password_hash = generate_password_hash(json_data['password']),  # Use password_hash instead of password
        usertype=json_data['usertype'],
        email=json_data['email'],
        phone=json_data['phone'],
        address=json_data['address'],
    )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'User registered successfully'}, 201


@app.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()

    # Validate required fields
    required_fields = ['username', 'password']
    for field in required_fields:
        if field not in json_data:
            return {'error': f'Missing required field: {field}'}, 400

    user = User.query.filter(User.username == json_data.get('username')).first()

    if not user:
        return {'error': 'User not found'}, 404

    if not user.authenticate(json_data.get('password')):
        return {'error': 'Invalid password'}, 401

    # Update session with user_id and user_type
    session['user_id'] = user.id
    session['user_type'] = user.usertype

    return user.to_dict(), 200  


@app.route('/check_session', methods=['GET'])
def check_session():
    user_id = session.get('user_id')

    if user_id is not None:
        user = User.query.get(user_id)
        if user:
            return user.to_dict(), 200
    return {}, 401

@app.route('/logout', methods=['DELETE'])
def logout():
    session.pop('user_id', None)
    session.pop('user_type', None)
    return {}, 204

@app.route('/clients', methods = ['GET', 'POST'])
def all_clients():
    if request.method == "GET":
        all_clients = Client.query.all()
        results = []
        for client in all_clients:
            results.append(client.to_dict())
        return results, 200
    
    elif request.method == "POST":
        json_data = request.get_json()
        new_client = Client(
            name = json_data.get('name'),
            email = json_data.get('email'),
            phone = json_data.get('phone'),
            address = json_data.get('address'),
            notes = json_data.get('notes')

        )
        db.session.add(new_client)
        db.session.commit()

        return new_client.to_dict(), 201
@app.route('/clients/<int:id>', methods = ["GET", "PATCH", "DELETE"])
def clients_by_id(id):
    client = Client.query.filter(Client.id == id).first()

    if client is None:
        return {'error':"Animal not found"}, 400
    if request.method == "GET":
        return client.to_dict(), 200
    elif request.method == "DELETE": 
        db.session.delete(client)
        db.session.commit()
        return {}, 204
    elif request.method == "PATCH":
        json_data = request.get_json()

        for field in json_data:
            if field != "client":
                setattr(client, field, json_data[field])
        
        db.session.add(client)
        db.session.commit()
    
    return client.to_dict(), 200




if __name__ == '__main__':
    app.run(port=5555, debug=True)
