#Desarrollado por Víctor García
import uvicorn
from fastapi import Depends,HTTPException, FastAPI #Libreria de FastAPI que importa lo necesario
from typing import List #Libreria para el tipo de dato Lista
from sqlalchemy.orm import Session #Libreria que nos permite conectar con la base de datos
from config.db import SessionLocal, engine #Libreria para las depencdencias de bd
from routes import unidades #Importación de las funciones que realizan las querys
from models import model #importación del modelo de la tabla de la bd
from schemas import schema #importación de la configuración de los datos hacia el cliente

model.Base.metadata.create_all(bind=engine) #Se crea el modelo o estructura de la tabla Unidades

#Creación del servidor con una configuración personalizada
app=FastAPI(
    title = "Unidades del Metrobus",
    description = "Data Pipeline en FastAPI",

    docs_url='/', #Interaccion con Swagger UI 
    redoc_url='/redoc' #Documentacion ReDoc
    )   

# Dependencia para la conexión con la base de datos
def get_db():
    db = SessionLocal()#Se crea un objeto de conexión bd
    try:
        yield db
    finally:
        db.close()

#Unidades-------------------------------------------------------------

#Ruta que utiliza un metodo get para solicitar peticiones al servidor
#En este caso retorna la cantidad de unidades disponibles en la tabla Unidades
@app.get('/unidades/cantidad', tags=["Unidades"])
def cantidad_de_unidades_disponibles(db: Session = Depends(get_db)):#Función que recibe la sesión actual con la bd
    contador_unidades = unidades.get_contar_unidades(db=db) #Función que desarrolla el proceso de query
    return f'Cantidad de unidades = {contador_unidades}'#Retonrna la cantidad de unidades

#Ruta que utiliza un metodo get para solicitar peticiones al servidor
#Lo que retorna es un listado de las unidades disponibles en la tabla Unidades
@app.get('/unidades', response_model=List[schema.Unidad], tags=["Unidades"]) #Recibe el schema con los datos deseados a mostrar 
def unidades_disponibles(skip: int = 0, limit: int = 207, db: Session = Depends(get_db)):#Recibe la sesion de bd, asi como el rango de datos aproximado
    contador_unidades = unidades.get_contar_unidades(db=db)#Función que retorna la cantidad de unidades
    
    if limit > contador_unidades:#Si el limite del rango solicitado por el usuario es mayor que la cantidad
        raise HTTPException(status_code=400, detail = f"¡Has sobrepasado el limite de {contador_unidades} datos existentes!")#Se envia un mensaje de error
    #Funcion que desarrolla la consulta para listar las unidades dependiendo del rango deseado
    listar_unidades = unidades.get_unidades(db=db, skip=skip, limit=limit)
    return  listar_unidades #Retorna el listado de unidades

#Ruta que utiliza un metodo get para solicitar peticion retornando una unidad por etiqueta vehicular
@app.get('/unidades/etiqueta/{num_label}', response_model=schema.Unidad, tags=["Unidades"])#Recibe un schema para la estructura de datos a mostrar
def unidad_por_num_etiqueta_vehicular(num_label: int, db: Session = Depends(get_db)): #Recibe una variable tipo entero num]_label, la sesion de base de datos
    unidad_num_etiqueta = unidades.get_unidad_etiqueta(db=db, num_label=num_label) #Realiza el filtrado por etiqueta vehicular de la unidad
 
    if unidad_num_etiqueta == None: #si la etiqueta devuelve un None es que no se encuentra en la base de datos
        raise HTTPException(status_code=400, detail = f"¡La etiqueta vehicular {num_label} no existe en los datos!")#Se envia un mensaje de error
    
    return unidad_num_etiqueta #Retorna la unidad por etiqueta vehicular

#Ruta que utiliza un metodo get para retorna la ubicacion de la unidad solicitada 
@app.get('/unidades/ubicacion/{id}', response_model=schema.UnidadU, tags=["Unidades"]) #Recibe un schema con la estructura de datos a mostrar
def ubicacion_de_unidad_por_id(id: int, db: Session = Depends(get_db)): #Funcion que recibe el id y la sesion hacia la bd
    ubicacion = unidades.get_unidad_ubicacion(db=db, id=id)#Se realiza la busqueda en la base de datos por el id 
    if ubicacion == None: #Si el id no se encuentra en la base de datos retornando None
        raise HTTPException(status_code=400, detail = f"¡El id {id} no existe en los datos!")# Se envia un mensaje de error
    
    return ubicacion #Retonrna la ubicacion por medio del id de la unidad

