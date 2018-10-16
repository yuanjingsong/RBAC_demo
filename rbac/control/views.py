from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    is_Login = request.session.get('logined', None)
    if not is_Login:
        return render (request, "login.html")

    context = {"name":"Yuan", "role": "Boss"}

    return render(request, "index.html", context)

def login(request):
    user = request.POST['username']
    pwd = request.POST['pwd']

    if check(user, pwd):
        request.session['logined'] = True

    return redirect("index")

def register(request):

    return 0

def check(user, pwd):
    return True
