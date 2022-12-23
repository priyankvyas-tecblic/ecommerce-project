# Generated by Django 4.0.5 on 2022-12-19 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('pdesc', models.CharField(max_length=100)),
                ('pcategory', models.CharField(max_length=30)),
                ('pdate', models.DateField()),
            ],
        ),
    ]