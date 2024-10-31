from django.db import models


class jeju(models.Model):
    kor_name = models.CharField(max_length=100, default='제주')
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)
    thumbnail = models.ImageField(default='thumbnails/jeju.jpg')


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