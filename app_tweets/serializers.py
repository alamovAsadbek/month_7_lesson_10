from rest_framework import serializers

from .models import *


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = '__all__'
