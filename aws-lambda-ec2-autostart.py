import boto3

# the ec2 resource
ec2 = boto3.resource('ec2')

# autostart filter
start_filter = [
    {'Name': 'tag:AutoStart', 'Values': ['true', 'True', 'TRUE']},
    {'Name': 'instance-state-name', 'Values': ['stopped']}
]


def lambda_handler(event, context):
    # get list of filtered instances
    instances = ec2.instances.filter(Filters=start_filter)

    # get instance id list
    filtered_ids = [instance.id for instance in instances]

    # verify there are instances to start
    if len(filtered_ids) > 0:
        print "AutoStart Instances:", filtered_ids
        start_message = instances.start()
        print "Start Response:"
        print start_message
    else:
        print "No EC2 instances found to start"
