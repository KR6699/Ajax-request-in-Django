from django.shortcuts import render
from .models import Post , Likes
from django.http import HttpResponse
# Create your views here.
def index(request):
    posts = Post.objects.all()
    pass
    return render(request , 'index.html' , {'posts' : posts})

def postlikes(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id) #getting the liked posts
        m = Likes(post=likedpost) # Creating Like Object
        m.save()  # saving it to store in database
        return HttpResponse("Success!") # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")