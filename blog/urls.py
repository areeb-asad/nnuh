from django.urls import path
from django.urls import include
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addpost/', views.addpost, name='addpost'),
    path('allposts/', views.allpost, name='allposts'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/addcomment/', views.addcomment, name='addcomment'),
    path('count/', views.count, name='count'),
]