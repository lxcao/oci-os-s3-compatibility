import boto3
import pandas
import oci

# s3 = boto3.resource(
#  's3',
#     region_name="ap-singapore-1",
#     aws_access_key_id="c4d2291e091a04b311eb0108bd4ef856bca397af",
#     aws_secret_access_key="t0GrQupfWblJyi2IJg2FB/ik0GEQ2E4cEhc52kFAJD8=",
#     endpoint_url="https://ocichina001.compat.objectstorage.ap-singapore-1.oraclecloud.com"
# )

s3 = boto3.resource('s3',
aws_access_key_id="3a8514e8914a012e82981da14e61d637e7de0927",
aws_secret_access_key="mpJEZrtEIktndD5i6QDNHSTIhB8/cEkktdA5mG9+YmQ=",
region_name="ap-seoul-1",
endpoint_url="https://hktwlab.compat.objectstorage.ap-seoul-1.oraclecloud.com"
)


 
# oci.identity.IdentityClient.update_user(
#     user_id="ocid1.user.oc1..aaaaaaaafawx54qczcs5w6dtpfzjlcbewrczky3vixnds5tcsd5vlvfl3via",
#     update_user_details=oci.identity.models.UpdateUserDetails(
#         description="EXAMPLE-description-Value",
#         email="EXAMPLE-email-Value",
#         db_user_name="EXAMPLE-dbUserName-Value",
#         freeform_tags={
#             'EXAMPLE_KEY_zivYh': 'EXAMPLE_VALUE_yU5fdf6CzqKYAveVAMtZ'},
#         defined_tags={
#             'EXAMPLE_KEY_b1lHV': {
#                 'EXAMPLE_KEY_kVuKb': 'EXAMPLE--Value'}}))
# Print out bucket names
# for bucket in s3.buckets.all():
#  print(bucket.name)

# # Upload a File to you OCI Bucket, 2nd value is your bucket name 
# s3.meta.client.upload_file('/Users/caolingxin/Documents/workspaces/oci-projects/oci-os-s3-compatibility/assets/business-financial-data-mar-2022-quarter-csv.csv', 'bucket-20220501-1555', 'businessfinancialdatamar2022')

####################### List out available buckets ####################################
for bucket in s3.buckets.all():
    print (bucket.name)


##############   create S3 bucket /object storage ##########################
# s3.create_bucket(Bucket='bucket-20220720')
# for bucket in s3.buckets.all():
#     print (bucket.name)


# ###################### upload file #######################################
# with open('/Users/caolingxin/Documents/workspaces/oci-projects/oci-os-s3-compatibility/assets/wholesale-trade-survey-mar-2022-quarter-csv.csv', 'r') as f:
#     content = f.read()

# print(content)

# s3.meta.client.upload_file('/Users/caolingxin/Documents/workspaces/oci-projects/oci-os-s3-compatibility/assets/wholesale-trade-survey-mar-2022-quarter-csv.csv', 'bucket-20220720', 'wholesaletradesurveymar2022quarter')


# ########################### access file from s3 ##########################
s3_object = s3.Object('bucket-20220720', 'wholesaletradesurveymar2022quarter')

from io import StringIO

s3_data = StringIO(s3_object.get()['Body'].read().decode('utf-8'))

data = pandas.read_csv(s3_data)
print(data.head())

######################## Delete bucket / object storage #####################
#s3.delete_bucket(Bucket='bucket-20220720')