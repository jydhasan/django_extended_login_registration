from django.urls import path
from . import views
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
# home page
    path('',views.home, name='home'),
    # path('login/', views.sign_in, name='login'),
    # path('logout/', views.sign_out, name='logout'),
    # path('register/', views.sign_up, name='register'),
        # path('register/', register, name='register'),
            # other URL patterns
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

]