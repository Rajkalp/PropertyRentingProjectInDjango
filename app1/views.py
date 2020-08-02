from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app1.forms import CreateUserForm
from django.contrib import messages


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import UploadProperty
from .models import Property



# Create your views here.
def index(request):
    if (request.user.is_authenticated):
        print("authenticated")
        if request.user.groups.filter(name='lessee').exists():
            return redirect("/landlorddash")
        elif request.user.groups.filter(name='tenant').exists():
            return redirect("/home")
    else:
        print(request.method)
        if (request.method == "POST"):
            username = request.POST.get("usernamelogin")
            password = request.POST.get("passwordlogin")
            print("username", username, "pwd", password)
        
            user = authenticate(request, username=username, password=password)
            print("user is ",user)   

            if (user is not None):
                login(request, user)  
                return redirect('/')
        elif (request.method =="GET"):
            print("get method")
            return render(request, "login.html")

def tenantRegister(request):
    form = CreateUserForm(request.POST)
    if(form.is_valid()):
        user = form.save()
        group = Group.objects.get(name="tenant")
        user.groups.add(group)
        return redirect("/")
    return render(request, "tenantregister.html", {'form': form})

def landlordRegister(request):
    if (request.user.is_authenticated):
        return redirect("/home")
    else:
        print(request.method)
        form = CreateUserForm(request.POST)
        if(request.method == "POST"):
            if(form.is_valid()):
                user = form.save()
                # Add registered user to tenent group
                group = Group.objects.get(name="lessee")
                user.groups.add(group)
                # user.groups.remove(group)      #remove from group
                return redirect("/")
        return render(request, "landlordregister.html",  {'form': form})


def register(request):
    if (request.user.is_authenticated):
        return redirect("/home")
    else:
        print(request.method)
        form = CreateUserForm(request.POST)
        if(request.method == "POST"):
            if(form.is_valid()):
                user = form.save()

                # Add registered user to tenent group
                group = Group.objects.get(name="tenant")
                user.groups.add(group)
                # user.groups.remove(group)      #remove from group
        return render(request, "register.html",  {'form': form})

def logoutuser(request):
    logout(request)
    return redirect('/')


def home(request):
    if (request.user.is_authenticated):
        return render(request,"home.html")
    else:
        return redirect("/")

def landlorddash(request):
    if request.user.groups.filter(name='lessee').exists():
        rentProperty = Property.objects.filter(owner__username=request.user).values()
        print(rentProperty)
        return render(request, "landlorddash.html", {'property':rentProperty})
    else:
        return redirect("/")
    

def userdashboard(request):
    result = Property.objects.filter(rentedby=request.user.username).values()
    print(request.user.username)
    return render(request, "userdashboard.html", {'properties': result})

def uploadproperty(request):
    form = UploadProperty(request.POST)
    if request.method == "POST":        
        if form.is_valid:
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            
            groupremove = Group.objects.get(name="tenant")
            request.user.groups.remove(groupremove)
            
            groupadd = Group.objects.get(name="lessee")
            request.user.groups.add(groupadd)
            
            return redirect("/")
    return render(request, "uploadproperty.html", {'form': form})

def deleteproperty(request, id):
    Property.objects.filter(id=id).delete()
    return redirect("/")

def searchresult(request):
    query = request.GET.get('search')
    result = Property.objects.filter(city=query).values()
    print(result.values('address1'))
    return render(request, "searchresult.html", {'data': result})

def bookproperty(request, id, userid):
    print(id, userid)
    Property.objects.filter(id=id).update(rentedby=userid)
    return redirect("/")

def removeproperty(request, id):
    Property.objects.filter(id=id).update(rentedby=None)
    return redirect('/userdash')