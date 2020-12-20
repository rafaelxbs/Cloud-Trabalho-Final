import sys
sys.path.insert(0,'/opt')

import boto3
import json
from random import randint
from random import randint
import random
import uuid
import os

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

xray_recorder.configure(service='My app')
patch_all()

def echo(event, context):
    
    message = json.loads(event["body"])["Message"]

    response = {
        "statusCode": 201,
        "body": json.dumps({"Message":message})
    }

    return response

def sendToSNS(event, context):
    ##body = json.loads(event.get('body'))
    print(f"event: %s" % json.dumps(event))
    
    
    ##grupo = body["Grupo"]
    ##entrega = body["Entrega"]
    ##nota = body["Nota"]

    
    # send to SNS
    sns = boto3.client('sns')
    snsArn=os.environ["snsArn"]

    res = sns.publish(
                    TopicArn=snsArn,
                    Subject="Order Creation",
                    Message=json.dumps(event),
                    )
    
    ##message="Nota: "+nota
    response = {
            "isBase64Encoded": False,
            "headers": {
                "Content-Type": "application/json"
            },
            "statusCode": 201,
            "body": json.dumps(event)
        }

    return response

def printar(event, context):
    try:
        if(bool(random.getrandbits(1))):
            print("Error!!!")
            raise Exception("Random Error generated")
        print(f"event: %s" % json.dumps(event))
    except Exception as ex:
        print(ex)
        raise ex

def sqshandler(event, context):
    body = json.loads(event.get('body'))
    print(f"body: %s" % json.dumps(body))
    

    # send to SNS
    sqs = boto3.client('sqs')
    
    queue_url=os.environ["sqsUrl"]
    ##queue_url = 'https://sqs.us-east-1.amazonaws.com/229169531288/SQS-Principal-dev'
    message=json.dumps(body)
    
    response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={},
    MessageBody=message
    )
    
    print(response['MessageId'])
    
    response = {
        "statusCode": 201,
        "body": message
    }

    return response
    
    
def sqshandler2(event, context):
    print(f"event: %s" % json.dumps(event))
    
    
    # send to SNS
    sqs = boto3.client('sqs')
    
    queue_url=os.environ["sqsUrl2"]
    
    ##queue_url = 'https://sqs.us-east-1.amazonaws.com/229169531288/SQS-2-dev'
    
    message=json.dumps(event)

##
    response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={},
    MessageBody=message
    )
    
    print(response['MessageId'])
    
    response = {
        "statusCode": 201,
        "body": message
    }

    return response

