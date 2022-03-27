from rest_framework import serializers
from .models import *

class SwordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sword
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class UserSwordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSword
        fields = '__all__'