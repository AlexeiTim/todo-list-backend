from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]