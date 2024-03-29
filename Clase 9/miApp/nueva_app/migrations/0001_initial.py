# Generated by Django 5.0.2 on 2024-03-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('completada', models.BooleanField(default=False)),
                ('responsable', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
