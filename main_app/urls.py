from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bangers/', views.bangers_index, name='index'),
    path('bangers/<int:banger_id>/', views.bangers_detail, name='detail'),
    path('bangers/create/', views.BangerCreate.as_view(), name='bangers_create'),
    path('bangers/<int:pk>/update/', views.BangerUpdate.as_view(), name='bangers_update'),
    path('bangers/<int:pk>/delete/', views.BangerDelete.as_view(), name='bangers_delete'),
    path('bangers/<int:banger_id>/add_listen/', views.add_listen, name='add_listen'),
    path('bangers/<int:banger_id>/assoc_playlist/<int:playlist_id>/', views.assoc_playlist, name="assoc_playlist"),
    path('playlists/', views.PlaylistList.as_view(), name='playlists_index'),
    path('playlists/<int:pk>/', views.PlaylistDetail.as_view(), name='playlists_detail'),
    path('playlists/create/', views.PlaylistCreate.as_view(), name='playlists_create'),
    path('playlists/<int:pk>/update/', views.PlaylistUpdate.as_view(), name='playlists_update'),
    path('playlists/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlists_delete'),
]