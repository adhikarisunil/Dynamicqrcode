# Generated by Django 4.1.7 on 2023-05-16 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicqrcode', '0004_remove_dynamicqrcode_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dynamicqrcode',
            old_name='another_field',
            new_name='qr_code_type',
        ),
    ]
