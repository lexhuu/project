# Generated by Django 4.2.7 on 2023-11-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('place', models.CharField(max_length=25)),
            ],
        ),
    ]
