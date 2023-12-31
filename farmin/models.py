from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#농부 model
class User(models.Model):
    Farmer_pic = models.TextField(null=True, default='path_to_default_pic')
    Farmer_back_pic = models.TextField(null=True, default='path_to_default_pic')
    Farmer_name = models.CharField(max_length=50, null=True)
    Farmer_tel = models.CharField(max_length=100, unique=True)
    Farmer_intro = models.TextField(null=True, default='반갑습니다')
    Farmer_others = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.Farmer_name

#농장 model
class Farm(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)

class FarmPics(models.Model):
    Farm_id = models.ForeignKey(Farm, on_delete=models.CASCADE)
    Farm_pics = models.TextField(null=True, default='path_to_default_pic')

#판매중인 상품 model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='posts')   
    author_pic = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length= 30, null = True)
    content = models.TextField(null = True)
    price = models.TextField(null =True)
    create_date = models.DateTimeField()
    like = models.PositiveIntegerField(default = 0) #양의 정수 필드: 기본값은 0에서 시작
    Post_pics=models.TextField(null=True, default='default_pic')

    def __str__(self):
        return self.title 
    
#방명록 model
class Guestbook(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()