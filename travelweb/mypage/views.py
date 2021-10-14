from django.shortcuts import render

from rest_framework.decorators import api_view


# Create your views here.
from rest_framework.response import Response

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer


@api_view(['GET'])
def mypage_list(request, id):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    pass


@api_view(['GET'])
def mypage_changeinfo(request, id):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    pass


@api_view(['PUT'])
def mypage_changeinfo_update(request, id, pk):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    pass


@api_view(['GET'])
def mypage_group(request, id):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    pass


@api_view(['POST'])
def mypage_group_create(request, id):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    pass


@api_view(['PUT'])
def mypage_group_update(request, id , pk):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    pass


@api_view(['DELETE'])
def mypage_group_delete(request, id , pk):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    pass


@api_view(['GET'])
def mypage_plan(request, id):
    # if request.user.is_authenticated:  --> 로그인 여부 체크
    # login_user = request.user.id
    # print(login_user)
    schedules = Schedule.objects.all()# id = login_user
    serializer = ScheduleSerializer(schedules,  many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['POST'])
def mypage_plan_create(request):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    # login_user = request.user.id
    # print(login_user)
    serializer = ScheduleSerializer(date=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    pass


@api_view(['PUT'])
def mypage_plan_update(request, pk):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    # login_user = request.user.id
    # print(login_user)

    schedules = Schedule.objects.all()# id = pk
    serializer = ScheduleSerializer(isinstance=schedules, date=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    pass


@api_view(['DELETE'])
def mypage_plan_delete(request, id , pk):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    # login_user = request.user.id
    # print(login_user)
    schedules = Schedule.objects.all()  # id = pk
    schedules.delete()
    return Response({"message": "delete"})

    pass

