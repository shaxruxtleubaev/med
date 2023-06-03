from django.contrib.admin import *
from .models import (
    Specializations,
    Doctors
)

@register(Specializations)
class SpecializationsAdmim(ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    ordering = ('id',)

@register(Doctors)
class DoctorsAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    list_display_links = ('first_name',)
    ordering = ('id',)