from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=128)
    symbol = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class StockMarketData(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='prices')
    price_open = models.FloatField()
    price_high = models.FloatField()
    price_low = models.FloatField()
    price_close = models.FloatField()
    volume = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock.name} - {self.price}"  



