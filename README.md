## Overview
This repository contains AWS Lambda functions to automatically start and stop EC2 instances on a schedule using tags. The solution helps optimize costs by running instances having tags only when needed. 

## Repository Contents
- `start_ec2.py`: Lambda function to start tagged EC2 instances
- `stop_ec2.py`: Lambda function to stop tagged EC2 instances
- `README.md`: Implementation and configuration guide

## Prerequisites
- AWS Account
- EC2 instances to schedule
- Basic knowledge of:
  - AWS Lambda
  - Amazon EC2
  - AWS IAM
  - Amazon EventBridge

## Implementation Guide

### 1. IAM Configuration

#### Create IAM Policy
1. Navigate to IAM Console
2. Create new policy with the following JSON:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:Start*",
                "ec2:Stop*"
            ],
            "Resource": "*"
        }
    ]
}
```

#### Create IAM Role
1. Go to IAM Console → Roles → Create Role
2. Choose AWS Lambda as the service
3. Attach the policy created above
4. Name the role appropriately (e.g., "EC2SchedulerLambdaRole")
5. Save the role ARN for Lambda configuration

### 2. Lambda Function Setup

#### Function Creation
1. Open AWS Lambda Console
2. Click "Create function"
3. Select "Author from scratch"
4. Configure basic settings:
   - Name: StartEC2Instances / StopEC2Instances
   - Runtime: Python 3.9
   - Architecture: x86_64
   - Permissions: Use existing role (created earlier)
5. Upload the respective Python scripts from this repository
6. Set function timeout to 10 seconds in Configuration tab
7. Deploy the function

### 3. Testing Your Functions
#### In Lambda Console:
1. Select your function
2. Create new test event
3. Use default event template
4. Save and run test

#### Verify Results:
- Check EC2 console for instance state changes
- Review CloudWatch logs for execution details
- Confirm expected behavior

### 4. EventBridge Schedule Configuration
1. Open EventBridge Console
2. Create new rule:
   - Name: Choose descriptive name (e.g., "StartEC2MorningSchedule")
   - Rule type: Schedule
3. Schedule Pattern:
   - For starting instances: `0 8 ? * MON-FRI *` (8 AM UTC weekdays)
   - For stopping instances: `0 18 ? * MON-FRI *` (6 PM UTC weekdays)
4. Target Configuration:
   - Select AWS Lambda function
   - Choose appropriate function
5. Create the rule

## Monitoring and Maintenance

### CloudWatch Monitoring
- Check `/aws/lambda/FunctionName` log groups
- Monitor execution status
- Set up alerts for failures

### CloudTrail Auditing
- Review Event History
- Filter by event names:
  - StartInstances
  - StopInstances

### EC2 State Monitoring
- Regular state checks
- Verify schedule effectiveness
- Monitor start/stop patterns

## Best Practices

### Tag Management
#### Consistent Tagging:
- Use standardized key names
- Follow organizational naming conventions
- Document all tags used

#### AWS Recommended Tags:
- Environment: (e.g., Production, Development)
- Owner: Team/Individual responsible
- Cost Center: For billing purposes

### Security Considerations
#### IAM Best Practices:
- Use least privilege principle
- Regular permission reviews
- Monitor unauthorized access attempts

#### Access Control:
- Restrict function invocation
- Implement resource-based policies
- Regular security audits

### Cost Optimization
#### Schedule Optimization:
- Regular usage pattern review
- Adjust schedules based on needs
- Monitor cost savings

#### Resource Management:
- Tag compliance checking
- Regular instance inventory
- Cost allocation tracking

## Troubleshooting Guide

### Common Issues
#### Function Failures:
- IAM permission issues
- Tag configuration mismatches
- Timeout problems

#### Schedule Issues:
- Timezone misconfigurations
- Invalid cron expressions
- Rule activation status

### Resolution Steps
#### Lambda Issues:
- Check CloudWatch logs
- Verify IAM roles
- Test functions manually

#### Instance Issues:
- Verify instance tags
- Check instance states
- Review security groups

## Support Resources
- AWS Lambda Documentation --- https://repost.aws/knowledge-center/start-stop-lambda-eventbridge
- EC2 User Guide -- https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html

## Contributing
- Fork the repository
- Create feature branch
- Submit pull request
- Follow coding standards


## Acknowledgments
- AWS Documentation
- Community contributors

Note: Adjust timezone settings, schedule patterns, and tag values according to your requirements. Always test in a non-production environment first.