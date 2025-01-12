# Generated by Django 3.1 on 2020-10-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.ImageField(default='/static/img/logo.png', upload_to='img/eventimages'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_content',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
