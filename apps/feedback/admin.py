from django.contrib import admin

from apps.feedback.models import FeedBack


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    ...
