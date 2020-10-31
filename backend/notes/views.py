from django.http import HttpResponse
import json
from .models import Note



def hello_world(request):
	return HttpResponse("hello world")


def get_json(request):
	body = request.GET["body"]
	return HttpResponse(json.dumps({
		"title": "Notes about CS 181",
		"body": body
	}))


def create(request):
	"""
	request.GET["title"]  => title of new note
	request.GET["body"]   => body of the new note
	"""
	

	note = Note.objects.create(
		title=request.GET["title"],
		body=request.GET["body"]
	)

	return HttpResponse("Success")

def notes(request, id):
	note = Note.objects.get(id=id)
	return HttpResponse(json.dumps({
		"title": note.title,
		"body": note.body
	}))

