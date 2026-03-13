from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/blog template.html', context={"posts": posts})


def post(request, pk):
    # This finds the post or returns a 404 error if it doesn't exist
    posts = Post.objects.get(id=pk)
    return render(request, 'posts/post.html', {'posts': posts})
