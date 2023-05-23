# Generated by Django 4.1.1 on 2023-01-21 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viesbuciai', '0015_remove_profile_balance_balance_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='client',
        ),
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
