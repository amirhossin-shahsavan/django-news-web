from django.contrib import admin
from .models import Category,Post,Author,Comment

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display=("title","category","created_at","updated_at")
    
admin.site.register(Post,AdminNews)
admin.site.register(Author)

class AdminComment(admin.ModelAdmin):
    list_display=("post","user","content","status","created_at","updated_at")
    
admin.site.register(Comment,AdminComment) 