#Ruta que utiliza un metodo get para retornar las unidades dependíendo de su estado actual (1 o 2)
@app.get('/unidades/status/{status}', response_model=List[schema.Unidad], tags=["Unidades"])#Recibe un schema con la estructura de datos a mostrar
def unidades_por_estado_actual(status: int, db: Session = Depends(get_db)): #Funcion que recibi una variable status como tipo de dato entero y la sesion hacia la bd
    unidades_status = unidades.get_unidades_status(db=db, status=status) #Se realiza el filttrado de las unidades por estado actual
    if unidades_status == []: #Si no se encuentra ningun dato correspondiente al estado actual ingresada
        raise HTTPException(status_code=400, detail = f"¡El estado {status} no existe en los datos!, ingresa 1 o 2") #Se envia un mensaje de error
   
    return unidades_status #Retorna un listado de unidades por estado actual (1 o 2)

#Ruta que utiliza un metodo get para retornar las unidades que se encuentran dentro de una alcaldia
@app.get('/unidades/alcaldia/{alcaldia}', response_model=List[schema.Unidad], tags=["Unidades"])#Recibe un schema con la estructura de datos a mostrar
def unidades_por_alcaldia(alcaldia: str,  db: Session = Depends(get_db)): #Funcion que recibi una variable alcaldia como tipo de dato string y la sesion hacia la bd
    unidades_alcaldia = unidades.get_unidades_alcaldia(db=db, alcaldia=alcaldia) #Se realiza el filttrado de las unidades por la alcadia ingresada
    if unidades_alcaldia == []: #Si no se encuentra ningun dato correspondiente a la alcaldia ingresada
        raise HTTPException(status_code=400, detail = f"¡La alcadia {alcaldia} no existe en los datos!") #Se envia un mensaje de error
   
    return unidades_alcaldia #Retorna un listado de unidades por alcaldia

#Ruta que utiliza un metodo get para retornar unidaddes por clave de alcaldia
@app.get('/unidades/alcaldia_cve/{cve_mun}', response_model=List[schema.Unidad], tags=["Unidades"])#Recibe un schema con la estructura de datos a mostrar
def unidades_por_clave_de_alcaldia(cve_mun: int, db: Session = Depends(get_db)): #Funcion que recibe una variable cve_mun de tipo entero y la sesion hacia la bd
    unidades_alcaldia_cve = unidades.get_unidades_alcaldia_cve(db=db, cve_mun=cve_mun) #Se realiza el filtrado o busqueda de unidades por clave de alcaldia
    if unidades_alcaldia_cve == []: #Si no se encuentra ningun dato con la clave ingresada
        raise HTTPException(status_code=400, detail = f"¡La clave de municipio {cve_mun} no existe en los datos!")#Envia un mensaje de error
    
    return unidades_alcaldia_cve #Retorna un listado de unidades por clave de alcaldia


#Alcaldias-------------------------------------------------------------

#Ruta que utiliza un metodo get para retornar la cantidad de alcaldias en la tabla Unidades
@app.get('/alcaldias/cantidad', tags=["Alcaldias"])
def cantidad_de_alcaldias_disponibles(db: Session = Depends(get_db)):#Funcion que recibe una sesion de base de datos
    contador_alcaldias = unidades.get_contar_alcaldias(db=db)#Función que realiza el conteo de alcaldias disponibles
    return f'Cantidad de alcaldias disponibles = {contador_alcaldias}'# Retorna la cantidad de alcaldias

#Ruta que utiliza un metodo get para listar las alcaldias disponibles en la tabla Unidades
@app.get('/alcaldias', response_model=List[schema.Alcaldias], tags=["Alcaldias"])#Recibe un schema con la estructura de datos a mostrar
def alcaldias_disponibles(skip: int = 0, limit: int = 11, db: Session = Depends(get_db)):#Recibe la sesion de bd, asi como el rango de datos aproximado
    contador_alcaldias = unidades.get_contar_alcaldias(db=db)#Contador de alcaldias disponibles
    
    if limit > contador_alcaldias:#Si el limite ingresado por el usuario es mayor que el contador de alcaldias disponibles
        raise HTTPException(status_code=400, detail = f"¡Has sobrepasado el limite de {contador_alcaldias} datos existentes!")#Se envia un mensaje de error
    
    listar_alcaldias = unidades.get_alcaldias(db=db, skip=skip, limit=contador_alcaldias)
    return  listar_alcaldias #Retorna el listado de alcaldias disponibles

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)