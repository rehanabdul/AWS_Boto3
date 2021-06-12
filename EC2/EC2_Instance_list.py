#from boto3 import ec2
import boto3
#ec2 = boto3.client('ec2')
#response = ec2.describe_instances()
#print(response)
def create_instance():
    ec2_client = boto3.client("ec2", region_name="ap-south-1")
    instances = ec2_client.run_instances(
        ImageId="ami-0bcf5425cdc1d8a85",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
    )
create_instance()
#ec2_client = boto3.client("ec2", region_name="ap-south-1")
#response = ec2_client.stop_instances(InstanceIds=["i-0d43ec54c13725ecc"])