# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Station(models.Model):
    id = models.AutoField(primary_key=True)
    Region = models.CharField(max_length=32)
    Regional_Drought_Stage = models.CharField(max_length=32)
    Reservoir_Name = models.CharField(max_length=32)
    Reservoir_Storage = models.DecimalField(max_digits=10, decimal_places=4)
    Reservoir_Level = models.DecimalField(max_digits=7, decimal_places=4)
    Date = models.CharField(max_length=32)