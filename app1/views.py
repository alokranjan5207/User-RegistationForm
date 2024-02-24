from django.shortcuts import render,HttpResponse,redirect
from .forms import RegistationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def registation_form(request):
    if request.method=='POST':
        fm=RegistationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("<h1>Registation Sucessfull</h1>")
    else:
        fm=RegistationForm()
    return render(request=request,template_name='registation.html',context={'form':fm})
    # return render(request=request,template_name='userform.html',context={'form':fm})


# def registation_form(request):
#     if request.method=='POST':
#             u=User.objects.filter(username=request.POST['username'])
#             if u.exists():
#                 messages.info(request,'Username is already exist')
#                 return redirect('registation')
#             fm=RegistationForm(request.POST)
#             if fm.is_valid():
#                 fm.save()

#     else:
#         fm=RegistationForm()
#     return render(request=request,template_name='registation.html',context={'form':fm})
#     # return render(request=request,template_name='userform.html',context={'form':fm})


def login_view(request):
    return render(request=request,template_name='login.html')