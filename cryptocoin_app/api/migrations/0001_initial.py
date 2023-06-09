# Generated by Django 4.1.7 on 2023-03-16 16:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('percent_change_24h', models.FloatField()),
                ('volume_24h', models.FloatField()),
                ('volume_7d', models.FloatField()),
                ('circulating_supply', models.IntegerField()),
                ('favorite_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
