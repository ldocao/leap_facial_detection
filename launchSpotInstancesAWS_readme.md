# Configuring and launching spot instance on Amazon Web Services 

1. Select EC2 (to arrive at EC2 dashboard)
2. In top right corner of dashboard, change region to "US West (N.California)"
3. On left panel of dashboard, find "Instances" and select "Spot Requests"
4. Select button for "Request Spot Instances"
5. On left panel of "Step 1: Choose Amazon Machine Image" page, select "Community AMIs"
6. In the search box, search for "ami-b141a2f5" and press "Select"
 - note, AMI # chosen is from following blog: http://markus.com/install-theano-on-aws/
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