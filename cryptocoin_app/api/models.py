from django.db import models

from django.contrib.auth import get_user_model

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    price = models.FloatField()
    percent_change_24h = models.FloatField()
    volume_24h = models.FloatField()
    volume_7d = models.FloatField()
    circulating_supply = models.IntegerField()

    favorite_by = models.ManyToManyField(
        get_user_model(),
        related_name='favorites'
    )

    class Meta: 
        verbose_name = "Cryptocurrency"
        verbose_name_plural = "Cryptocurrencies"
