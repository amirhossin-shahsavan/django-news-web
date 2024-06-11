from django.shortcuts import render
from .models import  Post, Category,Comment, Author

def home(request):
    news=Post.objects.all()
    comments = Comment.objects.all()
    return render(request,'post.html',{'news':news, 'comments': comments})