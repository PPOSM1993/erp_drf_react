from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', SigninView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('user/', GetUserView.as_view(), name='user'),
]   
