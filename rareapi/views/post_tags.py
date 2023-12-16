from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostTags, Post, Tag


class PostTagView(ViewSet):
    """Rare V2 Server Post Tags"""

    def retrieve(self, request, pk):
        """Handle GET requests for post tags
        Returns:
            Response -- JSON serialized post tags type
        """
        try:
            posttag = PostTags.objects.get(pk=pk)
            # Replace with the actual serializer
            serializer = PostTagSerializer(posttag)
            return Response(serializer.data)
        except posttag.DoesNotExist as failure:
            return Response({'message': failure.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """Handle GET requests to ALL post tags

        Returns:
            Response -- JSON serialized list of post tags
        """
        posttags = PostTags.objects.all()
        # Replace with the actual serializer
        serializer = PostTagSerializer(posttags, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle CREATE requests to create post tags"""
        post = Post.objects.get(pk=request.data['postId'])
        tag = Tag.objects.get(pk=request.data['tagId'])

        posttag = posttag.objects.create(
            post=post,
            tag=tag,
        )

        serializer = PostTagSerializer(posttag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle UPDATE post tags for a post"""
        posttag = PostTags.objects.get(pk=pk)
        post = Post.objects.get(pk=request.data['postId'])
        tag = Tag.objects.get(pk=request.data['tagId'])
        posttag.post = post
        posttag.tag = tag
        posttag.save()

        serializer = PostTagSerializer(posttag)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostTagSerializer(serializers.ModelSerializer):
    """Post Tags JSON serializer"""
    class Meta:
        model = PostTags
        fields = ('id', 'post_id', 'tag_id')
