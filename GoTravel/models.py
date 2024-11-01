from django.db import models
from django.contrib.auth.models import User

class jeju(models.Model):
    kor_name = models.CharField(max_length=100, default='제주')
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/') # 장소 리스트 썸네일
    address = models.CharField(max_length=255)
    thumbnail = models.ImageField(default='thumbnails/jeju.jpg') # 여행지 선택 썸네일


class gyeongju(models.Model):
    kor_name = models.CharField(max_length=100, default='경주')
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)
    thumbnail = models.ImageField(default='thumbnails/gyeongju.jpg')

class yeosu(models.Model):
    kor_name = models.CharField(max_length=100, default='여수')
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)
    thumbnail = models.ImageField(default='thumbnails/yeosu.jpg')

class jeonju(models.Model):
    kor_name = models.CharField(max_length=100, default='전주')
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)
    thumbnail = models.ImageField(default='thumbnails/jeonju.jpg')


class Recommendation(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title