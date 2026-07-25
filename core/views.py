from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from core.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

class RegisterView(View):
    def get(self, request):
        form=AuthenticationForm()
        return render(request, 'register.html', {'form':form })

    def post(self, request):
        form_data=AuthenticationForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data["username"]
            password=form_data.cleaned_data["password"]

            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'form':form_data, 'user_err':'user already exists' })
            else:
                user=User.objects.create_user(username=username, password=password)
                login(user)
                return redirect('home')
        else:
            return render(request, 'register.html', {'form':form_data, 'invalid':'invalid inputs entered' })
        
                
class LoginView(View):
    def get(self, request):
        form=AuthenticationForm()
        return render(request, 'login.html', {'form':form })

    def post(self, request):
            form_data=AuthenticationForm(request.POST)
            if form_data.is_valid():
                username=form_data.cleaned_data["username"]
                password=form_data.cleaned_data["password"]
                user=authenticate(username=username, password=password)
                if user is not None:
                    login(user)
                    return redirect('home')
                else:
                    return render(request, 'login.html', {'form':form_data, 'user_err':'User not found register.' })
            else:
                return render(request, 'login.html', {'form':form_data, 'invalid':'invalid inputs entered' })

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')  
