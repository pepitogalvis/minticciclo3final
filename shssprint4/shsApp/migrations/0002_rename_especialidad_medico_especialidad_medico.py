# Generated by Django 4.1.1 on 2022-09-24 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medico',
            old_name='especialidad',
            new_name='especialidad_medico',
        ),
    ]
