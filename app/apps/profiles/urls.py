from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import RegistrationView, UserView

app_name = 'profiles'

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='registration'),
    path('profile/', login_required(UserView.as_view()), name='profile'),
    path('login/',
         LoginView.as_view(template_name='profiles/login.html'),
         name='login'
         ),
    path('logout/',
         LogoutView.as_view(template_name='profiles/logout.html'),
         name='logout'
         ),

]
