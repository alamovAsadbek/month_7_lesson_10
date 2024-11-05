from rest_framework import generics
from rest_framework.response import Response

from .models import TweetModel
from .serializers import TweetSerializer


class TweetView(generics.GenericAPIView):
    serializer_class = TweetSerializer
    queryset = TweetModel.objects.all()

    def get(self, request):
        tweets = self.get_queryset()
        serializer = self.get_serializer(tweets, many=True)
        return Response(serializer.data)
