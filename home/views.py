from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from Blog.models import Blogpost

# Create your views here.

def home(request):
    return render(request, 'home/home.html')# we written home/home.html because all html files inside the another floder in the templates that  is home so.

def contact(request): 
   
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4 :
            messages.error (request,'Please Fill the form correctly')
        else:
            contact =Contact(Name=name,Emails=email,Phone=phone,content=content)# send the post data into the database of the model
            contact.save()
            messages.success (request,'Welcome to contact us Page')
        #print(name,email,phone,content)
    return render(request,'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    qurey=request.GET.get('query', '')
    allpost=Blogpost.objects.filter(Title__icontains=qurey)# this will fetch all the data from the database
    context={'allpost':allpost}
    return render(request,'home/search.html',context)



