# Generated by Django 3.0.7 on 2020-07-08 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto_pedido',
            name='idPizza',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
    ]