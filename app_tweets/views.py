from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
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

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)

    def delete(self, request, pk):
        tweet = TweetModel.objects.get(id=pk)
        tweet.delete()
        return Response({'message': 'Tweet deleted successfully!'})

    def put(self, request, pk):
        tweet = TweetModel.objects.get(id=pk)
        serializer = self.get_serializer(instance=tweet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        tweet = TweetModel.objects.get(id=pk)
        serializer = self.get_serializer(instance=tweet, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AllTweetView(generics.ListAPIView):
    serializer_class = TweetSerializer
    pagination_class = TweetPaginationView
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TweetModel.objects.exclude(user=self.request.user)

    def get(self, request):
        tweets = self.get_queryset()
        serializer = self.get_serializer(tweets, many=True)
        return Response(serializer.data)
