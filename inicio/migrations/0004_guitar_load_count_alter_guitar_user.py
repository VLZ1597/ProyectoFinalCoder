# Generated by Django 5.0.6 on 2024-07-02 01:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_remove_guitar_load_count_guitar_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='load_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
