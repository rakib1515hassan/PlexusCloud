from django.urls import path

from apps.cloud.View import instance

app_name = 'cloud'


urlpatterns = [
    path('instance-create/', instance.InstanceCreateView.as_view(), name='instance_create'),
]