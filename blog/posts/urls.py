from django.urls import path
from posts.views import home, post_detail
urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]
