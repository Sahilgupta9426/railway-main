from tkinter.tix import Form
from urllib import response
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponseRedirect
from django.template.loader import render_to_string
# from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import json
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Customer, Train, Travel_Schedule
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomerForm, TravelForm 

# Create your views here.
def home(request):
    return render(request,'files/home.html')
# ajax
def searchajax(request, form, template_name):
    data = dict() 
    if request.method == 'POST':
        if form.is_valid():
            # print(request.POST['source'],request.POST['destination'])
            t = Travel_Schedule.objects.filter(source=request.POST['source'], destination=request.POST['destination']) 
            date=request.POST['date']
            print("date:",date)
            data['html_train_list'] = render_to_string('files/ajaxinclude/train_results.html', {
                'trains': t,'date':date
            })
            
            data['form_is_valid'] = True
            
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def searchform(request ):
    if request.method == 'POST':
        form = TravelForm(request.POST)
    else:
        form = TravelForm()
    return searchajax(request, form, 'files/ajaxinclude/search.html')

# booking customer details
def customer(request,pk):
    t=Travel_Schedule(train_no=pk)
    print(t)
    form=CustomerForm()
    data=dict()
    data["html_form"]=render_to_string('files/ajaxinclude/booking_detail.html', {
                "form":form
            })
    return JsonResponse(data)
    
    
    
