from django.contrib import admin

from .models import Page, Video, Tutorial


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


class TutorialInline(admin.TabularInline):
    model = Tutorial
    extra = 1


class PageAdmin(admin.ModelAdmin):
    inlines = [TutorialInline, VideoInline]
    search_fields = ['title', ]


admin.site.register(Page, PageAdmin)
admin.site.register(Video)
admin.site.register(Tutorial)