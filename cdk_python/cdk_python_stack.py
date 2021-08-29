from aws_cdk import (
    core as cdk,
    cloudformation_include as cfn_inc,
    aws_s3 as s3,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    aws_ec2 as ec2,
    aws_iam as iam
)


class CdkPythonStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ####################################################################################
        # Example 1 - Importing cloudformation resources into CDK
        ####################################################################################

        # Import Existing Cloudformation Stack
        template = cfn_inc.CfnInclude(
            self, "Template",
            template_file="cdk_python\cformation_s3.json",
            preserve_logical_ids=True
        )

        # Use within CDK and convert to a L2 construct
        existing_bucket_l1 = template.get_resource("S3B4E9YC")
        existing_bucket_l2 = s3.Bucket.from_bucket_name(
            self, "Bucket", existing_bucket_l1.ref
        )

        # Show it being used with a lambda!
        handler = lambda_.Function(self, "WidgetHandler",
                                   runtime=lambda_.Runtime.NODEJS_10_X,
                                   code=lambda_.Code.from_asset(
                                       ".\cdk_python\lambda"
                                   ),
                                   handler="widgets.main",
                                   environment=dict(
                                       BUCKET=existing_bucket_l2.bucket_name
                                   )
                                   )

        existing_bucket_l2.grant_read_write(handler)

        api = apigateway.RestApi(self, "widgets-api",
                                 rest_api_name="Widget Service",
                                 description="This service serves widgets.")

        get_widgets_integration = apigateway.LambdaIntegration(handler,
                                                               request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_widgets_integration)   # GET /

        ####################################################################################
        # Example 2 - Referencing existing resources using CDK `from_lookups` feature
        ####################################################################################

        # You can use lookups for importing VPC's within environments like
        existing_vpc = ec2.Vpc.from_lookup(self, "TestVPC",
                                           is_default=False,
                                           vpc_name="TestVPC"
                                           )

        # Deploy an SSM managed EC2 instance within the VPC with a basic security group
        security_group = ec2.SecurityGroup(
            self,
            "ssh-security-group",
            vpc=existing_vpc,
            allow_all_outbound=True,
        )

        security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4('10.2.0.0/16'),
            description="allow ssh",
            connection=ec2.Port.tcp(22)
        )

        role = iam.Role(self, "InstanceSSM",
                        assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name(
            "AmazonSSMManagedInstanceCore"))

        ec2_instance = ec2.Instance(
            self,
            "ec2-instance",
            instance_name="ec2-instance01",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                edition=ec2.AmazonLinuxEdition.STANDARD,
                virtualization=ec2.AmazonLinuxVirt.HVM,
                storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
            ),
            vpc=existing_vpc,
            security_group=security_group,
        )
