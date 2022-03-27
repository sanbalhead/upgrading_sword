from tkinter.tix import Tree
from django import forms
from app.models import User

class Signform(forms.Form):
    id = forms.CharField(max_length=128, required=True)
    password = forms.CharField(max_length=128, required=True)
    password_check = forms.CharField(max_length=128, required=True)
    nickname = forms.CharField(max_length=128, required=True)
    money = forms.CharField(max_length=128, required=True)
    
    class Meta:
        model = User
        fields ='__all__'
        