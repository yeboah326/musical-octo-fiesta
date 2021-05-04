# Generated by Django 3.2 on 2021-05-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_app_backend', '0006_report_patientname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='completed',
            field=models.CharField(choices=[('done', 'DONE'), ('pending', 'PENDING')], default='pending', max_length=8),
        ),
    ]
