# Generated by Django 4.0.3 on 2022-04-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_post_d_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='D_day',
        ),
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
