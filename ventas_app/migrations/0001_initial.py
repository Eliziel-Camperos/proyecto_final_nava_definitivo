# Generated by Django 5.1.3 on 2024-12-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_tienda', models.IntegerField(primary_key=True, serialize=False)),
                ('id_comic', models.IntegerField()),
                ('id_empleado', models.IntegerField()),
                ('fecha_venta', models.DateField()),
                ('Cant_comic', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
