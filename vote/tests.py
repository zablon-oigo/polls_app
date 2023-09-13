from django.test import TestCase
import datetime
from django.urls import reverse
from .models import Question
from django.utils import timezone
class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(pub_date=time)

        self .assertEqual(future_question.was_published_recently(),False)


def create_question(question_text, days):
    time=timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response=self.client.get(reverse("vote:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No votes are available")
        