# Generated by Django 4.1.1 on 2022-10-31 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Userid', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('cell_phone', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
