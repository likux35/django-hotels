# Generated by Django 4.1.1 on 2023-01-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viesbuciai', '0018_hotel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Zmoniu_kiekis'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Uzsakymo_data'),
        ),
    ]
