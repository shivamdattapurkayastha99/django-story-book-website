from unicodedata import category
from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def story_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    story=Story.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        story=Story,filter(category=category)
    return render(request,'story/story_list.html',{'categories':categories,'story':story,'category':category})