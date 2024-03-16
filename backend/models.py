from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

from config import db

bcrypt = Bcrypt()


class User(db.Model, SerializerMixin):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _password_hash = db.Column(db.String(100), unique = True, nullable=False)
    usertype = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    @hybrid_property
    def password_hash(self):
        """getter"""
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, new_password):
        """setter"""
        pass_hash = bcrypt.generate_password_hash(new_password.encode('utf-8'))
        self._password_hash = pass_hash.decode('utf-8')
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8')) if self._password_hash else False

    # Add relationships
    animals = db.relationship('Animal', back_populates='user')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'usertype': self.usertype,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
            
        }

    # Update serialization rules
    
    

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'
