
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='F:/projects/nnuh/blog/templates/blog/login.html'), name='login'),
]
