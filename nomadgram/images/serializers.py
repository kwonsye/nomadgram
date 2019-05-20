# for DRF
from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):

    #image = ImageSerializer()

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    #image = ImageSerializer() # Like object의 image 필드에 nested serializer 적용

    class Meta:
        model = models.Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):

    #comment_set = CommentSerializer(many=True) # comment에서 foreign key로 연결된 image에 해당하는 comment object를 가져옴
    #like_set = LikeSerializer(many=True)
    comments = CommentSerializer(many=True) # model의 related_name
    likes = LikeSerializer(many=True)

    class Meta:
        model = models.Image
        fields = (
            'creator',
            'file',
            'location',
            'caption',
            #'comment_set',
            #'like_set',
            'comments',
            'likes',
        ) 
