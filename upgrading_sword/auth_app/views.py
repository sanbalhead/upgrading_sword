from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from .models import User as CustomUser
from app.models import UserSword


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/game")
            else:   
                msg = 'Invalid credentials'   
        else:
            msg = 'Error validating the form'   
    return render(request, "login.html", {"form": form, "msg" : msg})


def register_user(request):
   
    START_MONEY = 100000
    
    msg     = None
    success = False
   
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # new_user = CustomUser()
            # new_user.username = form.cleaned_data.get("username")
            # new_user.password = form.cleaned_data.get("password1")
            # new_user.nickname = form.cleaned_data.get("nickname")
            # new_user.email = form.cleaned_data.get("email")
            # new_user.money = START_MONEY
            # new_user.save()
            form.save()



            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)


            user.money = START_MONEY
            user.save(update_fields=['money'])


            newUserSword = UserSword()
            print("유저의 새 검 생성")
            newUserSword.user_id = user.id
            newUserSword.sword_name = '그냥 검'
            newUserSword.sword_level = '1'
            newUserSword.save()

         
            msg     = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect("/login/")


        else:
            msg = 'Form is not valid'   
   
    else:
        form = SignUpForm()
  
    return render(request, "register.html", {"form": form, "msg" : msg, "success" : success })