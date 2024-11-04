from django.urls import path

from apps.cloud.View import instance
from apps.cloud.View import apis

app_name = 'cloud'


urlpatterns = [
    path('instance-create/', instance.InstanceCreateView.as_view(), name='instance_create'),





    ## API
    path('api/services/', apis.ServiceNameListView.as_view(), name='service-list-api'), 
]