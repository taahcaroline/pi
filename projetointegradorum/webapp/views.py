
# Createfrom django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, context
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')


def sobre(request):
    return render(request, 'sobre.html')    

@login_required 
def formulario1(request):
    return render(request, 'formulario1.html')  

@login_required 
def formulario2(request):
    return render(request, 'formulario2.html')


# Create your views here.
