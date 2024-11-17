import os
from dotenv import load_dotenv

# Load .env file variables into environment
load_dotenv()

# Now you can access the OpenStack credentials from the environment
OS_AUTH_URL = os.getenv("OS_AUTH_URL")
OS_PROJECT_NAME = os.getenv("OS_PROJECT_NAME")
OS_USERNAME = os.getenv("OS_USERNAME")
OS_PASSWORD = os.getenv("OS_PASSWORD")
OS_PROJECT_DOMAIN_ID = os.getenv("OS_PROJECT_DOMAIN_ID")
OS_USER_DOMAIN_ID = os.getenv("OS_USER_DOMAIN_ID")
OS_REGION_NAME = os.getenv("OS_REGION_NAME")
OS_INTERFACE = os.getenv("OS_INTERFACE")
OS_IDENTITY_API_VERSION = os.getenv("OS_IDENTITY_API_VERSION")
