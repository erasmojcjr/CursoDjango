# Generated by Django 2.0.5 on 2018-05-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='clientes_fotos'),
        ),
    ]
