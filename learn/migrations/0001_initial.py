# Generated by Django 3.2 on 2023-01-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rom', models.CharField(max_length=500)),
                ('eng', models.CharField(max_length=500)),
            ],
        ),
    ]
