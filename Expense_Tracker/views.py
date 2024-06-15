from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def first_page(request):
        return render(request, "firstPage.html")

def login_user(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("expenses/home")
        else:
            print("Invalid Username or Password")
            return render(request, "login.html", {"error": "Invalid Username or Password"})
    else:
        return render(request, "login.html", {"error": ""})

def register(request):
    if request.method == "POST":
        first_name_form = request.POST.get("first_name")
        last_name_form = request.POST.get("last_name")
        email_id_form = request.POST.get("email_id")
        username_form = request.POST.get("username")
        passwd_form = request.POST.get("passwd")
        conf_passwd_form = request.POST.get("conf_passwd")
        if passwd_form == conf_passwd_form:
            if User.objects.filter(username=username_form).exists():
                print("Username Taken")
                messages.info(request, "Username Taken")
            elif User.objects.filter(email=email_id_form).exists():
                print("Email Taken")
                messages.info(request, "Email Taken")
            else:
                user = User.objects.create_user(
                    username=username_form,
                    password=passwd_form,
                    email=email_id_form,
                    first_name=first_name_form,
                    last_name=last_name_form,
                )
                user.save()
                return redirect("login")
        else:
            print("password doesnt match")
            messages.info(request, "Password Doesn't Match!!")
    return render(request, "register.html")

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def change_password(request):
    if request.method == "POST":
        username = request.POST.get("username")
        old_passwd = request.POST.get("old_passwd")
        new_passwd = request.POST.get("new_passwd")
        conf_passwd = request.POST.get("conf_passwd")
        user = authenticate(request, username=username, password=old_passwd)
        if user is not None:
            if new_passwd == conf_passwd:
                user.set_password(new_passwd)
                user.save()
            else:
                print("Password doesnt match")
                messages.info(request, "Password Doesn't Match!!")
    return render(request, "change_password.html")