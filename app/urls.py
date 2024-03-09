"""
URL configuration for app app.

"""
from django.contrib import admin
from django.urls import path, include
from .views import CreateView, EditView, ListView, IndexView

app_name = "app"

urlpatterns = [
    path( "", IndexView.as_view(), name = "home" ),

    path( "create/", CreateView.as_view(), name = "create" ),

    path( "edit/<slug:slug>", EditView.as_view(), name = "edit" ),

    path( "list/", ListView.as_view(), name = "list" ),
]
