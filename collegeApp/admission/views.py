from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserLoginDetails

def members(request):
    return render(request, "index.html")
def show(request):
    data = UserLoginDetails.objects.all().values()
    return render(request, "data.html", {"data": data})
def login(request):
    data = UserLoginDetails.objects.all().values()

def login(request):
    if request.method == "POST":
        email=request.POST.get('email')
        psw=request.POST.get('psw')

        ins = UserLoginDetails(email=email,  password=psw)
        ins.save()
    return redirect("/")


