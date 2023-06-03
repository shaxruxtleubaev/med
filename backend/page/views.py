from django.shortcuts import render
from .models import (
    Specializations,
    Doctors
)

def page(request):
    context = {}
    return render(request, 'base.html', context)