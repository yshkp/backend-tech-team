# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Order, Restaurant, Dish
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import SelectDish
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def land(request):
    if request.user.is_authenticated:
        return render(request, 'bellybean/home.html')
    else:
        return render(request, 'bellybean/index.html')

def home(request):
    return render(request, 'bellybean/home.html')

class RegisterRestaurant(LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('registerrest')
    model = Restaurant
    success_url = reverse_lazy('home')
    fields = ['rest_name', 'area']

class RegisterDishes(LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('registerrest')
    model = Dish
    success_url = reverse_lazy('home')
    fields = ['dish_name', 'dish_price']

    def form_valid(self, form):
        form.instance.restaurant = get_object_or_404(Restaurant, pk = self.kwargs['rest_id'])
        return super(RegisterDishes, self).form_valid(form)

@login_required
def selectrest(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'bellybean/selectrest.html', context)

@login_required
def select_dish(request, area, rest_id):
    form = SelectDish(request.POST, rest_id = rest_id)

    print(form.is_valid())
    if form.is_valid():
        instance = form.save(commit=False)
        instance.restaurant = get_object_or_404(Restaurant, pk = rest_id)
        instance.user = request.user
        instance.save()
        return redirect('home')

    return render(request, 'bellybean/formtemplate.html', {'form': form})

@login_required
def selectresttoorder(request, area):
    restaurants = Restaurant.objects.filter(area__iexact=area)
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'bellybean/selectresttoorder.html', context)

@login_required
def select_area(request):
    areas = Restaurant.objects.values_list('area', flat=True).distinct()

    context = {
        'areas': areas,
    }

    return render(request, 'bellybean/choose_area.html', context)