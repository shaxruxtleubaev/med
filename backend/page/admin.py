from django.contrib.admin import *
from .models import (
    Specializations,
    Doctors,
    ServicesCategories,
    Services,
    Patients,
    StaffsRoles,
    Staffs,
    Visits
)

@register(Specializations)
class SpecializationsAdmin(ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    ordering = ('name',)

@register(Doctors)
class DoctorsAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    list_display_links = ('first_name', 'last_name',)
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

@register(Patients)
class PatientsAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    list_display_links = ('first_name', 'last_name',)
    ordering = ('first_name',)

@register(StaffsRoles)
class StaffsRolesAdmin(ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    ordering = ('name',)

@register(Staffs)
class StaffsAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    list_display_links = ('first_name', 'last_name',)
    ordering = ('first_name',)

@register(Visits)
class VisitsAdmin(ModelAdmin):
    list_display = ('id', 'doctor', 'patient', 'visit_date', )
    list_display_links = ('doctor', 'patient',)
    ordering = ('-visit_date',)