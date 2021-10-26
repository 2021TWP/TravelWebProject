from django.contrib import admin
from authentication.models import UserInfo, UserGroup


admin.site.register(UserInfo)
admin.site.register(UserGroup)
