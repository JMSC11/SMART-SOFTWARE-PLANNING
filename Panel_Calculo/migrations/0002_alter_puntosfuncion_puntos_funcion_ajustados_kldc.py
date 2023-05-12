# Generated by Django 4.1.7 on 2023-05-12 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_pack', '0007_alter_proyecto_lenguaje'),
        ('Panel_Calculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntosfuncion',
            name='puntos_funcion_ajustados',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='KLDC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KLDC', models.FloatField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_pack.proyecto')),
            ],
        ),
    ]