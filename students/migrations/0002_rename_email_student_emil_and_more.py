# Generated by Django 5.0.7 on 2024-07-31 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='emil',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='FirstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='LastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='RegNo',
            new_name='regno',
        ),
    ]
