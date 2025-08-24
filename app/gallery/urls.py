from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Album URLs
    path('', views.AlbumListView.as_view(), name='album_list'),
    path('album/new/', views.AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('album/<int:pk>/edit/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
    
    # Photo URLs
    path('photos/', views.PhotoListView.as_view(), name='photo_list'),
    path('photo/new/', views.PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/<int:pk>/edit/', views.PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),
]
