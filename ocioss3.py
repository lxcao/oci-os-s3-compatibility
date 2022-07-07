import boto3

s3 = boto3.resource(
 's3',
 region_name="ap-singapore-1",
 aws_secret_access_key="**************",
 aws_access_key_id="****************************************",
 endpoint_url="https://ocichina001.compat.objectstorage.ap-singapore-1.oraclecloud.com"
)
 
# Print out bucket names
for bucket in s3.buckets.all():
 print(bucket.name)
# Upload a File to you OCI Bucket, 2nd value is your bucket name 
s3.meta.client.upload_file('/Users/caolingxin/Documents/workspaces/oci-projects/oci-os-s3-compatibility/assets/currybeef.mp4', 'bucket-20220501-1555', 'currybeeffroms3')