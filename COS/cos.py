import ibm_boto3
from ibm_botocore.client import Config

# IBM Cloud Object Storage credentials
cos_credentials = {
    "access_key_id": "37ac8527e8034eb48bcc5183ca52f307",
    "secret_access_key": "ef4781ef09a662980bbdc5480429ded92be02b8acc57e364",
    "endpoint_url": "https://s3.us-east.cloud-object-storage.appdomain.cloud"
}

cos_client = ibm_boto3.client(
    "s3",
    aws_access_key_id=cos_credentials["access_key_id"],
    aws_secret_access_key=cos_credentials["secret_access_key"],
    endpoint_url=cos_credentials["endpoint_url"],
    config=Config(signature_version="s3v4"),
)

bucket_name = "somebucket-for-interview"
file_name = "README.md"
local_file_path = "README.md"

try:
    cos_client.download_file(bucket_name, file_name, local_file_path)
    print(f"File '{file_name}' downloaded successfully!")
except Exception as e:
    print(f"Error: {e}")
