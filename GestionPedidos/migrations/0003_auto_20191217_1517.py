# Generated by Django 2.2.5 on 2019-12-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionPedidos', '0002_auto_20191201_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La dirección'),
        ),
    ]
