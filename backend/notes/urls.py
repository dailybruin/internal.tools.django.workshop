from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
# a/views/b
# notes/a/b
router.register('b',  views.NoteViewSet)

urlpatterns = [
	# /notes/hello_world
    path("hello_world", views.hello_world),
    path("json", views.get_json),
    path("create", views.create),
    path("read/<int:id>", views.read),
    path("update/<int:id>", views.update),
    path("list", views.list),
    path("delete/<int:id>", views.delete),
    path("a/", include(router.urls))
    # path("drf_notes/", views.NoteViewSet.as_view({'get': 'list'}))
]