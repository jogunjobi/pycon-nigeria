<!----- Conversion time: 19.71 seconds.


Using this Markdown file:

1. Cut and paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* GD2md-html version 1.0β11
* Mon Sep 10 2018 19:29:27 GMT-0700 (PDT)
* Source doc: https://docs.google.com/open?id=1Omo8hciVpVWN-FTlWvR40NwoPpT6gi2aChxIQ1ogiyo
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server.
----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 34.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>
<a href="#gdcalert13">alert13</a>
<a href="#gdcalert14">alert14</a>
<a href="#gdcalert15">alert15</a>
<a href="#gdcalert16">alert16</a>
<a href="#gdcalert17">alert17</a>
<a href="#gdcalert18">alert18</a>
<a href="#gdcalert19">alert19</a>
<a href="#gdcalert20">alert20</a>
<a href="#gdcalert21">alert21</a>
<a href="#gdcalert22">alert22</a>
<a href="#gdcalert23">alert23</a>
<a href="#gdcalert24">alert24</a>
<a href="#gdcalert25">alert25</a>
<a href="#gdcalert26">alert26</a>
<a href="#gdcalert27">alert27</a>
<a href="#gdcalert28">alert28</a>
<a href="#gdcalert29">alert29</a>
<a href="#gdcalert30">alert30</a>
<a href="#gdcalert31">alert31</a>
<a href="#gdcalert32">alert32</a>
<a href="#gdcalert33">alert33</a>
<a href="#gdcalert34">alert34</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



[TOC]



##### **<span style="text-decoration:underline;">A. INSTALLING SERVERLESS</span>** {#a-installing-serverless}

<span style="text-decoration:underline;">Installing on OSX</span>

1). Open a terminal and install node (Make sure Homebrew is already installed)


```
brew install node
```


2). Install serverless 


```
npm install -g serverless
```


<span style="text-decoration:underline;">Installing on Linux</span>

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


5).** **Type **_'serverless'_ **or **_'sls'_** within your terminal to confirm that serverless is now installed. This will show a list of all serverless commands.

6). Within AWS IAM, create a new user called **_<span style="text-decoration:underline;">serveless-admin</span>_** with programmatic access (_Make sure you have access to make changes to IAM within your AWS accoun_t)



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless0.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless0.png "image_tooltip")


7). Attach administrator access to this user. If you do not want to give full access to serverless, you can select the AWS services that you know that you will need.



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless1.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless1.png "image_tooltip")


8). Download your credentials file with Access Key and Secret Access Key ID and save in a safe location

9). Configure serverless using the username (_serverless-admin_) and access keys you just downloaded


```
serverless config credentials --provider aws --key [XXX] --secret [YYY] --profile serverless-admin
```


You should now see Serverless starting the setup within your AWS account and will also save the credentials to your local drive



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless2.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless2.png "image_tooltip")



##### **<span style="text-decoration:underline;">B. CREATING A SIMPLE LAMBDA FUNCTION</span>** {#b-creating-a-simple-lambda-function}

10). Create a new directory where you will save all of your serverless code and functions in a location of your choice (best practice)


```
mkdir ~/serverless_code && cd ~/serverless_code
```


11). Start by creating a python template for your project. The path name should properly identify the project you're working (For this tutorial, I will name it _<span style="text-decoration:underline;">pycon-ng</span>_)


```
sls create --template aws-python --path pycon-ng
```




<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless3.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless3.png "image_tooltip")


12). Type _<span style="text-decoration:underline;">'ls'</span>_ and you should see a directory called _<span style="text-decoration:underline;">pycon-ng</span>_. _<span style="text-decoration:underline;">'cd'</span>_ into that directory and type _<span style="text-decoration:underline;">'ls'</span>_ again and you should see a **handler.py** file, a **serverless.yml** file and a .gitignore file



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless4.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless4.png "image_tooltip")


The **handler.py** file is the main file which contains all the python code which will be executed while the **serverless.yml** file is the configuration which will be used to configure all the AWS services needed to successfully execute the function

13). Open both files using a text editor of your choice



*   The **handler.py** file will contain a sample function already defined for you. You can test the Serverless using the sample function, replace that with your current code (if you already have one) or create a new function
*   The serverless.yml has the configurations that are needed to access (almost) all the AWS services you need to run your serverless service.  Most of the configurations are commented and only services needed to run the current sample function in the **handler.py** file are active (you can un-comment and fill in the variables as needed)

