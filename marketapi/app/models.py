"""
Definition of models.
"""

from django.db import models

class marketdata(models.Model):
    ticker = models.CharField(max_length=10)
    buy = models.FloatField()
    sell = models.FloatField()
    volume = models.FloatField()

    def _str_(self):
        return self.ticker