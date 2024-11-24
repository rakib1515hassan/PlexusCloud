import openstack
import os, requests, logging, time
from openstack import connection
from django.conf import settings

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

## Custom Import
from apps.cloud.enum import data
    

class CreateOpenstackInstance:
    def __init__(self):
        # Load OpenStack config from Django settings
        config                   = settings.OPENSTACK_CONFIG
        self.auth_url            = config["AUTH_URL"]
        self.compute_url         = config["COMPUTE_URL"]
        self.image_url           = config["IMAGE_URL"]
        self.network_url         = config["NETWORK_URL"]
        self.username            = config["USERNAME"]
        self.password            = config["PASSWORD"]
        self.project_id          = config["PROJECT_ID"]
        self.project_name        = config["PROJECT_NAME"]
        self.project_domain_name = config["PROJECT_DOMAIN_NAME"]
        self.user_domain_id      = config["USER_DOMAIN_ID"]

    def get_openstack_token(self):
        auth_payload = {
            "auth": {
                "identity": {
                    "methods": ["password"],
                    "password": {
                        "user": {
                            "name"     : self.username,
                            "domain"   : {"name": self.project_domain_name},
                            "password" : self.password,
                        }
                    },
                },
                "scope": {
                    "project": {
                        "id": self.project_id,
                        "name": self.project_name,
                        "domain": {"id": self.user_domain_id},
                    }
                },
            }
        }

        response = requests.post(
            self.auth_url,
            headers={"Content-Type": "application/json"},
            json=auth_payload,
        )

        if response.status_code == 201:
            return response.headers.get("X-Subject-Token")
        else:
            print("-----------------------")
            print("Error: ",response.content)
            print("-----------------------")
            raise Exception(f"Failed to obtain OpenStack token: {response.content.decode()}")



    def create_flavor(self, token, flavor_data):
        flavor_payload = {
            "flavor": {
                "name"  : flavor_data.get("name"),
                "ram"   : flavor_data.get("ram") * 1024,  ##* Convert GB to MB
                "vcpus" : flavor_data.get("cpu"),
                "disk"  : flavor_data.get("storage"),     ##* Disk size in GB
            }
        }

        response = requests.post(
            f"{self.compute_url}/flavors",
            headers={
                "X-Auth-Token": token,
                "Content-Type": "application/json",
            },
            json=flavor_payload,
        )

        if response.status_code in [200, 201]:
            return response.json()["flavor"]["id"]
        else:
            raise Exception(f"Failed to create flavor: {response.content.decode()}")



    def launch_instance(self, flavor_data):
        token = self.get_openstack_token()

        print("-----------------------")
        print("Token : {token}")
        print("-----------------------")

        images_response = requests.get(
            self.image_url,
            headers={"X-Auth-Token": token},
        )
        networks_response = requests.get(
            self.network_url,
            headers={"X-Auth-Token": token},
        )

        image_id   = None
        network_id = None

        if images_response.status_code == 200:
            images = images_response.json().get("images", [])
            if images:
                image_id = images[0]["id"]

        if networks_response.status_code == 200:
            networks = networks_response.json().get("networks", [])
            if networks:
                network_id = networks[0]["id"]

        if not image_id or not network_id:
            raise Exception("Could not retrieve image or network details.")

        flavor_id = self.create_flavor(token, flavor_data)

        openstack_payload = {
            "server": {
                "name"     : f"{flavor_data.get('user_name')}-instance",
                "flavorRef": flavor_id,
                "imageRef" : image_id,
                "networks" : [{"uuid": network_id}],
            }
        }

        response = requests.post(
            f"{self.compute_url}/servers",
            headers={
                "X-Auth-Token": token,
                "Content-Type": "application/json",
            },
            json=openstack_payload,
        )

        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to launch instance: {response.content.decode()}")










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

#     try:
#         # Connect to OpenStack using environment variables from RC file
#         auth_url     = os.getenv('OS_AUTH_URL')
#         project_name = os.getenv('OS_PROJECT_NAME')
#         username     = os.getenv('OS_USERNAME')
#         password     = os.getenv('OS_PASSWORD')
#         region_name  = os.getenv('OS_REGION_NAME')
#         user_domain_id    = os.getenv('OS_USER_DOMAIN_ID')
#         project_domain_id = os.getenv('OS_PROJECT_DOMAIN_ID')
#         interface         = os.getenv('OS_INTERFACE')
#         identity_api_version = os.getenv('OS_IDENTITY_API_VERSION')

#         # Get the IP address of the OpenStack controller
#         controller_ip = os.getenv('OS_AUTH_URL').split(':')[0]

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
#         image_id   = "53b6c85f-a26c-4df1-9210-a79b01f5589e"  
#         network_id = "753a7568-4735-441c-82fd-5be900c4be90" 
#         flavor_id  = "2933a574-16ae-421d-b839-915563a8aafc"

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

