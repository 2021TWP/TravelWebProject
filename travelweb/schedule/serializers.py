from rest_framework import serializers

from .models import Schedule, Schedule_content

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'content_id', 'start_date',
                  'end_date', 'location']


class ScheduleContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule_content
        fields = ['id', 'content', 'travel_date']


