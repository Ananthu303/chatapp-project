from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.

def register(request):
   form=UserCreationForm()
   if request.method=='POST':
      form=UserCreationForm(request.POST)
      if form.is_valid():
        user=form.save(commit=False)
        user.username=user.username.lower()
        user.save()
        profile_obj=ProfileModel.objects.create(name=user)
        profile_obj.save()
        login(request,user)
        return redirect('home')
      else:
       messages.error(request,'An error occured during registration')
      
   return render(request,'register.html',{'form':form})




def loginPage(request):
   
   if request.method=='POST':
      
      username=request.POST.get('username')
      password=request.POST.get('password')

      try:
         user=User.objects.get(username=username)
      except:
         messages.error(request,'User not found')

        
      user=authenticate(request,username=username,password=password)

      if user is not None:
         login(request,user)
         return redirect('home')
    

   return render(request,'login.html')




def logoutuser(request):
   logout(request)
   return redirect('home')


   

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''

    room=Room.objects.filter(
       Q(topic__name__icontains=q) |
        Q(host__username__icontains=q) |
            Q(sub_topic__icontains=q)

    )
    room_count=room.count()
    a=room_count
    topic=Topic.objects.all()[0:6]
    
    room_messages=Message.objects.filter(Q(room__topic__name__icontains=q)|Q(user__username__icontains=q)).order_by('-created')[0:a]
    return render(request,'index.html',{'room':room,'topic':topic,'room_count':room_count,'room_messages':room_messages})





def room(request,id):

    room=Room.objects.get(id=id)
    room_messages=room.message_set.all()
    participants=room.participants.all()
    if request.method=='POST':
        message=Message.objects.create(
           user=request.user,
           room=room,
           body=request.POST.get('body'))
        room.participants.add(request.user)
        
        return redirect('room',id=room.id)

    return render(request,'roomnew.html',{'room':room,'message':room_messages,'participants':participants})



@login_required(login_url='index')
def userprofile(request,id):

   user=User.objects.get(id=id)
   Topicc=Topic.objects.all()[0:6]
   rooms=user.room_set.all() #can get all the rooms created by the user
   msg=user.message_set.all()
   

   return render(request,'profile-new.html',{'user':user,'rooms':rooms,'messages':msg,'Topic':Topicc})




@login_required(login_url='login')
def createroom(request):
    form=RoomForm()
    topics=Topic.objects.all()
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
           host=request.user,
           topic=topic,
           sub_topic=request.POST.get('sub_topic').title()
        )
        return redirect('home')
    
    return render(request,'create-room.html',{'form':form,'topics':topics})




@login_required(login_url='login')
def updateroom(request,id):
   room=Room.objects.get(id=id)
   form=RoomForm(instance=room)
   topics=Topic.objects.all()

   if request.method=='POST':
      form=RoomForm(request.POST,instance=room)
      topic_name=request.POST.get('topic')
      topic,created=Topic.objects.get_or_create(name=topic_name)
      #CHANging values
      room.topic=topic
      room.sub_topic=request.POST.get('sub_topic')
      room.save()
      
      return redirect('home')
   return render(request,'create-room.html',{'form':form,'topics':topics,'room':room,})

@login_required(login_url='login')
def deleteroom(request,id):
   room=Room.objects.get(id=id)

   if request.method=='POST':
      room.delete()
      return redirect('home')
   
   return render(request,'delete.html',{'sub':room})


@login_required(login_url='login')
def deletemessage(request,id):
   message=Message.objects.get(id=id)
   message.delete()
   return redirect(request.META.get('HTTP_REFERER'))




   
@login_required(login_url='login')
def updateuser(request,id):
   user_obj=User.objects.get(id=id)
   profile=user_obj.profilemodel
   
   
   form=UserForm(instance=profile)
   if request.method=='POST':
    form=UserForm(request.POST,request.FILES,instance=profile)
    if form.is_valid():
      obj=form.save(commit=False)
      # user=request.POST.get('username')
      # a=User.objects.get(username=user_obj)
      # a.username=user
      # a.save()
      a=obj.name
      a.username=request.POST.get('username')
      a.save()
      obj.save()
      return redirect('user-profile',id=request.user.id)
      
    
   return render(request,'update-user.html',{'form':form})




   
def topicspage(request):
   q=request.GET.get('q') if request.GET.get('q') != None else ''
   topics=Topic.objects.filter(name__icontains=q)
   return render(request,'topics.html',{'topics':topics})



   
   
def activitypage(request):
   room_messages=Message.objects.all()
   return render(request,'activity.html',{'room_messages':room_messages})