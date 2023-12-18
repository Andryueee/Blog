from django.urls import path
from .views import profile, create_post, create_comment, register, login_view

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('create_post/', create_post, name='create_post'),
    path('create_comment/<int:post_id>/', create_comment, name='create_comment'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]