from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UserSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=20, error_messages={"blank": "이름을 입력해주세요"})
    email = serializers.EmailField(required=True, error_messages={"blank": "이메일을 입력해주세요"})
    username = serializers.CharField(error_messages={"blank": "아이디를 입력해주세요"})
    password1 = serializers.CharField(error_messages={"blank": "비밀번호를 입력해주세요"})
    password2 = serializers.CharField(error_messages={"blank": "비밀번호 확인을 입력해주세요"})

    def get_cleaned_data(self):
        data_in_dictionary = super().get_cleaned_data()
        data_in_dictionary['name'] = self.validated_data.get('name', '')
        return data_in_dictionary


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True, error_messages={"blank": "아이디를 입력해주세요"})
    password = serializers.CharField(required=True, error_messages={"blank": "비밀번호를 입력해주세요"})


class GroupSerializer(ModelSerializer):
    groupName = serializers.CharField(required=True)
    pin = serializers.CharField(required=True)

    class Meta:
        model = Group
        fields = ['groupName', 'pin']


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
                 ('name',)