from django.contrib import admin
from django.urls import path

from webapp.views import PollsList, PollsCreate, PollsView, PollsUpdate, PollsDelete, ChoiceCreate, ChoiceUpdate, ChoiceDelete, PollsTake

urlpatterns = [
    path("", PollsList.as_view(), name="polls_index"),
    path("polls/", PollsCreate.as_view(), name="polls_create"),
    path("polls/<int:pk>", PollsView.as_view(), name="polls_view"),
    path("polls/<int:pk>/update", PollsUpdate.as_view(), name="polls_update"),
    path("polls/<int:pk>/delete", PollsDelete.as_view(), name="polls_delete"),
    path("polls/<int:pk>/choice/add/", ChoiceCreate.as_view(), name="polls_choice_create"),
    path("choices/<int:pk>/update/", ChoiceUpdate.as_view(), name="polls_choice_update"),
    path("choices/<int:pk>/delete/", ChoiceDelete.as_view(), name="polls_choice_delete"),
    path("polls/<int:pk>/take", PollsTake.as_view(), name="polls_take"),

    # path('tasks/', RedirectView.as_view(pattern_name="index")),
    # path('tasks/add/<int:pk>/', CreateTaskWithProject.as_view(), name='create_task'),
    # path("task/<int:pk>/", TaskView.as_view(), name="task_view"),
    # path('task/<int:pk>/update/', UpdateTask.as_view(), name="update_task"),
    # path('task/<int:pk>/delete/', DeleteTask.as_view(), name="delete_task"),
    # path("task/<int:pk>/comment/add/", CreateCommentView.as_view(), name="task_comment_create"),
    # path('comments/<int:pk>/update/', UpdateComment.as_view(), name="update_comment"),
    # path('comments/<int:pk>/delete/', DeleteComment.as_view(), name="delete_comment"),
    #
    #
    # path('projects/', ProjectsView.as_view(), name="projects_index"),
    # path('project/<int:pk>/', ProjectDetail.as_view(), name="project_view"),
    # path('project/', CreateProjectView.as_view(), name="project_create"),
    # path('projects/<int:pk>/update/', UpdateProject.as_view(), name="update_project"),
    # path('projects/<int:pk>/delete/', DeleteProject.as_view(), name="delete_project"),
]
