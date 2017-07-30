from django.contrib import admin

# Register your models here.
from website.models import (
    ElementWord, Event, Task,
    Submission, Post, Comment,
    PostType,
    Album, TaskStatistic,
    EventStatistic, UserStatistic,
)

admin.site.register(ElementWord)
admin.site.register(Event)
admin.site.register(Task)
admin.site.register(Submission)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostType)
admin.site.register(Album)
admin.site.register(TaskStatistic)
admin.site.register(EventStatistic)
admin.site.register(UserStatistic)

