"""from django.shortcuts import render, redirect
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

from .forms import (
    SpecializationsForm,
    DoctorsForm,
    ServicesCategoriesForm,
    ServicesForm
)

DEFAULT_TEMPLATE = 'base.html'

# Default page
def page(request):
    return render(request, DEFAULT_TEMPLATE)

# Main dashboard
def admin_dashboard(request):

    doctors = Doctors.objects.all()
    patients = Patients.objects.all()

    context = {
        'doctors': doctors,
        'patients': patients
    }

    return render(request, DEFAULT_TEMPLATE, context)

# Admin Doctors CRUD
def admin_doctors(request):

    doctors = Doctors.objects.all()

    context = {
        'doctors': doctors
    }

    return render(request, DEFAULT_TEMPLATE, context)

def admin_doctors_detail(request, pk):

    doctor = Doctors.objects.get(id=pk)

    context = {
        'doctor': doctor
    }

    return render(request, DEFAULT_TEMPLATE, context)

def admin_doctors_create(request):

    form = DoctorsForm()

    if request.method == 'POST':
        form = DoctorsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/adminn/doctors/')
    
    context = {
        'form': form
    }

    return render(request, DEFAULT_TEMPLATE, context)

def admin_doctors_edit(request, pk):

    doctor = Doctors.objects.get(id=pk)
    form = DoctorsForm(instance=doctor)

    if request.method == 'POST':
        form = DoctorsForm(request.POST, instance=doctor, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/adminn/doctors/')
    
    context = {
        'form': form
    }

    return render(request, DEFAULT_TEMPLATE, context)

def admin_doctors_delete(request, pk):

    doctor = Doctors.objects.get(id=pk)
    doctor.delete()

    return redirect('/adminn/doctors/')

# Admin Specializations CRUD
def admin_specializations(request):

    specializations = Specializations.objects.all()

    context = {
        'specializations': specializations
    }

    return render(request, DEFAULT_TEMPLATE, context)

def admin_specializations_create(request):
    
    form = SpecializationsForm()

    if request.method == 'POST':
        form = SpecializationsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/adminn/specializations/')
    
    context = {
        'form': form
    }
    
    return render(request, DEFAULT_TEMPLATE, context)

def admin_specializations_edit(request, pk):

    specializations = Specializations.objects.get(id=pk)
    form = SpecializationsForm(instance=specializations)

    if request.method == 'POST':
        form = SpecializationsForm(request.POST, instance=specializations, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/adminn/specializations/')
    
    context = {
        'form': form
    }

    return render(request, DEFAULT_TEMPLATE, context)

def admin_specializations_delete(request, pk):
    
    specialization = Specializations.objects.get(id=pk)
    specialization.delete()

    return redirect('/adminn/specializations/')

# Admin Services CRUD
def admin_services(request):

    services = Services.objects.all()

    context = {
        'services': services
    }

    return render(request, 'base.html', context)

def admin_services_create(request):

    form = ServicesForm()

    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/adminn/services/')
    
    context = {
        'form': form
    }

    return render(request, 'base.html', context)

def admin_services_edit(request, pk):

    service = Services.objects.get(id=pk)
    form = ServicesForm(instance=service)

    if request.method == 'POST':
        form = ServicesForm(request.POST, instance=service, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/adminn/services/')
    
    context = {
        'form': form
    }

    return render(request, 'base.html', context)

def admin_services_delete(request, pk):

    service = Services.objects.get(id=pk)
    service.delete()

    return redirect('/adminn/services/')

# Admin Services Categories CRUD
def admin_services_categories(request):

    services_categories = ServicesCategories.objects.all()

    context = {
        'services_categories': services_categories
    }

    return render(request, 'base.html', context)

def admin_services_categories_create(request):

    form = ServicesCategoriesForm()

    if request.method == 'POST':
        form = ServicesCategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/adminn/services-categories/')
    
    context = {
        'form': form
    }

    return render(request, 'base.html', context)

def admin_services_categories_edit(request, pk):

    service_category = ServicesCategories.objects.get(id=pk)
    form = ServicesCategoriesForm(instance=service_category)

    if request.method == 'POST':
        form = ServicesCategoriesForm(request.POST, instance=service_category, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/adminn/services-categories/')
    
    context = {
        'form': form
    }

    return render(request, 'base.html', context)

def admin_services_categories_delete(request, pk):

    service_category = ServicesCategories.objects.get(id=pk)
    service_category.delete()

    return redirect('/adminn/services-categories/')"""