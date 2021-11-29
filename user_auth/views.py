from django.db import connections
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,Group
from .models import *
from .decorators import *
from datetime import date
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.conf import settings
from posts_and_like import models as plmodels
import os
from posts_and_like import forms as plforms
from django.http import JsonResponse
import json

from PIL import Image
import base64


# Create your views here.
@unauthenticated_user
def loginPage(request):
	context={}

	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)

		if user:
			login(request,user)
			return redirect('homePage')
		else:
			messages.info(request,'Username or Password is incorrect')
			return redirect('loginPage')	


	return render(request,'loginPage.html',context)

@unauthenticated_user
def registerPage(request):
	context={}

	flag=1

	if request.method=="POST":
		firstname=request.POST['firstname']
		lastname=request.POST['lastname']
		dob=request.POST['dob']
		lives=request.POST['lives']
		email=request.POST['email']
		website=request.POST['website']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']

		flag=verify_data(request,firstname,lastname,dob,username,password1,password2)

		if flag:
			dob=datetime.strptime(dob,'%Y/%m/%d')
			user=User.objects.create(username=username,password=password1)
			user.set_password(password1)
			user.save()
			Profile.objects.create(user=user,firstname=firstname,lastname=lastname,dob=dob,lives=lives,email=email,website=website,joined=date.today())
			return redirect('loginPage')
		else:
			return redirect('registerPage')		
			

	return render(request,'registerPage.html',context)	


@login_required(login_url='loginPage')
def homePage(request):

	try:
		profile=Profile.objects.get(user=request.user)
	except:
		print("Data:",request.user.socialaccount_set.first().extra_data)
		data=request.user.socialaccount_set.first().extra_data
		print("Date:",date.today())
		profile=Profile.objects.create(user=request.user,firstname=data['given_name'],lastname=data['family_name'],email=data['email'],joined=date.today())	
		posts = plmodels.Post.objects.all().order_by("-timeday")
		likes = plmodels.Like.objects.all()
	context={'profile':profile}

	return render(request,'homePage.html',context)



@login_required(login_url='loginPage')
def profilePage(request,pk):
	profile=Profile.objects.get(user=User.objects.get(username=pk))

	posts = plmodels.Post.objects.all().order_by("-timeday")
	likes = plmodels.Like.objects.all()

	by_user_profile = Profile.objects.get(user=User.objects.get(username=request.user))
	friends = Friend.objects.filter(from_user = by_user_profile).all()
	num_friends = Friend.objects.filter(from_user = by_user_profile).count()

	context={'profile':profile,'posts':posts,'form':plforms.MakePost,'like':likes,'num_friends':num_friends}
	
	print(profile.profile_pic.url)

	if request.method=="POST":
		if 'inputGroupFile01' in request.FILES:
			cover_pic=request.FILES['inputGroupFile01']
			print(type(profile.profile_pic.url),profile.profile_pic.url)
			if 'default_cover.png' not in profile.cover_pic.url:
				os.remove(settings.BASE_DIR / profile.cover_pic.url[1:])
			profile.cover_pic=cover_pic

		if 'inputGroupFile02' in request.FILES:
			profile_pic=request.FILES['inputGroupFile02']
			if 'default_profile.png' not in profile.profile_pic.url:
				os.remove(settings.BASE_DIR / profile.profile_pic.url[1:])
			profile.profile_pic=profile_pic

		profile.save()		

		return redirect('profilePage',pk=request.user.username)

	return render(request,'profilePage.html',context)	


def between(n,l,h):
	return 1 if n>=l and n<=h else 0	

def verify_data(request,firstname,lastname,dob,username,password1,password2):
	flag=1

	all_names=[user.username for user in User.objects.all()]
	if username in all_names:
		messages.info(request,'Username already exists')
		flag=0

	data=dob.split('/')
	if len(data)!=3:
		messages.info(request,'Please follow the specified DOB format')
		flag=0
	elif len(data[0])!=4 or len(data[1])!=2 or len(data[2])!=2:
		messages.info(request,'DOB seems unusual')
	else:
		f=1
		for d in data:
			try:
				d=int(d)
			except:
				messages.info(request,'DOB should have only numbers')
				f=0
				break
		if f:
			if not (between(int(data[0]),1920,2020) and between(int(data[1]),1,12) and between(int(data[2]),1,31)):
				messages.info(request,'DOB seems unusual')
				flag=0
			else:
				try:
					date=datetime(year=int(data[0]),month=int(data[1]),day=int(data[2]))
				except:
					messages.info(request,'Date does not exist')
					flag=0

	if password1!=password2:
		messages.info(request,'Passwords don\'t match')
		flag=0

	return flag		

def updateProfileImage(request):
	data=json.loads(request.body)
	print(base64.decodestring(data['img_path']))
	img=Image.open(data['img_path'])
	print(img)


	return JsonResponse('Data accessible',safe=False)


"""
#name=fs.save(cover_pic.name,cover_pic)
#path=profile.cover_pic_path
#os.remove(settings.BASE_DIR / f"media\\{path}")
"""	
def makepost(request):
	
	print("\n\n\n\n\n\n\n")
	print(request.POST)
	info = request.POST["postinfo"]

	postobj = plmodels.Post.objects.create(
		postinfo = info,
		profile = Profile.objects.get(user=User.objects.get(username=request.user))

	)
	postobj.save()
	return redirect(profilePage,request.user)

def makecomment(request,pk):
	posts = plmodels.Post.objects.get(id=pk)
	comments = plmodels.Comment.objects.filter(on_post = posts).all()
	print(comments)
	context = {"post":posts,'comments':comments,'form':plforms.MakeComment}
	return render(request,'postdetail.html',context)

def make_a_comment(request,pk):
	post = plmodels.Post.objects.get(id=pk)
	print(request.POST,pk)

	info = request.POST["description"]

	comment_obj = plmodels.Comment.objects.create(
		on_post = post,
		description = info,
		by_user = Profile.objects.get(user=User.objects.get(username=request.user))

	)
	comment_obj.save()
	# postobj.save()
	return redirect(profilePage,request.user)

def likeclicked(request):
	print(request.POST)
	return JsonResponse("True",safe=False)

def make_a_friend(request,pk):
	print(request,pk)
	print('')
	print('')
	print('')
	print('in')
	by_user = Profile.objects.get(id = pk)
	to_user = Profile.objects.get(user=User.objects.get(username=request.user))
	print(by_user,to_user)

	friend_obj = Friend.objects.create(
		to_user = by_user,
		from_user = to_user
	)
	friend_obj.save()
	return redirect(profilePage,request.user)


def friend_list(request,pk):
	print(pk)
	profile=Profile.objects.get(id=pk)
	posts = plmodels.Post.objects.all().order_by("-timeday")
	likes = plmodels.Like.objects.all()
	
	by_user_profile = Profile.objects.get(user=User.objects.get(username=request.user))
	friends = Friend.objects.filter(from_user = by_user_profile).all()
	num_friends = Friend.objects.filter(from_user = by_user_profile).count()

	context={'profile':profile,'posts':posts,'form':plforms.MakePost,'like':likes,'friends':friends,'num_friends':num_friends}

	print(profile.profile_pic.url)
	# return redirect(friend_list,request.user)
	return render(request,'friendsList.html',context)



				



