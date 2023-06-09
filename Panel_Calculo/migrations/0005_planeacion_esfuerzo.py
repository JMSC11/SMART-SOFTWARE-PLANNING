# Generated by Django 4.1.7 on 2023-05-26 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_pack', '0007_alter_proyecto_lenguaje'),
        ('Panel_Calculo', '0004_ldcxpf_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planeacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Planeacion_jones', models.FloatField()),
                ('Planeacion_COCOMO', models.FloatField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_pack.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Esfuerzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Esfuerzo_jones', models.FloatField()),
                ('Esfuerzo_COCOMO', models.FloatField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_pack.proyecto')),
            ],
        ),
    ]
