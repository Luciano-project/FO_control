from django.db import models
from datetime import datetime

# Create your models here.

class Fields(models.Model):
    id = models.AutoField(primary_key=True)
    factory_order = models.CharField(max_length=10)
    factory_order_date = models.DateField(default=datetime.now)
    article_number = models.CharField(max_length=20)
    datasheet = models.BooleanField()
    datasheet_date = models.DateField(default=datetime.now)
    etools = models.BooleanField()
    sticker = models.BooleanField()
    sticker_date = models.DateField(default=datetime.now)
    description = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    
    def __str__(self):
            return self.factory_order
    
    class Meta:
        ordering = ['factory_order']
        verbose_name = 'Field'
        verbose_name_plural = 'Fields'
        

