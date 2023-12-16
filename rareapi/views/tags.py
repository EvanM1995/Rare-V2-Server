from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tag
from rareapi.serializers import TagSerializer

class TagView(ViewSet):
  
  def create(self, request):
    """Handles CREATE tag"""
    
    tag = Tag.objects.create(
      label=request.data["label"],
    )
    serializer = TagSerializer(tag)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def update(self, request, pk):
    """Handles UPDATE request for tags"""
    
    tag = Tag.objects.get(pk=pk)
    tag.label = request.data["label"]

    tag.save()
    serializer = TagSerializer(tag)
    return Response (serializer.data, status=status.HTTP_200_OK)

  def destroy(self, request, pk):
    """Handles Delete request for genre"""
    
    tag = Tag.objects.get(pk=pk)
    tag.delete()
    
    return Response (None, status=status.HTTP_204_NO_CONTENT)
