from django.urls import path
from members.views import signup_view, user_login_view, user_logout_view

urlpatterns = [
    path('register/', signup_view, name='signup'),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
]
