# Generated by Django 4.1.7 on 2023-05-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_pack', '0005_alter_preguntas_factores_p1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=500),
        ),
    ]
