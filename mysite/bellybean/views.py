# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def land(request):
    return render(request, 'bellybean/index.html')

def home(request):
    return render(request, 'bellybean/home.html')