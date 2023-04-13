from django import forms
from .models import Cart

class CartForm(forms.ModelForm):
    pass
    # title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={}))
    # quantity = forms.CharField(max_length=10, widget=forms.CharField(attrs={}))
    # price = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.CharField(attrs={}))


    class Meta:
        model = Cart
        fields = ('title', 'quantity', 'price')
