from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('blog/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]