# Configuring and launching spot instance on Amazon Web Services 

1. Select EC2 (to arrive at EC2 dashboard)
2. In top right corner of dashboard, change region to "US West (N.California)"
3. On left panel of dashboard, find "Instances" and select "Spot Requests"
4. Select button for "Request Spot Instances"
5. On left panel of "Step 1: Choose Amazon Machine Image" page, select "Community AMIs"
6. In the search box, search for "ami-b141a2f5" and press "Select"
 - note, AMI # chosen is from following blog: http://markus.com/install-theano-on-aws/

If you can't find the above AMI, you can also look for "ami-df6a8b9b".

7. On page "Step 2: Choose an Instance Type", scroll down and select "GPU instances | g2.2xlarge", and then select at bottom of page "Next: Configure Instance Details"
8. On page "Step 3: Configure Instance Details":
 - Number of instances: for now set to 1
 - Maximum price: for now set to 0.08?
 - Request valid to: you can set expiration date/time
 - at bottom of page, select "Review and Launch"
9. On page "Step 7: Review Spot Instance Request"
 - Select "edit security groups"
   - On page "Step 6: Configure Security Group", under column for "Source", change "Anywhere" to "My IP". Note, new security group name will now be "launch-wizard"-n unless you change that name too. 
10. On page "Step 7: Review Spot Instance Request", select button at bottom to "Launch"
 - A box will appear, "Select an existing key pair or create a new key pair"
   - The first time you see this box, you will need to select "Create a new key pair", and give it a name. This .pem file will download to your computer and you can store on your computer for safe keeping.
   - The second and subsequent times you see this box, select "Choose an existing key pair" and "Select a key pair" to select your key-pair file.
   - Select box to acknowledge access to selected private key file and select "Request Spot Instances"






#Connect kaggle data

Now you need to pull all the data from kaggle and install theano environment.

- Find the DNS address of your instance. It should be located at the bottom of the page as "Public DNS" in the instance page (once your spot instance has been approved).

- Then copy and paste the following line in your terminal:

```
ssh -i my-key.pem ubuntu@[DNS]
```

replace [DNS] by the DNS adress and my-key.pem by the full path to your key. If you encounter an error saying that your pem file has an 0640 access, then change its permission with the chmod command. Only the owner should be able to read the file.

- You should now be able to login onto your EC2 instance with the ssh command. It should look like that

```
ssh -i your_key.pem ubuntu@ec2-52-8-89-42.us-west-1.compute.amazonaws.com
```

- you need to use chrome web browser (there might be another way using other web browsers but I don't know...) . download [chrome extension](https://chrome.google.com/webstore/detail/cookietxt-export/lopabhfecdfhgogdbojmaicoicjekelh)

- go to the [kaggle data page](https://www.kaggle.com/c/facial-keypoints-detection/data)

- open chrome browser the cookie extension module and paste the entire message into a file cookies.txt . The content should look like that:


```
.kaggle.com	TRUE	/	TRUE	1504052919.896523	.ASPXAUTH	0E4988D1D297A050155C004A283E8EA38264C0C528C85A7CCEE2069565ED01BED343349F3B6876ECE06E6513E4F19BBC6D41E390BCAF572BC1319C0BA56C746C2118A78EAB8FADF3A530E1F7AB5830352BFED662
.www.kaggle.com	TRUE	/	FALSE	0	ARRAffinity	1f4f89825deb2c5dde2a9b78620703cdbacb765e0275867481e579474591fee1
www.kaggle.com	FALSE	/	FALSE	0	__RequestVerificationToken	a9G0R3z_7qPBpE302B6K7E-0tAGcfn7oCiY7ZlJNnr08CTJeLiP1c25FANEPXGYok0qu4s5QvtBswKqT732lQ1tn7V81
.kaggle.com	TRUE	/	FALSE	1442495611	__utmt	1
.kaggle.com	TRUE	/	FALSE	1505567011	__utma	158690720.1917037331.1440894516.1442483167.1442492711.17
.kaggle.com	TRUE	/	FALSE	1442496811	__utmb	158690720.17.10.1442492711
.kaggle.com	TRUE	/	FALSE	0	__utmc	158690720
.kaggle.com	TRUE	/	FALSE	1458263011	__utmz	158690720.1442426440.14.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)
```


- scp this file to your EC2 with:

```
scp -i your_key.pem cookies.txt ubuntu@ec2-52-8-89-42.us-west-1.compute.amazonaws.com:./
```

- you have now successfully copied the kaggle cookies.txt to your EC2.
- Now proceed to the last step by downloading the kaggle files as in defined by kaggle:

https://github.com/wendykan/AWSGPU_DeepLearning/blob/master/setup.sh