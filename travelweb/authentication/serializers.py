from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from dj_rest_auth.serializers import PasswordResetSerializer as _PasswordResetSerializer
from dj_rest_auth.serializers import PasswordResetConfirmSerializer as _PasswordResetConfirmSerializer
from django.contrib.auth.forms import PasswordResetForm
from authentication.models import UserGroup, UserInfo
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.conf import settings
from authentication.forms import CustomAllAuthPasswordResetForm

from schedule.serializers import ScheduleSerializer


class PasswordResetSerializer(_PasswordResetSerializer):

    @property
    def password_reset_form_class(self):
        if 'allauth' in settings.INSTALLED_APPS:
            return CustomAllAuthPasswordResetForm
        else:
            return PasswordResetForm

    def get_email_options(self):
        """Override this method to change default e-mail options"""
        print("check override")
        return {
            'email_template_name': 'password_reset_key_message.txt',
            'base_template_name': 'base_message.txt'
            }


class PasswordResetConfirmSerializer(_PasswordResetConfirmSerializer):
    new_password1 = serializers.CharField(max_length=127,
                                          required=True,
                                          error_messages={"blank": "변경하실 비밀번호를 입력해주세요"})
    new_password2 = serializers.CharField(max_length=127,
                                          required=True,
                                          error_messages={"blank": "비밀번호 확인을 입력해주세요"})


class UserSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=20, error_messages={"blank": "이름을 입력해주세요"})
    email = serializers.EmailField(required=True, error_messages={"blank": "이메일을 입력해주세요"})
    username = serializers.CharField(error_messages={"blank": "아이디를 입력해주세요"})
    password1 = serializers.CharField(error_messages={"blank": "비밀번호를 입력해주세요"})
    password2 = serializers.CharField(error_messages={"blank": "비밀번호 확인을 입력해주세요"})
    g_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def get_cleaned_data(self):
        data_in_dictionary = super().get_cleaned_data()
        data_in_dictionary['name'] = self.validated_data.get('name', '')
        return data_in_dictionary


class UserDataSerializer(ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20, error_messages={"blank": "이름을 입력해주세요"})
    email = serializers.EmailField(required=True, error_messages={"blank": "이메일을 입력해주세요"})
    username = serializers.CharField(error_messages={"blank": "아이디를 입력해주세요"})
    g_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'name', 'email', 'g_id']


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True, error_messages={"blank": "아이디를 입력해주세요"})
    password = serializers.CharField(required=True, error_messages={"blank": "비밀번호를 입력해주세요"})


class GroupSerializer(ModelSerializer):
    group_name = serializers.CharField(required=True)
    schedules = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    pin = serializers.CharField(required=True, max_length=8)

    class Meta:
        model = UserGroup
        fields = ['id', 'group_name', 'pin', 'schedules']


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
                 ('name',)