14). Replace the current sample code in the **handler.py** file with your new code and save.



*   For this example, I will replace the sample code with a function which takes a name argument and prints and returns the name back to us.

	

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


15). If you have only one AWS credential configured on your local drive, there is no need to make any changes to the **serverless.yml** file. However, if you have multiple credentials, add the corresponding profile name as shown below.



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless5.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless5.png "image_tooltip")


16). Make sure that your terminal is currently is in the directory with the lambda code


```
cd ~/serverless_code/pycon-ng
```


17). Deploy the Serverless code to AWS


```
sls deploy -v
```


18). The deploy process should take about a minute and you will see all the configurations that serverless is setting up within your AWS environment (e.g. cloudformation, S3, IAM, Lambda etc.)



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless6.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless6.png "image_tooltip")


19). You should now see the function created in your lambda functions page



<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless7.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless7.png "image_tooltip")


20). Click the newly created function and you should see that it has the same content that was created in the **handler.py** file



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless8.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless8.png "image_tooltip")


21). To test that the function is working as expected, click the dropdown next to the test button at the top right hand of the page and select "Configure test events"



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless9.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless9.png "image_tooltip")


22). Enter a name for your test values in the Event name field and replace the sample test data with correct details needed to test your function and save.

	Before:

	

<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless10.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless10.png "image_tooltip")


	After:

	

<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless11.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless11.png "image_tooltip")


23). Run the test using the configured test event and you should get a success message.



<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless12.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless12.png "image_tooltip")



##### **<span style="text-decoration:underline;">C. INVOKING SERVERLESS FUNCTIONS IN AWS FROM YOUR LOCAL DRIVE</span>** {#c-invoking-serverless-functions-in-aws-from-your-local-drive}

24). To invoke a deployed function locally


```
sls invoke --function <function_name>
```


25). To invoke the function with logs


```
sls invoke --function <function_name> -l 
```


26). To invoke the function in local mode (testing before deployment)


```
sls invoke local --function <function_name>
```


27). To invoke the function and pass data to the function


```
sls invoke --function <function_name> -l --data '{"key":"value"}'
```


**EXAMPLE:** Invoking the previously deployed function



<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless13.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless13.png "image_tooltip")



##### **<span style="text-decoration:underline;">D. UPDATING AND DELETING YOUR SERVERLESS CODE WITHIN AWS</span>** \


There are many scenarios where you may need to make changes to the Serverless project after your initial deployment

28). If you make changes within the handler.py file ONLY and you want to update a single function


```
sls deploy function -f <function_name>
```


29). To update the whole project (especially after making changes to both the **handler.py** and **serverless.yml** files)


```
sls deploy -v
```


30). To remove/delete your Serverless project from AWS


```
sls remove
```



##### **<span style="text-decoration:underline;">E. CREATING AN ADVANCED SERVERLESS FUNCTION USING SNS</span>** {#e-creating-an-advanced-serverless-function-using-sns}

31). Replace the current sample code in the **handler.py** file with your new code and save.



*   For this example, I will use a current SNS sample which we use to send messages to SNS

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


Note that the function name has changed from **_hello()_** to **_send_to_sns()_** and the function argument "event" has been changed to "message"

32). Go to the serverless.yml file and make the following config changes.



*   Under provider (line 20), we are going to add some more configurations
    *   Profile: your IAM user for serverless (i.e. serverless-admin)
    *   Region: Region for your lambda functions (i.e. us-west-2)

Before:



<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless14.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless14.png "image_tooltip")


After:



<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless15.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless15.png "image_tooltip")



    Note that the service key indicates the name of your project (i.e. pycon-ng)

33). You will also need to configure the name of your new handler function in the **serverless.yml** file. 



*   Scroll down to the bottom of the **serverless.yml** file to the <span style="text-decoration:underline;">functions</span> section
*   Given that our function name is no longer hello(), we need to change it to the current function name.

	

	Before:

	

<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless16.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless16.png "image_tooltip")


	After:



<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless17.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless17.png "image_tooltip")



    **Explanation:** Within the serverless.yml file, we add the new function (from the handler.py file) that we want to use to create the lambda function and then pass what we want the name of the handler should be within AWS lambda

