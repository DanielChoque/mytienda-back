# Generated by Django 4.0.6 on 2022-07-13 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_remove_medida_cantidad_remove_medida_tipo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidad',
            name='unidades',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ci',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ci',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
