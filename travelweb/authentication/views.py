from django.shortcuts import redirect
from rest_framework.decorators import api_view
from authentication.serializers import UserSerializer, GroupSerializer, UserDataSerializer
from rest_framework.response import Response
from allauth.account.models import EmailAddress

from authentication.models import UserInfo, UserGroup


@api_view(['GET'])
def user_check(request):
    # print(request.user)
    # print(request.auth)
    # print(request.user in Group.objects.get(name='abcd').user_set.all())
    # user = UserInfo.objects.all()
    # print(user)
    # serializer = UserDataSerializer(user, many=True)

    user2 = UserInfo.objects.filter(id=2)
    serializer = UserDataSerializer(user2, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def group_create(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        request.user.g_id.add(serializer.data['id'])
        return Response("good job")
    return Response("nope")

@api_view(['GET'])
def group_all(request):
    groups = UserGroup.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def my_groups(request):
    serializer = GroupSerializer(request.user.g_id.all(), many=True)
    my_group_id = list(map(lambda x: x['id'], serializer.data))
    return Response({'id': my_group_id, 'groups': serializer.data})


@api_view(['PUT'])
def group_join(request):
    group = UserGroup.objects.get(id=request.data['g_id'])
    serializer = GroupSerializer(group, many=False)
    serializer2 = GroupSerializer(request.user.g_id.all(), many=True)
    my_groups_id = list(map(lambda x: x['id'], serializer2.data))
    if request.user.is_authenticated:
        if serializer.data['pin'] == request.data['pin']:
            if group.id in my_groups_id:
                return Response({'error': '이미 가입한 그룹입니다.'})
            user = UserInfo.objects.get(id=request.user.id)
            user.g_id.add(group.id)
            return Response({'success': '가입 완료'})
        else:
            return Response({'error': 'pin번호가 틀렸습니다.'})
    else:
        return Response({'error': '로그인이 필요한 서비스입니다.'})


@api_view(['PUT'])
def group_withdraw(request):
    user = UserInfo.objects.get(id=request.user.id)
    user.g_id.remove(request.data['g_id'])
    try:
        UserInfo.objects.get(g_id=request.data['g_id'])
    except Exception:
        group = UserGroup.objects.get(id=request.data['g_id'])
        group.delete()
    return Response({"success": "탈퇴 완료"})

@api_view(['GET'])
def get_userinfo(request):
    userdata = {'username': request.user.username,
                'name': request.user.name,
                'id': request.user.id,
                'email': request.user.email}
    return Response(userdata)


@api_view(['GET'])
def users_in_group(request, g_id):
    users = UserInfo.objects.filter(g_id=g_id)
    serializer = UserDataSerializer(users, many=True)
    name = []
    print(serializer.data)
    for i in serializer.data:
        name.append(i['name'])
    print(name)
    return Response(name)
