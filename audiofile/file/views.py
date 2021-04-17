from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from .models import Song,Podcast,Audiobook
from .serializers import SongSerializer,PodcastSerializer,AudioSerializer
from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
from django.http import HttpResponse


def SavingSerializers(serializer):
	try:
		if serializer.is_valid():
			serializer.save()
			msg = 'Action is successful: 200 OK'
	except:
		msg = 'The request is invalid: 400 bad request'
	return msg

msg='Any error: 500 internal server error'

@api_view(['POST'])
def createdata(request,mk,pk):
	try:
		if mk=='song':
			serializer = SongSerializer(data=request.data)
			msg = SavingSerializers(serializer)
		elif mk == 'podcast':
			serializer = PodcastSerializer(data=request.data)
			msg = SavingSerializers(serializer)
		elif mk == 'audiobook':
			serializer = AudioSerializer(data=request.data)
			msg = SavingSerializers(serializer)
		return HttpResponse(msg)
	except:
		return HttpResponse(msg)
	
	
@api_view(['DELETE'])
def deletedata(request,mk,pk):
	if mk=='song':
		try:
			song  = Song.objects.get(ID=pk)
			song.delete()
			return HttpResponse('Action is successful: 200 OK')
		except:
			return HttpResponse('The request is invalid: 400 bad request')
	elif mk == 'podcast':
		try:
			podcast  = Podcast.objects.get(ID=pk)
			podcast.delete()
			return HttpResponse('Action is successful: 200 OK')
		except:
			return HttpResponse('The request is invalid: 400 bad request')
	elif mk == 'audiobook':
		try:
			audiobook  = Audiobook.objects.get(ID=pk)
			audiobook.delete()
			return HttpResponse('Action is successful: 200 OK')
		except:
			return HttpResponse('The request is invalid: 400 bad request')
	return HttpResponse('Any error: 500 internal server error')
	
@api_view(['POST'])
def updatedata(request,mk,pk):
	if mk=='song':
			song  = Song.objects.get(ID=pk)
			serializer = SongSerializer(instance = song,data=request.data)
			msg = SavingSerializers(serializer)

	elif mk == 'podcast':
		podcast  = Podcast.objects.get(ID=pk)
		serializer = PodcastSerializer(instance = podcast,data=request.data)
		msg = SavingSerializers(serializer)

	elif mk == 'audiobook':
		audiobook  = Audiobook.objects.get(ID=pk)
		serializer = AudioSerializer(instance = audiobook,data=request.data)
		msg = SavingSerializers(serializer)

	return HttpResponse(msg)

def getData(pk,modelname,serializername):
	if pk ==None:
		song  = modelname.objects.all()
		serializer = serializername(song,many=True)
	else:
		song  = modelname.objects.get(ID=pk)
		serializer = serializername(song,many=False)
	value = serializer.data
	return value

@api_view(['GET'])
def getdata(self,*args,**kwargs):
	value = 'Any error: 500 internal server error'
	mk= kwargs.get('mk')
	try:
		pk = kwargs.get('pk')
	except:
		pk=''
	if mk=='song':
		value = getData(pk,Song,SongSerializer)	
	elif mk == 'podcast':
		value = getData(pk,Podcast,PodcastSerializer)	
	elif mk == 'audiobook':
		value = getData(pk,Audiobook,AudioSerializer)
	return Response(value)