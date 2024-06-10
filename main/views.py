from django.shortcuts import render
from .models import  Post, Category,Comment

def home(request):
    all_news=Post.objects.all()
    return render(request,'all-news.html',{
        'all_news':all_news
    })