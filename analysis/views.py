from django.shortcuts import render

# Create your views here.

def charts(request):
    context = {}
    template_name = 'staff/charts.html'
    return render(request, template_name, context)


def dashboard(request):
    context = {}
    template_name = 'staff/dashboard.html'
    return render(request, template_name, context)
