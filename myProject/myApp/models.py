from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=(
        (1,"admin"),
        (2,"staff"),
        (3,"students"),
    )



    user_type=models.CharField(choices=USER,max_length=50,default=1)
    profile_pic=models.ImageField(upload_to="media/profile_pic")

# Create your models here.
