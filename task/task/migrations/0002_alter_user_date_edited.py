# Generated by Django 3.2.9 on 2021-11-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_edited',
            field=models.DateTimeField(null=True),
        ),
    ]
