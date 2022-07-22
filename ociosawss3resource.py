import boto3
import pandas

# create s3 resource
s3 = boto3.resource('s3',
aws_access_key_id="3a8514e8914a012e82981da14e61d637e7de0927",
aws_secret_access_key="mpJEZrtEIktndD5i6QDNHSTIhB8/cEkktdA5mG9+YmQ=",
region_name="ap-seoul-1",
endpoint_url="https://hktwlab.compat.objectstorage.ap-seoul-1.oraclecloud.com"
)

####################### List out available buckets ####################################
# for bucket in s3.buckets.all():
#     print (bucket.name)


##############   create S3 bucket ##########################
bucket = s3.Bucket('bucket-20220722')
#bucket.create()

# for bucket in s3.buckets.all():
#     print (bucket.name)

################# list objects in bucket ###############################
for object in bucket.objects.all():
    print(object.key)


###################### upload file ####################################
object = s3.Object('bucket-20220722','wholesaletradesurveymar2022quarter')
object.put(Body=open('/Users/caolingxin/Documents/workspaces/oci-projects/oci-os-s3-compatibility/assets/wholesale-trade-survey-mar-2022-quarter-csv.csv', 'rb'))

for object in bucket.objects.all():
    print(object.key)

object.get()['Body'].read().decode('utf-8')