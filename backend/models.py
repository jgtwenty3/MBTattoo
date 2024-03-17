from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from sqlalchemy.orm import relationship

from config import db

bcrypt = Bcrypt()


class User(db.Model, SerializerMixin):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _password_hash = db.Column(db.String(100), nullable=False)  
    usertype = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    clients = relationship("Client", back_populates="user")
    appointments = relationship("Appointment", back_populates="user")

    @hybrid_property
    def password_hash(self):
        """getter"""
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, new_password):
        """setter"""
        pass_hash = bcrypt.generate_password_hash(new_password.encode('utf-8'))
        self._password_hash = pass_hash.decode('utf-8')  # Set the password hash here
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8')) if self._password_hash else False

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'usertype': self.usertype,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

class Client(db.Model, SerializerMixin):
    __tablename__='clients'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    notes = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship("User", back_populates="clients")
    consent_form = relationship("ConsentForm", back_populates="client", uselist=False)
    appointments = relationship("Appointment", back_populates="client")

    def __repr__(self):
        return f'<Client {self.id}: {self.name}>'

class ConsentForm(db.Model,SerializerMixin):
    __tablename__ = 'consent_forms'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), unique=True, nullable=False)
    
    
    waive_and_release = db.Column(db.Boolean, nullable = False, default = False)
    questions = db.Column(db.Boolean, nullable=False, default=False)
    aftercare = db.Column(db.Boolean, nullable=False, default=False)
    drugs_or_booze = db.Column(db.Boolean, nullable=False, default=False)
    health_conditions = db.Column(db.String(), nullable=False)
    spelling_responsibility = db.Column(db.Boolean, nullable=False, default=False)
    no_refund = db.Column(db.Boolean, nullable=False, default=False)
    attorney_fees = db.Column(db.Boolean, nullable=False, default=False)
    photographic_consent = db.Column(db.Boolean, nullable=False, default=False)

    name =  db.Column(db.String(75), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    street_address = db.Column(db.String(255), nullable=False)
    city =  db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(30), nullable = False)

    date_signed = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    signature = db.Column(db.String(), nullable=False)

    client = relationship("Client", back_populates="consent_form")

    def __repr__(self):
        return f'<ConsentForm {self.id} for Client {self.client_id}>'

class Appointment(db.Model,SerializerMixin):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    appointment_datetime = db.Column(db.DateTime, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    client = relationship("Client", back_populates="appointments")
    user = relationship("User", back_populates="appointments")

    def __repr__(self):
        return f'<Appointment {self.id} for Client {self.client_id} at {self.appointment_datetime}>'
   
    
    
    



    
