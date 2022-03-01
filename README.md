# Unidades_Metrobus

Creación e implementación de una API REST que muestra datos referentes a las unidades del Metrobus CDMX. Dichos datos fueron exportados de [Datos abiertos de México](https://datos.cdmx.gob.mx/dataset/prueba_fetchdata_metrobus/resource/ad360a0e-b42f-482c-af12-1fd72140032e). No obstante, fueron añadidos en un archivo [dataset.csv](https://github.com/vicogarcia16/Unidades_Metrobus/blob/master/dataset.csv) para su posterior uso, asi como, se le asignaron las alcaldias a cada unidad.

En la siguiente imagen se muestran las funciones o peticiones GET con las que cuenta esta API:
![Listado de funciones](https://github.com/vicogarcia16/Unidades_Metrobus/blob/master/diagrama/listado_peticiones_GET.JPG)

## Diagrama de solución :printer:

Para observar como se llevo a cabo el procedimiento para la solución, se ha realizado un diagrama en el cual se explican las herramientas y pasos que se tomaron para dicho fin. Este se encuentra en la carpeta [diagrama](https://github.com/vicogarcia16/Unidades_Metrobus/tree/master/diagrama) de este repositorio contando con un archivo PDF o JPEG.

## Pre requisitos 	:pushpin:

* Descargar o clonar el repositorio donde se desee: **git clone https://github.com/vicogarcia16/Unidades_Metrobus**

## Bases de datos :dvd:

Por defecto y de manera local la API trabaja con la base de datos SQLite [metrobus.db](https://github.com/vicogarcia16/Unidades_Metrobus/blob/master/metrobus.db). Sin embargo, si se deseará trabajar en Docker, comentar sus lineas y descomentar las lineas correspondientes de PostgreSQL en el archivo [db.py](https://github.com/vicogarcia16/Unidades_Metrobus/blob/master/config/db.py).

### SQLite

file_path = os.path.abspath(os.getcwd())+"\metrobus.db"

SQLALCHEMY_DATABASE_URL = "sqlite:///"+file_path 

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

### PostgreSQL

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@db:5432/metrobus" 

engine = create_engine(SQLALCHEMY_DATABASE_URL) 


## Instalación 🔧

### Local
* Abrir una ventana CMD y rear un entorno virtual para Python si se desea trabajar en local. Ejem. **python3 -m venv fastapi-env**, activarlo con **fastapi-env\Scripts\activate.bat**. Posteriormente ejecutar el archivo requirements.txt con **pip install -r requirements.txt**

### Docker
* Si se requiere ejecutar en Docker, favor de realizar el siguiente comando en una ventana CMD: **docker-compose up -d** 
* Importar los datos de dataset.csv si en dado caso no se visualizan en la API.

## Ejecución del software ⚙️
### Local
* Ejecutar el comando en cmd o terminal [uvicorn main:app --reload]
* Posteriormente acceder a la url por defecto [127.0.0.1:8000]
### Docker
* Si ha realizado la imagen Docker ejecutar el contenedor creado "micro-service-fastapi" y posteriormente abrir el navegador en la URL: [localhost:5000]

## Video Demo :film_strip:

[![Alt text](https://img.youtube.com/vi/6EVTI3JVqFk/0.jpg)](https://www.youtube.com/watch?v=6EVTI3JVqFk)

## Construido con 🛠️

* [Python](https://www.python.org/) - Lenguaje de programación
* [SQLite](https://www.sqlite.org/index.html) - Base de datos
* [PostgreSQL](https://www.postgresql.org/) - Base de datos
* [FastAPI](https://fastapi.tiangolo.com/) - Framework Web
* [SQL Alchemy](https://www.sqlalchemy.org/) - Kit de herramientas SQL para Python

## Autor ✒️

* **Víctor García** [vicogarcia16](https://github.com/vicogarcia16) 
