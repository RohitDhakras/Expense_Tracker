from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import HttpResponse
from django.db.models import Q
from .forms import manageCategoriesForm
from .models import categories

@login_required
def manage_category_ins_fn(request):
    if request.method == "POST":
        manage_category_form = manageCategoriesForm(request.POST)
        if manage_category_form.is_valid():
            form = manage_category_form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("manage_category_ins")
        
    manage_category_form = manageCategoriesForm()
    manage_category_table_data = categories.objects.filter(user=request.user)
    data = {
        "manage_category_form": manage_category_form,
        "manage_category_table_data": manage_category_table_data,
        "username": request.user,
        "user_initial_img": "dist/img/user-"+request.user.username[0]+".png",
    }
    return render(request, "categories/manage_categories.html", data)

@login_required
def manage_category_upd_fn(request, category_id):
    category_inst = categories.objects.get(id=category_id)
    manage_category_form = manageCategoriesForm(instance=category_inst)

    if request.method == "POST":
        manage_category_form = manageCategoriesForm(request.POST, instance=category_inst)
        if manage_category_form.is_valid():
            manage_category_form.save()
            return redirect("manage_category_ins")
        
    manage_category_table_data = categories.objects.filter(user=request.user)
    data = {
        "manage_category_form": manage_category_form,
        "manage_category_table_data": manage_category_table_data,
        "username": request.user,
        "user_initial_img": "dist/img/user-"+request.user.username[0]+".png",
    }
    return render(request, "categories/manage_categories.html", data)

@login_required
def manage_category_del_fn(request, category_id):
    category_inst = categories.objects.get(id=category_id)
    category_inst.delete()
    messages.success(request,'Category deleted successfully!')
    return redirect("manage_category_ins")