[[TOC]]

##### **A. INSTALLING SERVERLESS**

Installing on OSX

1). Open a terminal and install node (Make sure Homebrew is already installed)

```
brew install node
```


2). Install serverless 

```
npm install -g serverless
```


Installing on Linux

3). Install node and npm

```
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
```


4). Install serverless

```
npm install -g serverless
```


5).** **Type **_‘serverless’_**** **or **_‘sls’_** within your terminal to confirm that serverless is now installed. This will show a list of all serverless commands.

6). Within AWS IAM, create a new user called **_serveless-admin_** with programmatic access (*Make sure you have access to make changes to IAM within your AWS accoun*t)

![image alt text](image_0.png)

7). Attach administrator access to this user. If you do not want to give full access to serverless, you can select the AWS services that you know that you will need.

![image alt text](image_1.png)

8). Download your credentials file with Access Key and Secret Access Key ID and save in a safe location

9). Configure serverless using the username (*serverless-admin*) and access keys you just downloaded

```
serverless config credentials --provider aws --key [XXX] --secret [YYY] --profile serverless-admin
```


You should now see Serverless starting the setup within your AWS account and will also save the credentials to your local drive

![image alt text](image_2.png)

##### **B. CREATING A SIMPLE LAMBDA FUNCTION**

10). Create a new directory where you will save all of your serverless code and functions in a location of your choice (best practice)

```
mkdir ~/serverless_code && cd ~/serverless_code
```


11). Start by creating a python template for your project. The path name should properly identify the project you’re working (For this tutorial, I will name it *pycon-ng*)

```
sls create --template aws-python --path pycon-ng
```


![image alt text](image_3.png)

9). Type *‘ls’* and you should see a directory called *pycon-ng*. *‘cd’* into that directory and type *‘ls’* again and you should see a **handler.py** file, a **serverless.yml** file and a .gitignore file

![image alt text](image_4.png)

The **handler.py** file is the main file which contains all the python code which will be executed while the **serverless.yml** file is the configuration which will be used to configure all the AWS services needed to successfully execute the function

10). Open both files using a text editor of your choice

* The **handler.py** file will contain a sample function already defined for you. You can test the Serverless using the sample function, replace that with your current code (if you already have one) or create a new function

* The serverless.yml has the configurations that are needed to access (almost) all the AWS services you need to run your serverless service.  Most of the configurations are commented and only services needed to run the current sample function in the **handler.py** file are active (you can un-comment and fill in the variables as needed)

11). Replace the current sample code in the **handler.py** file with your new code and save.

* For this example, I will replace the sample code with a function which takes a name argument and prints and returns the name back to us.

  

**Before:**

  

```
import json


def hello(event, context):
   body = {
       "message": "Go Serverless v1.0! Your function executed successfully!",
       "input": event
   }

   response = {
       "statusCode": 200,
       "body": json.dumps(body)
   }

   return response

   # Use this code if you don't use the http event with the LAMBDA-PROXY
   # integration
   """
   return {
       "message": "Go Serverless v1.0! Your function executed successfully!",
       "event": event
   }
   """
```


**After:**

```
import json


def hello(event, context):

   name = event['name']

   print "Hi {0}!!".format(name)
   return "Welcome to Serverless, {0}!!".format(name)
```


12). If you have only one AWS credential configured on your local drive, there is no need to make any changes to the **serverless.yml** file. However, if you have multiple credentials, add the corresponding profile name as shown below.

![image alt text](image_5.png)

13). Make sure that your terminal is currently is in the directory with the lambda code

```
cd ~/serverless_code/pycon-ng
```


14). Deploy the Serverless code to AWS

```
sls deploy -v
```


15). The deploy process should take about a minute and you will see all the configurations that serverless is setting up within your AWS environment (e.g. cloudformation, S3, IAM, Lambda etc.)

![image alt text](image_6.png)

16). You should now see the function created in your lambda functions page

![image alt text](image_7.png)

17). Click the newly created function and you should see that it has the same content that was created in the **handler.py** file

![image alt text](image_8.png)

18). To test that the function is working as expected, click the dropdown next to the test button at the top right hand of the page and select "Configure test events"

![image alt text](image_9.png)

19). Enter a name for your test values in the Event name field and replace the sample test data with correct details needed to test your function and save.

  Before:

  ![image alt text](image_10.png)

  After:

  ![image alt text](image_11.png)

20). Run the test using the configured test event and you should get a success message.

![image alt text](image_12.png)

##### **C. INVOKING SERVERLESS FUNCTIONS IN AWS FROM YOUR LOCAL DRIVE**

21). To invoke a deployed function locally

```
sls invoke --function <function_name>
```


22). To invoke the function with logs

```
sls invoke --function <function_name> -l 
```


23). To invoke the function in local mode (testing before deployment)

```
sls invoke local --function <function_name>
```


24). To invoke the function and pass data to the function

```
sls invoke --function <function_name> -l --data '{"key":"value"}'
```


**EXAMPLE:** Invoking the previously deployed function

![image alt text](image_13.png)

##### **D. UPDATING AND DELETING YOUR SERVERLESS CODE WITHIN AWS**

There are many scenarios where you may need to make changes to the Serverless project after your initial deployment

25). If you make changes within the handler.py file ONLY and you want to update a single function

```
sls deploy function -f <function_name>
```


26). To update the whole project (especially after making changes to both the **handler.py** and **serverless.yml** files)

```
sls deploy -v
```


27). To remove/delete your Serverless project from AWS

```
sls remove
```


##### **E. CREATING AN ADVANCED SERVERLESS FUNCTION USING SNS**

28). Replace the current sample code in the **handler.py** file with your new code and save.

* For this example, I will use a current SNS sample which we use to send messages to SNS

