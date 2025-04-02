from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from posts.forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-pk')
    paginator = Paginator(posts, 2) #shows 2 posts per page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(1)
        
    return render(request, 'posts/home.html', {'posts': posts, 'page_obj': page_obj})

def dashboard(request):
    posts = Post.objects.all().order_by('-pk') 
     
    context = {
        'posts': posts,        
    }
    return render(request, 'posts/dashboard.html', context)

def user_post_view(request):
    userPosts = Post.objects.filter(author = request.user).order_by('-pk')
    return render(request, 'posts/user-dashboard.html',{'userPosts': userPosts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/details.html', {'post': post})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # It automatically sets the logged in user as author
            post.save()
            messages.success(request, "New post created succesfully!!")
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})
        