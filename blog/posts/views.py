from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from posts.forms import PostForm
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-pk')
    return render(request, 'posts/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/details.html', {'post': post})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})
        