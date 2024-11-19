import openstack
import os
from openstack import connection
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



# def create_openstack_instance(user):
#     project_name  = "Test Project"
#     instance_name = "Test Instance"
#     availability_zone = "Dhaka"
#     storage_type = "SSD"
#     storage_size = 500    ## GB
#     bandwidth    = 10     ## MB
#     ip_type      = "IPv4" ## IPv4 or IPv6
#     ram_info     = 4096   ## In MB
#     cpu_info     = 4      ## Number of vCPUs

#     # print("-----------------------")
#     # print("Auth url =", os.getenv('OS_AUTH_URL'))
#     # print("-----------------------")

#     try:
#         # Connect to OpenStack using environment variables from RC file
#         # auth_url = os.getenv('OS_AUTH_URL')
#         auth_url = 'http://103.131.144.153:5000/v3/'
#         project_name = os.getenv('OS_PROJECT_NAME')
#         username = os.getenv('OS_USERNAME')
#         password = os.getenv('OS_PASSWORD')
#         region_name = os.getenv('OS_REGION_NAME')
#         user_domain_id = os.getenv('OS_USER_DOMAIN_ID')
#         project_domain_id = os.getenv('OS_PROJECT_DOMAIN_ID')
#         interface = os.getenv('OS_INTERFACE')
#         identity_api_version = os.getenv('OS_IDENTITY_API_VERSION')

#         # Get the IP address of the OpenStack controller
#         # controller_ip = os.getenv('OS_AUTH_URL').split(':')[1]

#         print("-----------------------")
#         print("controller_ip =", auth_url)
#         print("-----------------------")

#         # Create OpenStack connection with retry logic
#         conn = None
#         max_retries = 5
#         retry_delay = 2

#         for attempt in range(max_retries):
#             try:
#                 conn = connection.Connection(
#                     auth_url=auth_url,
#                     project_name=project_name,
#                     username=username,
#                     password=password,
#                     region_name=region_name,
#                     user_domain_id=user_domain_id,
#                     project_domain_id=project_domain_id,
#                     interface=interface,
#                     identity_api_version=identity_api_version,
#                     debug=True
#                 )
                
#                 # Test the connection by getting flavors
#                 conn.compute.flavors()
                
#                 break
#             except Exception as e:
#                 logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
#                 time.sleep(retry_delay)

#         if conn is None:
#             raise Exception("Failed to connect to OpenStack after multiple attempts")

#         # Example image and network IDs (ensure these are correct)
#         # image_id   = "53b6c85f-a26c-4df1-9210-a79b01f5589e"
#         image_id   = "8d454ddc-3e88-4396-acd5-76fff71e8807"
#         network_id = "753a7568-4735-441c-82fd-5be900c4be90"

#         flavor = {
#             "ram": ram_info,
#             "cpu": cpu_info
#         }

#         # Get available flavors and find the best match
#         flavors = conn.compute.flavors()
#         selected_flavor = None
#         for flavor in flavors:
#             if flavor.ram == ram_info and flavor.vcpus == cpu_info:
#                 selected_flavor = flavor
#                 break

#         if selected_flavor:
#             flavor_id = selected_flavor.id
#         else:
#             flavor_id = "m1.small"  # Fallback flavor

#         metadata = {
#             "project_name" : project_name,
#             "user" : user.email,  
#             "ram"  : f"{ram_info} MB",
#             "cpu"  : f"{cpu_info} vCPUs",
#             "storage"     : f"{storage_size} {storage_type}",
#             "bandwidth"   : bandwidth,
#             "ip_type"     : "private",
#             "environment" : "development",
#             "deployment_type": "standard",
#             "instance_tag"   : "web-server",
#             "created_by"     : user.email
#         }

#         # Create the server
#         instance = conn.compute.create_server(
#             name     = instance_name,
#             flavor   = flavor_id,
#             image    = image_id,
#             networks = [{"uuid": network_id}],
#             availability_zone = availability_zone,
#             metadata = metadata
#         )

#         # Wait for the server to become active
#         instance = conn.compute.wait_for_server(instance, wait=600)  # Wait for up to 10 minutes

#         return instance

#     except Exception as e:
#         logger.error(f"Failed to create OpenStack instance: {str(e)}")
#         return None









def create_openstack_instance(user):

    project_name  = "Test Project"
    instance_name = "Test Instance"
    availability_zone = "Dhaka"
    storage_type = "SSD"
    storage_size = 500    ## GB
    bandwidth    = 10     ## MB
    ip_type      = "IPv4" ## IPv4 or IPv6
    ram_info     = 4096   ## In MB
    cpu_info     = 4      ## Number of vCPUs


    try:
        ## Connect to OpenStack
        conn = connection.Connection(
                auth_url='http://103.131.144.153:5000/v3/',
                project_name="IAAS-PROJECT-1",
                username="user_iaas1",
                password="3BcdK4b=",
                region_name="RegionOne",
                user_domain_name="Default",  
                project_domain_name="Default",  
                interface="public",
                identity_api_version=3,
                debug=True,
            )

        image_id   = "53b6c85f-a26c-4df1-9210-a79b01f5589e"  
        network_id = "753a7568-4735-441c-82fd-5be900c4be90" 
        flavor_id  = "2933a574-16ae-421d-b839-915563a8aafc"
        
       
        metadata = {
            "project_name" : project_name,
            "user" : "rakib1515hassan@gmail.com",              
            "ram"  : str(ram_info) + " MB",   
            "cpu"  : str(cpu_info) + " vCPUs", 
            "storage"     : f"{storage_size} {storage_type}",  
            "bandwidth"   : bandwidth,         
            "ip_type"     : "private",         
            "environment" : "development",     
            "deployment_type": "standard",     
            "instance_tag"   : "web-server",  
            "created_by"     : "rakib1515hassan@gmail.com"     
        }

        ## Now use `flavor_id` when creating the server
        instance = conn.compute.create_server(
            name     = instance_name,
            flavor   = flavor_id, 
            image    = image_id,    ## Use the image ID
            networks = [{"uuid": network_id}],      ## Use the network ID
            availability_zone = availability_zone,  ## Use the availability zone
            metadata = metadata     ## Optional: add metadata
        )

        ## Wait for the server to become active
        instance = conn.compute.wait_for_server(instance)

        return instance  ## Return the instance details once created

    except Exception as e:
        ## Log any errors that occur
        print(f"Failed to create OpenStack instance: {e}")
        return None

