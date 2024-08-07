# Generated by Django 3.1 on 2020-10-26 09:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20201025_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blog_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='blogComment',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('linked_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogpost')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.blogcomment')),
            ],
        ),
    ]