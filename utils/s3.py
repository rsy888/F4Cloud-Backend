import sys

import boto3

from f4cloud.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

# S3 기존 설정
s3client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


# 파일 업로드
def upload_file(bucket, target, file_name):
    try:
        response = s3client.put_object(
            Bucket=bucket,
            Key=file_name,
            Body=target,
            ACL='public-read'
        )
        return response
    except Exception as e:
        print('Error on line {}'.format(
            sys.exc_info()[-1].tb_lineno), type(e).__name__, e
        )
        raise Exception('Upload Fail', e)


# 파일 삭제
def delete_file(bucket, target):
    try:
        response = s3client.delete_object(Bucket=bucket, Key=target)
        return response
    except Exception as e:
        print('Error on line {}'.format(
            sys.exc_info()[-1].tb_lineno), type(e).__name__, e
        )
        raise Exception('Delete Fail', e)


# 파일 이름 변경
def rename_file(bucket, target, new_name):
    try:
        s3client.copy_object(Bucket=bucket, Key=new_name, CopySource={
            'Bucket': bucket, 'Key': target
        }, ACL='public-read')
        s3client.delete_object(Bucket=bucket, Key=target)
    except Exception as e:
        print('Error on line {}'.format(
            sys.exc_info()[-1].tb_lineno), type(e).__name__, e
        )
        raise Exception('Rename Fail', e)


# 파일 복사
def copy_file(bucket, target, copy_name):
    try:
        s3client.copy_object(Bucket=bucket, Key=copy_name, CopySource={
            'Bucket': bucket, 'Key': target
        }, ACL='public-read')
    except Exception as e:
        print('Error on line {}'.format(
            sys.exc_info()[-1].tb_lineno), type(e).__name__, e
        )
        raise Exception('Copy Fail', e)
