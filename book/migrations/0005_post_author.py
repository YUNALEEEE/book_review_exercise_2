# Generated by Django 2.2.1 on 2019-05-16 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]