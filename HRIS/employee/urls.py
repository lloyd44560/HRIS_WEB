from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView
from .views import pagelogout

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', pagelogout, name='logout'),

    ]
