# Generated by Django 4.2.3 on 2023-08-16 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmin', '0023_merge_20230816_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Post_pic',
        ),
        migrations.AddField(
            model_name='postpics',
            name='Post_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='farmin.post'),
            preserve_default=False,
        ),
    ]