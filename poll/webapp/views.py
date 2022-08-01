from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from webapp.forms import PollsForm, ChoiceForm
from webapp.models import Poll, Choice, Answer
from django.urls import reverse, reverse_lazy


class PollsTake(TemplateView):
    template_name = "polls/take.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = Poll.objects.get(pk=context['pk'])
        context['choices'] = Choice.objects.filter(poll_id=context['pk'])
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        choice = Choice.objects.get(pk=self.request.POST.get('choice'))
        answer = Answer(poll=context['poll'], choice=choice)
        answer.save()
        return redirect('polls_view', pk=context['pk'])


class PollsList(ListView):
    model = Poll
    template_name = "polls/index.html"
    context_object_name = "polls"
    ordering = "-created_at"
    paginate_by = 5


class PollsCreate(CreateView):
    form_class = PollsForm
    template_name = "polls/create.html"

    def get_success_url(self):
        return reverse("polls_index")


class PollsView(DeleteView):
    model = Poll
    template_name = "polls/view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = self.object.choices.order_by("id")
        return context


class PollsUpdate(UpdateView):
    form_class = PollsForm
    template_name = "polls/update.html"
    model = Poll

    def get_success_url(self):
        return reverse("polls_index")


class PollsDelete(DeleteView):
    model = Poll
    template_name = "polls/delete.html"
    success_url = reverse_lazy("polls_index")


class ChoiceCreate(CreateView):
    form_class = ChoiceForm
    template_name = "choices/create.html"

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        form.instance.poll = poll
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("polls_view", kwargs={"pk": self.object.poll.pk})


class ChoiceUpdate(UpdateView):
    form_class = ChoiceForm
    template_name = "choices/update.html"
    model = Choice

    def get_success_url(self):
        return reverse("polls_view", kwargs={"pk": self.object.poll.pk})


class ChoiceDelete(DeleteView):
    model = Choice
    template_name = "choices/delete.html"

    def get_success_url(self):
        return reverse("polls_view", kwargs={"pk": self.object.poll.pk})
