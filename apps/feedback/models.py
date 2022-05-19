from django.db import models

TYPE_MESSAGE = None


class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()  # валидация нужно
    type_message = models.CharField(max_length=1, choices=TYPE_MESSAGE)
    text = models.TextField()

