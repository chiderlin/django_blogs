from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def logout_views(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))


def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save() # class, save會return user
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1']) # 認證新用戶 會return user
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('blog_app:homepage'))
    context = {"form": form}
    return render(request, "registration/register.html", context)

