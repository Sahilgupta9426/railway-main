from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Customer

class TravelForm(forms.Form):
    source=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'From'}))
    destination=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Where To'}))
    date=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'MM/DD/YYYY'}))
# class CustomerForm(forms.Form):
#     op=[('0', 'Male'),
#     ('1', 'Female'),
#     ('2', 'Transgender')]
#     cname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'From'}))
#     gender=forms.ChoiceField(choices = op)
#     number=forms.CharField(max_length=10)
class CustomerForm(ModelForm):
     class Meta:
        model = Customer
        fields = ['cname','gender','number','user']