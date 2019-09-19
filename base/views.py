from django.shortcuts import render

# Create your views here.

def indexView(request):
    """Index"""
    return render(request, 'index.html')

def projectView(request):
    """Projects"""
    return render(request, 'project.html')

def configurationView(request):
    """Configurations"""
    return render(request, 'configuration.html')

def dashboardView(request):
    """Dashboard"""
    return render(request, 'dashboard.html')