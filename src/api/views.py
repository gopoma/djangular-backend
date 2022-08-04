from rest_framework import viewsets
from .serializer import MovieSerializer
from .models import Movie

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
