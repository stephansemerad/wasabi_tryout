import os
import boto3

WASABI_ENDPOINT     = 'https://s3.wasabisys.com'
WASABI_ACCESS_KEY   = 'XXXXXXXXXXXXXXXXXXXX'
WASABI_SECRET_KEY   = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
WASABI_BUCKET       = 'XXX'

s3                  = boto3.client('s3', endpoint_url=WASABI_ENDPOINT, aws_access_key_id=WASABI_ACCESS_KEY, aws_secret_access_key=WASABI_SECRET_KEY)
list_buckets        = s3.list_buckets()


# Create s3 Bucket if not Exists
if list_buckets['Buckets'] ==[]:
    s3 = boto3.resource('s3', endpoint_url = 'https://s3.wasabisys.com',aws_access_key_id =WASABI_ACCESS_KEY,aws_secret_access_key = WASABI_SECRET_KEY)
    s3.create_bucket(Bucket=WASABI_BUCKET)


# Upload an Image to the Bucket and make it Public.
s3                  = boto3.client('s3', endpoint_url=WASABI_ENDPOINT, aws_access_key_id=WASABI_ACCESS_KEY, aws_secret_access_key=WASABI_SECRET_KEY)
list_buckets        = s3.list_buckets()
buckets             = list_buckets['Buckets']

path                = r'C:\Users\stephan\Desktop\wasabi_file_upload_test'
file_name           = 'test.png'
file_path           = os.path.join(path, file_name)
body                = open(file_path, 'rb')
s3.put_object(Bucket=WASABI_BUCKET, Key='imgs/'+file_name, Body=body, ACL='public-read')
body.close()

# Public Image 
url = 's3.wasabisys.com/aureusauction/imgs/test.png'

# creating a file
file_name   =  'test.txt'
file        = open(file_name, "w") 
file.write("Hello World!") 
file.close()

# Upload the file to S3
s3.upload_file(file_name, WASABI_BUCKET, file_name, ExtraArgs={'ACL':'public-read'})

# Download the file from S3
s3.download_file(WASABI_BUCKET, file_name, 'downloaded_'+file_name)

# Show if it worked :) 
print(open('downloaded_'+file_name).read())
