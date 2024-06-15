from django.contrib import admin
from django.urls import path
from expenses import views as expense_view

urlpatterns = [
    path(
        "manage-expense-ins",
        expense_view.manage_expense_ins_fn,
        name="manage_expense_ins"
    ),
    path(
        "manage-expense-upd/<int:expense_id>",
        expense_view.manage_expense_upd_fn,
        name="manage_expense_upd"
    ),
    path(
        "manage-expense-del/<int:expense_id>",
        expense_view.manage_expense_del_fn,
        name="manage_expense_del"
    ),
    path(
        "home",
        expense_view.home,
        name="home"
    ),
]