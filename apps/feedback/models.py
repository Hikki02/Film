from django.db import models

from apps.feedback import utils


class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    type_message = models.PositiveSmallIntegerField(choices=utils.FEEDBACK_CHOICE)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
