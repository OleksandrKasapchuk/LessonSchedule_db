# Generated by Django 5.0.1 on 2024-02-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]