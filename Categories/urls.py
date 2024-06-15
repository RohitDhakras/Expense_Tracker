from django.contrib import admin
from django.urls import path
from categories import views as category_view

urlpatterns = [
    path(
        "manage-category-ins",
        category_view.manage_category_ins_fn,
        name="manage_category_ins"
    ),
    path(
        "manage-category-upd/<int:category_id>",
        category_view.manage_category_upd_fn,
        name="manage_category_upd"
    ),
    path(
        "manage-category-del/<int:category_id>",
        category_view.manage_category_del_fn,
        name="manage_category_del"
    ),
]