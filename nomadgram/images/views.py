from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllImages(APIView):

    def get(self, request, format=None):
        """for get request"""
        all_images = models.Image.objects.all() # get all Image data from db
        serializer = serializers.ImageSerializer(all_images, many=True) # for serialize image objects
        
        return Response(data=serializer.data)

list_all_images_view = ListAllImages.as_view()

class ListAllComments(APIView):

    def get(self, request, format=None):
        
        all_comments = models.Comment.objects.all() # get all Comment data from db
        serializer = serializers.CommentSerializer(all_comments, many=True) # for serialize comment objects

        return Response(data=serializer.data)

list_all_comments_view = ListAllComments.as_view()

class ListAllLikes(APIView):

    def get(self, request, format=None):
        
        all_likes = models.Like.objects.all() # get all Like data from db
        serializer = serializers.LikeSerializer(all_likes, many=True) # for serialize like objects

        return Response(data=serializer.data)

list_all_likes_view = ListAllLikes.as_view()