# Generated by Django 5.1.6 on 2025-05-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_predictionlog_prediction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictionlog',
            name='Dependents',
            field=models.CharField(max_length=5),
        ),
    ]
