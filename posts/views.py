from django.db.models.fields import TextField
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'my_project/home.html'
    context_object_name = 'all_posts_list'

class AboutPageView(ListView):
    model = Post
    template_name = 'my_project/about.html'