from django.db import models
from nomadgram.users import models as user_models
from nomadgram.images import models as image_models

class Notification(image_models.TimeStampedModel):

    TYPE_CHOICES = (
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow'),
    )

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name="creator_notification") # User에 대한 외래키가 두개이므로 related_name 필수
    to = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name="to_notification")
    notification_type = models.CharField(max_length=40, choices=TYPE_CHOICES)
    image = models.ForeignKey(image_models.Image,on_delete=models.CASCADE, blank=True, null=True) # like와 comment 가 달린 image