from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import VideoSerializer
from .models import Video
from .vid_processing import process
import os
from django.core.files.base import File
from django.http import QueryDict

# Create your views here.

@api_view(['POST', 'GET'])
def upload_vid(request):
    if request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            Video.objects.all().delete()
            fi = os.listdir('media/video')
            if len(fi) > 0:
                for name in fi:
                    os.remove(os.path.join('media/video', name))
            serializer.save()
            filename = os.listdir('media/video')[0]
            process(filename)
            # vi = open(os.path.join('media/video', filename), 'rb')
            oridict = {'caption': 'response', 'video': '/media/video/response.avi'}
            return Response(oridict, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        