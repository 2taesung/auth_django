# Generated by Django 3.1.1 on 2020-09-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='class_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
