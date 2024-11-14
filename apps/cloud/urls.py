from django.urls import path

from apps.cloud.View import instance
from apps.cloud.View import apis
from apps.cloud.View import sslcommerzView

app_name = 'cloud'


urlpatterns = [
    path('instance-create/', instance.InstanceCreateView.as_view(), name='instance_create'),





    ## API
    path('api/services/', apis.ServiceNameListView.as_view(), name='service_list_api'),
    path('api/availabil-area-zone-list/', apis.AvailabilityZoneListAPIView.as_view(), name='availabil_area_zone_list'),

    path('api/payment/', sslcommerzView.InitiatePaymentView.as_view(), name='payment_method'),

    path('payment-success', sslcommerzView.payment_success, name='payment_success'), 
    path('payment-fail',    sslcommerzView.payment_fail,    name='payment_failed'), 
    path('payment-cancel',  sslcommerzView.payment_cancel,  name='payment_canceled'), 
    path('payment-ipn',     sslcommerzView.payment_ipn,     name='payment_ipn'), 
]