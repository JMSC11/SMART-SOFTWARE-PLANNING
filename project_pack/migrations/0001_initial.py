# Generated by Django 4.1.7 on 2023-03-16 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Macrofuncionalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macrofuncionalidad', models.CharField(max_length=255)),
                ('usuarios', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_proyecto', models.CharField(max_length=50)),
                ('lenguaje', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento_no_Funcional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requerimiento', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_pack.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento_Funcional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requerimiento', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=900)),
                ('macrofuncionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_pack.macrofuncionalidad')),
            ],
        ),
        migrations.CreateModel(
            name='Multiplicador_Influencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer1', models.SmallIntegerField()),
                ('Answer2', models.SmallIntegerField()),
                ('Answer3', models.SmallIntegerField()),
                ('Answer4', models.SmallIntegerField()),
                ('Answer5', models.SmallIntegerField()),
                ('Answer6', models.SmallIntegerField()),
                ('Answer7', models.SmallIntegerField()),
                ('Answer8', models.SmallIntegerField()),
                ('Answer9', models.SmallIntegerField()),
                ('Answer10', models.SmallIntegerField()),
                ('Answer11', models.SmallIntegerField()),
                ('Answer12', models.SmallIntegerField()),
                ('Answer13', models.SmallIntegerField()),
                ('Answer14', models.SmallIntegerField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_pack.proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='macrofuncionalidad',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_pack.proyecto'),
        ),
        migrations.CreateModel(
            name='AspectosANDComplejidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numEntradasBaja', models.SmallIntegerField()),
                ('numEntradasMedia', models.SmallIntegerField()),
                ('numEntradasAlta', models.SmallIntegerField()),
                ('numSalidasBaja', models.SmallIntegerField()),
                ('numSalidasMedia', models.SmallIntegerField()),
                ('numSalidasAlta', models.SmallIntegerField()),
                ('numConsultasBaja', models.SmallIntegerField()),
                ('numConsultasMedia', models.SmallIntegerField()),
                ('numConsultasAlta', models.SmallIntegerField()),
                ('numArchivosInternosBaja', models.SmallIntegerField()),
                ('numArchivosInternosMedia', models.SmallIntegerField()),
                ('numArchivosInternosAlta', models.SmallIntegerField()),
                ('numExternosBaja', models.SmallIntegerField()),
                ('numExternosMedia', models.SmallIntegerField()),
                ('numExternosAlta', models.SmallIntegerField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_pack.proyecto')),
            ],
        ),
    ]
