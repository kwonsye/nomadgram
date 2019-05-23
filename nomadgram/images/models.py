from django.db import models
from nomadgram.users import models as user_models

class TimeStampedModel(models.Model):
    
    """ base model for timestamp """

    created_at = models.DateTimeField(auto_now_add=True) # 인스턴스가 생성될때마다 자동으로 채워짐
    updated_at = models.DateTimeField(auto_now=True) # 인스턴스가 업데이트 될때마다 업데이트됨

    class Meta:
        abstract = True # 다른 class의 base abstract class 로 사용될 것임 https://docs.djangoproject.com/en/1.11/topics/db/models/#abstract-base-classes

class Image(TimeStampedModel):
    
    """ 사진 model """

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True, related_name="images") # on_delete=models.CASCADE : creator모델이 지워지면 Image모델도 지워짐
    file = models.ImageField() # 이미지 파일
    location = models.CharField(max_length=140)
    caption = models.TextField()

    def __str__(self): # 인스턴스가 admin 페이지에 보이는 형식 
        return "{}-{}".format(self.location,self.caption)

    class Meta:
        ordering = ['-created_at'] # 생성된 최근 순으로 db에서 가져온다.

class Comment(TimeStampedModel):
    
    """ 댓글 model """
    
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='comments') 
        # related_name : Image object에서 해당 comment를 부를때 사용하는 필드이름 = image object에서 comment_set 필드와 동일 
                                                 

    def __str__(self):
        return self.message

class Like(TimeStampedModel):

    """ 좋아요 model """

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE,null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name="likes")

    def __str__(self):
        return "User:{} - Image Caption{}".format(self.creator.username, self.image.caption)