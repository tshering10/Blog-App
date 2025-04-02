from django.urls import path
from posts.views import home, post_detail, create_post ,dashboard, user_post_view
urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('create/', create_post, name="new_post"),
    path('dashboard/', dashboard, name='dashboard'),
    path('userposts/', user_post_view, name="user_post_view"),
]
