from django.db import models
from rest_framework.generics import get_object_or_404


# class student(models.Model):
#     firstname = models.CharField(max_length=10)
#     lastname = models.CharField(max_length=10)
#     std_id = models.IntegerField()
#
#     def __str__(self):
#         return self.firstname
#
#     # def get_object(self):
#     #     obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
#     #     self.check_object_permissions(self.request, obj)
#     #     return obj