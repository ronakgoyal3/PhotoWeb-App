# Generated by Django 3.1.2 on 2021-04-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20210424_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Owner',
            field=models.CharField(max_length=250),
        ),
    ]
