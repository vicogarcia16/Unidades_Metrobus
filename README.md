# Unidades_Metrobus

This job consists of get requests that return lists or values from a PostgreSql or SQLite database. The database SQLITE is metrobus.db
This data has been entered from a dataset.csv file to the "unidades" table. In the code there is no INSERT query so everything is done with SELECT filters.
The intention is to upload this REST API to a DOCKER container and to be able to make the requests from there with the previously entered data.
- The main.py file is used to start the application: uvicorn main:app --reload
- Check the Docker files 

## Database Conection

In the db.py file, comment or uncomment to use the desired connection (PostgreSql or SQLite).

###PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@db:5432/metrobus" 
engine = create_engine(SQLALCHEMY_DATABASE_URL) 


###SQLite
file_path = os.path.abspath(os.getcwd())+"\metrobus.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///"+file_path #Crea o lee la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})




![listado_unidades](https://github.com/vicogarcia16/Unidades_Metrobus/blob/master/unidades.JPG)
