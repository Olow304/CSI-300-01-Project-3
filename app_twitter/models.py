from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class User(models.Model):
    user_id = models.IntegerField()
    fn = models.CharField(max_length=25)
    ln = models.CharField(max_length=25)
    twitter_handle = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

class Tweets(models.Model):
    id_user = models.IntegerField()
    content = models.CharField(max_length=280)

class Follows(models.Model):
    id_user = models.IntegerField()
    following_id = models.IntegerField()
    user_fllw = models.ForeignKey(User, on_delete=models.CASCADE)

class Retweet(models.Model):
    id_user = models.IntegerField()
    twt_id = models.IntegerField()
    user_tweet = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_id = models.ForeignKey(Tweets, on_delete=models.CASCADE)

class favorite(models.Model):
    fav_id = models.IntegerField()
    twt_id = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    user_twt = models.ForeignKey(User, on_delete=models.CASCADE)
