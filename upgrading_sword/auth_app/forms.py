from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "닉네임",               
                "class": "form-control"
            }
        ))
 
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "비밀번호",               
                "class": "form-control"
            }
        ))
 
 
 
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "닉네임",               
                "class": "form-control"
            }
        ))
    nickname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "이름",               
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "이메일",               
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "비밀번호",               
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "비밀번호 확인",               
                "class": "form-control"
            }
        ))
    money = forms.IntegerField(required=False)
 
 
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'nickname', 'money')