# Generated by Django 4.2 on 2023-05-15 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicqrcode', '0002_remove_dynamicqrcode_type_dynamicqrcode_book_choice_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dynamicqrcode',
            old_name='Book_Choice',
            new_name='type',
        ),
    ]