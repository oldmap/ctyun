from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 重定向到用户之前的URL，分割
            redirect_to = request.GET.get('next')
            return HttpResponseRedirect(redirect_to)
        else:
            error_msg = '用户名或密码错误'
            return render(request, 'home/login.html', {'error': error_msg})
    else:
        return render(request, 'home/login.html', )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def index(request):
    return render(request, 'home/index.html')
