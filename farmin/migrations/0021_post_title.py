# Generated by Django 4.2.4 on 2023-08-16 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmin', '0020_alter_farmpics_farm_pics_alter_postpics_post_pics_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]