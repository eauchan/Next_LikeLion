# Generated by Django 4.0.3 on 2022-04-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='D_day',
            field=models.DateField(null=True),
        ),
    ]