# Generated by Django 3.1 on 2020-11-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_admodal'),
    ]

    operations = [
        migrations.CreateModel(
            name='testlink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_test', models.CharField(default='', max_length=50)),
                ('time_of_test', models.CharField(default='', max_length=50, null=True)),
                ('duration_of_test', models.CharField(default='', max_length=50, null=True)),
                ('link_of_test', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
