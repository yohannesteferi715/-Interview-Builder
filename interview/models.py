from django.db import models

# Create your models here.
from django.db import models

from documents.models import Document


class Interview(models.Model):

    DIFFICULTY_CHOICES = [
        ("junior", "Junior"),
        ("mid", "Mid"),
        ("senior", "Senior"),
    ]

    QUESTION_TYPE_CHOICES = [
        ("technical", "Technical"),
        ("conceptual", "Conceptual"),
        ("scenario", "Scenario"),
        ("mixed", "Mixed"),
    ]

    title = models.CharField(max_length=255)

    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="interviews",
    )

    topic = models.CharField(max_length=255)

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
    )

    question_type = models.CharField(
        max_length=20,
        choices=QUESTION_TYPE_CHOICES,
        default="mixed",
    )

    number_of_questions = models.PositiveIntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Question(models.Model):

    interview = models.ForeignKey(
        Interview,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    question = models.TextField()

    answer = models.TextField(
        blank=True
    )

    explanation = models.TextField(
        blank=True
    )

    difficulty = models.CharField(
        max_length=20,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.question[:100]