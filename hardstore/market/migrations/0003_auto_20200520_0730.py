# Generated by Django 3.0.5 on 2020-05-20 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20200520_0730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nombre',
            new_name='name',
        ),
    ]
