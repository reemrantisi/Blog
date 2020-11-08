from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('<slug:title>/', views.post_detail, name='post_detail'),
    path('<str:username>', views.home, name='user_posts'),

] 
