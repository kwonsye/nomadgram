from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    GENDER_CHOICES = (
        ('male','Male'), #앞에 값은 db에 저장되는 값, 뒤에 값은 admin 페이지나 폼에서 표시하는 값
        ('female','Female'),
        ('not-specified','Not specified')
    ) 

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(null=True) # migration 전의 User에게 해당 필드는 공백으로 남겨짐
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
