from django.urls import path
from posts.views import home
urlpatterns = [
    path('', home, name='home'),
]
