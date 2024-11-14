from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from sslcommerz_lib import SSLCOMMERZ 
from decimal import Decimal
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json, uuid

## Custom Import
from apps.cloud.models import Instance, ServiceDetails, AvailabilityZone
from apps.cloud.service import sslcommerz, openstack

class InitiatePaymentView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            data = json.loads(request.body)

            project_name  = data.get('project_name')
            instence_name = data.get('instence_name')
            availability_zone = data.get('availability_zone')
            ram = data.get('ram')
            cpu = data.get('cpu')
            storage_type = data.get('storage_type')
            storage_size = data.get('storage_size')
            bandwidth = data.get('bandwidth')
            ip_type   = data.get('ip_type')
            total_amount = data.get('total_amount')

            # Create an instance record in the database
            zone   = AvailabilityZone.objects.filter(id=availability_zone).first()
            tranId = 'TR_' + str(uuid.uuid4().hex)
            ins    = None
            if zone:
                ins = Instance.objects.create(
                    user  = user,
                    name  = instence_name,
                    zone  = zone,
                    ram   = ram,
                    cpu   = cpu,
                    ip    = ip_type,
                    total = total_amount,
                    project_name = project_name,
                    description  = 'Test Description',
                    storage      = f"{storage_size} {storage_type}",
                    bandwidth    = bandwidth,
                    tranId       = tranId  
                )

            # Prepare SSLCommerz payment data, including tranId and success URL with tranId as query param
            payment_data = {
                'total_amount': total_amount,
                'currency'    : data.get("currency", "BDT"),
                'order_id'    : tranId,

                'success_url' : request.build_absolute_uri(reverse('cloud:payment_success')) + f"?tranId={tranId}",
                'fail_url'    : request.build_absolute_uri(reverse('cloud:payment_failed')),
                'cancel_url'  : request.build_absolute_uri(reverse('cloud:payment_canceled')),
                'ipn_url'     : request.build_absolute_uri(reverse('cloud:payment_ipn')),

                'product_category': data.get("product_category", "Category"),
                'product_name'    : data.get("product_name", "Product Name"),

                'customer_info': {
                    'name'    : data["customer_info"].get("name", f"{user.first_name} {user.last_name}"),
                    'email'   : data["customer_info"].get("email", user.email),
                    'address1': data["customer_info"].get("address1", "Customer Address"),
                    'city'    : data["customer_info"].get("city", "Dhaka"),
                    'postcode': data["customer_info"].get("postcode", "1216"),
                    'country' : data["customer_info"].get("country", "Bangladesh"),
                    'phone'   : data["customer_info"].get("phone", user.phone if user.phone else "017XXXXXXXX"),
                },
            }

            # Initiate payment session through SSLCommerz service function
            response_data = sslcommerz.create_payment_session(payment_data)

            if response_data.get("status") == "SUCCESS" and response_data.get("GatewayPageURL"):
                return JsonResponse({"GatewayPageURL": response_data["GatewayPageURL"]})
            else:
                return JsonResponse({"error": "Failed to initiate payment."}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)




@csrf_exempt
def payment_success(request):
    """
    Handles the success callback after payment is successful and creates the OpenStack instance.
    """
    tranId = request.GET.get('tranId')
    if not tranId:
        return HttpResponse("Transaction ID not provided.", status=400)

    ## Retrieve the instance based on the transaction ID
    instance = Instance.objects.filter(tranId=tranId).first()
    if not instance:
        return JsonResponse({"error": "Instance not found."}, status=404)

    ## Update the instance as paid and active
    instance.is_active = True
    instance.is_payment = True
    instance.save()

    ##! Call OpenStack instance creation service
    # created_instance = openstack.create_openstack_instance(
    #     user = request.user,
    #     project_name      = instance.project_name,
    #     instance_name     = instance.name,
    #     availability_zone = instance.zone,
    #     ram = instance.ram,
    #     cpu = instance.cpu,
    #     storage_type = instance.storage.split()[1],
    #     storage_size = instance.storage.split()[0],
    #     bandwidth    = instance.bandwidth,
    #     ip_type      = instance.ip
    # )

    created_instance = openstack.create_openstack_instance(user = request.user)

    if created_instance:
        return JsonResponse({"status": "Instance created successfully"})
    else:
        return JsonResponse({"error": "Failed to create OpenStack instance"}, status=500)






def payment_fail(request):
    return HttpResponse("<h1>Payment Fail</h1>")



def payment_cancel(request):
    return HttpResponse("<h1>Payment Cancel</h1>")




def payment_ipn(request):
    return HttpResponse("<h1>Payment IPN</h1>")



# class InitiatePaymentView(View):
#     def post(self, request, *args, **kwargs):
#         """
#         Handles the payment initiation and processes the response from the payment gateway.
#         If payment is successful, activates the instance and creates a new OpenStack instance.
#         """
#         user = request.user

#         try:
#             data = json.loads(request.body)

#             # Extract necessary fields from the request
#             project_name = data.get('project_name')
#             instence_name = data.get('instence_name')
#             availability_zone = data.get('availability_zone')
#             ram = data.get('ram')
#             cpu = data.get('cpu')
#             storage_type = data.get('storage_type')
#             storage_size = data.get('storage_size')
#             bandwidth = data.get('bandwidth')
#             ip_type = data.get('ip_type')
#             total_amount = data.get('total_amount')

#             # Retrieve the availability zone and create the instance
#             zone = AvailabilityZone.objects.filter(id=availability_zone).first()
#             if zone:
#                 ins = Instance.objects.create(
#                     user=user,
#                     name=instence_name,
#                     zone=zone,
#                     ram=ram,
#                     cpu=cpu,
#                     ip=ip_type,
#                     total=total_amount,
#                     project_name=project_name,
#                     description='Test Description',
#                     storage=f"{storage_size} {storage_type}",
#                     bandwidth=bandwidth,
#                 )

