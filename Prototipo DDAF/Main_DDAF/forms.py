from django import forms
from .models import Cursos, Usuarios, CursosDDAF, asistencia
from multiselectfield import MultiSelectField


class Formulario(forms.Form):
    nombre = forms.CharField(label='Ingrese Nombre',widget=forms.TextInput(
        attrs={
            'class':'form-control',


        }))

    apellido = forms.CharField(label='Ingrese Apellido',widget=forms.TextInput(
        attrs={
            'class':'form-control',


        }))
    rut = forms.CharField(label='Ingrese RUT',widget=forms.TextInput(
        attrs={
            'class':'form-control',


        }))
    direccion = forms.CharField(label='Ingrese Direccion',widget=forms.TextInput(
        attrs={
            'class':'form-control',


        }))
    puntaje_psu = forms.IntegerField(label='Ingrese Puntaje_PSU',widget=forms.TextInput(
        attrs={'class':'form-control',
            'type':'number'}))
    
    email = forms.CharField(label='Ingrese Email',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'type':'mail',


        })) 

    username = forms.CharField(label='Ingrese username',widget=forms.TextInput(
        attrs={
            'class':'form-control',


        }))

    password = forms.CharField(label='Ingrese Password',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'type':'password'


        })) 
    password2 = forms.CharField(label='Reingrese Password',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'type':'password'

        })) 

#horarios ocupados:
HORARIOS_OCUPADOS=[]
HORARIOS_BASE1 = CursosDDAF.objects.distinct()
HORARIOS_BASE2 = []

HORARIOS_DISPONIBLES = []

for cursos in HORARIOS_BASE1:
    HORARIOS_BASE2.append((cursos.horario,cursos.nombre))

for (v,k) in HORARIOS_BASE2:
    HORARIOS_OCUPADOS.append(int(v))
#todos los horarios disponibles
HORARIOS_INICIALES=[(7,'08:00-08:30'),(8,'8:30-9:00'),(9,'9:00-9:30'),(10,'9:00-9:30'),(11,'9:00-9:30'),(12,'9:00-9:30'),(13,'9:00-9:30')]

for v in HORARIOS_INICIALES:
    if v[0] not in HORARIOS_OCUPADOS:
        HORARIOS_DISPONIBLES.append((v[0],str(v[0])+":00"))

PISTAS = [(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6")]
DIAS = [("lunes-miércoles-viernes","lunes-miércoles-viernes"),("martes-jueves-sábado","martes-jueves-sábado")]

class FormularioCursos(forms.Form):
    nombre = forms.CharField(label='Ingrese Nombre del curso',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            }))
    tipo = forms.CharField(label='Ingrese Tipo de Curso',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            }))

    horario = forms.IntegerField(label='Ingrese Horario',widget=forms.Select(choices=HORARIOS_DISPONIBLES))
    profesor = forms.CharField(label='¿Qué profesor se asigna al curso?', widget=forms.TextInput(attrs={
            'class':'form-control',
            }))
    pista = forms.IntegerField(label='¿Qué pista se utilizara?', widget=forms.Select(choices=PISTAS))
    dias =  forms.CharField(label='¿Qué días seran los cursos?', widget=forms.Select(choices=DIAS))


    # 6 a 23


'''
#Versión vieja

class Asistencia(forms.Form):
    ALUMNOS =(('CARLOS','CARLOS'),('ADRIANA','ADRIANA'),)

    nombre_alumno =forms.MultiChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices = ALUMNOS)

'''

Alumnos = (('pepito','pepito'),('juanito','juanito'),)

class TestForm(forms.Form):
    test = forms.MultipleChoiceField(choices=Alumnos, widget=forms.CheckboxSelectMultiple(), required=False)
    def __init__(self, pk=None, *args, **kwargs):
        # we explicit define the foo keyword argument, cause otherwise kwargs will 
        # contain it and passes it on to the super class, who fails cause it's not
        # aware of a foo keyword argument.
        super(TestForm, self)#.__init__(*args, **kwargs)
        print(pk)  # prints the value of the foo url conf param
  

