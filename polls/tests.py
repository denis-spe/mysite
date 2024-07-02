import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question



# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_recently_published(), False)


    def test_was_published_recently_with_old_question(self):
        """
        was_recently_published() returns
        False for question whose pub_date
        is older then 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)

        self.assertIs(old_question.was_recently_published(), False)

    def test_published_recently_with_recently_question(self):
        """
        was_recently_published() returns
        True for question pub_date is within
        the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)

        recently_question = Question(
                pub_date=time)
        self.assertIs(
            recently_question.was_recently_published(), True)
