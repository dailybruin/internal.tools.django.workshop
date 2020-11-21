from django.http import HttpResponse, JsonResponse
import json
from .models import Note
from .serializers import NoteSerializer
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 




def hello_world(request):
	return HttpResponse("hello world")


def get_json(request):
	body = request.GET["body"]
	return HttpResponse(json.dumps({
		"title": "Notes about CS 181",
		"body": body
	}))

#
# GET (read), POST (writing)
#
#  CRUD operations
#   c = create
#   r = read
#   u = update
#   d = delete
#
@api_view(["POST"])
def create(request):
	"""
	request.GET["title"]  => title of new note
	request.GET["body"]   => body of the new note
	"""
	serializer = NoteSerializer(data=request.data)
	if serializer.is_valid():
		note = serializer.save()
		return JsonResponse({
			'id': note.id
		})
	else:
		return JsonResponse(serializer.errors)
	# note = Note.objects.create(
	# 	title=request.data["title"],
	# 	body=request.data["body"]
	# )

	# return JsonResponse({
	# 	'id': note.id
	# })

@api_view(['GET'])
def read(request, id):
	note = get_object_or_404(
		Note,
		id=id
	)
	# note = Note.objects.get(id=id)
	serializer = NoteSerializer(note)
	return JsonResponse(serializer.data)
	# return JsonResponse({
	# 	"title": note.title,
	# 	"body": note.body
	# })

# GET, POST, PUT (updates)
@api_view(['PUT'])
def update(request, id):
	note = get_object_or_404(
		Note,
		id=id
	)
	serializer = NoteSerializer(note, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return JsonResponse({
			'id': note.id
		})
	else:
		return JsonResponse(serializer.errors)

# DELETE => DELETE
@api_view(['DELETE'])
def delete(request, id):
	note = get_object_or_404(
		Note,
		id=id
	)

	note.delete()

	return JsonResponse({
		'id': id
	})


@api_view(['GET'])
def list(request):
	notes = Note.objects.all()

	serializer = NoteSerializer(notes, many=True)

	return JsonResponse(serializer.data, safe=False)


# class NoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Note
#         fields = ['title', 'body', 'id']

# # ViewSets define the view behavior.
# list() => get 
# create() => post
# read()  => GET /1
# destroy() => DELETE /1
# update() => PUT /1
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

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