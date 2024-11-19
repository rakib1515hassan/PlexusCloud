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
                            "name": self.username,
                            "domain": {"name": self.project_domain_name},
                            "password": self.password,
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



