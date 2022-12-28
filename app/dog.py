from sqlalchemy import (create_engine, desc)

engine = create_engine('sqlite:///:memory:')
from models import Dog

def create_table(base):
    base.metadata.create_all(engine)
    return base

def save(session, dog):
    session.add(dog)
    session.commit()

def new_from_db(session, arg):
    return arg

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(name)).first()

def find_by_id(session, id):
    return session.query(Dog).order_by(desc(Dog.id)).first()
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.like(name)).filter(Dog.breed.like(breed)).first()

def update_breed(session, dog, breed):
    dog.breed = breed 
    session.commit()