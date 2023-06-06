from django.urls import path
from .views import (
    page,
    admin_dashboard,

    # Admin Doctors
    admin_doctors,
    admin_doctors_detail,
    admin_doctors_create,
    admin_doctors_edit,
    admin_doctors_delete,

    # Admin Specializations
    admin_specializations,
    admin_specializations_create,
    admin_specializations_edit,
    admin_specializations_delete,

)

urlpatterns = [

    # Default page
    path('', page, name='page'),

    # Admin Dashboard
    path('dashboard/', admin_dashboard, name='admin_dashboard'),

    # Doctors CRUD
    path('doctors/', admin_doctors, name='admin_doctors'),
    path('doctors/<int:pk>/', admin_doctors_detail, name='admin_doctors_detail'),
    path('doctors/create/', admin_doctors_create, name='admin_doctors_create'),
    path('doctors/<int:pk>/edit/', admin_doctors_edit, name='admin_doctors_edit'),
    path('doctors/<int:pk>/delete/', admin_doctors_delete, name='admin_doctors_delete'),

    # Specializations CRUD
    path('specializations/', admin_specializations, name='admin_specializations'),
    path('specializations/create/', admin_specializations_create, name='admin_specializations_create'),
    path('specializations/<int:pk>/edit/', admin_specializations_edit, name='admin_specializations_edit'),
    path('specializations/<int:pk>/delete/', admin_specializations_delete, name='admin_specializations_delete'),

]
