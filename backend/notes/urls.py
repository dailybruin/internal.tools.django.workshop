from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	# /notes/hello_world
    path("hello_world", views.hello_world),
    path("json", views.get_json),
    path("create", views.create),
    path("notes/<int:id>", views.notes) 

]