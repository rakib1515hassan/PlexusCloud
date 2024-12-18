import openstack

# Initialize connection
conn = openstack.connect(
    auth_url          = "http://your_openstack_auth_url",
    project_name      = "your_project_name",
    username          = "your_username",
    password          = "your_password",
    region_name       = "your_region_name",
    user_domain_id    = "your_user_domain_id",
    project_domain_id = "your_project_domain_id",
)

# Instance parameters
image_name    = "your_image_name"            # Name of the image to use
flavor_name   = "your_flavor_name"           # Name of the flavor, or create a new one below
network_name  = "your_network_name"          # Network to connect the instance to
instance_name = "your_instance_name"         # Name of the new instance
fixed_ip      = "your_preferred_ip_address"  # Specify a preferred IP address, if available
security_group_name = "your_security_group"  # Optional security group
keypair_name  = "your_keypair_name"          # Optional keypair for SSH access





#! 1. Find the image and network
image   = conn.compute.find_image(image_name)
network = conn.network.find_network(network_name)





##! 2. Create or find the flavor with the desired CPU and RAM settings
# You can create a custom flavor if needed
desired_vcpus = 2    # Number of vCPUs
desired_ram   = 4096 # RAM in MB (e.g., 4096MB = 4GB)
desired_disk  = 20   # Disk size in GB

flavor = conn.compute.find_flavor(flavor_name)
if not flavor:
    flavor = conn.compute.create_flavor(
        name  = flavor_name,
        ram   = desired_ram,
        vcpus = desired_vcpus,
        disk  = desired_disk,
    )
    print(f"Custom flavor '{flavor_name}' created with {desired_vcpus} vCPUs, {desired_ram}MB RAM, and {desired_disk}GB disk.")





##! 3. Create a port with a specific IP address (optional)
port = conn.network.create_port(
    network_id = network.id,
    fixed_ips  = [{"ip_address": fixed_ip}]
)




##! 4. Create the instance with the specified configurations
server = conn.compute.create_server(
    name      = instance_name,
    image_id  = image.id,
    flavor_id = flavor.id,
    networks  = [{"port": port.id}],
    key_name  = keypair_name,
    security_groups = [{"name": security_group_name}],
)




## Wait until the server is active
server = conn.compute.wait_for_server(server)
print(f"Instance '{instance_name}' created successfully with ID: {server.id} and IP: {fixed_ip}")
