import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('')
# Iterates through all the objects, doing the pagination for you. Each obj
# is an ObjectSummary, so it doesn't contain the body. You'll need to call
# get to get the whole body.
for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read()
    print body

a1 = bucket.Object('-12-21-15--43-')
body = a1.get()['Body'].read()
print body
 
