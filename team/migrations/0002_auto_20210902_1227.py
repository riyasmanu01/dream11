# Generated by Django 3.1.7 on 2021-09-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='peviospoint',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
