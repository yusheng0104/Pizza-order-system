# Generated by Django 2.0.3 on 2019-04-07 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='withtopping',
            new_name='edittable',
        ),
    ]
