from django.db import models


class FeedBack(models.Model):
    FEEDBACK_CHOICE = (
        (1, 'Правообладание и юридические аспекты'),
        (2, 'Вопросы рекламы'),
        (3, 'Проблемы на сайте'),
        (4, 'Пожелания и хотелки'),
    )

    name = models.CharField(max_length=50)
    email = models.EmailField()
    type_message = models.PositiveSmallIntegerField(choices=FEEDBACK_CHOICE)
    text = models.TextField()
