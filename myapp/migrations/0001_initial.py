# Generated by Django 5.0 on 2024-06-15 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('popular', models.BooleanField(default=False)),
                ('tendencia', models.BooleanField(default=False)),
                ('nuevo', models.BooleanField()),
                ('fecha_fabricacion', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.marca')),
            ],
        ),
    ]
