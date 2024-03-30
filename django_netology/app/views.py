from django.shortcuts import render
from .models import Phone

def catalog_view(request):
    phones = Phone.objects.all()
    return render(request, 'catalog.html', {'phones': phones})
