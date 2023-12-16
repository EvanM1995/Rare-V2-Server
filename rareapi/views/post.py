from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post
from .auth import User
from .category import Category

class PostView(ViewSet):
  def retrieve(self, request, pk):

    try:
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except post.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

  def list(self, request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

  def create(self, request):
      rare_user_id = User.objects.get(pk=request.data['rare_user_id'])
      category_id = Category.objects.get(pk=request.data['category_id'])

      post = Post.objects.create(
          rare_user_id = rare_user_id,
          category_id = category_id,
          title = request.data["title"],
          publication_date = request.data["publication_date"],
          image_url = request.data["image_url"],
          content = request.data["content"],
          approved = request.data["approved"],
      )

      serializer = PostSerializer(post)
      return Response(serializer.data)

  def update(self, request, pk):
      post = Post.objects.get(pk=pk)
      post.title = request.data["title"]
      post.publication_date = request.data["publication_date"]
      post.image_url = request.data["image_url"]
      post.content = request.data["content"]
      post.approved - request.data["approved"]

      rare_user_id = User.objects.get(uid=request.data["rare_user_id"])
      post.rare_user_id = rare_user_id
      post.save()

      category_id = Category.objects.get(pk=request.data["category_id"])
      post.category_id = category_id
      post.save()

      return Response(None, status=status.HTTP_204_NO_CONTENT)

  def destroy(self, request, pk):

      post = Post.objects.get(pk=pk)
      post.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)


class PostSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Post
        fields = ('id', 'rare_user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved')
