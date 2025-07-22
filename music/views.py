from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import (
    Genre, Song, Album, Playlist, Like, Comment, Favorite, RecentlyPlayed, Artist
)
from .serializers import (
    ArtistSerializer,
    GenreSerializer,
    SongSerializer,
    AlbumSerializer,
    PlaylistSerializer,
    LikeSerializer,
    CommentSerializer,
    FavoriteSerializer,
    RecentlyPlayedSerializer,
)

# Artist Views
class ArtistCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Genre.objects.all()
    serializer_class = ArtistSerializer

class ArtistListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
# Genre Views
class GenreCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Song Views
class SongCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            song = serializer.save()
            return Response(SongSerializer(song).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            song = Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response({"error": "Song not found."}, status=status.HTTP_404_NOT_FOUND)

        # Save this play to RecentlyPlayed
        RecentlyPlayed.objects.create(
            user=request.user,
            song=song
        )

        # Serialize and return the song
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Album Views
class AlbumCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'id'


# Playlist Views
class PlaylistCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaylistSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlaylistListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user).order_by('-created_at')


# Like Views
class LikeCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Comment Views
class CommentCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        song_id = self.kwargs.get('song_id')
        return Comment.objects.filter(song__id=song_id)


# Favorite Views
class FavoriteCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Recently Played Views
class RecentlyPlayedListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RecentlyPlayedSerializer

    def get_queryset(self):
        return RecentlyPlayed.objects.filter(user=self.request.user).order_by('-played_at')[:20]
