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
create_preauthenticated_request_response = object_storage_client.create_preauthenticated_request(
    namespace_name="ocichina001",
    bucket_name="bucket-20220501-1555",
    create_preauthenticated_request_details=oci.object_storage.models.CreatePreauthenticatedRequestDetails(
        name="par-ds-ads-dataset-iris",
        access_type="ObjectReadWrite",
        time_expires=datetime.strptime(
            "2043-03-01T02:20:55.385Z",
            "%Y-%m-%dT%H:%M:%S.%fZ"),
        bucket_listing_action="Deny",
        object_name="ds/ads/dataset/iris.csv"),
    #opc_client_request_id="ocid1.test.oc1..<unique_ID>EXAMPLE-opcClientRequestId-Value"
    )

# Get the data from response
print(create_preauthenticated_request_response.data)