from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def stats(request):
    return render(request, 'static.html')