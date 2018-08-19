# Generated by Django 2.0.7 on 2018-08-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_DDAF', '0018_auto_20180816_1212'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Asistencia',
        ),
        migrations.RenameField(
            model_name='cursos_alumno',
            old_name='usuario',
            new_name='glosa_alumno',
        ),
        migrations.RenameField(
            model_name='cursos_alumno',
            old_name='curso',
            new_name='glosa_curso',
        ),
        migrations.AddField(
            model_name='cursos_alumno',
            name='id_alumno',
            field=models.IntegerField(db_column='id_alumno', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cursos_alumno',
            name='id_curso',
            field=models.IntegerField(db_column='id_curso', default=2),
            preserve_default=False,
        ),
    ]
