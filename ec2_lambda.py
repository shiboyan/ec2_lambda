import boto3
region = 'us-east-1'
ec2=boto3.client('ec2',region_name=region)
response=ec2.describe_instances()
dict=response
x=dict["Reservations"]
instances=[]
for i in range(len(x)):
    instances.append(dict["Reservations"][i]["Instances"][0]["InstanceId"])
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
