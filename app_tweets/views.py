from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import TweetModel
from .serializers import TweetSerializer


class TweetPaginationView(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class TweetView(generics.GenericAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        return TweetModel.objects.filter(user=self.request.user)

    def get(self, request):
        tweets = self.get_queryset()
        serializer = self.get_serializer(tweets, many=True)
        return Response(serializer.data)
