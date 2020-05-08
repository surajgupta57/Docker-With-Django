# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.status import HTTP_401_UNAUTHORIZED
# from . models import student
# from . serializers import studentSerializer
#
#
# # Create your views here.
#
# class studentList(APIView):
#     # def GET(self, request):
#     #     queryset = student.objects.all()
#     #     serializer_class = studentSerializer
#     #     from django.db.migrations import serializer
#     #     return Response(serializer.data)
#     #
#     # def POST(self):
#     #     pass
#
#     def get(self, request):
#         students = student.objects.all()
#         serializer = studentSerializer(students)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = studentSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]