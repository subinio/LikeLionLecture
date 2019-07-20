from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .models import Setting

# Create your views here.

def home(request):
    blogs = Blog.objects
    settings = Setting.objects
    
    for a in settings.all():
        title=a.title
        color=a.color
        image=a.image
    
    return render(request, 'home.html', {'blogs':blogs, 'settings':settings, 'title':title, 'color':color, 'image':image} )

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)

    settings = Setting.objects
   
    for a in settings.all():
        color=a.color

    return render(request, 'detail.html', {'details':details, 'color':color})

def new(request):
    settings = Setting.objects

    for a in settings.all():
        color=a.color

    return render(request, 'new.html', {'color':color})

def create(request):
  
    settings = Setting.objects
   
    for a in settings.all():
        color=a.color

    if request.method == 'POST':
        blog = Blog()
        blog.title = request.POST.get('title', '')
        blog.body = request.POST.get('body', '')
        blog.pub_date = timezone.datetime.now() 
        blog.save()
        return redirect('/blog/' + str(blog.id))
    
  
def postview(request):
    blogs = Blog.objects
    
    settings = Setting.objects
   
    for a in settings.all():
        color=a.color

    return render(request, 'postview.html', {'blogs':blogs, 'color':color})

def settings(request):
    settings = Setting.objects
   
    for a in settings.all():
        title=a.title
        color=a.color

    if request.method == 'POST':
        setting = Setting()
        setting.title = request.POST.get('title', '')
        setting.color = request.POST.get('color', '')
        setting.image = 'images/'+ request.POST.get('image', '')
        setting.save()
        return redirect('home')
    else:
        return render(request, 'settings.html', {'title':title, 'color':color})