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
from rest_framework.validators import UniqueValidator

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
        return {
            'email_template_name': 'password_reset_key_message.txt',
            'base_template_name': 'base_message.txt',
            }


class PasswordResetConfirmSerializer(_PasswordResetConfirmSerializer):
    new_password1 = serializers.CharField(max_length=127,
                                          required=True,
                                          error_messages={"blank": "변경하실 비밀번호를 입력해주세요"})
    new_password2 = serializers.CharField(max_length=127,
                                          required=True,
                                          error_messages={"blank": "비밀번호 확인을 입력해주세요"})


class GroupSerializer(ModelSerializer):
    group_name = serializers.CharField(required=True,
                                       validators=[UniqueValidator(queryset=UserGroup.objects.all(),
                                                                   message="이미 같은 이름의 그룹이 존재합니다.")],
                                       error_messages={"blank": "그룹 명을 작성해 주세요"})
    schedules = ScheduleSerializer(many=True, read_only=True)
    pin = serializers.CharField(required=True, max_length=8, error_messages={"blank": "PIN을 입력해 주세요"})

    class Meta:
        model = UserGroup
        fields = ['id', 'group_name', 'pin', 'schedules', 'created_date']

    def validate_pin(self, value):
        if len(value) > 8 or len(value) < 4:
            raise serializers.ValidationError("PIN은 4자 이상 8자 이하의 문자열로 이루어져야 합니다")
        return value


class UserSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=20, error_messages={"blank": "이름을 입력해주세요"})
    email = serializers.EmailField(required=True, error_messages={"blank": "이메일을 입력해주세요"})
    username = serializers.CharField(error_messages={"blank": "아이디를 입력해주세요"})
    password1 = serializers.CharField(error_messages={"blank": "비밀번호를 입력해주세요"})
    password2 = serializers.CharField(error_messages={"blank": "비밀번호 확인을 입력해주세요"})
    g_id = GroupSerializer(many=True, read_only=True)

    def get_cleaned_data(self):
        data_in_dictionary = super().get_cleaned_data()
        data_in_dictionary['name'] = self.validated_data.get('name', '')
        return data_in_dictionary


class UserDataSerializer(ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20, error_messages={"blank": "이름을 입력해주세요"})
    email = serializers.EmailField(required=True, error_messages={"blank": "이메일을 입력해주세요"})
    username = serializers.CharField(error_messages={"blank": "아이디를 입력해주세요"})
    g_id = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'name', 'email', 'g_id']


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True, error_messages={"blank": "아이디를 입력해주세요"})
    password = serializers.CharField(required=True, error_messages={"blank": "비밀번호를 입력해주세요"})




class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
                 ('name',)