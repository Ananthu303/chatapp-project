from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Room(models.Model):
    host=models.ForeignKey(User,models.SET_NULL,null=True)
    topic= models.ForeignKey(Topic,models.SET_NULL,null=True)
    sub_topic=models.CharField(max_length=200)
    participants=models.ManyToManyField(User,related_name='participants')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.sub_topic
    


class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.body[0:50]

class ProfileModel(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    email=models.EmailField(null=True,blank=True)
    bio=models.CharField(max_length=200,null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True,default="gofg_7CJTSER.jpg")
    def __str__(self):
        return self.name.__str__()
