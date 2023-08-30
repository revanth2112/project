# Generated by Django 4.2 on 2023-04-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpName', models.CharField(max_length=30)),
                ('EmpId', models.IntegerField()),
                ('Desg', models.CharField(max_length=30)),
                ('Doj', models.DateField()),
                ('Dep', models.CharField(max_length=30)),
                ('Sal', models.FloatField()),
                ('Exp', models.IntegerField()),
            ],
        ),
    ]