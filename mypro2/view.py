from django.shortcuts import render,redirect
def login(request):
    return render(request,"login.html")
def check(request):
    username=request.GET['username']
    password=request.GET['password']

    if(username =="admin" and password =="admin123"):
        return redirect(home)
    else:
        return redirect(invalid)

def home(request):
    return render(request,"home.html")
def invalid(request):
    return render(request,"invalid.html")