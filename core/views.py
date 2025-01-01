
from django.shortcuts import redirect, render

from core.forms import PostForm
from core.models import Post

def index(request):
    posts = Post.objects.all()
    
    context={
        'posts': posts,
    }
    return render(request,'core/index.html',context)

def detail(request,pk):
    post = Post.objects.get(pk=pk)
    
    context={
        'p': post,
    }
    return render(request,'core/detail.html',context)

def create(request):
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form=PostForm()
        
    context={
        'form': form,
    }
    return render(request,'core/create.html',context)