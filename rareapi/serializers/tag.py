from rest_framework import serializers
from rareapi.models import Tag 

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ('id', 'description')
    depth = 1
