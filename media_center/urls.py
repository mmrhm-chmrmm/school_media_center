from django.urls import path
from . import views

app_name = 'media_center'

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),

    path('gallery/', views.gallery_folders, name='gallery_folders'),
    path('gallery/folder/create/', views.folder_create, name='folder_create'),
    path('gallery/photo/upload/', views.photo_upload, name='photo_upload'),
    path('gallery/<int:folder_id>/', views.gallery_photos, name='gallery_photos'),

    path('videos/', views.video_list, name='video_levels'),
    path('videos/add/', views.video_create, name='video_create'),
    path('videos/<int:pk>/delete/', views.video_delete, name='video_delete'),
]
