from django.contrib import admin

# Register your models here.
from website.models import (
    ElementWord, Event, Task,
    Submission, Post, Comment,
    PostType,
    Album, TaskStatistic,
    EventStatistic, UserStatistic,
)
ADMIN_PMB = 'adminpmb'


class ElementWordModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'testimony', 'approved')
    list_filter = ('approved', )

    def get_readonly_fields(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return ()
        return ('author', 'testimony')

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = ElementWord


class EventModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'start_time', 'end_time')

    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = Event


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_kenalan')
    list_filter = ('is_kenalan',)

    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = Task


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'summary', 'content', 'post_type')
    list_filter = ('post_type',)

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = Post


class SubmissionModelAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'task', 'file_link',
                    'is_checked', 'is_approved', 'created_at', 'updated_at')
    list_filter = ('task', 'is_checked', 'is_approved')
    search_fields = ('user__profile__name', )

    def user_profile(self, obj):
        return obj.user.profile

    def get_readonly_fields(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return ()
        return ('file_link', 'user_profile', 'task',)

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = Submission


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment')

    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = Comment


class PostTypeModelAdmin(admin.ModelAdmin):
    list_display = ('post_type',)

    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = PostType


class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'album_link')

    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = Album


class TaskStatisticModelAdmin(admin.ModelAdmin):
    list_display = ('task', 'amount')

    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = TaskStatistic


class EventStatisticModelAdmin(admin.ModelAdmin):
    list_display = ('event', 'attendee', 'on_time', 'late', 'permission', 'absent')

    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = EventStatistic


class UserStatisticModelAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'name', 'task', 'amount_total', 'amount_approved_total',)
    search_fields = ('user__profile__name',)

    def user_profile(self, obj):
        return obj.user.profile.name

    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB:
            return True
        return False

    class Meta:
        model = UserStatistic


admin.site.register(ElementWord, ElementWordModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(Task, TaskModelAdmin)
admin.site.register(Submission, SubmissionModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(PostType, PostTypeModelAdmin)
admin.site.register(Album, AlbumModelAdmin)
admin.site.register(TaskStatistic, TaskStatisticModelAdmin)
admin.site.register(EventStatistic, EventStatisticModelAdmin)
admin.site.register(UserStatistic, UserStatisticModelAdmin)
