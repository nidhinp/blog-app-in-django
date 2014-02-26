from django.shortcuts import render
from forms import LoginForm, NewblogpostsForm, CommentForm
from django.http import HttpResponse
from models import Newblogposts, Comments
from time import *


USERNAME = 'admin'
PASSWORD = 'password'

def home(request):
    return render(request, 'home.html')
    
def newposts(request):
    if request.method == 'POST':
        form = NewblogpostsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            p = Newblogposts(title=cd['title'], body=cd['body'], day=strftime("%d %b %Y ", gmtime()),
                time=strftime("%H:%M:%S ", gmtime()))
            p.save()
            posts = Newblogposts.objects.order_by("-id")
            comments = Comments.objects.order_by("-id")
            comment_form = CommentForm()
            return render(request, 'posts.html', {'posts': posts, 'comments': comments, 'comment_form': comment_form})
    else:
        form = NewblogpostsForm()
    return render(request, 'newposts.html', {'form': form})
    
def posts(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            p = Comments(name=cd['name'], comment=cd['comment'], title=request.POST['post_title'])
            p.save()
            posts = Newblogposts.objects.order_by("-id")
            comments = Comments.objects.order_by("-id")
            comment_form = CommentForm()
            return render( request, 'posts.html', {'posts': posts, 'comments': comments, 'comment_form': comment_form})
        else:
            posts = Newblogposts.objects.order_by("-id")
            comments = Comments.objects.order_by("-id")
            comment_form = CommentForm()
            return render( request, 'posts.html', {'posts': posts, 'comments': comments, 'comment_form': comment_form})
    else:
        posts = Newblogposts.objects.order_by("-id")
        comments = Comments.objects.order_by("-id")
        comment_form = CommentForm()
        return render( request, 'posts.html', {'posts': posts, 'comments': comments, 'comment_form': comment_form})
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['username'] == USERNAME and cd['password'] == PASSWORD:
                form = NewblogpostsForm()
                return render(request, 'newposts.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})    
