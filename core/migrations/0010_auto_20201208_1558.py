# Generated by Django 3.1.2 on 2020-12-08 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_credito_rubro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='email_institucional',
            field=models.CharField(max_length=126, validators=[django.core.validators.RegexValidator(message='El formato del correo debe ser @tectijuana.edu.mx', regex='(^[a-zA-Z0-9_.+-]+@tectijuana.edu.mx+$)|(^[a-zA-Z0-9_.+-]+@tectijuana.tecnm.mx+$)')]),
        ),
    ]
