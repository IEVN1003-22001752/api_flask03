from flask import Flask, jsonify, request

from flask_mysqldb import MySQL

from flask_cors import CORS

from config import config

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/alumnos', methods=['GET'])
def listar_alumnos():
    try: 
        cursor = conexion.connection.cursor()
        sql = "SELECT matricula, nombre, apaterno, amaterno, correo FROM alumnos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        alumnos = []
        for fila in datos:
            alumno = {
                'matricula': fila[0],
                'nombre': fila[1],
                'apaterno': fila[2],
                'amaterno': fila[3],
                'correo': fila[4]
            }
            alumnos.append(alumno)
        return jsonify({'alumnos': alumnos, 'mensaje': 'Alumnos encontrados', 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': 'Error al obtener alumnos: ' + str(ex), 'exito': False})
        
        

    
    
def leer_alumnos_db():
    try:
        cursor = conexion.connection.cursor()  # Corregido: se necesita cursor real
        sql = "SELECT matricula, nombre, apaterno, amaterno, correo FROM alumnos"
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos is not None:
            alumno = {
                'matricula': datos[0],
                'nombre': datos[1],
                'apaterno': datos[2],
                'amaterno': datos[3],
                'correo': datos[4]
            }
            return alumno
        else:
            return None
    except Exception as ex:
        raise ex
    
    
@app.route('/alumnos/<mat>', methods=['GET'])
def leer_curso(mat):
    try:
        alumno = leer_alumnos_db()
        if alumno != None:
            return jsonify({'alumno': alumno, 'mensaje': 'Alumno encontrado', 'exito': True})
        else:
            return jsonify({'mensaje': 'Alumno no encontrado', 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'exito': False})
    
    
    
def paguina_no_encontrada(error):
    return jsonify({'mensaje': '<h1>La página que intenta buscar no existe</h1>'})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, paguina_no_encontrada)
    app.run()
        
