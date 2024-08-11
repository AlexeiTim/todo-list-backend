from django.shortcuts import render
from rest_framework import viewsets
from core import models, serializers, filters

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    filterset_class = filters.TaskFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer