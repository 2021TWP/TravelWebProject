"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include, re_path
from authentication import views
from dj_rest_auth.registration.views import VerifyEmailView
from allauth.account.views import ConfirmEmailView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    re_path(r'^signup/account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),
    path('test/', views.user_check, name="test"),
    path('userinfo/', views.get_userinfo, name="get_userinfo"),
    path('group/', views.group_all, name="group_all"),
    path('group/myGroups/', views.my_groups, name="my_groups"),
    path('group/join/', views.group_join, name="group_join"),
    path('group/withdraw/', views.group_withdraw, name="group_join"),
    path('group/usersInGroup/<int:g_id>', views.users_in_group, name="user_in_group"),
    path('group/create/', views.group_create, name="group_create"),

    # path()
]
