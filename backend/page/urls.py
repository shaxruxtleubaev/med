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

    # Admin Services
    admin_services, 
    admin_services_create, 
    admin_services_edit,
    admin_services_delete,

    # Admin Services Categories
    admin_services_categories,
    admin_services_categories_create,
    admin_services_categories_edit,
    admin_services_categories_delete,
)

urlpatterns = [

    # Default page
    path('', page, name='page'),

    # Admin Dashboard
    path('dashboard/', admin_dashboard, name='admin_dashboard'),

    # Admin Doctors CRUD
    path('doctors/', admin_doctors, name='admin_doctors'),
    path('doctors/<int:pk>/', admin_doctors_detail, name='admin_doctors_detail'),
    path('doctors/create/', admin_doctors_create, name='admin_doctors_create'),
    path('doctors/<int:pk>/edit/', admin_doctors_edit, name='admin_doctors_edit'),
    path('doctors/<int:pk>/delete/', admin_doctors_delete, name='admin_doctors_delete'),

    # Admin Specializations CRUD
    path('specializations/', admin_specializations, name='admin_specializations'),
    path('specializations/create/', admin_specializations_create, name='admin_specializations_create'),
    path('specializations/<int:pk>/edit/', admin_specializations_edit, name='admin_specializations_edit'),
    path('specializations/<int:pk>/delete/', admin_specializations_delete, name='admin_specializations_delete'),

    # Admin Services CRUD
    path('services/', admin_services, name='admin_services'),
    path('services/create/', admin_services_create, name='admin_services_create'),
    path('services/<int:pk>/edit/', admin_services_edit, name='admin_services_edit'),
    path('services/<int:pk>/delete/', admin_services_delete, name='admin_services_delete'),

    # Admin Services Categories CRUD
    path('services-categories/', admin_services_categories, name='services_categories'),
    path('services-categories/create/', admin_services_categories_create, name='services_categories_create'),
    path('services-categories/<int:pk>/edit/', admin_services_categories_edit, name='admin_services_categories_edit'),
    path('services-categories/<int:pk>/delete/', admin_services_categories_delete, name='admin_services_categories_delete'),

]
