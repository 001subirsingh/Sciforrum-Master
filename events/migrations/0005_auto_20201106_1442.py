# Generated by Django 3.1 on 2020-11-06 09:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20201102_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_description',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_content',
            field=ckeditor.fields.RichTextField(default='', max_length=2000),
        ),
    ]
