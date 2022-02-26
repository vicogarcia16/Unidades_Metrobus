from sqlalchemy.orm import Session #Se importa la sesion de la base de datos
from sqlalchemy import func #Metodo func de sqlalchemy
from models import model #Se importa el modelo de la tabla Unidades


#Unidades-------------------------------------------------------------

#Funcion que retorna el listado de las unidades en base a un rango 
def get_unidades(db: Session, skip: int, limit: int):
    #Se retorna la consulta realizada por medio del metodo query e 
    #indicando que liste todas las unidades con all()
    return db.query(model.Unidades).offset(skip).limit(limit).all()

#Funcion que retorna la cantidad de unidades disponibles
def get_contar_unidades(db: Session):
    #Se retorna la cantidad de unidades por medio del metodo count()
    # Query indica a que modelo de tabla urilizar y agrupando los no repetidos
    return db.query(model.Unidades).group_by(model.Unidades.id).count()

#Funcion que retorna la unidad filtrado por etiqueta vehicular
def get_unidad_etiqueta(db: Session, num_label: int):
    #Se realiza la consulta en la tabla Unidades filtrando y comparando si la etiqueta
    #vehicular ingresada se encuentra dentro de los datos, si es asi se arroja el primero
    return db.query(model.Unidades).filter(model.Unidades.vehicle_label == num_label).first()

#Funcion que retorna la ubicacion de la unidad filtrada por id 
def get_unidad_ubicacion(id: int, db: Session):
     #Se realiza la consulta en la tabla Unidades filtrando y comparando si el id de la unidad
    #ingresado por el usuario se encuentra dentro de los datos, si es asi se arroja el primero
    return db.query(model.Unidades).filter(model.Unidades.id == id).first()

#Funcion que retorna las unidades filtradas por estado actual (1,2)
def get_unidades_status(status: int, db: Session):
    #La consulta hacia la tabla Unidades consiste en filtrar las unidades por status 
    #Se realiza la comparacion del dato ingresado vs el estado actual dentro de la tabla Unidades
    return db.query(model.Unidades).filter(model.Unidades.vehicle_current_status == status).all()



#Funcion que retorna las unidades filtradas por alcaldia
def get_unidades_alcaldia(alcaldia: str, db: Session):
    #La consulta hacia la tabla Unidades consiste en filtrar las unidades por alcaldia ingresada
    #Se ocupa la funcion UPPER para que permita las mayusculas y minusculas 
    #Se realiza la comparacion del dato ingresado vs las alcaldias dentro de la tabla Unidades
    return db.query(model.Unidades).filter(func.upper(model.Unidades.nom_alcaldia) == alcaldia.upper()).all()

#Funcion que retorna las unidades filtradas por clave alcaldia
def get_unidades_alcaldia_cve(cve_mun: str, db: Session):
    #Retorna el listado de las unidades por clave de alcaldia para ellos realiza una comparacion
    return db.query(model.Unidades).filter(model.Unidades.cve_mun == cve_mun).all()


#Alcaldias-------------------------------------------------------------

#Funcion que retorna la cantidad de alcaldias disponibles
def get_contar_alcaldias(db: Session):
    #La consulta realiza un conteo por de las alcaldias encontradas en la tabla Unidades
    #Mientras el registro tenga un valor se realiza el conteo agrupando y filtrando los no repetidos
    return db.query(model.Unidades.nom_alcaldia).where(model.Unidades.nom_alcaldia != "null" ).group_by(model.Unidades.nom_alcaldia).count()

#Funcion que retorna el listado de alcaldias disponibles dependiendo un rango deseado
def get_alcaldias(db: Session, skip: int, limit: int):
    #Consulta realizada a la tabla Unidades para filtrar las alcaldias disponibles para ello se realiza una comparativa
    #mientras los datos no sean nulos
    return db.query(model.Unidades.cve_mun, model.Unidades.nom_alcaldia).where(model.Unidades.nom_alcaldia != "null" ).group_by(model.Unidades.nom_alcaldia,model.Unidades.cve_mun).offset(skip).limit(limit).all()

