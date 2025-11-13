from wtforms import Form
from wtforms import StringField, EmailField, PasswordField, IntegerField, RadioField, SelectMultipleField
from wtforms import FloatField  
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField('Matricula', [validators.DataRequired(message="La matricula es obligatoria")])
    nombre =StringField('Nombre', [validators.DataRequired(message="El campo es requerido")])
    apellido = StringField('Apellido', [validators.DataRequired(message="El campo es requerido")])
    correo = StringField('Correo', [validators.DataRequired(message="El campo es requerido")])
    
    
    
class AreaForm(Form):
    X1 = IntegerField('X1', [validators.DataRequired(message="La matricula es obligatoria")])
    X2 = IntegerField('X2', [validators.DataRequired(message="El campo es requerido")])
    
    
    
class PizzaForm(Form):
    nombre = StringField('Nombre', [validators.DataRequired(message="El campo es requerido")])
    direccion = StringField('Direccion', [validators.DataRequired(message="El campo es requerido")])
    telefono = IntegerField('Telefono', [validators.DataRequired(message="El campo es requerido")])
    numeroPizzas = IntegerField('Num. Pizzas', [validators.DataRequired(message="El campo es requerido")])
    tamaño = RadioField('Tamaño', choices=[
        ('Chica', 'Chica'),
        ('Mediana', 'Mediana'),
        ('Grande', 'Grande')
    ], validators=[validators.DataRequired(message="Selecciona un tamaño")])
    ingredientes = SelectMultipleField('Ingredientes', choices=[
        ('Jamon', 'Jamón'),
        ('Piña', 'Piña'),
        ('Champiñones', 'Champiñones')
    ])

