import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('DBJUAN.db')
c = conn.cursor()
resp = 'si'


def create_table():
    try:
        c.execute(
                '''CREATE TABLE Empleados(ID INTEGER PRIMARY KEY,
         NAME TEXT NOT NULL,
         AGE INT NOT NULL);''')
        time.sleep(3)
    except Exception as e:
        print("Error vuelte a intentarlo:\nDetalles:", e.args)


def insertar():
    try:
        name = str(input("Inserte el nombre del empleado"))
        age = int(input("Edad del empleado"))
        c.execute("INSERT INTO Empleados (name, age) VALUES (?,?)", (name, age))
        conn.commit()
        time.sleep(3)
    except Exception as e:
        print("Error vuelte a intentarlo:\nDetalles:", e.args)


def close():
    c.close()
    conn.close()


def delete():
    try:
        c.execute("DROP TABLE Empleados")
        time.sleep(3)
    except Exception as e:
        print("Error vuelte a intentarlo:\nDetalles:", e.args)


def date_time():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%y-%m-%d %H:%M:%S'))
    print(unix)
    print(date)


def read_from_db():
    c.execute('SELECT * FROM Empleados')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)

try:
    while resp == 'si':
        opc = input('\nData Base Juan prueba'
                    '\n1.Crear Tabla\n2.Insertar Datos\n3.Borrar la tabla actual'
                    '\n4.Cerrar coneccion\n5.Time\nDigite la funcion que utilizara:')
        if opc == '1':
            create_table()
        if opc == '2':
            insertar()
        if opc == '3':
            delete()
        if opc == '4':
            close()
        if opc == '5':
            date_time()
        if opc == '6':
            read_from_db()
except Exception as e:
    ram = random.randrange(1100)
    print("\n(BROMA)Error#", ram, " : ", e.args,"\nTienes 5 segundos para analisar el problema antes que cierre")
    time.sleep(5)
