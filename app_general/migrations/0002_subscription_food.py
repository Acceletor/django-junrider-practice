# Generated by Django 5.0.2 on 2024-02-16 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_food', '0003_rename_is_prenuim_food_is_premium'),
        ('app_general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='food',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_food.food'),
        ),
    ]
