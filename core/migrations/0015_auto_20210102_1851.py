# Generated by Django 3.1.2 on 2021-01-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210102_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='modulo',
            field=models.ManyToManyField(blank=True, to='core.Modulo'),
        ),
    ]
