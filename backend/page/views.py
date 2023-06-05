from django.shortcuts import render
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

def page(request):
    return render(request, 'base.html')