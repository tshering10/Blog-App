from django.urls import path
from posts.views import home, post_detail, create_post ,dashboard, user_post_view, update_post, delete_post_view, like_view, change_password_view
urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('create/', create_post, name="new_post"),
    path('dashboard/', dashboard, name='dashboard'),
    path('userposts/', user_post_view, name="user_post_view"),
    path('edit/<int:pk>/', update_post, name='edit_post'),
    path('delete/<int:pk>/', delete_post_view, name='delete_post'),
    path('post/<int:pk>/like/', like_view, name="like_post"),
    
    path('change-password/', change_password_view, name="change_password"),
]