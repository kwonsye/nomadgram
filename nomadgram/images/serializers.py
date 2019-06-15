# for DRF
from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models

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


class ImageSerializer(serializers.ModelSerializer):

    #comment_set = CommentSerializer(many=True) # comment에서 foreign key로 연결된 image에 해당하는 comment object를 가져옴
    #like_set = LikeSerializer(many=True)
    comments = CommentSerializer(many=True) # model의 related_name
    creator = FeedUserSerializer()

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
            'like_count',
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