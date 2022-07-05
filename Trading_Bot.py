import boto3
import pandas as pd

# Use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('credentials.txt', 'rb')
s3.Bucket('algo-trading-bot').put_object(Key='credentials.txt', Body=data)