**Before:**

```
import json


def hello(event, context):

   name = event['name']

   print "Hi {0}!!".format(name)
   return "Welcome to Serverless, {0}!!".format(name)
```


**After:**

```
from __future__ import print_function
import json
import urllib
import boto3

print ('Loading message function...')


def send_to_sns(message, context):

   sns = boto3.client('sns')
   sns.publish(
       TopicArn=message['topic'],
       Subject=message['subject'],
       Message=message['body']
   )
  
   return (message['body'] + " published to " + message['topic'])
```


Note that the function name has changed from **_hello()_** to **_send_to_sns()_** and the function argument "event" has been changed to “message”

29). Go to the serverless.yml file and make the following config changes.

* Under provider (line 20), we are going to add some more configurations

    * Profile: your IAM user for serverless (i.e. serverless-admin)

    * Region: Region for your lambda functions (i.e. us-west-2)

Before:

![image alt text](image_14.png)

After:

![image alt text](image_15.png)

Note that the service key indicates the name of your project (i.e. pycon-ng)

30). You will also need to configure the name of your new handler function in the **serverless.yml** file. 

* Scroll down to the bottom of the **serverless.yml** file to the functions section

* Given that our function name is no longer hello(), we need to change it to the current function name.

  

  Before:

  ![image alt text](image_16.png)

  After:

![image alt text](image_17.png)

**Explanation:** Within the serverless.yml file, we add the new function (from the handler.py file) that we want to use to create the lambda function and then pass what we want the name of the handler should be within AWS lambda

31). From within the directory, type ‘sls deploy -v’ to deploy your project

```
sls deploy -v
```


32). You should now see the function created in your lambda functions page

![image alt text](image_18.png)

33). If you open the function, you will see that it is the same function that we copied into the **handler.py** file

![image alt text](image_19.png)

34). In order to test that this lambda function is working correctly, I set up a simple SNS topic (which will be deleted after this tutorial 

![image alt text](image_20.png)

* Testing the lambda function with the sns ARN details

![image alt text](image_21.png)

* When a test is run with the configured SNS topic, you should experience an error

![image alt text](image_22.png)

* The reason for the failure is due to the fact that the lambda function that we created does not have the required access needed to publish messages to the SNS topic.

* We can easily go to the IAM configuration page within AWS and add the required policy for publish messages to the SNS topic.

* However, one of the major advantages of Serverless is that it allows users to create all the configurations needed within the **serverless.yml** file 

##### **F. CREATING IAM POLICIES WITHIN SERVERLESS**

35). In order to make configuration changes to the Serverless project, I will first delete/remove our project from the AWS environment

```
sls remove
```


21). In the** serverless.yml **file, we need to add the correct IAM policies in order to allow our function to publish messages to SNS.

 ![image alt text](image_23.png)

* Adding this IAM role statement to the **serverless.yml** file will give the role created by Serverless full access to ALL SNS topics. (you can make updates to the statement if you want to provide access to only one or more topics)

36). Save the **serverless.yml** file and re-deploy your Serverless project 

```
sls deploy -v
```


37). After the deployment has been completed, you can confirm that the role has the assigned policy

![image alt text](image_24.png)

38). Now, when we go to retest the lambda function, we should have better results

![image alt text](image_25.png)

##### **G. BONUS: CREATING AN ADVANCED PYTHON FUNCTION (WITH ADDITIONAL PACKAGES)**

**_Prerequisites:_*** You will need to have **[Docker for Ma*c](https://www.docker.com/docker-mac)* installed (for Mac OSX users). *

* So far we have created lambda functions which use native python packages.  In this section, we will create functions which require non-native python packages that are installed using **pip**.

39). For this section, we will replace the function within the **handler.py** file with a function which will insert records into a RDS database

```
import json
import sys
import logging
import pymysql


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def run_query(query):

   #config settings
   rds_host = 'sample_host_name'
   name     = 'user'
   password = 'password'
   db_name  = 'test_db'

   try:
       conn = pymysql.connect(rds_host,user=name,passwd=password,db=db_name,autocommit=True,connect_timeout=5)
   except:
       logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
       sys.exit()
   logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
   try:
       with conn.cursor() as cur:
           cur.execute(query)
           conn.commit()
           logger.info("INSERTED entries")
       cur.close()
       conn.close()
   except:
       print("There is a problem with query")

def insert_to_table(event, context):
   query = """
   INSERT INTO test_db.sample_table (id, first_name, last_name)
   VALUES
   (1, 'Jide', 'Ogunjobi');
   """
   insert = run_query(query)
```


* You will notice in new lambda function is that line 4 is importing **pymysql** which is an external package

40). In order to use this package within lambda, we will need to first install the **serverless-python-requirements** package

Run:

```
npm init
```


This will ask you for some questions. Accept all the defaults

![image alt text](image_26.png)

This will create a **package.json** file within your directory

Now run:

```
npm install --save serverless-python-requirements
```


![image alt text](image_27.png)

This will create an additional **node_modules** directory and a **package-lock.json** file.

41). To configure our project to use the plugin, we need to add the following lines to the **serverless.yml** file

![image alt text](image_28.png)

NOTE: If you are on a linux system, chna

42). Remember to also change the handler information for the new function 

![image alt text](image_29.png)

43). You will also need to create a **requirements.txt** file within our project directory and add the new **pymysql** package into it.

![image alt text](image_30.png)

44). Final directory structure

![image alt text](image_31.png)

44). Deploy your project

```
sls deploy -v
```


45). Notice that the lambda function name will be different since we changed the function and handler names

![image alt text](image_32.png)

46). Open up the function it will reveal that there are some external packages 

![image alt text](image_33.png)

