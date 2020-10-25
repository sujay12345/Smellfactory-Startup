from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import User, Post, addcomment


def index(request):
    return render(request, "smellfactory/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "smellfactory/login.html", {
                "message": "Invalid username and/or password."
            })

    else:
        return render(request, "smellfactory/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "smellfactory/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "smellfactory/register.html", {
                "message": "Username already taken."
            })
        except ValueError:
            return render(request, "smellfactory/register.html", {
        "message": "Bad Credentials. Please enter valid data and try again.",
        "msg_type": "danger" 
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))


    else:
        return render(request, "smellfactory/register.html")
        



@login_required(login_url='login')
def forum(request):


    allpost = Post.objects.order_by("-timestamp").all()
    paginator = Paginator(allpost, 10)
    page = request.GET.get('page')

    return render(request, "smellfactory/forum.html", {
       
        "allposts": paginator.get_page(page)
    })

@login_required(login_url='login')
def newpost(request): # only accepts post request
    allpost = Post.objects.order_by("-timestamp").all()
    paginator = Paginator(allpost, 10)
    page = request.GET.get('page')
    post = Post(content=request.POST["content"], postcreator=User.objects.get(pk=request.user.pk))
    post.save()
    return render(request, "smellfactory/forum.html", {
    "allposts": paginator.get_page(page)
    })

def like(request, postid):
    post = Post.objects.get(pk=postid)
    comments = addcomment.objects.filter(forumid=postid)
    liked = User.objects.get(pk=request.user.pk).upvoted_posts
    allpost = Post.objects.order_by("-timestamp").all()
    paginator = Paginator(allpost, 10)
    page = request.GET.get('page')
    if post not in liked.all():
        liked.add(post)
    else:
        liked.remove(post)

    return render(request, "smellfactory/forum.html", {
        "allposts": paginator.get_page(page),
        "comments": comments
        })
@login_required(login_url='/login')
def viewposting(request, product_id):
    comments = addcomment.objects.filter(forumid=product_id)
    product = Post.objects.get(id=product_id)
    return render(request, "smellfactory/viewpost.html", {
            "post": product,
            "comments": comments

    })

@login_required(login_url='/login')
def comment(request, product_id):
    cmt = addcomment()
    cmt.commentcontent = request.POST.get("comment")
    comments = addcomment.objects.filter(forumid=product_id)
    product = Post.objects.get(id=product_id)
    allpost = Post.objects.order_by("-timestamp").all()
    paginator = Paginator(allpost, 10)
    page = request.GET.get('page')
    cmt.user = request.user.username
    cmt.forumid = product_id
    cmt.save()
    return render(request, "smellfactory/viewpost.html", {
        "comments": comments,
        "post": product

    })



def currentnews(request):
    return render(request, "smellfactory/currentnews.html")


def faq(request):
    return render(request, "smellfactory/faq.html")
