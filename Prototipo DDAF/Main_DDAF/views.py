from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Formulario, FormularioCursos, TestForm
from django.core.files.storage import FileSystemStorage
from .models import Cursos,Usuarios, CursosDDAF, Cursos_Alumno, asistencia
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView


def index(request):
    bienvenida={'titulo': 'Bienvenido al Prototipo de Control y Gestión de la Piscina','intro': '¿Qué sección quieres ver?'}
    return render(request, 'Main_DDAF/index.html', bienvenida)


def cursos(request):
    bienvenida={'titulo':'Cursos registrados', 'intro':"Nombre de los cursos rendidos almenos una vez ", 
    'cursos':Cursos.objects.values('nombre').distinct(),'cursosddaf':CursosDDAF.objects.all()}
    return render(request,'Main_DDAF/cursos.html', bienvenida)

def users(request):
    info={'titulo':'Usuarios registrados en el sistema', 'intro':"Los siguientes usuarios están registrados en nuestra base de datos",
    'user':Usuarios.objects.all(),'user_beau':Usuarios.objects.exclude(puntaje_psu__gt=740)} # se escribe como atributo__condicion = valor_buscado # esto es del tipo where usuarios.puntaje_psu>740
    return render(request,'Main_DDAF/users.html', info)

def adduser(request):
    form=Formulario()
    info={'titulo':'Agregar Usuarios', 'intro':"Registrese, Entreguenos todos sus datos aqui",'form':form} # se escribe como atributo__condicion = valor_buscado # esto es del tipo where usuarios.puntaje_psu>740
    return render(request,'Main_DDAF/adduser.html', info)
   
def added(request):
    new_user = User.objects.create_user(username = request.POST['username'], password = request.POST['password']);  
    new_user.save()
    usuario = Usuarios(nombre = request.POST['nombre'],apellido = request.POST['apellido'],
        direccion = request.POST['direccion'], rut = request.POST['rut'], puntaje_psu = request.POST['puntaje_psu'], 
        user = new_user);
    usuario.save()
    context={'Titulo':'Felicidades', 'comentario':'Te haz registrado bien!'}
    return render(request, 'Main_DDAF/error.html', context)

def reclamos(request):
    context={'texto2':'Aquí deberian ir los reclamos','texto1':'Reclamos'}
    return render(request, 'Main_DDAF/reclamos.html',context)

def indicadores(request):
    context={'texto2':'Aquí deberian ir los indicadores','texto1':'Indicadores'}
    return render(request, 'Main_DDAF/indicadores.html',context)
'''CURSOS'''    
def addcurso(request):

    form=FormularioCursos()
    context={'texto2':'Aquí deberian ir los campos del formulario','texto1':'Agregar curso','form':form}
    return render(request, 'Main_DDAF/addcurso.html',context)

def addedcurso(request):
    context={'Titulo':request.POST['nombre'], 'comentario':request.POST['tipo'],'comentario2':request.POST['horario']}
    curso = CursosDDAF(nombre=request.POST['nombre'],tipo=request.POST['tipo'],horario=request.POST['horario'],profesor=request.POST['profesor'],
        pista=request.POST['pista'],días=request.POST['dias'],capacidad=int(request.POST['pista'])*10)
    curso.save()
    return render(request, 'Main_DDAF/addedcurso.html', context)

def inscribircurso(request,pk):
    #guardo el user ingresado en el login
    usuario=request.session['user']
    #obtengo el id asociado a ese user del modelo User de Django
    usuarioobj=User.objects.values_list('id', flat=True).get(username=usuario)
    #Genero el objeto CursoDDAF asociado al id ingresado
    t=CursosDDAF.objects.get(id=pk)
    #Actualizo la capacidad del curso
    if int(t.capacidad)>0:
        a=int(t.capacidad)-1
        t.capacidad=a
        print(usuarioobj)
        if Cursos_Alumno.objects.filter(glosa_alumno=usuario, glosa_curso=t.nombre):
            context={'texto3':"Ya estás inscrite en este curso, intenta otro.",'texto1':request.session['user']}
            return render(request,'Main_DDAF/curso_inscrito.html',context)
            
        else:
            print("no existe")
            #Aquí se genera el objeto "Cursos_alumnos" definido en el modelo con 5 columnas [id,id_curso,glosa_curso,id_alumno,glosa_alumno]
            curso_alumno=Cursos_Alumno(glosa_curso=t.nombre, glosa_alumno=usuario, id_curso=t.id, id_alumno=usuarioobj)
            curso_alumno.save()
            t.save()
            context={'texto4':'En el horario:'+t.horario,'texto2':'Curso inscrito:'+t.nombre,'texto1':request.session['user']}
            return render(request,'Main_DDAF/curso_inscrito.html',context)

    else:
        context={'texto1':'No hay cupo para el curso seleccionado','texto2':'Por favor elegir otro curso.'}
        return render(request,'Main_DDAF/lleno.html',context)


def ver_alumnos_curso(request,pk):
    usuario=request.session['user']
    t=CursosDDAF.objects.get(id=pk)
    a=t.nombre
    print(a)
    print(Cursos_Alumno.objects.values_list('glosa_alumno', flat=True).filter(glosa_alumno=usuario))
    info={'titulo':'Usuarios registrados en el sistema', 'intro':"Los siguientes usuarios están registrados en nuestra base de datos",
    'user':Cursos_Alumno.objects.filter(glosa_curso=a).distinct()} # se escribe como atributo__condicion = valor_buscado # esto es del tipo where usuarios.puntaje_psu>740
    return render(request,'Main_DDAF/users_curso.html', info)

def asistencias(request,pk):
    print(pk+"la ide del curso es:",pk)
    form=TestForm()
    t=CursosDDAF.objects.get(id=pk)
    a=t.nombre
    print(a)
    pkkk=(('pepito','pepito'),('juanito','juanito'),)
    #print(request.GET())
    texto1=TestForm.hola(pkkk)
    print(Cursos_Alumno.objects.values_list('glosa_alumno', flat=True).filter(id_curso=pk))
    context={'texto2':'Aquí deberian ir las asistencias','texto1':texto1,'form':form,'user':Cursos_Alumno.objects.filter(glosa_curso=a).distinct()}
    return render(request, 'Main_DDAF/asistencias.html',context)

def add_asistencia(request):
    return render(request, 'Main_DDAF/asistencias.html')

class MyCreateView(CreateView):
    model = asistencia
    form_class = TestForm
    template_name = 'Main_DDAF/asistencias.html'

    def get_form_kwargs(self):
        kwargs = super( MyCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs


