from django.contrib.admin import *
from .models import (
    Specializations,
    Doctors,
    ServicesCategories,
    Services
)

@register(Specializations)
class SpecializationsAdmim(ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    ordering = ('name',)

@register(Doctors)
class DoctorsAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    list_display_links = ('first_name',)
    ordering = ('first_name',)

@register(ServicesCategories)
class ServicesCategoriesAdmin(ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    ordering = ('name',)

@register(Services)
class ServicesAdmin(ModelAdmin):
    list_display = ('id', 'name', 'status',)
    list_display_links = ('name',)
    ordering = ('name',)