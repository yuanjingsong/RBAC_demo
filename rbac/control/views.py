from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Role, Url, user_role, Op, Resource
# Create your views here.
def index(request):
    is_Login = request.session.get('logined', None)
    username = request.session.get('user', None)

    if not is_Login:
        return render (request, "login.html")
    
    user = getUser(username)
    url = getUrl("/control")
    role = getRole(user, url)

    context = {"name": user.nickName,
            "role": role,
            }

    return render(request, "index.html", context)

def login(request):
    user = request.POST['username']
    pwd = request.POST['pwd']
    if check(user, pwd):
        request.session['logined'] = True
        request.session['user'] = user

    return redirect("index")

def logOut(request):
    is_Login = request.session.get('logined', None)
    if is_Login:
        del request.session['logined']

    #return render(request, 'login.html')
    return redirect("index")

def check(username, pwd):
    password = User.objects.get(name=username).pwd
    try:
        password = User.objects.get(name=username).pwd
        print(password)
        if pwd == password:
            return True
        else :
            return False
    except : 
        return False

def getUser(username):
    return User.objects.get(name=username)

def getUrl(url):
    return Url.objects.get(url=url)

def getRole(user, url):
    ur = user_role.objects.get(user_id=user, url_id=url)
    return ur.role_id.name

