import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all stopped EC2 instances.
    filters = [{
            'Name': 'tag:Environment', #AWS recommended tag key
            'Values': ['Production']  #AWS recommended tag value
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)
    print(instances)
    #locate all stopped instances
    StoppedInstances = [instance.id for instance in instances]
    
    #print the instances for logging purposes
    #print StoppedInstances 
    
    #make sure there are actually instances to shut down. 
  
    if len(StoppedInstances) > 0:
        #perform the shutdown
        shuttingDown = ec2.instances.filter(InstanceIds=StoppedInstances).start()
        print ("startingInstances")
    else:
        print ("Nothing to see here")