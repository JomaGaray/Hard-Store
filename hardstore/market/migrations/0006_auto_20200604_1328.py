# Generated by Django 3.0.5 on 2020-06-04 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200525_1154'),
        ('market', '0005_auto_20200525_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(default='default.jpg', null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='orden',
            name='producto',
        ),
        migrations.AddField(
            model_name='orden',
            name='f_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Cliente'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Confirmada', 'Confirmada')], max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.CreateModel(
            name='ItemVendido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Orden')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Cliente')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ManyToManyField(to='market.ImagenProducto'),
        ),
    ]