# Generated by Django 3.1 on 2020-11-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20201106_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
