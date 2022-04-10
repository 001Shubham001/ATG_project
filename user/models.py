from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin= models.BooleanField('is_admin',default=False),
    is_doctor= models.BooleanField('is_doctor',default=False),
    is_patient= models.BooleanField('is_patient',default=False),