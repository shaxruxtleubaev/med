from django.shortcuts import render

def page(request):
    context = {}
    return render(request, 'base.html', context)