# Generated by Django 5.0.6 on 2024-07-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='load_count',
            field=models.IntegerField(default=0),
        ),
    ]
