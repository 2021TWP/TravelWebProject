from rest_framework import serializers

from .models import Schedule, Schedule_content


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id',  'start_date',
                  'end_date', 'location']


class ScheduleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule_content
        fields = ['id', 'content', 'schedule_id']



