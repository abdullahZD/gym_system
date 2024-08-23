from django.shortcuts import render ,redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.db.models import Q
import logging
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'web/index.html')

#register new user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registeration is Successfuly')
            return redirect('login.html')
    else:
        form = CreateUserForm()    

    context = {'form':form}        
    return render(request, 'web/register.html',context)


#login
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                messages.success(request,'Login is Successfuly')
                return redirect('dashboard')
    else:
        form = LoginForm()
    context = {'form':form}  
    return render(request, 'web/login.html',context)  


#dashboard
@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    return render(request,'web/dashboard.html',context={'records':records})


#logout
def my_logout(request):
    logout(request)
    messages.success(request,'Logout is Successfuly')
    return redirect('login')

#Create Record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Record is Successfuly Created')
            return redirect('dashboard')
    else:
        form = CreateRecordForm()    
        
    context = {'form':form}   
    return render(request,'web/create-record.html',context=context) 

#View Records
@login_required(login_url='login')
def view_record(request,record_id):
    all_records = get_object_or_404(Record,id=record_id)
    context = {'records':all_records}
    return render(request,'web/view_record.html',context)

#Update Record
@login_required(login_url='login')
def update_record(request,record_id):
    record = get_object_or_404(Record,id=record_id)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record is Successfuly Updated')
            return redirect('dashboard')
        
    context = {'form':form}
    return render(request,'web/update-record.html',context)   


#Delete Record
@login_required(login_url='login')
def delete_record(request,record_id):
    record = get_object_or_404(Record,id=record_id)
    record.delete()
    messages.success(request,'Record is Successfuly Deleted')
    return redirect('dashboard')

#Search view
logger = logging.getLogger(__name__)
@login_required(login_url='login')
def search(request):
    query = request.GET.get('query')
    results = []
    try:
        if query:
            results = Record.objects.filter(Q(first_name__icontains = query) | Q(id__icontains = query))
    except Exception as e:
        logger.error('Error during search: %s',e)    
    return render(request,'web/search.html',context={'results':results,'query':query})    

#custom 404
def custom_page_not_found(request,exception):
    return render(request,'web/404.html',status=404)   
