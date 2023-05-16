# Generated by Django 4.2 on 2023-05-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicqrcode', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dynamicqrcode',
            name='type',
        ),
        migrations.AddField(
            model_name='dynamicqrcode',
            name='Book_Choice',
            field=models.CharField(choices=[('E', 'English'), ('N', 'Nepali')], default='E', max_length=1),
        ),
        migrations.AlterField(
            model_name='dynamicqrcode',
            name='content',
            field=models.JSONField(max_length=255),
        ),
    ]
