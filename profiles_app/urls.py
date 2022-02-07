from django.urls import path
from profiles_app.views import *
# from allauth.account.views import


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('restore_password/', RestorePasswordView.as_view(), name='restore_password'),
]