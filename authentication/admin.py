from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Organization, User

admin.site.register(User)
admin.site.register(Organization)