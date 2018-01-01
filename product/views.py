from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product
from .forms import LoginForm, RegisterForm, UploadForm
from django.utils import timezone
import pandas as pd
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def index(request):
    log_form = LoginForm()
    reg_form = RegisterForm()
    return render(request, 'product/index.html', {'log_form': log_form, 'reg_form': reg_form})

def detail(request, product_name):
    product = get_object_or_404(Product, product_name=product_name)
    return render(request, 'product/detail.html', {'product': product})

def uploaddata(request):
    if request.method=='POST' and request.FILES:        
    
        uploadform = UploadForm(request.POST, request.FILES)
        
        if uploadform.is_valid():
            
            datafile = request.FILES['uploadfile']
            data = pd.read_excel(datafile)
            i=0
            #Delete all products as a start
            Product.objects.all().delete()
            for prod in data['product_name']: 
                if Product.objects.filter(product_name__exact=prod).exists():
                    pass
                else:
                    p = Product(product_name = prod, pub_date = timezone.now(), product_des = data.iloc[i]['product_des'],
                                product_price = data.iloc[i]['product_price'], product_image = data.iloc[i]['Image'])
                    p.save()
                    i=i+1
        
        product_list = Product.objects.all()
        uploadform = UploadForm()
        return render(request, 'product/user.html', {
                                             'product_list': product_list,
                                             'uploadform': uploadform})
    else:
       
        product_list = Product.objects.all()
        uploadform = UploadForm()
        return render(request, 'product/user.html', { 
                                             'product_list': product_list,
                                             'uploadform': uploadform})
            
def validate_username(request):
    username = request.GET.get('username', None)
    user = {
            'exists': User.objects.filter(username__exact=username).exists()
            }   
    return JsonResponse(user)
        
def register_user(request):
    if request.method=='POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['reg_username']
            email = reg_form.cleaned_data['reg_email']
            password = reg_form.cleaned_data['reg_password']
            user = User.objects.create_user(username, email, password)
            user.save()
        else:
            reg_form=RegisterForm()
            return render (request, 'product/index.html', {'reg_form': reg_form})
        return render(request, 'product/user.html', {'user': username})

def login_user(request):
    if request.method=='POST':
        log_form=LoginForm(request.POST)
        if log_form.is_valid():
            username = log_form.cleaned_data['log_username']
            password = log_form.cleaned_data['log_password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                product_list = Product.objects.all()
                uploadform = UploadForm()
                return render(request, 'product/user.html', {'user': username, 
                                                             'product_list': product_list,
                                                             'uploadform': uploadform})
            else:
                return HttpResponse('Login error')
    
#
    
