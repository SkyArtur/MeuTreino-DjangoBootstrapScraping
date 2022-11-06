from django.shortcuts import render, redirect
from django.contrib import auth, messages
from myApp.forms import LoginForm


# Create your views here.
def view_login(request):
    form = LoginForm(request.POST)
    if request.method != 'POST':
        return render(request, 'accounts/login.html', {'form': form})
    user = auth.authenticate(request,
                             username=request.POST['username'],
                             password=request.POST['password'])
    if not user:
        messages.error(request, 'Usuario ou senha inválidos!')
        return render(request, 'accounts/login.html', {'form': form})
    else:
        messages.success(request, 'Login Efetuado com sucesso')
        auth.login(request, user)
        return redirect('index')
