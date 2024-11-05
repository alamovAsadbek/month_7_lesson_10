from rest_framework import generics

from .models import TweetModel
from .serializers import TweetSerializer


class TweetView(generics.GenericAPIView):
    serializer_class = TweetSerializer
    queryset = TweetModel.objects.all()
