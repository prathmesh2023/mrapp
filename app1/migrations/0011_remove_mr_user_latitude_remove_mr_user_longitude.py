# Generated by Django 4.0.3 on 2022-03-13 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_visit_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mr_user',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='mr_user',
            name='longitude',
        ),
    ]
