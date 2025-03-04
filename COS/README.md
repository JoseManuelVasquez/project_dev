# COS

Connect to a Bucket and download a file using your favorite language.

The information you need to get the file is the following:

```
bucket name: somebucket-for-interview
bucket location: United States - Washington DC
filename: README.md


{
    "apikey": "TSVin6SwAzb9Cg2cL_pYLXDvmMuIuh42VhuFfjuWe8oQ",
    "cos_hmac_keys": {
        "access_key_id": "37ac8527e8034eb48bcc5183ca52f307",
        "secret_access_key": "ef4781ef09a662980bbdc5480429ded92be02b8acc57e364"
    },
    "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
    "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:cloud-object-storage:global:a/90f4ad63175d479a84ee05b5445012dd:7bfbe08e-c4c2-4231-a36f-28e027577860:resource-key:37ac8527-e803-4eb4-8bcc-5183ca52f307",
    "iam_apikey_id": "ApiKey-c5854c91-78d9-4635-bc52-95b4536ce736",
    "iam_apikey_name": "reader-creds",
    "iam_role_crn": "crn:v1:bluemix:public:cloud-object-storage::::serviceRole:ContentReader",
    "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/90f4ad63175d479a84ee05b5445012dd::serviceid:ServiceId-058e100a-cae0-46dc-976e-ade69620771c",
    "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/90f4ad63175d479a84ee05b5445012dd:7bfbe08e-c4c2-4231-a36f-28e027577860::"
}

```


**Note: the file contains a password to extract zip file for exercise 3 (Kubernetes)