# Generated by Django 4.0.3 on 2022-09-13 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de Usuario')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastName', models.CharField(max_length=50, verbose_name='Apellido')),
                ('tDocument', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjeria'), ('TI', 'Tarjeta de Identidad')], max_length=21, verbose_name='Tipo de Documento')),
                ('nDocument', models.IntegerField(verbose_name='Número de Documento')),
                ('phone', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('dateBirth', models.DateField(verbose_name='Fecha Nacimiento')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('user_admin', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]