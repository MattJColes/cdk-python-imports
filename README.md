# cdk-python-imports

## Summary
Sample Project to showcase:

* Importing cloudformation resources into CDK
* Referencing existing resources using CDK `from_lookups` feature (used to find common resources like VPC's,Subnets, Load Balancers, etc)

To explore the project, open up ```cdk_python\cdk_python_stack.py```. 
The first section of this class imports cloudformation (located in the ```cdk_python\cformation_s3.json``` file) into your CDK project for use as part of your CDK stack. 
The second section of the code shows how to create a VPC with CDK and lookup your existing VPC and Subnets.

## Getting Started

### Pre-requisites:

* Python 3.6+ installed: https://www.python.org/downloads/
* NodeJS installed (for cdk cli): https://nodejs.org/en/download/
* AWS CLI installed: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
* AWS CLI configured and linked to an aws account / user / region via running ```aws configure``` within your terminal

### Steps to run:

* Install cdk cli via running ```npm install -g aws-cdk``` within your terminal
* In your terminal run ```python3 -m venv env``` to create a Python virtual environment followed by ```source env/bin/activate``` to activate the virtual environment
* Run ```pip install -r requirements.txt``` within your terminal to pull down cdk and python dependencies
* Enter the following command to bootstrap to your aws environment ```cdk bootstrap```
* Edit ```app.py``` and add your aws account number and region within the ```existing_environment``` object
* Run ```cdk deploy``` to deploy the app

Enjoy :)
