from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment, Post, User

class CommentView(ViewSet):
  """Comment View"""
  
  def retrieve(self, request, pk):
    """Get Request for a single comment"""
    
    try:
      comment = Comment.objects.get(pk=pk)
      serializer = CommentSerializer(comment)
      return Response(serializer.data)
    except Comment.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
  def list(self, request):
    """˝Get all comments"""
    
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True) 
    return Response(serializer.data)
  
  def create(self, request):
    """Create a comment"""
    
    author = User.objects.get(pk=request.data['author_id'])
    post = Post.objects.get(pk=request.data['post_id'])
    
    comment = Comment.objects.create(
      author = author, 
      post = post,
      content = request.data['content'],
    )
    
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  
  def update(self, request, pk):
    """Updating a comment"""
    
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response({"error": "Comment does not exist"}, status=status.HTTP_404_NOT_FOUND)
   
    if 'content' in request.data:
        comment.content = request.data['content']
  
    if 'author_id' in request.data:
        try:
            author = User.objects.get(pk=request.data['author_id'])
            comment.author = author
        except User.DoesNotExist:
            return Response({"error": "Author does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if 'post_id' in request.data:
        try:
            post = Post.objects.get(pk=request.data['post_id'])
            comment.post = post
        except Post.DoesNotExist:
            return Response({"error": "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_200_OK)

  
  def destroy(self, request, pk):
    """Delete Comment"""
    
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  
class CommentSerializer(serializers.ModelSerializer):  
  """Comment JSON serializer"""
  
  class Meta:
    model = Comment
    fields = ('id', 'author_id', 'post_id', 'content', 'created_on')
      
