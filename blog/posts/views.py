from django.shortcuts import render, get_object_or_404
from posts.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-pk')
    return render(request, 'posts/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/details.html', {'post': post})