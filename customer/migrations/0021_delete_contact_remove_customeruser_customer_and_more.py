# Generated by Django 4.2.9 on 2024-12-31 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_remove_order_deliverycontact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
