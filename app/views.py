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
from django.template import RequestContext
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
            # this loop is used for get seat from Train Table which is fecthed with foreign key
            
            for train_num in t: # sending Travel_schedule object in train_num
                p=train_num.train_no #saving train number from Travel Schedule in p variable
                a=Train.objects.filter(sid=p)#searching 'sid' whic is Train Number in Train Model 
                for obj in a: #sending all 'a' object in obj 
                    seat=obj.seat1 #to get total seats
            
            date=request.POST['date']
            
            data['html_train_list'] = render_to_string('files/ajaxinclude/train_results.html', {
                'trains': t,'date':date,'seat':seat
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
    t=Travel_Schedule.objects.filter(train_no=pk)
    seat=Train.objects.filter(sid=pk)
    
    
    form=CustomerForm()
    data=dict()
    data["html_form"]=render_to_string('files/ajaxinclude/booking_detail.html', {
                "form":form,'trains':t,'seat':seat
            },request=request)
    return JsonResponse(data)
    
    
    
