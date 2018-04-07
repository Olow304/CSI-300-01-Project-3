from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    twitter_handle = models.CharField(max_length = 20)
    email_address = models.CharField(max_length = 60)

    def __str__(self):
        return self.name

#TODO: tweet model
class tweet(models.Model):
    twt_id = models.AutoField(primary_key = True)
    content = models.CharField(max_length = 140)
    ret_id = models.IntegerField()
    fav_id = models.IntegerField()
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE)

    def __str__(self):
        return self.content
