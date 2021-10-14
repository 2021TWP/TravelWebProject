from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Schedule, Schedule_content
from .serializers import ScheduleSerializer, ScheduleContentSerializer


@api_view(['GET'])
def schedule_list(request):
    list = Schedule.objects.all()
    serializer = ScheduleSerializer(list, many= True)
    return Response(serializer.data)


@api_view(['GET'])
def schedule_detail(request, pk):
    schedule = Schedule.objects.get(id=pk)
    serializer = ScheduleSerializer(schedule, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def schedule_create(request):
    serializer = ScheduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "success"})
    else:
        return Response({"msg": "failed"})


@api_view(['PUT'])
def schedule_update(request, pk):
    schedule = Schedule_content.objects.get(id=pk)
    serializer = ScheduleSerializer(instance=schedule, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "success"})
    else:
        return Response({"msg": "failed"})


@api_view(['DELETE'])
def schedule_delete(request, pk):
    schedule = Schedule.objects.get(id=pk)
    schedule.delete()


@api_view(['POST'])
def schedule_content_create(request):
    serializer = ScheduleContentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "success"})
    else:
        return Response({"msg": "failed"})


@api_view(['PUT'])
def schedule_content_update(request, pk):
    content = Schedule.objects.get(id=pk)
    serializer = ScheduleContentSerializer(instance=content, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "success"})
    else:
        return Response({"msg": "failed"})


@api_view(['DELETE'])
def schedule_content_delete(request, pk):
    content = ScheduleContentSerializer.objects.get(id=pk)
    content.delete()




