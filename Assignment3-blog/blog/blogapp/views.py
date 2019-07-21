from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .models import Setting
from .forms import SettingForm

# Create your views here.

def home(request):
    blogs = Blog.objects
    settings = Setting.objects
    
    cnt=0
    for a in settings.all():
        title=a.title
        color=a.color
        image=a.image
        cnt+=1

    if cnt==0:
        st = Setting()
        st.title="SUBIN BLOG"
        st.color="#ac4e4e"
        st.image="images/homeboard.jpg"
        st.save()

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
        form = SettingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SettingForm(initial={'title': title, 'color':color})
        return render(request, 'settings.html', {'title':title, 'color':color, 'form':form})