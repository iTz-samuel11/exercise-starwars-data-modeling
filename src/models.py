import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def serialize(self):
        return{
            "id": self.id,
            "usermane": self.name,
            "password": self.password
        }

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class Favorite_Planet(Base):
    __tablename__ = 'favorite planet' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

    def to_dict(self):
        return {}
    
class Favorite_Character(Base):
    __tablename__ = 'favorite character' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Planet(Base):
    __tablename__ = 'planet' 
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    climate = Column(String(100))
    diameter = Column(Integer)
    population = Column(Integer)
    terrain = Column(Integer)

class Character(Base):
    __tablename__ = 'character' 
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(Integer)
    films = Column(String(250))
    gender = Column(String(250))
    eye_color = Column(String(250))


render_er(Base, 'diagram.png')