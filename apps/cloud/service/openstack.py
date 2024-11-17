import openstack


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
        conn = openstack.connect(
            auth_url     = "http://103.131.144.53:5000/v3",
            project_name = "admin",
            username     = "user_iaas1",
            password     = "3BcdK4b=",
            region_name  = "RegionOne",
            user_domain_id    = "default",
            project_domain_id = "default",
            timeout = 60,
        )

        image_id   = "53b6c85f-a26c-4df1-9210-a79b01f5589e"  
        network_id = "753a7568-4735-441c-82fd-5be900c4be90" 
        
        flavor = {
            "ram": ram_info,
            "cpu": cpu_info
        }

        ## List all flavors available
        flavors = conn.compute.flavors()

        ## Find the flavor that matches the required RAM and CPU
        selected_flavor = None
        for flavor in flavors:
            if flavor.ram == ram_info and flavor.vcpus == cpu_info:
                selected_flavor = flavor
                break

        if selected_flavor:
            flavor_id = selected_flavor.id
        else:
            ## Handle case where no matching flavor is found (e.g., use default flavor)
            flavor_id = "m1.small"  ## Or a fallback flavor


        metadata = {
            "project_name" : project_name,
            "user" : user.email,               ## Use the user's email as metadata
            "ram"  : str(ram_info) + " MB",    ## Store the RAM size as metadata
            "cpu"  : str(cpu_info) + " vCPUs", ## Store the CPU count as metadata
            "storage"     : f"{storage_size} {storage_type}",  ## Store the storage size and type
            "bandwidth"   : bandwidth,         ## Store the bandwidth
            "ip_type"     : "private",         ## Store the IP type (e.g., public or private)
            "environment" : "development",     ## Store environment info (e.g., production, development)
            "deployment_type": "standard",     ## Define the type of deployment
            "instance_tag"   : "web-server",   ## Custom tag for categorizing the server
            "created_by"     : user.email      ## Store the username of the person who created the server
        }

        ## Now use `flavor_id` when creating the server
        instance = conn.compute.create_server(
            name     = instance_name,
            flavor   = flavor_id,   ## Use the dynamically selected flavor
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

