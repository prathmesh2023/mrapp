# Generated by Django 4.0.3 on 2022-03-07 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_mr_user_latitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mr_user',
            name='latitude',
            field=models.FloatField(default=0),
        ),
    ]
