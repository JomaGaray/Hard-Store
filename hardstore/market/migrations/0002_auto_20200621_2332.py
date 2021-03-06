# Generated by Django 3.0.5 on 2020-06-22 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oferta',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='market.Producto'),
        ),
        migrations.AddField(
            model_name='itemvendido',
            name='orden',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Orden'),
        ),
        migrations.AddField(
            model_name='itemvendido',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Producto'),
        ),
        migrations.AddField(
            model_name='imagenproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Producto'),
        ),
        migrations.AddField(
            model_name='favorito',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Producto'),
        ),
        migrations.AddField(
            model_name='favorito',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
