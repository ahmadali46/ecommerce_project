from numpy import product
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        
        
class RandomListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RandomList
        fields = "__all__"

class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = "__all__"

class MyUserManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUserManager
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


