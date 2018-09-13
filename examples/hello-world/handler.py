import json


def hello(event, context):

   name = event['name']

   print "Hi {0}!!".format(name)
   return "Welcome to Serverless, {0}!!".format(name)