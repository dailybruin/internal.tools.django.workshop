from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register('notes',  views.NoteViewSet);

urlpatterns = [
	# /notes/hello_world
    path("hello_world", views.hello_world),
    path("json", views.get_json),
    path("create", views.create),
    path("notes/<int:id>", views.notes) ,
    path("drf_notes/", views.NoteViewSet.as_view({'get': 'list'}))
]