34). From within the directory, type 'sls deploy -v' to deploy your project


```
sls deploy -v
```


35). You should now see the function created in your lambda functions page



<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless18.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless18.png "image_tooltip")


36). If you open the function, you will see that it is the same function that we copied into the **handler.py** file



<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless19.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless19.png "image_tooltip")


37). In order to test that this lambda function is working correctly, I set up a simple SNS topic (which will be deleted after this tutorial 



<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless20.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless20.png "image_tooltip")




*   Testing the lambda function with the sns ARN details



<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless21.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless21.png "image_tooltip")




*   When a test is run with the configured SNS topic, you should experience an error



<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless22.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless22.png "image_tooltip")




*   The reason for the failure is due to the fact that the lambda function that we created does not have the required access needed to publish messages to the SNS topic.
*   We can easily go to the IAM configuration page within AWS and add the required policy for publish messages to the SNS topic.
*   However, one of the major advantages of Serverless is that it allows users to create all the configurations needed within the **serverless.yml** file 


##### **<span style="text-decoration:underline;">F. CREATING IAM POLICIES WITHIN SERVERLESS</span>** {#f-creating-iam-policies-within-serverless}

38). In order to make configuration changes to the Serverless project, I will first delete/remove our project from the AWS environment


```
sls remove
```


39). In the** serverless.yml **file, we need to add the correct IAM policies in order to allow our function to publish messages to SNS.

 

<p id="gdcalert24" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless23.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert25">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless23.png "image_tooltip")




*   Adding this IAM role statement to the **serverless.yml** file will give the role created by Serverless full access to ALL SNS topics. (you can make updates to the statement if you want to provide access to only one or more topics)

40). Save the **serverless.yml** file and re-deploy your Serverless project 


```
sls deploy -v
```


41). After the deployment has been completed, you can confirm that the role has the assigned policy



<p id="gdcalert25" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless24.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert26">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless24.png "image_tooltip")


42). Now, when we go to retest the lambda function, we should have better results



<p id="gdcalert26" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless25.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert27">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless25.png "image_tooltip")



##### **<span style="text-decoration:underline;">G. BONUS: CREATING AN ADVANCED PYTHON FUNCTION (WITH ADDITIONAL PACKAGES)</span>**

**_<span style="text-decoration:underline;">Prerequisites:</span> You will need to have [Docker for Mac](https://www.docker.com/docker-mac) installed (for Mac OSX users). _**



*   So far we have created lambda functions which use native python packages.  In this section, we will create functions which require non-native python packages that are installed using **pip**.

43). For this section, we will replace the function within the **handler.py** file with a function which will insert records into a RDS database


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




*   You will notice in new lambda function is that <span style="text-decoration:underline;">line 4</span> is importing **pymysql** which is an external package

44). In order to use this package within lambda, we will need to first install the **serverless-python-requirements** package

Run:


```
npm init
```


This will ask you for some questions. Accept all the defaults



<p id="gdcalert27" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless26.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert28">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless26.png "image_tooltip")


This will create a **package.json** file within your directory

Now run:


```
npm install --save serverless-python-requirements
```




<p id="gdcalert28" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless27.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert29">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless27.png "image_tooltip")


This will create an additional **node_modules** directory and a **package-lock.json** file.

45). To configure our project to use the plugin, we need to add the following lines to the **serverless.yml** file



<p id="gdcalert29" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless28.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert30">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless28.png "image_tooltip")


NOTE: If you are on a linux system, chna

46). Remember to also change the handler information for the new function 



<p id="gdcalert30" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless29.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert31">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless29.png "image_tooltip")


47). You will also need to create a **requirements.txt** file within our project directory and add the new **pymysql** package into it.



<p id="gdcalert31" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless30.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert32">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless30.png "image_tooltip")


48). Final directory structure



<p id="gdcalert32" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless31.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert33">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless31.png "image_tooltip")


49). Deploy your project


```
sls deploy -v
```


50). Notice that the lambda function name will be different since we changed the function and handler names



<p id="gdcalert33" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless32.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert34">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless32.png "image_tooltip")


51). Open up the function it will reveal that there are some external packages 



<p id="gdcalert34" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Pycon-Serverless33.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert35">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Pycon-Serverless33.png "image_tooltip")



<!-- GD2md-html version 1.0β11 -->

