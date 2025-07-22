from rest_framework import serializers
from .models import (
    Artist, Genre, Song, Album, Playlist,
    Like, Comment, Favorite, RecentlyPlayed
)

class ArtistSerializer(serializers.ModelSerializer):
 
   class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            'id', 'title', 'description', 'audio', 'cover_image',
            'duration', 'release_date', 'artist', 'genres',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id', 'title', 'description', 'cover_image', 'release_date',
            'artist', 'songs', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class PlaylistSerializer(serializers.ModelSerializer):  # Fixed spelling
    class Meta:
        model = Playlist
        fields = ['id', 'title', 'description', 'user', 'songs', 'created_at']
        read_only_fields = ['id', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'song', 'liked_at'] 
        read_only_fields = ['id', 'liked_at']


class CommentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Comment
        fields = ['id', 'user', 'song', 'text', 'commented_at']
        read_only_fields = ['id', 'commented_at']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'song', 'favorited_at']
        read_only_fields = ['id', 'favorited_at']


class RecentlyPlayedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentlyPlayed
        fields = ['id', 'user', 'song', 'played_at']
        read_only_fields = ['id', 'played_at']
