from django.urls import path
from django.urls import include
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addpost/', views.addpost, name='addpost'),
    path('logout_view/', views.logout_view, name='logout_view'),
]