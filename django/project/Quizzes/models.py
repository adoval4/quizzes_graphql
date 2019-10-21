"""
Quizzes models
"""

# Django
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Models
from Developers.models import Developer

# Utilities
from Utils.models import CustomBaseModel


class Topic(CustomBaseModel):
    """
    Quiz topics model
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Quiz(CustomBaseModel):
    """
    Quiz model
    """
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return '{} - {}'.format(self.topic, self.name)


class Response(CustomBaseModel):
    """
    Quiz response model
    """
    quiz = models.CharField(max_length=200)
    developer = models.ForeignKey(
        Developer,
        on_delete=models.CASCADE
    )
    points = models.PositiveIntegerField()

    def __str__(self):
        return '{} - {}'.format(self.topic, self.name)

