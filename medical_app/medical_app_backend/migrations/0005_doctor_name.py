# Generated by Django 3.2 on 2021-05-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app_backend', '0004_alter_nurse_numberofreportscreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='unknownDoctor', max_length=50),
        ),
    ]
