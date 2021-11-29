from django.db import models
from django.contrib.auth.models import User,Group
#from django.contrib.postgres.fields import ArrayField



# Create your models here.

class Profile(models.Model):

	def image_dir(self,filename):
		self._image_dir=f"uploads/{self.user.username}/{filename}"
		return self._image_dir


	user = models.OneToOneField(User,on_delete=models.CASCADE)
	firstname = models.CharField(max_length=200)
	lastname  = models.CharField(max_length=200)
	dob = models.DateField(null=True)
	about = models.CharField(max_length=300)
	#profile_pic_path = models.CharField(max_length=200,default='default_profile.png')
	#cover_pic_path = models.CharField(max_length=200,default='default_cover.png')
	joined = models.DateField(null=True)
	lives = models.CharField(max_length=150,null=True)
	email = models.EmailField(max_length=300,null=True)
	website = models.URLField(max_length=100,null=True)

	profile_pic = models.ImageField(upload_to=image_dir,default='default_profile.png')
	cover_pic = models.ImageField(upload_to=image_dir,default='default_cover.png')


	def __str__(self):
		return self.firstname

class Friend(models.Model):
	from_user = models.ForeignKey(Profile,on_delete= models.CASCADE,related_name='from_user')
	to_user = models.ForeignKey(Profile,on_delete= models.CASCADE,related_name='to_user')

	class Meta:
		unique_together = ('from_user', 'to_user')

		