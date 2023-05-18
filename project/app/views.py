from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import VideoSerializer
from .models import Video
from .vid_processing import process
import os

# Create your views here.

@api_view(['POST', 'GET'])
def upload_vid(request):
    if request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            Video.objects.all().delete()
            fi = os.listdir('media/video')[0]
            os.remove(os.path.join('media/video', fi))
            serializer.save()
            filename = os.listdir('media/video')[0]
            process(filename)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        