#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON data."}, status=400)

#         # Prepare payment data for SSLCommerz
#         payment_data = {
#             'total_amount': total_amount,
#             'currency'   : data.get("currency", "BDT"),
#             'order_id'   : data.get("order_id", "default_order_id"),
#             'success_url': request.build_absolute_uri(reverse('cloud:payment_success')),
#             'fail_url'   : request.build_absolute_uri(reverse('cloud:payment_failed')),
#             'cancel_url' : request.build_absolute_uri(reverse('cloud:payment_canceled')),
#             'ipn_url'    : request.build_absolute_uri(reverse('cloud:payment_ipn')),
#             'product_category': data.get("product_category", "Category"),
#             'product_name': data.get("product_name", "Product Name"),
#             'customer_info': {
#                 'name' : data["customer_info"].get("name", f"{user.first_name} {user.last_name}"),
#                 'email': data["customer_info"].get("email", user.email),
#                 'address1': data["customer_info"].get("address1", "Customer Address"),
#                 'city': data["customer_info"].get("city", "Dhaka"),
#                 'postcode': data["customer_info"].get("postcode", "1216"),
#                 'country' : data["customer_info"].get("country", "Bangladesh"),
#                 'phone'   : data["customer_info"].get("phone", user.phone if user.phone else "017XXXXXXXX"),
#             },
#         }

#         # Initiate payment session through SSLCommerz service function
#         response_data = sslcommerz.create_payment_session(payment_data)

#         # Handle response
#         if response_data.get("status") == "SUCCESS" and response_data.get("GatewayPageURL"):
#             return JsonResponse({"GatewayPageURL": response_data["GatewayPageURL"]})
#         else:
#             return JsonResponse({"error": "Failed to initiate payment."}, status=500)








# class InitiatePaymentView(View):
#     def post(self, request, *args, **kwargs):
#         user = request.user

#         try:
#             data = json.loads(request.body)

#             project_name = data.get('project_name')
#             instence_name = data.get('instence_name')
#             availability_zone = data.get('availability_zone')
#             ram = data.get('ram')
#             cpu = data.get('cpu')
#             storage_type = data.get('storage_type')
#             storage_size = data.get('storage_size')
#             bandwidth = data.get('bandwidth')
#             ip_type = data.get('ip_type')
#             total_amount = data.get('total_amount')

#             # print("----------------------------")
#             # print("project_name =", project_name)
#             # print("instence_name =", instence_name)
#             # print("availability_zone =", availability_zone)
#             # print("ram =", ram)
#             # print("cpu =", cpu)
#             # print("storage_type =", storage_type)
#             # print("storage_size =", storage_size)
#             # print("bandwidth =", bandwidth)
#             # print("ip_type =", ip_type)
#             # print("total_amount =", total_amount)
#             # print("----------------------------")

#             zone = AvailabilityZone.objects.filter(id = availability_zone).first()

#             if zone:
#                 ins = Instance.objects.create(
#                     user = user,
#                     name = instence_name,
#                     zone = zone,
#                     ram  = ram,
#                     cpu  = cpu,
#                     ip   = ip_type,
#                     total = total_amount,
#                     project_name = project_name,
#                     description  = 'Test Description',
#                     storage   = f"{storage_size} {storage_type}",
#                     bandwidth = bandwidth,
#                 )

#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON data."}, status=400)

#         sslcz = SSLCOMMERZ({
#             'store_id':   settings.SSLCOMMERZ_STORE_ID,
#             'store_pass': settings.SSLCOMMERZ_STORE_PASSWORD,
#             'issandbox':  settings.SSLCOMMERZ_SANDBOX_MODE
#         })

#         payment_data = {
#             'total_amount': str(Decimal(data.get("total_amount", "0"))),  
#             'currency': data.get("currency", "BDT"),
#             'tran_id' : data.get("order_id", "default_order_id"),

#             ## Set URLs for payment success, failure, and cancellation
#             'success_url': request.build_absolute_uri(reverse('cloud:payment_success')),
#             'fail_url'   : request.build_absolute_uri(reverse('cloud:payment_failed')),
#             'cancel_url' : request.build_absolute_uri(reverse('cloud:payment_canceled')),
#             'ipn_url'    : request.build_absolute_uri(reverse('cloud:payment_ipn')),

#             ## Set Product Info.
#             'product_category': data.get("product_category", "Category"),
#             'product_name': data.get("product_name", "Product Name"),

#             ## Set Customer Info from the authenticated user
#             'cus_name': data["customer_info"].get("name", f"{user.first_name} {user.last_name}"),
#             'cus_email': data["customer_info"].get("email", user.email),
#             'cus_add1': data["customer_info"].get("address1", "Customer Address"),  
#             'cus_city': data["customer_info"].get("city", "Dhaka"),
#             'cus_postcode': data["customer_info"].get("postcode", "1216"),
#             'cus_country': data["customer_info"].get("country", "Bangladesh"),
#             'cus_phone': data["customer_info"].get("phone", user.phone if user.phone else "017XXXXXXXX"),

#             'shipping_method': "NO",
#             'num_of_item': 1,
#             'product_profile': 'general',
#         }

#         response_data = sslcz.createSession(payment_data)


#         if response_data.get("status") == "SUCCESS" and response_data.get("GatewayPageURL"):
#             return JsonResponse({"GatewayPageURL": response_data["GatewayPageURL"]})
#         else:
#             return JsonResponse({"error": "Failed to initiate payment."}, status=500)