from django.contrib import admin

from webapp.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    list_display_links = ['question']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_display_links = ['text']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)