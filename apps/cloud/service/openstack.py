# utils/openstack_utils.py
import openstack

def create_openstack_instance(user, project_name, instance_name, availability_zone, ram, cpu, storage_type, storage_size, bandwidth, ip_type):
    try:

        conn = openstack.connect(
            auth_url     = "http://103.131.144.53:5000",
            project_name = "admin",
            username     = "user_iaas1",
            password     = "3BcdK4b=",
            region_name  = "RegionOne",
            user_domain_id    = "default",
            project_domain_id = "default",
        )

        # Assuming `conn` is the OpenStack connection
        instance = conn.compute.create_server(
            name=instance_name,
            flavor={
                "ram": ram,
                "cpu": cpu
            },
            image="image_id",  # Replace with actual image ID
            network="network_id",  # Replace with actual network ID
            availability_zone=availability_zone,
            metadata={
                "project_name": project_name,
                "user": user.username,
                "storage": f"{storage_size} {storage_type}",
                "bandwidth": bandwidth,
                "ip_type": ip_type,
            }
        )

        # Wait for the instance to be active
        instance = conn.compute.wait_for_server(instance)

        return instance  # Return instance details

    except Exception as e:
        # Log and handle any OpenStack connection errors
        print(f"Failed to create OpenStack instance: {e}")
        return None




# def create_openstack_instance(instance):
#     """
#     Creates an OpenStack instance using the specified details from the Django instance model.
#     """
#     conn = openstack.connect(
#         auth_url="http://your_openstack_auth_url",
#         project_name="your_project_name",
#         username="your_username",
#         password="your_password",
#         region_name="your_region_name",
#         user_domain_id="your_user_domain_id",
#         project_domain_id="your_project_domain_id",
#     )

#     # Find the image, flavor, and network for the server
#     image = conn.compute.find_image('your_image_name')  # Replace with actual image name
#     flavor = conn.compute.find_flavor('your_flavor_name')  # Replace with actual flavor name
#     network = conn.network.find_network('your_network_name')  # Replace with actual network name

#     # Create the server with specified configurations
#     server = conn.compute.create_server(
#         name=instance.name,
#         image_id=image.id,
#         flavor_id=flavor.id,
#         networks=[{"uuid": network.id}],
#         key_name='your_keypair_name'  # Optional: Specify SSH keypair if needed
#     )

#     # Wait until the server is active
#     conn.compute.wait_for_server(server)
#     print(f"OpenStack instance '{server.name}' created with ID: {server.id}")































# import openstack

# # Initialize connection
# conn = openstack.connect(
#     auth_url="http://your_openstack_auth_url",
#     project_name="your_project_name",
#     username="your_username",
#     password="your_password",
#     region_name="your_region_name",
#     user_domain_id="your_user_domain_id",
#     project_domain_id="your_project_domain_id",
# )

# # Instance parameters
# image_name = "your_image_name"       # Name of the image to use
# flavor_name = "your_flavor_name"      # Name of the flavor, or create a new one below
# network_name = "your_network_name"    # Network to connect the instance to
# instance_name = "your_instance_name"  # Name of the new instance
# fixed_ip = "your_preferred_ip_address"  # Specify a preferred IP address, if available
# security_group_name = "your_security_group"  # Optional security group
# keypair_name = "your_keypair_name"    # Optional keypair for SSH access

# # 1. Find the image and network
# image = conn.compute.find_image(image_name)
# network = conn.network.find_network(network_name)

# # 2. Create or find the flavor with the desired CPU and RAM settings
# # You can create a custom flavor if needed
# desired_vcpus = 2   # Number of vCPUs
# desired_ram = 4096  # RAM in MB (e.g., 4096MB = 4GB)
# desired_disk = 20   # Disk size in GB

# flavor = conn.compute.find_flavor(flavor_name)
# if not flavor:
#     flavor = conn.compute.create_flavor(
#         name=flavor_name,
#         ram=desired_ram,
#         vcpus=desired_vcpus,
#         disk=desired_disk,
#     )
#     print(f"Custom flavor '{flavor_name}' created with {desired_vcpus} vCPUs, {desired_ram}MB RAM, and {desired_disk}GB disk.")

# # 3. Create a port with a specific IP address (optional)
# port = conn.network.create_port(
#     network_id=network.id,
#     fixed_ips=[{"ip_address": fixed_ip}]
# )

# # 4. Create the instance with the specified configurations
# server = conn.compute.create_server(
#     name=instance_name,
#     image_id=image.id,
#     flavor_id=flavor.id,
#     networks=[{"port": port.id}],
#     key_name=keypair_name,
#     security_groups=[{"name": security_group_name}],
# )

# # Wait until the server is active
# server = conn.compute.wait_for_server(server)
# print(f"Instance '{instance_name}' created successfully with ID: {server.id} and IP: {fixed_ip}")
