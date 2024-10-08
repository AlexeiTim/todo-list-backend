from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

app_name = 'core'

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')
router.register('categories', views.CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls))
]