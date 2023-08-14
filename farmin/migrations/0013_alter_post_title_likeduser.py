# Generated by Django 4.2.3 on 2023-08-14 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmin', '0012_remove_post_like_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='LikedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmin.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmin.user')),
            ],
        ),
    ]
