from django import forms
from django.forms import widgets
from webapp.models import Poll, Choice


class PollsForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ['question']
        widgets = {
            # 'poll': widgets.CheckboxSelectMultiple,
            'question': widgets.Textarea(attrs={'placeholder': 'Введите вопрос...', 'rows': 3, 'class': 'form-control'})
        }


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ['text']
        widgets = {
            'text': widgets.Textarea(attrs={'placeholder': 'Введите вариант ответа...', 'rows': 3, 'class': 'form-control'})
        }
