# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    rest_name = models.CharField(max_length=100, verbose_name="Restaurant Name")
    area = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.rest_name

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None,null=True, blank=True)
    dish_name = models.CharField(max_length=100, default=None,null=True, blank=True)
    dish_price = models.IntegerField(default=0)

    def __str__(self):
        return self.dish_name

class Order(models.Model):
    item_name = models.CharField(max_length=100, verbose_name="Your Address")
    quantity = models.IntegerField(default=0)
    dish_name = models.ForeignKey(Dish, on_delete=models.CASCADE,default=None,null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,default=None,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    contact = models.CharField(default="0", max_length=10)

    def __str__(self):
        return self.restaurant.rest_name