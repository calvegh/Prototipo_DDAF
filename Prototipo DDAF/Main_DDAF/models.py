# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField



class Cursos(models.Model):
    id = models.IntegerField(primary_key=True)
    semestres = models.ForeignKey('Semestres', models.DO_NOTHING)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING)
    anho = models.DateField(db_column='Anho')  # Field name made lowercase.
    horario = models.CharField(db_column='Horario', max_length=32)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=64)  # Field name made lowercase.
    codigo = models.CharField(max_length=10)
    ud = models.CharField(db_column='UD', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cursos'


class Departamento(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=64)  # Field name made lowercase.
    sitioweb = models.CharField(max_length=45, blank=True, null=True)
    jefe_depto = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Jefe_depto_id')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'departamento'


class RolUsuarioCurso(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_usuario = models.ForeignKey('TipoUsuario', models.DO_NOTHING)
    cursos = models.ForeignKey(Cursos, models.DO_NOTHING)
    usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'rol_usuario_curso'


class Semestres(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_semestre = models.CharField(db_column='Nombre_Semestre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'semestres'


class TipoUsuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipo_usuario'


class UsuarioTipoUsuario(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING)
    usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'usuario_tipo_usuario'


class Usuarios(models.Model):
    id = models.IntegerField(db_column="id",primary_key=True,)
    nombre = models.CharField(db_column='Nombre', max_length=64)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=64)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=128)  # Field name made lowercase.
    rut = models.CharField(db_column='RUT', max_length=32)  # Field name made lowercase.
    puntaje_psu = models.IntegerField(db_column='Puntaje_PSU')  # Field name made lowercase.

    user = models.OneToOneField(User, on_delete=models.CASCADE, default = True)

    class Meta:
        managed = True
        db_table = 'usuarios'

class CursosDDAF(models.Model):
    id = models.IntegerField(db_column="id", primary_key=True)
    nombre = models.CharField(db_column="nombre", max_length=64)  # Field name made lowercase.
    tipo = models.CharField(db_column="tipo", max_length=64)
    horario = models.IntegerField(db_column="horario")  # Field name made lowercase.
    profesor = models.CharField(db_column="profesor", max_length=64)
    pista = models.IntegerField(db_column="pista")
    días = models.CharField(db_column="dias", max_length=32)
    capacidad = models.IntegerField(db_column="capacidad")

    class Meta:
        managed = True
        db_table = 'cursos_ddaf'

class Cursos_Alumno(models.Model):
    id = models.IntegerField(db_column="id", primary_key=True)
    id_curso = models.IntegerField(db_column="id_curso")
    glosa_curso = models.CharField(db_column="nombre_curso", max_length=64)
    id_alumno = models.IntegerField(db_column="id_alumno")
    glosa_alumno = models.CharField(db_column="usuario", max_length=64)

    class Meta:
        managed = True
        db_table = 'curso_alumno'
'''
#versión vieja
class Asistencia(models.Model):
    ALUMNOS =(('CARLOS','CARLOS'),('ADRIANA','ADRIANA'),)

    nombre_alumno = MultiSelectField(choices = ALUMNOS)
'''

class asistencia(models.Model):
    id = models.IntegerField(db_column="id", primary_key=True)
    asistentes = models.CharField(db_column='asistentes', max_length=64)
