from django.contrib import admin

from goals.models import Goal, GoalCategory, GoalComment


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_deleted',)
    list_display_links = ('title',)
    search_fields = ('title', 'user',)
    list_filter = ('is_deleted', 'user')
    readonly_fields = ('created', 'updated',)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'category', 'status', 'priority')
    search_fields = ('title', 'description',)
    list_filter = ('status', 'priority')
    readonly_fields = ('created', 'updated',)


@admin.register(GoalComment)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'goal',)
    readonly_fields = ('created', 'updated',)
    list_filter = ('goal',)
