# Generated by Django 4.0.3 on 2022-03-10 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_mr_user_latitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='mr_user',
            name='status',
            field=models.CharField(default='Active', max_length=255),
        ),
    ]