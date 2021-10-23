from django.shortcuts import render

from rest_framework.decorators import api_view

# Create your views here.
from rest_framework.response import Response

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer

from authentication.models import UserInfo

from authentication.serializers import UserSerializer

from board.models import Board

from board.serializer import BoardSerializer

# 내 정보
from authentication.serializers import UserDataSerializer


@api_view(['GET'])
def mypage_list(request):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    myinfo = UserInfo.objects.filter(username=request.user.username) #request.user.username
    serializer = UserDataSerializer(myinfo, many=True)
    return Response(serializer.data)

# 내가 작성한 글
@api_view(['GET'])
def mypage_board(request):
    boards = Board.objects.filter(id=request.user.id)
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)


# 내 정보 수정
@api_view(['PUT'])
def mypage_changeinfo(request):
    # if request.user.is_authenticated:     --> 로그인 여부 체크
    myinfo = UserInfo.objects.get(id=request.user.id)
    serializer = UserSerializer(instance=myinfo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Information change success!!"})
    else:
        return Response({"message": "Failed to change!"})


# @api_view(['PUT'])
# def mypage_changeinfo_update(request, id, pk):
#     # if request.user.is_authenticated:     --> 로그인 여부 체크
#     pass


# @api_view(['GET'])
# def mypage_group(request, id):
#     # if request.user.is_authenticated:     --> 로그인 여부 체크
#     pass
#
#
# @api_view(['POST'])
# def mypage_group_create(request, id):
#     # if request.user.is_authenticated:     --> 로그인 여부 체크
#     pass
#
#
# @api_view(['PUT'])
# def mypage_group_update(request, id, pk):
#     # if request.user.is_authenticated:     --> 로그인 여부 체크
#     pass
#
#
# @api_view(['DELETE'])
# def mypage_group_delete(request, id, pk):
#     # if request.user.is_authenticated:     --> 로그인 여부 체크
#     pass

#
# @api_view(['GET'])
# def mypage_plan(request, id):
#     # if request.user.is_authenticated:  --> 로그인 여부 체크
#     # login_user = request.user.id
#     # print(login_user)
#     schedules = Schedule.objects.all()# id = login_user
#     serializer = ScheduleSerializer(schedules,  many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
#
#
# @api_view(['POST'])
# def mypage_plan_create(request):
#     # if request.user.is_authenticated:     --> 로그인 여부 체크
#     # login_user = request.user.id
#     # print(login_user)
#     serializer = ScheduleSerializer(date=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
#     pass
#

# @api_view(['PUT'])
# def mypage_plan_update(request, pk):
#     # if request.user.is_authenticated:     --> 로그인 여부 체크
#     # login_user = request.user.id
#     # print(login_user)
#
#     schedules = Schedule.objects.all()# id = pk
#     serializer = ScheduleSerializer(isinstance=schedules, date=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
#     pass
#
#
# @api_view(['DELETE'])
# def mypage_plan_delete(request, id , pk):
#     # if request.user.is_authenticated:     --> 로그인 여부 체크
#     # login_user = request.user.id
#     # print(login_user)
#     schedules = Schedule.objects.all()  # id = pk
#     schedules.delete()
#     return Response({"message": "delete"})
#
#     pass
