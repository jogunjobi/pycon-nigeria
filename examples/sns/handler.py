from __future__ import print_function
import json
import urllib
import boto3

print('Loading message function...')


def send_to_sns(message, context):
    sns = boto3.client('sns')
    sns.publish(
        TopicArn=message['topic'],
        Subject=message['subject'],
        Message=message['body']
    )

    return (message['body'] + " published to " + message['topic'])