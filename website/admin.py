from django.contrib import admin

# Register your models here.
from website.models import (
    ElementWord, Event, Task,
    Submission, Post, Comment,
    PostType,
    Album, TaskStatistic,
    EventStatistic, UserStatistic,
)


class ElementWordModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'testimony', 'approved')
    list_filter = ('approved', )

    class Meta:
        model = ElementWord


class EventModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'start_time', 'end_time')

    class Meta:
        model = Event


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_kenalan')
    list_filter = ('is_kenalan',)

    class Meta:
        model = Task


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'summary', 'content', 'post_type')
    list_filter = ('post_type',)

    class Meta:
        model = Post


class SubmissionModelAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'task', 'file_link',
                    'is_checked', 'is_approved', 'created_at', 'updated_at')
    list_filter = ('task', 'is_checked', 'is_approved')

    def user_profile(self, obj):
        return obj.user.profile

    class Meta:
        model = Submission

admin.site.register(ElementWord, ElementWordModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(Task, TaskModelAdmin)
admin.site.register(Submission, SubmissionModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment)
admin.site.register(PostType)
admin.site.register(Album)
admin.site.register(TaskStatistic)
admin.site.register(EventStatistic)
admin.site.register(UserStatistic)

