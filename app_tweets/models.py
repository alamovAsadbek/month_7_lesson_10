from django.db import models


class TweetModel(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tweet = models.CharField(max_length=140)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tweet

    class Meta:
        verbose_name_plural = 'Tweets'
        verbose_name = 'Tweet'
