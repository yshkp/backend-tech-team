from django import forms
from .models import Order, Restaurant, Dish


class SelectDish(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['dish_name', 'quantity', 'item_name', 'contact']

    def __init__(self, *args, **kwargs):
        self.rest_id = kwargs.pop('rest_id')
        super(SelectDish, self).__init__(*args, **kwargs)
        self.fields['dish_name'].queryset = Dish.objects.filter(restaurant_id = self.rest_id)