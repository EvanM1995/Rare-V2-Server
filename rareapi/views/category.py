from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category

class CategoryView(ViewSet):

    def list(self, request):
        """Handle GET requests for all categories
        
        Returns -> Response -- JSON serialized list of categories with status of 200"""

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests for all categories
        
        Returns -> JSON serialized post instance with a status of 201"""

        category = Category.objects.create(
            label = request.data['label']
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT request for a post
        
        Returns -> JSON serialized post with a 200 status"""

        category = Category.objects.get(pk=pk)
        category.label = request.data['label']

        category.save()

        return Response(None, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        """Handles DELETE requests for a post
      
        Returns -> Empty body with 204 status"""

        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'label')
