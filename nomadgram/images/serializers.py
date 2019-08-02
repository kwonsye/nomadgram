# for DRF
from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class FeedUserSerializer(serializers.ModelSerializer):
    """Feed에서 필요한 image creator의 정보 / Comment creator 의 정보"""
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image',
        )

class CommentSerializer(serializers.ModelSerializer):
    """ image의 댓글 """

    creator = FeedUserSerializer(read_only=True) # 수정할 수 없도록 

    class Meta:
        model = models.Comment
        fields = (
            'id', # read only field
            'message',
            'creator',
        )

class LikeSerializer(serializers.ModelSerializer):

    #image = ImageSerializer() # Like object의 image 필드에 nested serializer 적용

    class Meta:
        model = models.Like
        fields = '__all__'


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    #comment_set = CommentSerializer(many=True) # comment에서 foreign key로 연결된 image에 해당하는 comment object를 가져옴
    #like_set = LikeSerializer(many=True)
    comments = CommentSerializer(many=True) # model의 related_name
    creator = FeedUserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = models.Image
        fields = (
            'creator',
            'file',
            'created_at',
            'location',
            'caption',
            #'comment_set',
            #'like_set',
            'comments',
            'like_count',
            'tags',
        ) 

class SimpleCountImageSerializer(serializers.ModelSerializer):

    """Image 게시물의 comments 와 likes 개수를 보여주는 serializer """
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count',
        )

class SmallImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class InputImageSerializer(serializers.ModelSerializer):

    """image 수정/게시를 위한 시리얼라이저"""

    #file = serializers.FileField(required=False) # 필수 필드가 아니여서 partial update가 가능하도록 설정 -> view에서 partial=True로 설정해도됨

    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption',
        )