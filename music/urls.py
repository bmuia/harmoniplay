from django.urls import path
from .views import (
    GenreCreateView, GenreListView,
    SongCreateView, SongListView,
    AlbumCreateView, AlbumListView, AlbumDetailView,
    PlaylistCreateView, PlaylistListView,
    LikeCreateView,
    CommentCreateView, CommentListView,
    FavoriteCreateView,
    RecentlyPlayedListView,
    SongDetailView
)

urlpatterns = [
    # Genre
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('genres/create/', GenreCreateView.as_view(), name='genre-create'),

    # Song
    path('songs/', SongListView.as_view(), name='song-list'),
    path('songs/create/', SongCreateView.as_view(), name='song-create'),
    path('songs/<int:id>/', SongDetailView.as_view(), name='song-detail'),


    # Album
    path('albums/', AlbumListView.as_view(), name='album-list'),
    path('albums/create/', AlbumCreateView.as_view(), name='album-create'),
    path('albums/<int:id>/', AlbumDetailView.as_view(), name='album-detail'),

    # Playlist
    path('playlists/', PlaylistListView.as_view(), name='playlist-list'),
    path('playlists/create/', PlaylistCreateView.as_view(), name='playlist-create'),

    # Likes
    path('likes/create/', LikeCreateView.as_view(), name='like-create'),

    # Comments
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:song_id>/', CommentListView.as_view(), name='comment-list'),

    # Favorites
    path('favorites/create/', FavoriteCreateView.as_view(), name='favorite-create'),

    # Recently Played
    path('recently-played/', RecentlyPlayedListView.as_view(), name='recently-played'),
]
