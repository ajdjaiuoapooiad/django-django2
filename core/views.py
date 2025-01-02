
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from core.forms import LoginForm, PostForm, RegisterForm
from core.models import Post
from django.contrib.auth import login

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

def update(request,pk):
    post=Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=PostForm(instance=post)
        
    context={
        'form': form,
    }
    return render(request,'core/create.html',context)

def delete(request,pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect('index')

# def delete(request,pk):
#     post=Post.objects.get(pk=pk)
#     post.like += request.user
#     return redirect('index')[]

class register(CreateView):
    form_class = RegisterForm
    template_name='core/register.html'
    success_url=reverse_lazy('index')
    

class login(LoginView):
    form_class = LoginForm
    template_name='core/login.html'
    
class logout(LogoutView):
    success_url=reverse_lazy('index')
