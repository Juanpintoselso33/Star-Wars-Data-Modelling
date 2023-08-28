import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY, BigInteger, Text, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    name = Column(String)
    favourites = Column(ARRAY(Integer), ForeignKey('favourite.id_fav'))

class Favourite(Base):
    __tablename__ = 'favourite'
    id_fav = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id_user'))
    id_favourite_planet = Column(Integer, ForeignKey('planet.id'))
    id_favourite_person = Column(Integer, ForeignKey('person.id'))
    id_favourite_film = Column(Integer, ForeignKey('film.id'))
    id_favourite_starship = Column(Integer, ForeignKey('starship.id'))
    id_favourite_vehicle = Column(Integer, ForeignKey('vehicle.id'))

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    homeworld = Column(String)
    url = Column(String)
    description = Column(String)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String)
    population = Column(Integer)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)
    url = Column(String)
    description = Column(String)

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    episode_id = Column(Integer)
    director = Column(String)
    producer = Column(String)
    release_date = Column(String)
    opening_crawl = Column(String)
    url = Column(String)
    description = Column(String)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    starship_class = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(String)
    passengers = Column(String)
    max_atmosphering_speed = Column(String)
    hyperdrive_rating = Column(String)
    MGLT = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    url = Column(String)
    description = Column(String)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    vehicle_class = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(Integer)
    length = Column(String)
    crew = Column(String)
    passengers = Column(String)
    max_atmosphering_speed = Column(String)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    url = Column(String)
    description = Column(String)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
