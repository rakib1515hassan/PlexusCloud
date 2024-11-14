from sslcommerz_lib import SSLCOMMERZ
from django.conf import settings
from decimal import Decimal
import uuid

# sslcommerz service function
def create_payment_session(data):
    """
    Creates a payment session with SSLCommerz and returns the response.
    """
    sslcz = SSLCOMMERZ({
        'store_id'  : settings.SSLCOMMERZ_STORE_ID,
        'store_pass': settings.SSLCOMMERZ_STORE_PASSWORD,
        'issandbox' : settings.SSLCOMMERZ_SANDBOX_MODE
    })

    payment_data = {
        ##? Define Basic Information
        'total_amount': str(Decimal(data.get("total_amount", "0"))),
        'currency': data.get("currency", "BDT"),
        'tran_id' : data.get("order_id"),

        ##? Define URL's
        'success_url': data.get("success_url"),
        'fail_url'   : data.get("fail_url"),
        'cancel_url' : data.get("cancel_url"),
        'ipn_url'    : data.get("ipn_url"),

        ##? Define Product Information
        'product_category': data.get("product_category", "Category"),
        'product_name': data.get("product_name", "Product Name"),

        ##? Define Customer Information
        'cus_name' : data["customer_info"].get("name"),
        'cus_email': data["customer_info"].get("email"),
        'cus_add1' : data["customer_info"].get("address1", "Customer Address"),
        'cus_city' : data["customer_info"].get("city", "Dhaka"),
        'cus_postcode': data["customer_info"].get("postcode", "1216"),
        'cus_country' : data["customer_info"].get("country", "Bangladesh"),
        'cus_phone'   : data["customer_info"].get("phone"),

        ##? Define Shipping Information
        'shipping_method' : "NO",
        'num_of_item'     : 1,
        'product_profile' : 'general',
    }

    return sslcz.createSession(payment_data)
