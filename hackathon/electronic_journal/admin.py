from django.contrib import admin
from .models import (Group, Subject, Quest, UserQuest, User)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_login', 'username', 'email', 'phone', 'role')
    list_display_links = ('id', 'last_login', 'username', 'email', 'phone')
    search_fields = ('id', 'username', 'phone', 'email')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'curs')
    list_display_links = ('id', 'name', 'curs')
    search_fields = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


class QuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'quest_name', 'subject', 'teacher', 'group', 'description', 'date_added', 'date_pass')
    list_display_links = ('id', 'subject')
    search_fields = ('id', 'subject', 'description')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name', 'subject_code', 'description')
    list_display_links = ('id', 'subject_name')
    search_fields = ('id', 'subject_name')
    prepopulated_fields = {'slug': ('subject_name',)}


class UserQuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'quest', 'user', 'comment', 'date_added')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'quest')
    # prepopulated_fields = {'slug': ('user', 'quest')}


admin.site.register(Group, GroupAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Quest, QuestAdmin)
admin.site.register(UserQuest, UserQuestAdmin)
admin.site.register(User, UserAdmin)
