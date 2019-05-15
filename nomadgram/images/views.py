from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllImages(APIView):

    def get(self, request, format=None):
        """for get request"""
        all_images = models.Image.objects.all() # get all Image data from db
        serializer = serializers.ImageSerializer(all_images, many=True) # for serialize images object
        
        return Response(data = serializer.data)
