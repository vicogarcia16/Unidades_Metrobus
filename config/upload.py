import sqlite3
import csv
import os

file_path = os.path.abspath(os.getcwd())+"\metrobus.db"
file_path_csv = os.path.abspath(os.getcwd())+"\dataset.csv"
#Abrimos el archivo CSV
f=open(file_path_csv,'r') 
#Omitimos la linea de encabezado
next(f, None)
reader = csv.reader(f, delimiter=';')

#Crea la BD en la carpeta donde se encuentra el script
sql = sqlite3.connect(file_path)
cur = sql.cursor()

#Creamos la tabla si no existe
cur.execute('''CREATE TABLE IF NOT EXISTS unidades
            (posicion integer primary key autoincrement, 
            date_updated text, vehicle_id integer, vehicle_label text
            vehicle_current_status integer, position_latitude real, position_longitude real,
            geo_point text, position_speed integer, position_odometer integer,
            trip_schedule_relationship, trip_id integer, trip_start_date text, 
            trip_route_id integer, nom_alcaldia text, cve_mun integer 
            )''')

#Llenamos la BD con los datos del CSV
for row in reader:
    cur.execute("""INSERT INTO posiciones VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                , ?, ?, ?, ?, ?, ?)""", (row[0], row[1], row[2], row[3], row[4]
                                         , row[5], row[6], row[7], row[8], row[9]
                                         , row[10], row[11], row[12], row[13], row[14]
                                         , row[15]))

#Muestro las filas guardadas en la tabla
for row in cur.execute('SELECT * FROM unidades'):
    print(row)

#Cerramos el archivo y la conexion a la bd
f.close()
sql.commit()
sql.close()