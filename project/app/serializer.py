from .models import Video
from django import forms
from rest_framework import serializers

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('caption', 'video')