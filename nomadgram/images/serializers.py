# for DRF
from rest_framework import serializers
from . import models

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__' # Image model의 모든 필드 시리얼라이즈

class CommentSerializer(serializers.ModelSerializer):

    image = ImageSerializer()
    
    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    image = ImageSerializer() # Like object의 image 필드에 nested serializer 적용

    class Meta:
        model = models.Like
        fields = '__all__'
