# Generated by Django 3.1.2 on 2020-12-04 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201204_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='rubro',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
    ]
