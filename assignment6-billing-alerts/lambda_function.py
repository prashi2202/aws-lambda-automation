import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    print("=== Starting Billing Alert ===")

    cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
    sns = boto3.client('sns')
    topic_arn = "arn:aws:sns:region:account-id:BillingAlert"  # replace with your SNS topic ARN
    threshold = 50  # USD

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[{'Name': 'Currency', 'Value': 'USD'}],
        StartTime=datetime.utcnow() - timedelta(hours=24),
        EndTime=datetime.utcnow(),
        Period=86400,
        Statistics=['Maximum']
    )

    if response['Datapoints']:
        amount = response['Datapoints'][0]['Maximum']
        print(f"Current billing amount: ${amount}")

        if amount > threshold:
            message = f"AWS billing exceeded threshold: ${amount}"
            sns.publish(
                TopicArn=topic_arn,
                Message=message,
                Subject="AWS Billing Alert"
            )
            print(f"Alert sent: {message}")
        else:
            print(f"Billing is within threshold: ${amount}")
    else:
        print("No billing data available.")

    print("=== Billing Alert Completed ===")
