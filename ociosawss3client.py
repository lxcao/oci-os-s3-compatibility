import boto3
import pandas

# create s3 client
s3 = boto3.client('s3',
aws_access_key_id="3a8514e8914a012e82981da14e61d637e7de0927",
aws_secret_access_key="mpJEZrtEIktndD5i6QDNHSTIhB8/cEkktdA5mG9+YmQ=",
region_name="ap-seoul-1",
endpoint_url="https://hktwlab.compat.objectstorage.ap-seoul-1.oraclecloud.com"
)

###########################list buckets##############################################
print("########################list_buckets######################################")
for bucket in s3.list_buckets()['Buckets']:
    print(f'{bucket["Name"]}')
print("########################put_object######################################")
s3.put_object(
    Body=open('/Users/caolingxin/Documents/workspaces/oci-projects/oci-os-s3-compatibility/assets/wholesale-trade-survey-mar-2022-quarter-csv.csv', 'rb'),
    Bucket='bucket-20220722',
    Key='wholesaletradesurveymar2022quarter6',
)
print("########################list_objects######################################")
for object in s3.list_objects(Bucket='bucket-20220722')['Contents']:
    print(f'{object["Key"]}')
print("########################list_objects_v2###################################")
for object in s3.list_objects_v2(Bucket='bucket-20220722')['Contents']:
    print(f'{object["Key"]}')
print("########################get_object###################################")
from io import StringIO
s3_data = StringIO(s3.get_object(Bucket='bucket-20220722',Key='wholesaletradesurveymar2022quarter6')['Body'].read().decode('utf-8'))
data = pandas.read_csv(s3_data)
print(data.head())




