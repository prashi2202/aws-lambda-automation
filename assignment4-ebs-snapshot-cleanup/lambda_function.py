import boto3
import datetime

def lambda_handler(event, context):
    print("=== Starting EBS Snapshot Automation ===")

    # Configuration
    ec2 = boto3.client('ec2', region_name='us-west-2')
    volume_id = "vol-07ee48906bb06ac5b"  # replace with your volume ID
    days_threshold = 30

    # Create snapshot
    snapshot = ec2.create_snapshot(
        VolumeId=volume_id,
        Description="Automated backup"
    )
    print(f"Created snapshot: {snapshot['SnapshotId']}")

    # Cleanup old snapshots
    cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days_threshold)
    snapshots = ec2.describe_snapshots(Filters=[{'Name':'volume-id','Values':[volume_id]}])

    for snap in snapshots['Snapshots']:
        snap_id = snap['SnapshotId']
        start_time = snap['StartTime']
        if start_time < cutoff_date:
            print(f"Deleting old snapshot: {snap_id}")
            ec2.delete_snapshot(SnapshotId=snap_id)
            print(f"Deleted snapshot: {snap_id}")
        else:
            print(f"Snapshot {snap_id} is newer than cutoff, keeping.")

    print("=== EBS Snapshot Automation Completed ===")
