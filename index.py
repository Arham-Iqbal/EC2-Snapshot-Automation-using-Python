import boto3
session=boto3.Session()
ec2=session.resource("ec2")
def create_snapshots():
    instances=list(ec2.instances.all())
    if not instances:
        print("there are no running instances")
    else:
        try:
          for instance in instances:
            for device in instance.block_device_mappings:
                volume_id=device["Ebs"]["VolumeId"]
                volume=ec2.Volume(volume_id)
                snapshot=volume.create_snapshot(Description="automated backup")
                print(f"snapshot created :{snapshot.id} , volume of snapshot {volume.id}")
        except Exception as e:
            print(f"error occured as {e}")
def delete_snapshots(description_filter):
    try:
        snapshots = ec2.snapshots.filter(OwnerIds=['self']) 
        for snapshot in snapshots:
            if description_filter in snapshot.description:
                snapshot.delete()
                print(f"Snapshot deleted: {snapshot.id}")
            else:
                print(f"Snapshot description does not match. Snapshot ID: {snapshot.id}")
    except Exception as e:
        print(f"Error occurred while deleting snapshots: {e}")
while True:
    print("\n Choose an action  ")
    print("1. Create snapshots")
    print("2. Delete snapshots")
    print("3. exit")
    c=input("enter your Choice :  ")
    if c=='3':
        break
    elif c=='1':
        create_snapshots()
    elif c=='2':
        delete_snapshots("automated backup")
    else:
        print("invalid instance ")

    





    