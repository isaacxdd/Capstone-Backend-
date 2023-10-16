from .models import Album
from rest_framework import viewsets, permissions
from .serializers import AlbumSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    ## queryset is a list of all Todo objects
    queryset = Album.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing and deserializing queryset and model instances.
    serializer_class = AlbumSerializer
    # Set permission_classes to allow unrestricted access to the API.
    permission_classes = [permissions.AllowAny]