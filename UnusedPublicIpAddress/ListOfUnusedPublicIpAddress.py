import boto3
client=boto3.client('ec2')
response=client.describe_addresses()
for i in response['Addresses']:
    if 'PrivateIpAddress' not in i:
        print(i['PublicIp'])

