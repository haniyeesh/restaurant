from menu.models import Food
from django import forms


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        field = ["category","name","detail","image ","price"]
