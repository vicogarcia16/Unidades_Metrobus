#Librerias necesarias para el modelo de la tabla Unidades (Tipos de datos)
from sqlalchemy import Column, Integer, String,Float
#Se importa Base para la estructura dentro de la conexión de la bd
from config.db import Base

#Clase que estructura la tabla Unidades con cada uno de sus campos o columnas
#Aunque los datos fueran existentes dentro de la tabla, se debe crear la estructura 
#ya que sqlalchemy maneja sesiones y modelos necesarios para operar 

class Unidades(Base):
    __tablename__ = 'unidades'
    id = Column(Integer, primary_key=True) #Dato de tipo entero siendo clave primaria
    date_updated = Column(String) #Dato de tipo string (fecha de datos actualizados)
    vehicle_id = Column(Integer) #Dato de tipo entero (id del vehiculo)
    vehicle_label = Column(Integer) #Dato de tipo entero (etiqueta vehicular)
    vehicle_current_status = Column(Integer) #Dato de tipo entero (estado del vehiculo)
    position_latitude = Column(Float) #Dato de tipo flotante (posicion latitud)
    position_longitude = Column(Float) #Dato de tipo flotante (posicion longitud)
    geo_point = Column(String) # Dato de tipo string (posicion geo)
    position_speed = Column(Integer) #Dato de tipo entero
    position_odometer = Column(Integer) #Dato de tipo entero
    trip_schedule_relationship = Column(Integer) #Dato de tipo entero
    trip_id = Column(Integer) #Dato de tipo entero
    trip_start_date = Column(String) #Dato de tipo string 
    trip_route_id = Column(Integer)#Dato de tipo entero
    nom_alcaldia = Column(String) #Dato de tipo string (nombre de la alcaldia)
    cve_mun = Column(Integer) #Dato de tipo entero (clave de municipio o alcaldia)
    
    