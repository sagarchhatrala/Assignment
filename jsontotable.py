#!/usr/bin/python3
import json

# load data using Python JSON module
with open('normalize2.json','r') as f:
    data = json.loads(f.read())

# S3 Bicket IDs where ACL is not private

for value in data['aws_s3_bucket']:
    if value['config']['acl'] != 'private':
        print("Acl is not private for: {}".format(value['id'])) 

# S3 Bicket IDs where Bucket policy has Principal = '*'

for value in data['aws_s3_bucket_policy']:
    policy = json.loads(value['config']['policy'])
    
    for id in policy['Statement']:
        if id['Principal'] == '*':
            print("S3 Bicket IDs where Bucket policy has Principal = '*': {}".format(value['id']))
