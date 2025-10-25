from flask import Flask, render_template, request

app =  Flask(__name__)

@app.route('/')
def home():
    return "Hello, World"


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