# Generated by Django 4.1.1 on 2023-01-21 18:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viesbuciai', '0009_profile_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='info',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='Adresas', max_length=50, verbose_name='Adresas'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='city', max_length=20, verbose_name='Miestas'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='Lithuania', max_length=30, verbose_name='Salis'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='your@email.com', max_length=30, validators=[django.core.validators.EmailValidator()], verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='Your lastname', max_length=15, verbose_name='Pavarde'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Your Name', max_length=15, verbose_name='Vardas'),
        ),
        migrations.AlterField(
            model_name='admindetails',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viesbuciai.profile'),
        ),
        migrations.AlterField(
            model_name='balance',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viesbuciai.profile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viesbuciai.profile'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
