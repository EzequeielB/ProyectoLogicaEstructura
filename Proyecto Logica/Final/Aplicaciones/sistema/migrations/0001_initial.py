# Generated by Django 4.2.6 on 2023-11-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
                ('direccion', models.CharField(max_length=150)),
                ('numeroDeTelefono', models.CharField(max_length=50)),
            ],
        ),
    ]
