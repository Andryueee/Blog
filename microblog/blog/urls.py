from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import profile, create_post, create_comment, register, login_view, delete_profile, edit_profile, HomePageView, add_comment


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('create_post/', create_post, name='create_post'),
    path('create_comment/<int:post_id>/', create_comment, name='create_comment'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', HomePageView.as_view(), name='home'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
]