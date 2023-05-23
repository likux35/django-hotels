# Generated by Django 4.1.1 on 2023-01-21 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viesbuciai', '0014_remove_balance_client_profile_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='balance',
        ),
        migrations.AddField(
            model_name='balance',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viesbuciai.profile'),
        ),
    ]