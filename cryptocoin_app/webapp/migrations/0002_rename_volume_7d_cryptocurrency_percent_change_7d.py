# Generated by Django 4.1.7 on 2023-03-17 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptocurrency',
            old_name='volume_7d',
            new_name='percent_change_7d',
        ),
    ]
