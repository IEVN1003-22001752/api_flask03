from flask import Flask, render_template, request, make_response, jsonify
import forms
import math
import json
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms import validators

app =  Flask(__name__)








@app.route('/')
def home():
    return "Hello, World"






@app.route('/Pizzeria', methods=['GET', 'POST'])
def pizzeria():
    pizzas_clase = forms.PizzaForm(request.form)
    pizzas = []
    totalDia = 0
    total = 0

    # Leer cookies previas
    pizzas_cookie = request.cookies.get('pizzas')
    total_cookie = request.cookies.get('totalDia')

    if pizzas_cookie:
        pizzas = json.loads(pizzas_cookie)
    if total_cookie:
        totalDia = float(total_cookie)

    if request.method == 'POST' and pizzas_clase.validate():
        nombre = pizzas_clase.nombre.data
        direccion = pizzas_clase.direccion.data
        telefono = pizzas_clase.telefono.data
        numeroPizzas = pizzas_clase.numeroPizzas.data
        tamaño = pizzas_clase.tamaño.data
        ingredientes = pizzas_clase.ingredientes.data

        # Calcular total base según tamaño
        if tamaño == "Chica":
            total = 40
        elif tamaño == "Mediana":
            total = 80
        elif tamaño == "Grande":
            total = 120

        total =  total * numeroPizzas

        if ingredientes:
            total += len(ingredientes) * 10

        # Crear pedido
        datos = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'numeroPizzas': numeroPizzas,
            'tamaño': tamaño,
            'ingredientes': ', '.join(ingredientes),
            'total': total
        }

        pizzas.append(datos)
        totalDia += total

    # Preparar respuesta con cookies actualizadas
    response = make_response(render_template(
        'Pizzeria.html',
        form=pizzas_clase,
        pizzas=pizzas,
        total=total,
        totalDia=totalDia
    ))

    response.set_cookie('pizzas', json.dumps(pizzas))
    response.set_cookie('totalDia', str(totalDia))
    return response


@app.route('/get_coockies')
def get_cookies():
    datos_str=request.cookies.get('pizzas')
    if not datos_str: 
        return "No hay datos"
    datos=json.loads(datos_str)
    return jsonify(datos)



    













    


@app.route('/Alumnos', methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    estudiantes=[]
    datos={}
    
    alumnos_clase=forms.UserForm(request.form)
    if request.method == 'POST'and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
        datos={'matricula':mat,'nombre':nom,'apellido':ape,'correo':em}
        
        datos_str=request.cookies.get('estudiantes')
        if not datos_str: 
            return "No hay datos"
        tem=json.loads(datos_str)
        estudiantes=tem
        print(type(estudiantes))
        estudiantes=json.loads(datos_str)
        estudiantes.append(datos)
                
    response=make_response(render_template('Alumnos.html',form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em))
    response.set_cookie('estudiantes', json.dumps(estudiantes))
    return response





@app.route('/get_coockie')
def get_cookie():
    datos_str=request.cookies.get('estudiantes')
    if not datos_str: 
        return "No hay datos"
    datos=json.loads(datos_str)
    return jsonify(datos)











@app.route('/Figuras', methods=['GET', 'POST'])
def figuras():
    X1 = 0 
    X2 = 0
    res = 0
    figura = ""
    
    figuras_clase = forms.AreaForm(request.form)
    
    if request.method == 'POST':
        X1 = figuras_clase.X1.data
        X2 = figuras_clase.X2.data
        figura = request.form.get('figura')
        
        if figura == 'Triangulo':
            res = (X1 * X2) / 2
        elif figura == 'Cuadrado':
            res = X1 * X2
        elif figura == 'Circulo':
            res = 3.1416 * math.pow(X1, 2)
        elif figura == 'Pentagono':
            res = (5 * X1 * X2) / 2
            
    return render_template('figuras.html', form=figuras_clase, res=res)
















@app.route('/about')
def about():
    return "<h1>This is the about page.</h1>"

@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user 

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero {} " .format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}" .format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1, n2):
    return "ID: {} nombre: {}" .format(id, username)




@app.route("/operas", methods=['GET', 'POST'])
def operas():
    
    if request.method=='POST':
        x1=int(request.form.get('x1'))
        
        x2=int(request.form.get('x2'))
        resultado=x1+x2
        return render_template('operas.html', resultado=resultado)
    
    return render_template('operas.html')

@app.route("/distancia")
def distancia():
    return render_template('distancia.html')






@app.route("/index")
def index():
    titulo="IEVN1003-PWA"
    listado=["Opera 1","Opera 2","Opera 4"]
    return render_template('index.html', titulo=titulo, listado=listado)



@app.route("/prueba")
def prueba():
    return '''
    <h1> Prueba de HTML </h1>
    <P> Esto es un parrrafo </P>
    <ul>
    <li> Elemento 1 </li>
    <li> Elemento 2 </li>
    <li> Elemento 3 </li>
    <li> Elemento 4 </li>
    
    </ul>
    '''
    
    
    
    
    


if __name__ == '__main__':
    app.run(debug=True)