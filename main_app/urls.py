from django.contrib.auth.views import LoginView, LogoutView
from .views import main_app, shop, register, search
from django.urls import path

urlpatterns = (
    path('', main_app, name='main'),
    path('men/', shop, name='men'),
    path('women/', shop, name='women'),
    path('kids/', shop, name='kids'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('search/', search, name='search')

)
