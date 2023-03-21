from django.contrib import admin

from apps.newsletter.admin import SubscriptionAdmin
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (SubscriptionAdmin,)
