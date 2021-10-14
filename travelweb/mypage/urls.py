"""travelweb URL Configuration

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
from django.contrib import admin

from django.urls import path
from mypage import views

urlpatterns = [
    path('<str:id>/', views.mypage_list, name="mypage_list"),

    path('<str:id>/changeinfo/', views.mypage_changeinfo, name="mypage_changeinfo"),
    path('<str:id>/changeinfo/update/<str:pk>', views.mypage_changeinfo_update, name="mypage_changeinfo_update"),

    path('<str:id>/group/', views.mypage_group, name="mypage_group"),
    path('<str:id>/group/create/', views.mypage_group_create, name="mypage_group_create"),
    path('<str:id>/group/update/<str:pk>/', views.mypage_group_update, name="mypage_group_update"),
    path('<str:id>/group/delete/<str:pk>/', views.mypage_group_delete, name="mypage_group_delete"),

    path('<str:id>/plan/', views.mypage_plan, name="mypage_plan"),
    path('<str:id>/plan/create/', views.mypage_plan_create, name="mypage_plan_create"),
    path('<str:id>/plan/update/<str:pk>', views.mypage_plan_update, name="mypage_plan_update"),
    path('<str:id>/plan/delete/<str:pk>', views.mypage_plan_update, name="mypage_plan_delete"),

]
