# Generated by Django 3.2 on 2021-05-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app_backend', '0002_auto_20210503_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='completedOn',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='createdOn',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
