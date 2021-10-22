from django.shortcuts import redirect
from rest_framework.decorators import api_view
from authentication.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from allauth.account.models import EmailAddress

from authentication.models import UserInfo, UserGroup


@api_view(['POST'])
def user_check(request):
    # print(request.user)
    # print(request.auth)
    print(request.user in Group.objects.get(name='abcd').user_set.all())
    print(Group.objects.get(name='abcd'))
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def group_create(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        UserGroup.objects.create(group_name=request.data['group_name'], pin=request.data['pin'])
        return Response("good job")
    else:
        print(serializer.data)
        return Response("응 안됨")


@api_view(['GET'])
def get_userinfo(request):
    userdata = {'username': request.user.username,
                'name': request.user.name,
                'id': request.user.id,
                'email': request.user.email}
    return Response(userdata)



