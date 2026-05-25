from django.urls import path
from .views import *

urlpatterns = [
    path("", AlbumListView.as_view(), name="album-list"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album-detail"),
    path("album/new/", AlbumCreateView.as_view(), name="album-create"),
    path("album/<int:pk>/edit/", AlbumUpdateView.as_view(), name="album-update"),
    path("album/<int:pk>/delete/", AlbumDeleteView.as_view(), name="album-delete"),
    path("photo/new/", PhotoCreateView.as_view(), name="photo-create"),
]