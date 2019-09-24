from django import forms
from django.forms import widgets
CATEGORY_CHOICES = [('other', 'Разное'), ('cat_1', 'Категория 1'), ('cat_2', 'Категория 2'), ('cat_3', 'Категория 3')]


class ProductsForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=widgets.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Категория')
    count = forms.IntegerField(required=False, min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=False, label='Цена')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': "form-control mr-sm-2"}))
