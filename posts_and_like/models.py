from django.db import models
from django.db.models.deletion import CASCADE
from user_auth import models as usmodels
from django.utils import timezone
from django.contrib.auth.models import User,Group


import user_auth
class Post(models.Model):
    profile = models.ForeignKey(usmodels.Profile,on_delete=models.CASCADE)
    postinfo = models.TextField(max_length=400)
    likecount = models.IntegerField(default=0)
    
    timeday = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.profile,self.postinfo)
	   
class Comment(models.Model):
    on_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    description= models.CharField(max_length=500)
    by_user  =  models.ForeignKey(usmodels.Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.description



class Like(models.Model):
    isliked = models.BooleanField(default=False)
    profile = models.ForeignKey(usmodels.Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return '%s - %s' % (self.profile,self.post)