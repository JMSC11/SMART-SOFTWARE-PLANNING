# Generated by Django 4.1.7 on 2023-05-12 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_pack', '0007_alter_proyecto_lenguaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuntosFuncion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos_funcion_sin_ajustar', models.SmallIntegerField()),
                ('puntos_funcion_ajustados', models.SmallIntegerField()),
                ('multiplicador', models.SmallIntegerField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_pack.proyecto')),
            ],
        ),
    ]
