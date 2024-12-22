import boto3
import time

# S3 업로드 함수
def upload_to_s3(file_name, bucket_name, object_name=None):
    s3_client = boto3.client('s3', region_name="us-east-1")
    if object_name is None:
        object_name = file_name
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"{file_name} successfully uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Failed to upload {file_name}: {e}")

# CloudWatch 로그 함수
def log_to_cloudwatch(log_group, log_stream, message):
    client = boto3.client('logs', region_name="us-east-1")
    try:
        response = client.describe_log_streams(logGroupName=log_group, logStreamNamePrefix=log_stream)
        stream = response['logStreams'][0]
        sequence_token = stream.get('uploadSequenceToken', None)

        log_event = {
            'logGroupName': log_group,
            'logStreamName': log_stream,
            'logEvents': [
                {
                    'timestamp': int(round(time.time() * 1000)),
                    'message': message,
                }
            ]
        }
        if sequence_token:
            log_event['sequenceToken'] = sequence_token
        client.put_log_events(**log_event)
        print(f"Logged to {log_group}/{log_stream}: {message}")
    except Exception as e:
        print(f"Failed to log to CloudWatch: {e}")
