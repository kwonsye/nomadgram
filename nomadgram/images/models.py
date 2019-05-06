from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    #base model for timestamp
    created_at = models.DateTimeField(auto_now_add=True) # 인스턴스가 생성될때마다 자동으로 채워짐
    updated_at = models.DateTimeField(auto_now=True) # 인스턴스가 업데이트 될때마다 업데이트됨

    class Meta:
        abstract = True # 다른 class의 base abstract class 로 사용될 것임 https://docs.djangoproject.com/en/1.11/topics/db/models/#abstract-base-classes

class Image(TimeStampedModel):
    # 사진 model
    file = models.ImageField() # 이미지 파일
    location = models.CharField(max_length=140)
    caption = models.TextField()

class Comment(TimeStampedModel):
    # 댓글 model
    message = models.TextField()