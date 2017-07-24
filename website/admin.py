from django.contrib import admin

# Register your models here.
from website.models import (
    ElementWord, Events, Task,
    Submission, Post, Comments,
    PostType, TaskType, Attachment,
)

admin.site.register(ElementWord)
admin.site.register(Events)
admin.site.register(Task)
admin.site.register(Submission)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(PostType)
admin.site.register(TaskType)
admin.site.register(Attachment)
