import boto3
import datetime

def lambda_handler(event, context):
    print("=== Starting S3 Cleanup ===")

    # Configuration
    bucket_name = "lambda-s3-cleanup-demo"   # replace with your bucket name
    days_threshold = 30

    # Initialize S3 client
    s3 = boto3.client('s3')

    # Calculate cutoff date
    cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days_threshold)
    print(f"Deleting files older than {days_threshold} days (before {cutoff_date})")

    # List objects in bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' not in response:
        print("Bucket is empty.")
        return

    for obj in response['Contents']:
        key = obj['Key']
        last_modified = obj['LastModified']
        print(f"Checking {key}, last modified {last_modified}")

        if last_modified < cutoff_date:
            print(f"Deleting {key}...")
            s3.delete_object(Bucket=bucket_name, Key=key)
            print(f"{key} deleted.")
        else:
            print(f"{key} is newer than cutoff, skipping.")

    print("=== S3 Cleanup Completed ===")
