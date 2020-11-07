from django.http import HttpResponse, JsonResponse
import json
from .models import Note
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view



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


# class NoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Note
#         fields = ['title', 'body', 'id']

# # ViewSets define the view behavior.
# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# @api_view(["GET"])
# def episode_latest(request, series_title):
# 	print("hi")
# 	logging.debug('This message should go to the log file')
# 	series = get_object_or_404(
# 		Series,
# 		series_title__iexact=series_title
# 	)
# 	serializer = EpisodeSerializer(series.episode_set.order_by("-episode_number").first())
# 	return JsonResponse(serializer.data)


# @api_view(['POST'])
# def post_create(request):
#     user = request.user
#     req_data = request.data
#     print(req_data)
#     return JsonResponse({"status": "ok"})