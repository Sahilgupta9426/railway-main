# Generated by Django 3.2.11 on 2022-01-29 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_Schedule',
            fields=[
                ('train_no', models.IntegerField(primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('arrival_time', models.CharField(max_length=30)),
                ('fare', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat1', models.IntegerField()),
                ('seat2', models.IntegerField()),
                ('seat3', models.IntegerField()),
                ('seat4', models.IntegerField()),
                ('seat5', models.IntegerField()),
                ('seat6', models.IntegerField()),
                ('seat7', models.IntegerField()),
                ('seat8', models.IntegerField()),
                ('seat9', models.IntegerField()),
                ('seat10', models.IntegerField()),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.travel_schedule')),
            ],
        ),
    ]
