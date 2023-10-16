from .models import Album
from rest_framework import serializers


## Class CarsSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'date', 'country', 'city', 'hotel', 'memory')