import boto3
import sys
import traceback

def lambda_handler(event, context):
    print("=== Starting Lambda Handler ===")

    try:
        # Step 1: Create EC2 client with SSL verification disabled
        print("Creating EC2 client for region us-west-2...")
        ec2 = boto3.client(
            'ec2',
            region_name='us-west-2',
        )
        print("EC2 client created successfully.")

        # Step 2: Describe instances
        print("Calling describe_instances...")
        response = ec2.describe_instances()
        print("describe_instances call succeeded.")

        reservations = response.get('Reservations', [])
        print(f"Found {len(reservations)} reservations.")

        if not reservations:
            print("No instances found in region us-west-2.")
            return

        # Step 3: Iterate through instances
        for reservation in reservations:
            for instance in reservation.get('Instances', []):
                instance_id = instance.get('InstanceId')
                tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
                print(f"Instance {instance_id} has tags: {tags}")

                action = tags.get('Action')
                if action == 'Auto-Stop':
                    print(f"Attempting to stop {instance_id}...")
                    resp = ec2.stop_instances(InstanceIds=[instance_id])
                    print(f"Stop response: {resp}")
                elif action == 'Auto-Start':
                    print(f"Attempting to start {instance_id}...")
                    resp = ec2.start_instances(InstanceIds=[instance_id])
                    print(f"Start response: {resp}")
                else:
                    print(f"No Action tag for {instance_id}, skipping.")

        print("=== Lambda Handler Completed ===")

    except Exception as e:
        print("ERROR occurred during Lambda execution:")
        traceback.print_exc(file=sys.stdout)
        print("=== Lambda Handler Aborted ===")

if __name__ == "__main__":
    # Run locally
    lambda_handler({}, {})

