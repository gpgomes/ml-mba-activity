import urllib.parse
import boto3
import pandas as pd

from datetime import datetime


def get_file_name(base_name):
    return datetime.now().strftime(f"%Y%m%d%H%M%S-{base_name}")


def create_structured_file(json_content):
    file_name = get_file_name('titanic.csv')
    local_csv_file = f'/tmp/{file_name}'

    df = pd.DataFrame(eval(json_content))
    df.to_csv(local_csv_file, index=False)
    bucket_name = 'titanic-pipeline-structured-files'

    s3 = boto3.resource("s3")
    s3.meta.client.upload_file(local_csv_file, bucket_name, file_name)


def lambda_handler(event, context):
    s3_client = boto3.resource('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        object = s3_client.Object(bucket, key)
        file_content = object.get()['Body'].read()
        create_structured_file(file_content)
        return 'SUCCESS'
    except Exception as e:
        print(e)
        print(f'Error getting object {key} from bucket {bucket}.')
        raise e