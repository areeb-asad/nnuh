from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponse
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Post, Comments

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-post_date')[:5]

@login_required(login_url='/accounts/login/?next=/blog/addpost/')
def addpost(request):
    if request.method == 'POST':
        if request.POST.get('post-title'):
            if request.POST.get('post-content'):
                sss= Post(title=request.POST.get('post-title'),content=request.POST.get('post-content'),pub_user=request.user.username,post_date=datetime.datetime.now())
                sss.save()
                return HttpResponseRedirect(reverse('blog:index'))
            
    else:
            return render(request, 'blog/addpost.html')




def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})

