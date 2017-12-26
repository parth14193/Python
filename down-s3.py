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
from datetime import datetime, timedelta

LOCAL_PATH = '/Securonix/elbaccess/'

####### Code for last N days ###########

N = 2
datetime=datetime.now() - timedelta(days=N)
datetime=str(datetime.date()) + "T" + str(datetime.time())
datetime=datetime.split(".")
datetime=str(datetime[0])

#######################################

AWS_KEY = 'AKIAIJXH4AML6UZ3Z23Q'
AWS_SECRET = '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'
aws_connection = S3Connection(AWS_KEY, AWS_SECRET)

bucket = aws_connection.get_bucket('elbacesslog' , validate=False)

for key in bucket.list():
	l=key.last_modified
	l=l.split(".")
	l=str(l[0])
	if ( l > datetime ):
		keyString = str(key.key)
		a1=keyString.replace('/','_')
		key.get_contents_to_filename( LOCAL_PATH + a1)
