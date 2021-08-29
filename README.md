# cdk-python-imports

## Summary
Sample Project to showcase:

* Importing cloudformation resources into CDK
* Looking up existing resources using cdk `from_lookups`

To explore the project, open up ```cdk_python\cdk_python_stack.py```. The first section of this class imports cloudformation (located in the ```cdk_python\cformation_s3.json``` file) into your CDK project for use as part of your CDK stack. The second half of the code shows how to create a VPC with CDK and lookup your existing VPC and Subnets.

## Getting Started

### Pre-requisites

* Python 3.6+ installed: https://www.python.org/downloads/
* NodeJS installed (for cdk cli): https://nodejs.org/en/download/
* AWS CLI installed: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
* AWS ClI configured and linked to an aws account / user / region via running ```aws configure``` within your terminal

### Steps to run

* Install cdk cli via running ```npm install -g aws-cdk``` within your terminal
* Run the following command to bootstrap to your aws environment ```cdk bootstrap```
* Edit ```app.py``` and add your aws account number and region within the ```existing_environment``` object
* Run ```CDK deploy``` to deploy the app

Enjoy :)
