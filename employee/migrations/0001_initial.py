# Generated by Django 4.0.4 on 2022-06-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=120)),
                ('desig', models.CharField(max_length=120)),
                ('salary', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('experience', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]