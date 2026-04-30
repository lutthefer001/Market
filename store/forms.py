from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mahsulot nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mahsulot haqida ma\'lumot'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Narxi'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
