####################################################################
########### AUTHOR #################################################
########### PARTHKUMAR PATEL #######################################
########### DATE: 26th Nov 2017 ####################################
####################################################################

import os,sys
import boto
from boto.s3.key import Key
from boto.s3.connection import S3Connection
import tarfile
from boto.exception import S3ResponseError

LOCAL_PATH = '/Securonix/elbaccess/'

AWS_KEY = 'AKIAIJXH4AML6UZ3Z23Q'
AWS_SECRET = '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'
aws_connection = S3Connection(AWS_KEY, AWS_SECRET)

bucket = aws_connection.get_bucket('elbacesslog' , validate=False)

for key in bucket.list():
    keyString = str(key.key)
    a1=keyString.replace('/','_')
    print a1
    key.get_contents_to_filename( LOCAL_PATH + a1)