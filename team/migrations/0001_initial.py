# Generated by Django 3.1.7 on 2021-09-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sports', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('nationalteam', models.CharField(max_length=200)),
                ('club', models.CharField(max_length=200)),
                ('gameplayed', models.CharField(max_length=200)),
                ('peviospoint', models.CharField(max_length=200)),
                ('newpoint', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('dreamteam', models.CharField(max_length=200)),
                ('captiancy', models.CharField(max_length=200)),
                ('vicecaptiancy', models.CharField(max_length=200)),
            ],
        ),
    ]
