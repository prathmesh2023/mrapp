# Generated by Django 4.0.3 on 2022-03-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_visit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='timestamp',
            field=models.CharField(default='00-00-0000', max_length=255),
        ),
    ]
