from django.shortcuts import render,HttpResponse
from .models import Blogpost 

# Create your views here.
# def home(index):
#     return HttpResponse("Hello guys find your Perfect Match")

def bloghome(request):
    allpost=Blogpost.objects.all()# this will fetch all the data from the database
    context={'allpost':allpost}
    return render(request,'blog/bloghome.html' ,context)
 
def blogpost(request,slug):
    post=Blogpost.objects.filter(Slug=slug).first()# this will fetch all the data from the database
    context={'post':post}
    return render(request,'blog/blogpost.html',context) #the blogpost  is inside the blog floder do blog/blogpost.html

