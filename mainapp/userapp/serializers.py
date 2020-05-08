# from rest_framework import serializers
# from . models import student
#
# # from . models import *
# # from django.contrib.auth import login, logout
#
#
# class studentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = student
#         fields = '__all__'


from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']