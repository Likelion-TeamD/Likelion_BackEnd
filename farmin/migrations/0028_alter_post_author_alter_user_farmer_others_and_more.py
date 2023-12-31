# Generated by Django 4.2.4 on 2023-08-17 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmin', '0027_neighbor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='farmin.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Farmer_others',
            field=models.ManyToManyField(blank=True, to='farmin.user'),
        ),
        migrations.DeleteModel(
            name='Neighbor',
        ),
    ]
