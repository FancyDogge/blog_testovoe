# Generated by Django 3.2.13 on 2022-05-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]