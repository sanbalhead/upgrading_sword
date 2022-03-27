from unicodedata import name
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('game/', views.game, name='game'),
    path('item/', views.item, name='item'),
    path('shop/', views.shop, name='shop'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign/', views.sign, name='sign'),
    path('ranking/', views.ranking, name='ranking'),    
    path('api/sword/', views.sword, name='sword'),
    path('api/user/', views.user, name='user'),
    path('api/level/', views.level, name='level'),
    path('api/usersword/', views.user_sword, name='user_sword'),
    re_path(r'^image/.*\.*', views.image, name='image')
]