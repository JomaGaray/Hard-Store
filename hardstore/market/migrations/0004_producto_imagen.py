# Generated by Django 3.0.5 on 2020-05-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20200521_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='img_productos'),
        ),
    ]
