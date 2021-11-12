from django.contrib import admin

# Register your models here.
from schedule.models import Schedule, Schedule_content

admin.site.register(Schedule)
admin.site.register(Schedule_content)