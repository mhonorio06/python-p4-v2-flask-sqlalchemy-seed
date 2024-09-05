#!/usr/bin/env python3
#server/seed.py
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    #Create and initialize a faker generator
    fake = Faker()

    #Delete all rows in the pets query:
    Pet.query.delete()

    # Create an empty list
    pets = []
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add some Pet instances to the list
    pets.append(Pet(name = "Fido", species = "Dog"))
    pets.append(Pet(name = "Whiskers", species = "Cat"))
    pets.append(Pet(name = "Hermie", species = "Hamster"))
    pets.append( Pet (name = "Slither", species = "Snake"))

    #adding pet instances to the list
    for n in range(1,10):
        pet = Pet(name = fake.name(), species = rc(species))
        pets.append(pet)

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()