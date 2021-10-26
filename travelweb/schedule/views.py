from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Schedule, Schedule_content
from .serializers import ScheduleSerializer, ScheduleContentSerializer
from authentication.models import UserGroup
from authentication.serializers import GroupSerializer


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
        return Response(serializer.data)
    else:
        return Response({"msg": "failed"})


@api_view(['PUT'])
def schedule_update(request, pk):
    schedule = Schedule.objects.get(id=pk)
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
    return Response('Deleted')


@api_view(['GET'])
def schedule_content_num(request, pk):
    list = Schedule_content.objects.filter(schedule_id=pk)
    serializer = ScheduleContentSerializer(list, many=True)
    return Response(serializer.data)



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
    content = Schedule_content.objects.get(id=pk)
    serializer = ScheduleContentSerializer(instance=content, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "success"})
    else:
        return Response({"msg": "failed"})


@api_view(['DELETE'])
def schedule_content_delete(request, pk):
    content = Schedule_content.objects.get(id=pk)
    content.delete()
    return Response('Deleted')


@api_view(['GET'])
def schedule_content_detail(request, pk):
    content = Schedule_content.objects.get(id=pk)
    serializer = ScheduleContentSerializer(content, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def schedule_content_list(request):
    list = Schedule_content.objects.all()
    serializer = ScheduleContentSerializer(list, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def get_data(request):



@api_view(['POST'])
def group_schedule_create(request, g_id):

    serializer = ScheduleSerializer(data=request.data)
    group = UserGroup.objects.get(id=g_id)#시케쥴??
    if serializer.is_valid():
        serializer.save()
        group.schedules.add(serializer.data['id'])
        return Response(serializer.data)
    else:
        return Response({"msg": "failed"})


@api_view(['GET'])
def group_schedule_list(request, g_id):
    group = UserGroup.objects.get(id=g_id)
    serializer =GroupSerializer(group, many=False)

    return Response(serializer.data['schedules'])

