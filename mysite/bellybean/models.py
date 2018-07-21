# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Order(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name