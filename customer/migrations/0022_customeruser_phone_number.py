# Generated by Django 4.2.9 on 2024-12-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0021_delete_contact_remove_customeruser_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='phone_number',
            field=models.CharField(default=1234567890, max_length=15),
            preserve_default=False,
        ),
    ]
