from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    def __str__(self) -> str:
        return self.question_text

    def was_recently_published(self):
        now = timezone.now()

        return (now -
            datetime.timedelta(days=1)
            <= self.pub_date <= now
            )

class Choice(models.Model):
    question = models.ForeignKey(
            Question,
            on_delete=models.CASCADE
            )
    choice_text = models.CharField(
            max_length=200
            )
    vote = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
