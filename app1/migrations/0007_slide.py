# Generated by Django 4.0.3 on 2022-03-12 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_mr_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('sub_category', models.CharField(max_length=255)),
                ('slide_pic', models.ImageField(blank=True, null=True, upload_to='profiles')),
            ],
        ),
    ]
