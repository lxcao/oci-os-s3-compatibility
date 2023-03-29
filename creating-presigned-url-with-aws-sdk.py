import boto3
s3 = boto3.client(
        's3',
        region_name = 'ap-singapore-1',
        aws_access_key_id = '10258e471005511474a465fd46bab0c7c830b19e',
        aws_secret_access_key = 'HUs1qDNgfRUgOsvyEemo1CcQ++Hd6C09z38OvrP1+ZY=',
        endpoint_url = 'https://ocichina001.compat.objectstorage.ap-singapore-1.oraclecloud.com'
)

url = s3.generate_presigned_url(
        'get_object',
        Params = {'Bucket': 'bucket-20220501-1555', 'Key': 'ds/ads/dataset/iris.csv'},
        ExpiresIn = 3600)
print('URL: ' + url)

post = s3.generate_presigned_post('bucket-20220501-1555', 
                                  'ds/ads/dataset/iris.csv', 
                                  Fields=None, 
                                  Conditions=None, 
                                  ExpiresIn=3600)
print('POST URL: ' + post['url'])