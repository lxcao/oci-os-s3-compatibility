import oci
from datetime import datetime

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file(profile_name="specialist2-4sdk")


# Initialize service client with default config file
object_storage_client = oci.object_storage.ObjectStorageClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_preauthenticated_requests_response = object_storage_client.list_preauthenticated_requests(
    namespace_name="ocichina001",
    bucket_name="bucket-20220501-1555",
    #object_name_prefix="EXAMPLE-objectNamePrefix-Value",
    #limit=673,
    #page="EXAMPLE-page-Value",
    )

# Get the data from response
print(list_preauthenticated_requests_response.data)
