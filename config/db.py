#Librerias y metodos necesarios para sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

file_path = os.path.abspath(os.getcwd())+"\metrobus.db"

#PostgreSQL
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@db:5432/metrobus" #Crea o lee la base de datos
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL #Se crea la comunicación con la base de datos
# ) 

#SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///"+file_path #Crea o lee la base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL #Se crea la comunicación con la base de datos
, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Se un objeto de conexión

Base = declarative_base() #Funcion que construye una clase base necesaria para la creación de la estructura de la tabla