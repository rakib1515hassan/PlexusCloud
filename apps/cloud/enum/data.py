from enum import Enum


class InstanceData(Enum):
    PROJECT_NAME  = "Test Project"
    PROJECTID     = "bbf9956cfdde42f28e125f1ebbe995fc"

    INSTANCE_NAME = "Test Instance"
    REGION_NAME   = "RegionOne"

    USERNAME      = "user_iaas2"
    PASSWORD      = "4V4z2fG#"

    PROJECTDOMAIN     = "Default"
    PROJECT_DOMAIN_ID = "default"

    NETWORK_NAME = "private"
    SUBNET_NAME  = "private_subnet"

    SECRET_NAME       = "secret_key"
    SECRET_NAMESPACE  = "default"
    SECRET_CONTENT    = "This is a secret key"
    SECRET_PROJECT_ID = "bbf9956cfdde42f28e125f1ebbe995fc"

    IMAGE_NAME   = "ubuntu-18.04-server-amd64"
    IMAGE_ID     = "84550540-752b-4565-b19b-997a6d9c7764"

    FLOATING_IP_POOL_NAME = "floating_ip_pool"
    FLOATING_IP_POOL_ID   = "55828601-c38c-4758-83c3-2825999063a8"

    KEYPAIR_NAME = "my_keypair"
    KEYPAIR_ID   = "9677a4c1-5812-4b7c-88c6-4947b04750c9"

    SUBNET_RANGE = "192.168.0.0/24"

    VOLUME_TYPE = "SSD"
    VOLUME_NAME = "my_volume"
    VOLUME_ID   = "99a7725a-9190-4778-893c-10095806f569"
    VOLUME_SNAPSHOT_NAME = "my_volume_snapshot"
    VOLUME_SNAPSHOT_ID   = "686b528a-3895-40d9-8c43-8d8d1774f974"
    VOLUME_SNAPSHOT_PROJECT_ID  = "bbf9956cfdde42f28e125f1ebbe995fc"
    FLOATING_IP_POOL_PROJECT_ID = "bbf9956cfdde42f28e125f1ebbe995fc"