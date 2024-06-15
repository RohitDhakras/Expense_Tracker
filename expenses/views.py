from json import dumps
import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import HttpResponse
from django.db.models import Q
from .forms import manageExpenseForm
from .models import expense
from categories.models import categories
import django.utils.timezone as date

@login_required
def manage_expense_ins_fn(request):
    if request.method == "POST":
        manage_expense_form = manageExpenseForm(request.POST)
        manage_expense_form.fields["expense_category"].queryset = categories.objects.filter(user=request.user)
        if manage_expense_form.is_valid():
            form = manage_expense_form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("manage_expense_ins")
        
    manage_expense_form = manageExpenseForm()
    manage_expense_form.fields["expense_category"].queryset = categories.objects.filter(user=request.user)
    manage_expense_table_data = expense.objects.filter(user=request.user)
    data = {
        "manage_expense_form": manage_expense_form,
        "manage_expense_table_data": manage_expense_table_data,
        "username": request.user,
        "user_initial_img": "dist/img/user-"+request.user.username[0]+".png",
    }
    return render(request, "expenses/manage_expenses.html", data)

@login_required
def manage_expense_upd_fn(request, expense_id):
    expense_inst = expense.objects.get(id=expense_id)
    manage_expense_form = manageExpenseForm(instance=expense_inst)
    manage_expense_form.fields["expense_category"].queryset = categories.objects.filter(user=request.user)

    if request.method == "POST":
        manage_expense_form = manageExpenseForm(request.POST, instance=expense_inst)
        manage_expense_form.fields["expense_category"].queryset = categories.objects.filter(user=request.user)
        if manage_expense_form.is_valid():
            manage_expense_form.save()
            return redirect("manage_expense_ins")
        
    manage_expense_table_data = expense.objects.filter(user=request.user)
    data = {
        "manage_expense_form": manage_expense_form,
        "manage_expense_table_data": manage_expense_table_data,
        "username": request.user,
        "user_initial_img": "dist/img/user-"+request.user.username[0]+".png",
    }
    return render(request, "expenses/manage_expenses.html", data)

@login_required
def manage_expense_del_fn(request, expense_id):
    expense_inst = expense.objects.get(id=expense_id)
    expense_inst.delete()
    messages.success(request,'Expense Record deleted successfully!')
    return redirect("manage_expense_ins")

def home(request):
    categories_list = categories.objects.filter(user=request.user)
    expense_list = expense.objects.filter(user=request.user)

    categories_list_arr = []
    categories_values_arr = []
    categories_colours_arr = []
    for record in categories_list:
        categories_list_arr.append(record.category)

    for element in categories_list_arr:
        sum = 0
        for record in expense_list:
            if str(record.expense_category) == element:
                sum = 1*sum + 1*record.expense_amount
            colour = "%06x" % random.randint(0, 0xFFFFFF)
        categories_values_arr.append(sum)
        categories_colours_arr.append('#'+colour)


    dates_list =[]
    amounts_list = []
    for record in expense_list:
        if record.expense_date not in dates_list:
            dates_list.append(record.expense_date)
            date_records = expense_list.filter(expense_date=record.expense_date)
            sum = 0
            for date_record in date_records:
                sum = sum + date_record.expense_amount
            amounts_list.append(sum)

    print(dates_list)
    print(amounts_list)


    data = {
        "username": request.user,
        "user_initial_img": "dist/img/user-"+request.user.username[0]+".png",
        "pieChartLabels": categories_list_arr,
        "pieChartData": categories_values_arr,
        "pieChartColours": categories_colours_arr,
    }
    return render(request, "expenses/home.html", data)