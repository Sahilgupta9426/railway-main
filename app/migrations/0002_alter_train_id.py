# Generated by Django 3.2.11 on 2022-01-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
