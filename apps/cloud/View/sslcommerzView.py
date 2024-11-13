from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from sslcommerz_lib import SSLCOMMERZ 
from decimal import Decimal
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse
import json

## 
from apps.cloud.models import Instance, ServiceDetails

class InitiatePaymentView(View):
    def post(self, request, *args, **kwargs):
        user = request.user

        try:
            data = json.loads(request.body)

            project_name = data.get('project_name')
            instence_name = data.get('instence_name')
            availability_zone = data.get('availability_zone')
            ram = data.get('ram')
            cpu = data.get('cpu')
            storage_type = data.get('storage_type')
            storage_size = data.get('storage_size')
            bandwidth = data.get('bandwidth')
            ip_type = data.get('ip_type')
            total_amount = data.get('total_amount')

            print("----------------------------")
            print("project_name =", project_name)
            print("instence_name =", instence_name)
            print("availability_zone =", availability_zone)
            print("ram =", ram)
            print("cpu =", cpu)
            print("storage_type =", storage_type)
            print("storage_size =", storage_size)
            print("bandwidth =", bandwidth)
            print("ip_type =", ip_type)
            print("total_amount =", total_amount)
            print("----------------------------")

            ins = Instance.objects.create(
                user = user,
                name = instence_name,
                zone = availability_zone,
                ram  = ram,
                cpu  = cpu,
                ip   = ip_type,
                total = total_amount,
                project_name = project_name,
                description  = 'Test Description',
                storage   = f"{storage_size} {storage_type}",
                bandwidth = bandwidth,
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

        sslcz = SSLCOMMERZ({
            'store_id':   settings.SSLCOMMERZ_STORE_ID,
            'store_pass': settings.SSLCOMMERZ_STORE_PASSWORD,
            'issandbox':  settings.SSLCOMMERZ_SANDBOX_MODE
        })

        payment_data = {
            'total_amount': str(Decimal(data.get("total_amount", "0"))),  
            'currency': data.get("currency", "BDT"),
            'tran_id' : data.get("order_id", "default_order_id"),

            ## Set URLs for payment success, failure, and cancellation
            'success_url': request.build_absolute_uri(reverse('cloud:payment_success')),
            'fail_url'   : request.build_absolute_uri(reverse('cloud:payment_failed')),
            'cancel_url' : request.build_absolute_uri(reverse('cloud:payment_canceled')),
            'ipn_url'    : request.build_absolute_uri(reverse('cloud:payment_ipn')),

            ## Set Product Info.
            'product_category': data.get("product_category", "Category"),
            'product_name': data.get("product_name", "Product Name"),

            ## Set Customer Info from the authenticated user
            'cus_name': data["customer_info"].get("name", f"{user.first_name} {user.last_name}"),
            'cus_email': data["customer_info"].get("email", user.email),
            'cus_add1': data["customer_info"].get("address1", "Customer Address"),  
            'cus_city': data["customer_info"].get("city", "Dhaka"),
            'cus_postcode': data["customer_info"].get("postcode", "1216"),
            'cus_country': data["customer_info"].get("country", "Bangladesh"),
            'cus_phone': data["customer_info"].get("phone", user.phone if user.phone else "017XXXXXXXX"),

            'shipping_method': "NO",
            'num_of_item': 1,
            'product_profile': 'general',
        }

        response_data = sslcz.createSession(payment_data)


        if response_data.get("status") == "SUCCESS" and response_data.get("GatewayPageURL"):
            return JsonResponse({"GatewayPageURL": response_data["GatewayPageURL"]})
        else:
            return JsonResponse({"error": "Failed to initiate payment."}, status=500)





def payment_success(request):
    return HttpResponse("<h1>Payment Success</h1>")



def payment_fail(request):
    return HttpResponse("<h1>Payment Fail</h1>")



def payment_cancel(request):
    return HttpResponse("<h1>Payment Cancel</h1>")




def payment_ipn(request):
    return HttpResponse("<h1>Payment IPN</h1>")



