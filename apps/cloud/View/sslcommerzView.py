from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
# from sslcommerz_python.payment import SSLCSession
from sslcommerz_lib import SSLCOMMERZ 
from decimal import Decimal
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse

# class InitiatePaymentView(View):
#     def post(self, request, *args, **kwargs):

#         sslcz = SSLCOMMERZ(
#             store_id   = settings.SSLCOMMERZ_STORE_ID,
#             store_pass = settings.SSLCOMMERZ_STORE_PASSWORD,
#             sandbox    = settings.SSLCOMMERZ_SANDBOX_MODE
#         )

#         # Sample transaction data
#         order_id = "order_12345"  # Generate or get your order ID dynamically
#         total_amount = Decimal('100.50')  # Replace with the actual amount

#         # Set transaction info
#         sslcz.set_urls(
#             success_url = request.build_absolute_uri(reverse('payment_success')),
#             fail_url    = request.build_absolute_uri(reverse('payment_failed')),
#             cancel_url  = request.build_absolute_uri(reverse('payment_canceled')),
#             ipn_url     = request.build_absolute_uri(reverse('payment_ipn'))
#         )
        
#         sslcz.set_product_integration(
#             total_amount = total_amount,
#             currency     = 'BDT',
#             product_category ='Category',
#             product_name     = 'Product Name',
#             product_profile  = 'general'
#         )
        
#         # Set customer info (customize as needed)
#         sslcz.set_customer_info(
#             name  = 'Customer Name',
#             email = 'customer@example.com',
#             city  = 'Dhaka',
#             address1 = 'Customer Address',
#             postcode = '1216',
#             country  = 'Bangladesh',
#             phone = '017XXXXXXXX'
#         )

#         # Set shipping info if needed
#         sslcz.set_shipping_info(
#             shipping_method = 'Courier',
#             num_of_items    = 1,
#             shipping_address = 'Customer Address',
#             shipping_city    = 'Dhaka',
#             shipping_postcode = '1216',
#             shipping_country  = 'Bangladesh'
#         )
        
#         # Get the payment URL
#         response_data = sslcz.init_payment()
#         if response_data.get('status') == 'SUCCESS':
#             # Redirect user to SSLCommerz payment page
#             return redirect(response_data['GatewayPageURL'])
#         else:
#             # Handle errors (e.g., log the error, show an error message)
#             return JsonResponse({'error': 'Failed to initiate payment'}, status=500)



class InitiatePaymentView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST

        print("--------------------")
        print("OK")
        print("--------------------")

        # sslcz = SSLCOMMERZ(
        #     store_id   = settings.SSLCOMMERZ_STORE_ID,
        #     store_pass = settings.SSLCOMMERZ_STORE_PASSWORD,
        #     sandbox    = settings.SSLCOMMERZ_SANDBOX_MODE
        # )

        # # Use dynamic data from request payload
        # order_id = data.get("order_id", "default_order_id")
        # total_amount = Decimal(data.get("total_amount", "0"))

        # sslcz.set_urls(
        #     success_url = request.build_absolute_uri(reverse('payment_success')),
        #     fail_url    = request.build_absolute_uri(reverse('payment_failed')),
        #     cancel_url  = request.build_absolute_uri(reverse('payment_canceled')),
        #     ipn_url     = request.build_absolute_uri(reverse('payment_ipn'))
        # )
        
        # sslcz.set_product_integration(
        #     total_amount = total_amount,
        #     currency     = data.get("currency", "BDT"),
        #     product_category = data.get("product_category", "Category"),
        #     product_name     = data.get("product_name", "Product Name"),
        #     product_profile  = 'general'
        # )
        
        # sslcz.set_customer_info(
        #     name  = data.get("customer_info[name]", "Customer Name"),
        #     email = data.get("customer_info[email]", "customer@example.com"),
        #     city  = data.get("customer_info[city]", "Dhaka"),
        #     address1 = data.get("customer_info[address1]", "Customer Address"),
        #     postcode = data.get("customer_info[postcode]", "1216"),
        #     country  = data.get("customer_info[country]", "Bangladesh"),
        #     phone = data.get("customer_info[phone]", "017XXXXXXXX")
        # )

        # response_data = sslcz.init_payment()

        
        response_data = ''
        return JsonResponse(response_data)



def payment_success(request):
    return HttpResponse("<h1>Payment Success</h1>")

def payment_fail(request):
    return HttpResponse("<h1>Payment Fail</h1>")

def payment_cancel(request):
    return HttpResponse("<h1>Payment Cancel</h1>")

def payment_ipn(request):
    return HttpResponse("<h1>Payment IPN</h1>")