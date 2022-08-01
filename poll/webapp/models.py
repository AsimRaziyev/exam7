from django.db import models


class Poll(models.Model):
    question = models.TextField(verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата создания опроса")

    class Meta:
        db_table = "polls"
        verbose_name = "Poll"
        verbose_name_plural = "Polls"


class Choice(models.Model):
    text = models.TextField(verbose_name="Вариант")
    poll = models.ForeignKey(to=Poll, on_delete=models.CASCADE, related_name="choices")

    class Meta:
        db_table = "choices"
        verbose_name = "Choice"
        verbose_name_plural = "Choices"


class Answer(models.Model):
    poll = models.ForeignKey(to=Poll, on_delete=models.CASCADE, related_name="answers")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата создания ответа")
    choice = models.ForeignKey(to=Choice, on_delete=models.CASCADE, related_name="answers")

    class Meta:
        db_table = "answers"
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
