from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Question(models.Model):
    auth = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    image = models.ImageField(upload_to='poll_pics',default='poll_pics/empty.png')
    def __str__(self):
        return self.question
    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    # likes = models.IntegerField(max_length=None)
    # comment_number = models.IntegerField(max_length=None)
    # eyes = models.IntegerField(max_length=None)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
class Comments(models.Model):
    auth = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    def __str__(self):
        return self.question.question
