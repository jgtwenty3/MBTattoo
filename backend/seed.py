from config import app, db
from models import User, Client, ConsentForm, Appointment
from faker import Faker
from random import choice as rc, randint

if __name__ == '__main__':
    fake = Faker()
    
    with app.app_context():
        print("Starting seed...")

        # Seed Users
        for _ in range(10):  # Adjust the number of users you want
            user = User(
                username=fake.user_name(),
                password_hash=fake.password(),
                usertype=rc(['admin', 'artist']),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
            )
            db.session.add(user)
        db.session.commit()  # Commit users first to get valid user IDs

        # Seed Clients and Consent Forms
        for _ in range(20):  # Adjust the number of clients you want
            user = User.query.get(randint(1, User.query.count()))  # Get a random user
            client = Client(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                date_of_birth=fake.date_of_birth(),
                address=fake.address(),
                notes=fake.text(),
                user=user,
            )
            db.session.add(client)
            
            consent_form = ConsentForm(
                client=client,
                waive_and_release=fake.boolean(),
                questions=fake.boolean(),
                aftercare=fake.boolean(),
                drugs_or_booze=fake.boolean(),
                health_conditions=fake.sentence(),
                spelling_responsibility=fake.boolean(),
                no_refund=fake.boolean(),
                attorney_fees=fake.boolean(),
                photographic_consent=fake.boolean(),
                name=fake.name(),
                date_of_birth=fake.date_of_birth(),
                street_address=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                date_signed=fake.date_time_this_year(),
                signature=fake.image_url(width=100, height=100),  # Fake signature as image URL
            )
            db.session.add(consent_form)

        db.session.commit()

        # Seed Appointments
        for _ in range(30):  # Adjust the number of appointments you want
            client = Client.query.get(randint(1, Client.query.count()))  # Get a random client
            user = User.query.get(randint(1, User.query.count()))  # Get a random user
            appointment = Appointment(
                client=client,
                user=user,
                appointment_datetime=fake.date_time_this_year(),
                duration_minutes=randint(30, 240),
                notes=fake.text(),
            )
            db.session.add(appointment)

        db.session.commit()

    print("Seed completed!")