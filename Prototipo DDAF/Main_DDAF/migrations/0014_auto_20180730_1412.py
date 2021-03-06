# Generated by Django 2.0.7 on 2018-07-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_DDAF', '0013_cursosddaf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursosddaf',
            name='días',
            field=models.CharField(db_column='días', default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cursosddaf',
            name='pista',
            field=models.IntegerField(db_column='pista', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cursosddaf',
            name='profesor',
            field=models.CharField(db_column='profesor', default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cursosddaf',
            name='horario',
            field=models.IntegerField(db_column='horario'),
        ),
    ]
