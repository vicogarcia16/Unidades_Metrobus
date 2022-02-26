from typing import Optional #metodo que permite que un campo sea opcional
from pydantic import BaseModel #Estructura de una base modelo utilizada en pydantic
#Nos permite indicar el tipo de dato que es necesario ingresar, de igual manera 
#automaticamente realiza un modo de verificacion

#Unidades-------------------------------------------------------------
class Unidad(BaseModel): #Clase que estructura los datos que deseamos que se visualicen
    id: Optional[int]
    vehicle_label: int
    vehicle_current_status: int
    position_latitude: float
    position_longitude: float
    geo_point: str
    nom_alcaldia: Optional[str]
    cve_mun: Optional[int]
    
    class Config: #Class que permite configurar si es de modo ORM Object Relational Mapper
        orm_mode = True #Permite manipular la tabla o estructura como un objeto
        
class UnidadU(BaseModel): #Estructura de modelo para indicar la ubicacion de la unidad
    id: Optional[int]
    position_latitude: float
    position_longitude: float
    geo_point: str
    nom_alcaldia: Optional[str]
    cve_mun: Optional[int]
    
    class Config:
        orm_mode = True
        
#Alcaldias-------------------------------------------------------------     
class Alcaldias(BaseModel): #Estructura modelo para visualizar solo los datos que competen a las alcaldias
    cve_mun: Optional[int]
    nom_alcaldia: Optional[str]
    
    
    class Config:
        orm_mode = True