from django.db import models
from django.forms import IntegerField

# Create your models here.
class Payment(models.Model):
    amount = models.IntegerField()
    primary_lightning_address = models.CharField(max_length=500)
    payment_split_lightning_addresses = models.JSONField()
    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE,
    )
    
class Status(models.Model):
    status = models.CharField(max_length=200)
