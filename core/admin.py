from django.contrib import admin
from core import models


# Register your models here.
@admin.register(models.Task)
class Task(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    pass
