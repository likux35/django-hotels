# Generated by Django 4.1.1 on 2023-01-21 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viesbuciai', '0013_remove_balance_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='client',
        ),
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viesbuciai.balance'),
        ),
    ]
