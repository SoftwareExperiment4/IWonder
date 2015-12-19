from django.db import models
from django.utils import timezone


class Questionaire(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        'membership.User',
        on_delete=models.CASCADE)
    hits = models.PositiveIntegerField(default=0)
    replies = models.PositiveIntegerField(default=0)
    # shape = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Page(models.Model):
    number = models.PositiveIntegerField(default=0)
    questionaire = models.ForeignKey(
        'Questionaire',
        on_delete=models.CASCADE
    )

    # prev_page = models.ForeignKey(
    #     'Page',
    #     on_delete=PREV.PREV
    # )
    # next_page = models.ForeignKey(
    #     'Page',
    #     on_delete=NEXT.NEXT
    # )

    def __str__(self):
        return self.questionaire + ' ' + self.number


class Question(models.Model):
    number = models.IntegerField(default=0)
    page = models.ForeignKey(
        'Page',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)

    OBJECTIVE = 'OBJ'
    MULTIPLE = 'MUL'
    SHORT_SENTENCE = 'SHS'
    LONG_SENTENCE = 'LNS'

    TYPE_CHOICES = (
        (OBJECTIVE, 'Objective'),
        (MULTIPLE, 'Multiple'),
        (SHORT_SENTENCE, 'Short Sentence'),
        (LONG_SENTENCE, 'Long Sentence'),
    )
    type = models.CharField(max_length=3,
                           choices=TYPE_CHOICES,
                           default=OBJECTIVE)

    description = models.TextField()
    # prev_question = models.ForeignKey(
    #     'Question',
    #     on_delete=PREV.PREV
    # )
    # next_question = models.ForeignKey(
    #     'Question',
    #     on_delete=NEXT.NEXT
    # )

    def __str__(self):
        return self.page + ' - ' + self.number