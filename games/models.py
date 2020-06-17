from django.db import models
# add this import path, more flexible way of grabbing the user
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

# name your model in the singular, convention
class Game(models.Model):
    title = models.CharField(max_length=64)
    # under the hood getting the same thing as auth.user
    player = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game_detail',args=[str(self.id)])