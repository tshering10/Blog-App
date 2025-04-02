from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Like
from posts.forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
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
    comments = post.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Comment added successfully!")
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    context = {
        'form': form,
        'post': post,
        'comments': comments
    }
    return render(request, 'posts/details.html', context)

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

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk) #fetching data to update
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post updated successfully!!")
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts/edit.html", {'form': form})
    
def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, "Your post deleted!!") 
    return redirect("user_post_view") #redirect to my post section after delete

@login_required
def like_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if not Like.objects.filter(post=post, author=request.user).exists():
        Like.objects.create(post=post, author=request.user)
    return redirect('post_detail', pk=post.pk)