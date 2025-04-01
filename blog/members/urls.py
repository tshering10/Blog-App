from django.urls import path
from members.views import SignupView, UserloginView, UserlogoutView

urlpatterns = [
    path('register/', SignupView.as_view(), name='signup'),
    path('login/', UserloginView.as_view(), name='login'),
    path('logout/', UserlogoutView.as_view(), name='logout'),
]
