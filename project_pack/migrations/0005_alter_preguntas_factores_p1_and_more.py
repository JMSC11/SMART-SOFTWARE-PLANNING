# Generated by Django 4.1.7 on 2023-05-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_pack', '0004_preguntas_factores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p1',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p10',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p11',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p12',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p13',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p14',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p2',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p3',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p4',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p5',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p6',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p7',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p8',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='preguntas_factores',
            name='p9',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='requerimiento_no_funcional',
            name='descripcion',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='requerimiento_no_funcional',
            name='requerimiento',
            field=models.CharField(max_length=500),
        ),
    ]
