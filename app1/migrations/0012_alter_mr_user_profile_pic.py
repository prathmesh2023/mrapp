# Generated by Django 4.0.3 on 2022-03-18 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_remove_mr_user_latitude_remove_mr_user_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mr_user',
            name='profile_pic',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
