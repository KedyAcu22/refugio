# Generated by Django 4.0.6 on 2022-08-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('especie', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=20)),
                ('edad_aprox', models.IntegerField()),
                ('ingreso', models.DateField()),
                ('observaciones', models.TextField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
