# Generated by Django 5.1.3 on 2024-12-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id_comics', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('serie', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
