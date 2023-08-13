from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    Farmer_pic = models.ImageField(upload_to='Farmer_pic', null=True, default='default_pic')
    Farmer_name = models.CharField(max_length=50, null=True)
    Farmer_tel = models.CharField(max_length = 100, unique=True)
    Farmer_intro = models.TextField(null=True, default='반갑습니다')
    Farmer_others = models.ManyToManyField('self')

    def __str__(self):
        return self.Farmer_name

class FarmPics(models.Model):
    Farm_pics = models.ImageField(upload_to='MyFarm/photos/', null=True, default='default_pic')

class Farm(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    Farm_pic = models.ManyToManyField(FarmPics)   

class PostPics(models.Model):
    Post_pics = models.ImageField(upload_to='MyFarm/photos/', null=True, default='default_pic')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50, null = True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    like = models.PositiveIntegerField(default = 0) #양의 정수 필드: 기본값은 0에서 시작
    #like = models.ManyToManyField(User, related_name='likes' ,blank=True)-----> 우리는 슈퍼유저에서 좋아요 수를 무한정 늘릴 수 있으므로 위의 필드로 대체하는 것이 좋지 않을까?
    Post_pic = models.ManyToManyField(PostPics, blank = True)

    def __str__(self):
        return self.title 

class Comment(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)