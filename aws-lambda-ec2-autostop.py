import boto3

# the ec2 resource
ec2 = boto3.resource('ec2')

# autostop filter
stop_filter = [
    {'Name': 'tag:AutoStop', 'Values': ['true', 'True', 'TRUE']},
    {'Name': 'instance-state-name', 'Values': ['running']}
]


def lambda_handler(event, context):
    # get list of filtered instances
    instances = ec2.instances.filter(Filters=stop_filter)

    # get instance id list
    filtered_ids = [instance.id for instance in instances]

    # verify there are instances to stop
    if len(filtered_ids) > 0:
        print "AutoStop Instances:", filtered_ids
        stop_message = instances.stop()
        print "Stop Response:"
        print stop_message
    else:
        print "No EC2 instances found to stop"
