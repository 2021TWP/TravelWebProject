from django.urls import path

# from travel import views
# from  import views
from schedule import views

urlpatterns = [
    path('', views.schedule_list, name="schedule_list"),
    path('<int:pk>', views.schedule_detail, name="schedule_detail"),
    path('create/', views.schedule_create, name="schedule_list"),
    path('update/<int:pk>/', views.schedule_update, name="schedule_list"),
    path('delete/<int:pk>/', views.schedule_delete, name="schedule_list"),
    path('content/create/', views.schedule_content_create, name="schedule_list"),
    path('content/update/<int:pk>/', views.schedule_content_update, name="schedule_list"),
    path('content/delete/<int:pk>/', views.schedule_content_delete, name="schedule_list"),
]
