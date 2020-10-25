from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newpost", views.newpost, name="newpost"),
    path("like/<int:postid>", views.like, name="like"),
    path("addcomment/<int:product_id>", views.comment, name="addcomment"),
    path("forum", views.forum, name="forum"),
    path("viewlisting/<int:product_id>", views.viewposting, name="viewpost"),
    path("smelltraining", views.currentnews, name="news"),
    path("senseofsmellfaq", views.faq, name="faq")

   

]
