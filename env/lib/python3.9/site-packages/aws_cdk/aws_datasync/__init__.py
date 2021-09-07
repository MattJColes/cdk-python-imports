'''
# AWS::DataSync Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_datasync as datasync
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAgent(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-datasync.CfnAgent",
):
    '''A CloudFormation ``AWS::DataSync::Agent``.

    :cloudformationResource: AWS::DataSync::Agent
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        activation_key: builtins.str,
        agent_name: typing.Optional[builtins.str] = None,
        security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_endpoint_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DataSync::Agent``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param activation_key: ``AWS::DataSync::Agent.ActivationKey``.
        :param agent_name: ``AWS::DataSync::Agent.AgentName``.
        :param security_group_arns: ``AWS::DataSync::Agent.SecurityGroupArns``.
        :param subnet_arns: ``AWS::DataSync::Agent.SubnetArns``.
        :param tags: ``AWS::DataSync::Agent.Tags``.
        :param vpc_endpoint_id: ``AWS::DataSync::Agent.VpcEndpointId``.
        '''
        props = CfnAgentProps(
            activation_key=activation_key,
            agent_name=agent_name,
            security_group_arns=security_group_arns,
            subnet_arns=subnet_arns,
            tags=tags,
            vpc_endpoint_id=vpc_endpoint_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAgentArn")
    def attr_agent_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AgentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEndpointType")
    def attr_endpoint_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: EndpointType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::DataSync::Agent.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="activationKey")
    def activation_key(self) -> builtins.str:
        '''``AWS::DataSync::Agent.ActivationKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-activationkey
        '''
        return typing.cast(builtins.str, jsii.get(self, "activationKey"))

    @activation_key.setter
    def activation_key(self, value: builtins.str) -> None:
        jsii.set(self, "activationKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="agentName")
    def agent_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::Agent.AgentName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-agentname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentName"))

    @agent_name.setter
    def agent_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "agentName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupArns")
    def security_group_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::DataSync::Agent.SecurityGroupArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-securitygrouparns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupArns"))

    @security_group_arns.setter
    def security_group_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "securityGroupArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetArns")
    def subnet_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::DataSync::Agent.SubnetArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-subnetarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetArns"))

    @subnet_arns.setter
    def subnet_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "subnetArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcEndpointId")
    def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::Agent.VpcEndpointId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-vpcendpointid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcEndpointId"))

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "vpcEndpointId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-datasync.CfnAgentProps",
    jsii_struct_bases=[],
    name_mapping={
        "activation_key": "activationKey",
        "agent_name": "agentName",
        "security_group_arns": "securityGroupArns",
        "subnet_arns": "subnetArns",
        "tags": "tags",
        "vpc_endpoint_id": "vpcEndpointId",
    },
)
class CfnAgentProps:
    def __init__(
        self,
        *,
        activation_key: builtins.str,
        agent_name: typing.Optional[builtins.str] = None,
        security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_endpoint_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DataSync::Agent``.

        :param activation_key: ``AWS::DataSync::Agent.ActivationKey``.
        :param agent_name: ``AWS::DataSync::Agent.AgentName``.
        :param security_group_arns: ``AWS::DataSync::Agent.SecurityGroupArns``.
        :param subnet_arns: ``AWS::DataSync::Agent.SubnetArns``.
        :param tags: ``AWS::DataSync::Agent.Tags``.
        :param vpc_endpoint_id: ``AWS::DataSync::Agent.VpcEndpointId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "activation_key": activation_key,
        }
        if agent_name is not None:
            self._values["agent_name"] = agent_name
        if security_group_arns is not None:
            self._values["security_group_arns"] = security_group_arns
        if subnet_arns is not None:
            self._values["subnet_arns"] = subnet_arns
        if tags is not None:
            self._values["tags"] = tags
        if vpc_endpoint_id is not None:
            self._values["vpc_endpoint_id"] = vpc_endpoint_id

    @builtins.property
    def activation_key(self) -> builtins.str:
        '''``AWS::DataSync::Agent.ActivationKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-activationkey
        '''
        result = self._values.get("activation_key")
        assert result is not None, "Required property 'activation_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::Agent.AgentName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-agentname
        '''
        result = self._values.get("agent_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::DataSync::Agent.SecurityGroupArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-securitygrouparns
        '''
        result = self._values.get("security_group_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::DataSync::Agent.SubnetArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-subnetarns
        '''
        result = self._values.get("subnet_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::DataSync::Agent.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::Agent.VpcEndpointId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-vpcendpointid
        '''
        result = self._values.get("vpc_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAgentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLocationEFS(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-datasync.CfnLocationEFS",
):
    '''A CloudFormation ``AWS::DataSync::LocationEFS``.

    :cloudformationResource: AWS::DataSync::LocationEFS
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        ec2_config: typing.Union["CfnLocationEFS.Ec2ConfigProperty", aws_cdk.core.IResolvable],
        efs_filesystem_arn: builtins.str,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::DataSync::LocationEFS``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param ec2_config: ``AWS::DataSync::LocationEFS.Ec2Config``.
        :param efs_filesystem_arn: ``AWS::DataSync::LocationEFS.EfsFilesystemArn``.
        :param subdirectory: ``AWS::DataSync::LocationEFS.Subdirectory``.
        :param tags: ``AWS::DataSync::LocationEFS.Tags``.
        '''
        props = CfnLocationEFSProps(
            ec2_config=ec2_config,
            efs_filesystem_arn=efs_filesystem_arn,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::DataSync::LocationEFS.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2Config")
    def ec2_config(
        self,
    ) -> typing.Union["CfnLocationEFS.Ec2ConfigProperty", aws_cdk.core.IResolvable]:
        '''``AWS::DataSync::LocationEFS.Ec2Config``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-ec2config
        '''
        return typing.cast(typing.Union["CfnLocationEFS.Ec2ConfigProperty", aws_cdk.core.IResolvable], jsii.get(self, "ec2Config"))

    @ec2_config.setter
    def ec2_config(
        self,
        value: typing.Union["CfnLocationEFS.Ec2ConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "ec2Config", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="efsFilesystemArn")
    def efs_filesystem_arn(self) -> builtins.str:
        '''``AWS::DataSync::LocationEFS.EfsFilesystemArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-efsfilesystemarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "efsFilesystemArn"))

    @efs_filesystem_arn.setter
    def efs_filesystem_arn(self, value: builtins.str) -> None:
        jsii.set(self, "efsFilesystemArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationEFS.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-subdirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subdirectory", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-datasync.CfnLocationEFS.Ec2ConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_arns": "securityGroupArns",
            "subnet_arn": "subnetArn",
        },
    )
    class Ec2ConfigProperty:
        def __init__(
            self,
            *,
            security_group_arns: typing.Sequence[builtins.str],
            subnet_arn: builtins.str,
        ) -> None:
            '''
            :param security_group_arns: ``CfnLocationEFS.Ec2ConfigProperty.SecurityGroupArns``.
            :param subnet_arn: ``CfnLocationEFS.Ec2ConfigProperty.SubnetArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_arns": security_group_arns,
                "subnet_arn": subnet_arn,
            }

        @builtins.property
        def security_group_arns(self) -> typing.List[builtins.str]:
            '''``CfnLocationEFS.Ec2ConfigProperty.SecurityGroupArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-securitygrouparns
            '''
            result = self._values.get("security_group_arns")
            assert result is not None, "Required property 'security_group_arns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_arn(self) -> builtins.str:
            '''``CfnLocationEFS.Ec2ConfigProperty.SubnetArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-subnetarn
            '''
            result = self._values.get("subnet_arn")
            assert result is not None, "Required property 'subnet_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Ec2ConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-datasync.CfnLocationEFSProps",
    jsii_struct_bases=[],
    name_mapping={
        "ec2_config": "ec2Config",
        "efs_filesystem_arn": "efsFilesystemArn",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationEFSProps:
    def __init__(
        self,
        *,
        ec2_config: typing.Union[CfnLocationEFS.Ec2ConfigProperty, aws_cdk.core.IResolvable],
        efs_filesystem_arn: builtins.str,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DataSync::LocationEFS``.

        :param ec2_config: ``AWS::DataSync::LocationEFS.Ec2Config``.
        :param efs_filesystem_arn: ``AWS::DataSync::LocationEFS.EfsFilesystemArn``.
        :param subdirectory: ``AWS::DataSync::LocationEFS.Subdirectory``.
        :param tags: ``AWS::DataSync::LocationEFS.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "ec2_config": ec2_config,
            "efs_filesystem_arn": efs_filesystem_arn,
        }
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def ec2_config(
        self,
    ) -> typing.Union[CfnLocationEFS.Ec2ConfigProperty, aws_cdk.core.IResolvable]:
        '''``AWS::DataSync::LocationEFS.Ec2Config``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-ec2config
        '''
        result = self._values.get("ec2_config")
        assert result is not None, "Required property 'ec2_config' is missing"
        return typing.cast(typing.Union[CfnLocationEFS.Ec2ConfigProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def efs_filesystem_arn(self) -> builtins.str:
        '''``AWS::DataSync::LocationEFS.EfsFilesystemArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-efsfilesystemarn
        '''
        result = self._values.get("efs_filesystem_arn")
        assert result is not None, "Required property 'efs_filesystem_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationEFS.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::DataSync::LocationEFS.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationEFSProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLocationFSxWindows(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-datasync.CfnLocationFSxWindows",
):
    '''A CloudFormation ``AWS::DataSync::LocationFSxWindows``.

    :cloudformationResource: AWS::DataSync::LocationFSxWindows
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        fsx_filesystem_arn: builtins.str,
        password: builtins.str,
        security_group_arns: typing.Sequence[builtins.str],
        user: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::DataSync::LocationFSxWindows``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param fsx_filesystem_arn: ``AWS::DataSync::LocationFSxWindows.FsxFilesystemArn``.
        :param password: ``AWS::DataSync::LocationFSxWindows.Password``.
        :param security_group_arns: ``AWS::DataSync::LocationFSxWindows.SecurityGroupArns``.
        :param user: ``AWS::DataSync::LocationFSxWindows.User``.
        :param domain: ``AWS::DataSync::LocationFSxWindows.Domain``.
        :param subdirectory: ``AWS::DataSync::LocationFSxWindows.Subdirectory``.
        :param tags: ``AWS::DataSync::LocationFSxWindows.Tags``.
        '''
        props = CfnLocationFSxWindowsProps(
            fsx_filesystem_arn=fsx_filesystem_arn,
            password=password,
            security_group_arns=security_group_arns,
            user=user,
            domain=domain,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::DataSync::LocationFSxWindows.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> builtins.str:
        '''``AWS::DataSync::LocationFSxWindows.FsxFilesystemArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-fsxfilesystemarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "fsxFilesystemArn"))

    @fsx_filesystem_arn.setter
    def fsx_filesystem_arn(self, value: builtins.str) -> None:
        jsii.set(self, "fsxFilesystemArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        '''``AWS::DataSync::LocationFSxWindows.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-password
        '''
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        jsii.set(self, "password", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupArns")
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''``AWS::DataSync::LocationFSxWindows.SecurityGroupArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-securitygrouparns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupArns"))

    @security_group_arns.setter
    def security_group_arns(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "securityGroupArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        '''``AWS::DataSync::LocationFSxWindows.User``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-user
        '''
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        jsii.set(self, "user", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationFSxWindows.Domain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-domain
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "domain", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationFSxWindows.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-subdirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subdirectory", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-datasync.CfnLocationFSxWindowsProps",
    jsii_struct_bases=[],
    name_mapping={
        "fsx_filesystem_arn": "fsxFilesystemArn",
        "password": "password",
        "security_group_arns": "securityGroupArns",
        "user": "user",
        "domain": "domain",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationFSxWindowsProps:
    def __init__(
        self,
        *,
        fsx_filesystem_arn: builtins.str,
        password: builtins.str,
        security_group_arns: typing.Sequence[builtins.str],
        user: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DataSync::LocationFSxWindows``.

        :param fsx_filesystem_arn: ``AWS::DataSync::LocationFSxWindows.FsxFilesystemArn``.
        :param password: ``AWS::DataSync::LocationFSxWindows.Password``.
        :param security_group_arns: ``AWS::DataSync::LocationFSxWindows.SecurityGroupArns``.
        :param user: ``AWS::DataSync::LocationFSxWindows.User``.
        :param domain: ``AWS::DataSync::LocationFSxWindows.Domain``.
        :param subdirectory: ``AWS::DataSync::LocationFSxWindows.Subdirectory``.
        :param tags: ``AWS::DataSync::LocationFSxWindows.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "fsx_filesystem_arn": fsx_filesystem_arn,
            "password": password,
            "security_group_arns": security_group_arns,
            "user": user,
        }
        if domain is not None:
            self._values["domain"] = domain
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def fsx_filesystem_arn(self) -> builtins.str:
        '''``AWS::DataSync::LocationFSxWindows.FsxFilesystemArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-fsxfilesystemarn
        '''
        result = self._values.get("fsx_filesystem_arn")
        assert result is not None, "Required property 'fsx_filesystem_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''``AWS::DataSync::LocationFSxWindows.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_arns(self) -> typing.List[builtins.str]:
        '''``AWS::DataSync::LocationFSxWindows.SecurityGroupArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-securitygrouparns
        '''
        result = self._values.get("security_group_arns")
        assert result is not None, "Required property 'security_group_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def user(self) -> builtins.str:
        '''``AWS::DataSync::LocationFSxWindows.User``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-user
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationFSxWindows.Domain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationFSxWindows.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::DataSync::LocationFSxWindows.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationFSxWindowsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLocationNFS(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-datasync.CfnLocationNFS",
):
    '''A CloudFormation ``AWS::DataSync::LocationNFS``.

    :cloudformationResource: AWS::DataSync::LocationNFS
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        on_prem_config: typing.Union[aws_cdk.core.IResolvable, "CfnLocationNFS.OnPremConfigProperty"],
        server_hostname: builtins.str,
        subdirectory: builtins.str,
        mount_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLocationNFS.MountOptionsProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::DataSync::LocationNFS``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param on_prem_config: ``AWS::DataSync::LocationNFS.OnPremConfig``.
        :param server_hostname: ``AWS::DataSync::LocationNFS.ServerHostname``.
        :param subdirectory: ``AWS::DataSync::LocationNFS.Subdirectory``.
        :param mount_options: ``AWS::DataSync::LocationNFS.MountOptions``.
        :param tags: ``AWS::DataSync::LocationNFS.Tags``.
        '''
        props = CfnLocationNFSProps(
            on_prem_config=on_prem_config,
            server_hostname=server_hostname,
            subdirectory=subdirectory,
            mount_options=mount_options,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::DataSync::LocationNFS.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="onPremConfig")
    def on_prem_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnLocationNFS.OnPremConfigProperty"]:
        '''``AWS::DataSync::LocationNFS.OnPremConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-onpremconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnLocationNFS.OnPremConfigProperty"], jsii.get(self, "onPremConfig"))

    @on_prem_config.setter
    def on_prem_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnLocationNFS.OnPremConfigProperty"],
    ) -> None:
        jsii.set(self, "onPremConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverHostname")
    def server_hostname(self) -> builtins.str:
        '''``AWS::DataSync::LocationNFS.ServerHostname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-serverhostname
        '''
        return typing.cast(builtins.str, jsii.get(self, "serverHostname"))

    @server_hostname.setter
    def server_hostname(self, value: builtins.str) -> None:
        jsii.set(self, "serverHostname", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> builtins.str:
        '''``AWS::DataSync::LocationNFS.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-subdirectory
        '''
        return typing.cast(builtins.str, jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: builtins.str) -> None:
        jsii.set(self, "subdirectory", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mountOptions")
    def mount_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLocationNFS.MountOptionsProperty"]]:
        '''``AWS::DataSync::LocationNFS.MountOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-mountoptions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLocationNFS.MountOptionsProperty"]], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLocationNFS.MountOptionsProperty"]],
    ) -> None:
        jsii.set(self, "mountOptions", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-datasync.CfnLocationNFS.MountOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"version": "version"},
    )
    class MountOptionsProperty:
        def __init__(self, *, version: typing.Optional[builtins.str] = None) -> None:
            '''
            :param version: ``CfnLocationNFS.MountOptionsProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''``CfnLocationNFS.MountOptionsProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html#cfn-datasync-locationnfs-mountoptions-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MountOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-datasync.CfnLocationNFS.OnPremConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"agent_arns": "agentArns"},
    )
    class OnPremConfigProperty:
        def __init__(self, *, agent_arns: typing.Sequence[builtins.str]) -> None:
            '''
            :param agent_arns: ``CfnLocationNFS.OnPremConfigProperty.AgentArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "agent_arns": agent_arns,
            }

        @builtins.property
        def agent_arns(self) -> typing.List[builtins.str]:
            '''``CfnLocationNFS.OnPremConfigProperty.AgentArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html#cfn-datasync-locationnfs-onpremconfig-agentarns
            '''
            result = self._values.get("agent_arns")
            assert result is not None, "Required property 'agent_arns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnPremConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-datasync.CfnLocationNFSProps",
    jsii_struct_bases=[],
    name_mapping={
        "on_prem_config": "onPremConfig",
        "server_hostname": "serverHostname",
        "subdirectory": "subdirectory",
        "mount_options": "mountOptions",
        "tags": "tags",
    },
)
class CfnLocationNFSProps:
    def __init__(
        self,
        *,
        on_prem_config: typing.Union[aws_cdk.core.IResolvable, CfnLocationNFS.OnPremConfigProperty],
        server_hostname: builtins.str,
        subdirectory: builtins.str,
        mount_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLocationNFS.MountOptionsProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DataSync::LocationNFS``.

        :param on_prem_config: ``AWS::DataSync::LocationNFS.OnPremConfig``.
        :param server_hostname: ``AWS::DataSync::LocationNFS.ServerHostname``.
        :param subdirectory: ``AWS::DataSync::LocationNFS.Subdirectory``.
        :param mount_options: ``AWS::DataSync::LocationNFS.MountOptions``.
        :param tags: ``AWS::DataSync::LocationNFS.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "on_prem_config": on_prem_config,
            "server_hostname": server_hostname,
            "subdirectory": subdirectory,
        }
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def on_prem_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnLocationNFS.OnPremConfigProperty]:
        '''``AWS::DataSync::LocationNFS.OnPremConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-onpremconfig
        '''
        result = self._values.get("on_prem_config")
        assert result is not None, "Required property 'on_prem_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnLocationNFS.OnPremConfigProperty], result)

    @builtins.property
    def server_hostname(self) -> builtins.str:
        '''``AWS::DataSync::LocationNFS.ServerHostname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-serverhostname
        '''
        result = self._values.get("server_hostname")
        assert result is not None, "Required property 'server_hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subdirectory(self) -> builtins.str:
        '''``AWS::DataSync::LocationNFS.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-subdirectory
        '''
        result = self._values.get("subdirectory")
        assert result is not None, "Required property 'subdirectory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLocationNFS.MountOptionsProperty]]:
        '''``AWS::DataSync::LocationNFS.MountOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-mountoptions
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLocationNFS.MountOptionsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::DataSync::LocationNFS.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationNFSProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLocationObjectStorage(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-datasync.CfnLocationObjectStorage",
):
    '''A CloudFormation ``AWS::DataSync::LocationObjectStorage``.

    :cloudformationResource: AWS::DataSync::LocationObjectStorage
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        agent_arns: typing.Sequence[builtins.str],
        bucket_name: builtins.str,
        server_hostname: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        server_port: typing.Optional[jsii.Number] = None,
        server_protocol: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::DataSync::LocationObjectStorage``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param agent_arns: ``AWS::DataSync::LocationObjectStorage.AgentArns``.
        :param bucket_name: ``AWS::DataSync::LocationObjectStorage.BucketName``.
        :param server_hostname: ``AWS::DataSync::LocationObjectStorage.ServerHostname``.
        :param access_key: ``AWS::DataSync::LocationObjectStorage.AccessKey``.
        :param secret_key: ``AWS::DataSync::LocationObjectStorage.SecretKey``.
        :param server_port: ``AWS::DataSync::LocationObjectStorage.ServerPort``.
        :param server_protocol: ``AWS::DataSync::LocationObjectStorage.ServerProtocol``.
        :param subdirectory: ``AWS::DataSync::LocationObjectStorage.Subdirectory``.
        :param tags: ``AWS::DataSync::LocationObjectStorage.Tags``.
        '''
        props = CfnLocationObjectStorageProps(
            agent_arns=agent_arns,
            bucket_name=bucket_name,
            server_hostname=server_hostname,
            access_key=access_key,
            secret_key=secret_key,
            server_port=server_port,
            server_protocol=server_protocol,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::DataSync::LocationObjectStorage.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.AgentArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-agentarns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "agentArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        '''``AWS::DataSync::LocationObjectStorage.BucketName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-bucketname
        '''
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        jsii.set(self, "bucketName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverHostname")
    def server_hostname(self) -> builtins.str:
        '''``AWS::DataSync::LocationObjectStorage.ServerHostname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverhostname
        '''
        return typing.cast(builtins.str, jsii.get(self, "serverHostname"))

    @server_hostname.setter
    def server_hostname(self, value: builtins.str) -> None:
        jsii.set(self, "serverHostname", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.AccessKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-accesskey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "accessKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.SecretKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-secretkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "secretKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverPort")
    def server_port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::DataSync::LocationObjectStorage.ServerPort``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverport
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serverPort"))

    @server_port.setter
    def server_port(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "serverPort", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverProtocol")
    def server_protocol(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.ServerProtocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverprotocol
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverProtocol"))

    @server_protocol.setter
    def server_protocol(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serverProtocol", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-subdirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subdirectory", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-datasync.CfnLocationObjectStorageProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_arns": "agentArns",
        "bucket_name": "bucketName",
        "server_hostname": "serverHostname",
        "access_key": "accessKey",
        "secret_key": "secretKey",
        "server_port": "serverPort",
        "server_protocol": "serverProtocol",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationObjectStorageProps:
    def __init__(
        self,
        *,
        agent_arns: typing.Sequence[builtins.str],
        bucket_name: builtins.str,
        server_hostname: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        server_port: typing.Optional[jsii.Number] = None,
        server_protocol: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DataSync::LocationObjectStorage``.

        :param agent_arns: ``AWS::DataSync::LocationObjectStorage.AgentArns``.
        :param bucket_name: ``AWS::DataSync::LocationObjectStorage.BucketName``.
        :param server_hostname: ``AWS::DataSync::LocationObjectStorage.ServerHostname``.
        :param access_key: ``AWS::DataSync::LocationObjectStorage.AccessKey``.
        :param secret_key: ``AWS::DataSync::LocationObjectStorage.SecretKey``.
        :param server_port: ``AWS::DataSync::LocationObjectStorage.ServerPort``.
        :param server_protocol: ``AWS::DataSync::LocationObjectStorage.ServerProtocol``.
        :param subdirectory: ``AWS::DataSync::LocationObjectStorage.Subdirectory``.
        :param tags: ``AWS::DataSync::LocationObjectStorage.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "agent_arns": agent_arns,
            "bucket_name": bucket_name,
            "server_hostname": server_hostname,
        }
        if access_key is not None:
            self._values["access_key"] = access_key
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if server_port is not None:
            self._values["server_port"] = server_port
        if server_protocol is not None:
            self._values["server_protocol"] = server_protocol
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_arns(self) -> typing.List[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.AgentArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-agentarns
        '''
        result = self._values.get("agent_arns")
        assert result is not None, "Required property 'agent_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''``AWS::DataSync::LocationObjectStorage.BucketName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-bucketname
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_hostname(self) -> builtins.str:
        '''``AWS::DataSync::LocationObjectStorage.ServerHostname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverhostname
        '''
        result = self._values.get("server_hostname")
        assert result is not None, "Required property 'server_hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.AccessKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-accesskey
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.SecretKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-secretkey
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::DataSync::LocationObjectStorage.ServerPort``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverport
        '''
        result = self._values.get("server_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_protocol(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.ServerProtocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverprotocol
        '''
        result = self._values.get("server_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationObjectStorage.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::DataSync::LocationObjectStorage.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationObjectStorageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLocationS3(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-datasync.CfnLocationS3",
):
    '''A CloudFormation ``AWS::DataSync::LocationS3``.

    :cloudformationResource: AWS::DataSync::LocationS3
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        s3_bucket_arn: builtins.str,
        s3_config: typing.Union[aws_cdk.core.IResolvable, "CfnLocationS3.S3ConfigProperty"],
        s3_storage_class: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::DataSync::LocationS3``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param s3_bucket_arn: ``AWS::DataSync::LocationS3.S3BucketArn``.
        :param s3_config: ``AWS::DataSync::LocationS3.S3Config``.
        :param s3_storage_class: ``AWS::DataSync::LocationS3.S3StorageClass``.
        :param subdirectory: ``AWS::DataSync::LocationS3.Subdirectory``.
        :param tags: ``AWS::DataSync::LocationS3.Tags``.
        '''
        props = CfnLocationS3Props(
            s3_bucket_arn=s3_bucket_arn,
            s3_config=s3_config,
            s3_storage_class=s3_storage_class,
            subdirectory=subdirectory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::DataSync::LocationS3.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3BucketArn")
    def s3_bucket_arn(self) -> builtins.str:
        '''``AWS::DataSync::LocationS3.S3BucketArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "s3BucketArn"))

    @s3_bucket_arn.setter
    def s3_bucket_arn(self, value: builtins.str) -> None:
        jsii.set(self, "s3BucketArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3Config")
    def s3_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnLocationS3.S3ConfigProperty"]:
        '''``AWS::DataSync::LocationS3.S3Config``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnLocationS3.S3ConfigProperty"], jsii.get(self, "s3Config"))

    @s3_config.setter
    def s3_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnLocationS3.S3ConfigProperty"],
    ) -> None:
        jsii.set(self, "s3Config", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3StorageClass")
    def s3_storage_class(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationS3.S3StorageClass``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3StorageClass"))

    @s3_storage_class.setter
    def s3_storage_class(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "s3StorageClass", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationS3.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subdirectory", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-datasync.CfnLocationS3.S3ConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_access_role_arn": "bucketAccessRoleArn"},
    )
    class S3ConfigProperty:
        def __init__(self, *, bucket_access_role_arn: builtins.str) -> None:
            '''
            :param bucket_access_role_arn: ``CfnLocationS3.S3ConfigProperty.BucketAccessRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_access_role_arn": bucket_access_role_arn,
            }

        @builtins.property
        def bucket_access_role_arn(self) -> builtins.str:
            '''``CfnLocationS3.S3ConfigProperty.BucketAccessRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html#cfn-datasync-locations3-s3config-bucketaccessrolearn
            '''
            result = self._values.get("bucket_access_role_arn")
            assert result is not None, "Required property 'bucket_access_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-datasync.CfnLocationS3Props",
    jsii_struct_bases=[],
    name_mapping={
        "s3_bucket_arn": "s3BucketArn",
        "s3_config": "s3Config",
        "s3_storage_class": "s3StorageClass",
        "subdirectory": "subdirectory",
        "tags": "tags",
    },
)
class CfnLocationS3Props:
    def __init__(
        self,
        *,
        s3_bucket_arn: builtins.str,
        s3_config: typing.Union[aws_cdk.core.IResolvable, CfnLocationS3.S3ConfigProperty],
        s3_storage_class: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DataSync::LocationS3``.

        :param s3_bucket_arn: ``AWS::DataSync::LocationS3.S3BucketArn``.
        :param s3_config: ``AWS::DataSync::LocationS3.S3Config``.
        :param s3_storage_class: ``AWS::DataSync::LocationS3.S3StorageClass``.
        :param subdirectory: ``AWS::DataSync::LocationS3.Subdirectory``.
        :param tags: ``AWS::DataSync::LocationS3.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "s3_bucket_arn": s3_bucket_arn,
            "s3_config": s3_config,
        }
        if s3_storage_class is not None:
            self._values["s3_storage_class"] = s3_storage_class
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def s3_bucket_arn(self) -> builtins.str:
        '''``AWS::DataSync::LocationS3.S3BucketArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn
        '''
        result = self._values.get("s3_bucket_arn")
        assert result is not None, "Required property 's3_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnLocationS3.S3ConfigProperty]:
        '''``AWS::DataSync::LocationS3.S3Config``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config
        '''
        result = self._values.get("s3_config")
        assert result is not None, "Required property 's3_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnLocationS3.S3ConfigProperty], result)

    @builtins.property
    def s3_storage_class(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationS3.S3StorageClass``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass
        '''
        result = self._values.get("s3_storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationS3.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory
        '''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::DataSync::LocationS3.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationS3Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLocationSMB(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-datasync.CfnLocationSMB",
):
    '''A CloudFormation ``AWS::DataSync::LocationSMB``.

    :cloudformationResource: AWS::DataSync::LocationSMB
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        agent_arns: typing.Sequence[builtins.str],
        password: builtins.str,
        server_hostname: builtins.str,
        subdirectory: builtins.str,
        user: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLocationSMB.MountOptionsProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::DataSync::LocationSMB``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param agent_arns: ``AWS::DataSync::LocationSMB.AgentArns``.
        :param password: ``AWS::DataSync::LocationSMB.Password``.
        :param server_hostname: ``AWS::DataSync::LocationSMB.ServerHostname``.
        :param subdirectory: ``AWS::DataSync::LocationSMB.Subdirectory``.
        :param user: ``AWS::DataSync::LocationSMB.User``.
        :param domain: ``AWS::DataSync::LocationSMB.Domain``.
        :param mount_options: ``AWS::DataSync::LocationSMB.MountOptions``.
        :param tags: ``AWS::DataSync::LocationSMB.Tags``.
        '''
        props = CfnLocationSMBProps(
            agent_arns=agent_arns,
            password=password,
            server_hostname=server_hostname,
            subdirectory=subdirectory,
            user=user,
            domain=domain,
            mount_options=mount_options,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLocationUri")
    def attr_location_uri(self) -> builtins.str:
        '''
        :cloudformationAttribute: LocationUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationUri"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::DataSync::LocationSMB.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        '''``AWS::DataSync::LocationSMB.AgentArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-agentarns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "agentArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        '''``AWS::DataSync::LocationSMB.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-password
        '''
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        jsii.set(self, "password", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverHostname")
    def server_hostname(self) -> builtins.str:
        '''``AWS::DataSync::LocationSMB.ServerHostname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-serverhostname
        '''
        return typing.cast(builtins.str, jsii.get(self, "serverHostname"))

    @server_hostname.setter
    def server_hostname(self, value: builtins.str) -> None:
        jsii.set(self, "serverHostname", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> builtins.str:
        '''``AWS::DataSync::LocationSMB.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-subdirectory
        '''
        return typing.cast(builtins.str, jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: builtins.str) -> None:
        jsii.set(self, "subdirectory", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        '''``AWS::DataSync::LocationSMB.User``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-user
        '''
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        jsii.set(self, "user", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationSMB.Domain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-domain
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "domain", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mountOptions")
    def mount_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLocationSMB.MountOptionsProperty"]]:
        '''``AWS::DataSync::LocationSMB.MountOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-mountoptions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLocationSMB.MountOptionsProperty"]], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLocationSMB.MountOptionsProperty"]],
    ) -> None:
        jsii.set(self, "mountOptions", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-datasync.CfnLocationSMB.MountOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"version": "version"},
    )
    class MountOptionsProperty:
        def __init__(self, *, version: typing.Optional[builtins.str] = None) -> None:
            '''
            :param version: ``CfnLocationSMB.MountOptionsProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''``CfnLocationSMB.MountOptionsProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html#cfn-datasync-locationsmb-mountoptions-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MountOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-datasync.CfnLocationSMBProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_arns": "agentArns",
        "password": "password",
        "server_hostname": "serverHostname",
        "subdirectory": "subdirectory",
        "user": "user",
        "domain": "domain",
        "mount_options": "mountOptions",
        "tags": "tags",
    },
)
class CfnLocationSMBProps:
    def __init__(
        self,
        *,
        agent_arns: typing.Sequence[builtins.str],
        password: builtins.str,
        server_hostname: builtins.str,
        subdirectory: builtins.str,
        user: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLocationSMB.MountOptionsProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DataSync::LocationSMB``.

        :param agent_arns: ``AWS::DataSync::LocationSMB.AgentArns``.
        :param password: ``AWS::DataSync::LocationSMB.Password``.
        :param server_hostname: ``AWS::DataSync::LocationSMB.ServerHostname``.
        :param subdirectory: ``AWS::DataSync::LocationSMB.Subdirectory``.
        :param user: ``AWS::DataSync::LocationSMB.User``.
        :param domain: ``AWS::DataSync::LocationSMB.Domain``.
        :param mount_options: ``AWS::DataSync::LocationSMB.MountOptions``.
        :param tags: ``AWS::DataSync::LocationSMB.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "agent_arns": agent_arns,
            "password": password,
            "server_hostname": server_hostname,
            "subdirectory": subdirectory,
            "user": user,
        }
        if domain is not None:
            self._values["domain"] = domain
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_arns(self) -> typing.List[builtins.str]:
        '''``AWS::DataSync::LocationSMB.AgentArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-agentarns
        '''
        result = self._values.get("agent_arns")
        assert result is not None, "Required property 'agent_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def password(self) -> builtins.str:
        '''``AWS::DataSync::LocationSMB.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_hostname(self) -> builtins.str:
        '''``AWS::DataSync::LocationSMB.ServerHostname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-serverhostname
        '''
        result = self._values.get("server_hostname")
        assert result is not None, "Required property 'server_hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subdirectory(self) -> builtins.str:
        '''``AWS::DataSync::LocationSMB.Subdirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-subdirectory
        '''
        result = self._values.get("subdirectory")
        assert result is not None, "Required property 'subdirectory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user(self) -> builtins.str:
        '''``AWS::DataSync::LocationSMB.User``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-user
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::LocationSMB.Domain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLocationSMB.MountOptionsProperty]]:
        '''``AWS::DataSync::LocationSMB.MountOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-mountoptions
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLocationSMB.MountOptionsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::DataSync::LocationSMB.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationSMBProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTask(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-datasync.CfnTask",
):
    '''A CloudFormation ``AWS::DataSync::Task``.

    :cloudformationResource: AWS::DataSync::Task
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        destination_location_arn: builtins.str,
        source_location_arn: builtins.str,
        cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
        excludes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnTask.FilterRuleProperty"]]]] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTask.OptionsProperty"]] = None,
        schedule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTask.TaskScheduleProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::DataSync::Task``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param destination_location_arn: ``AWS::DataSync::Task.DestinationLocationArn``.
        :param source_location_arn: ``AWS::DataSync::Task.SourceLocationArn``.
        :param cloud_watch_log_group_arn: ``AWS::DataSync::Task.CloudWatchLogGroupArn``.
        :param excludes: ``AWS::DataSync::Task.Excludes``.
        :param name: ``AWS::DataSync::Task.Name``.
        :param options: ``AWS::DataSync::Task.Options``.
        :param schedule: ``AWS::DataSync::Task.Schedule``.
        :param tags: ``AWS::DataSync::Task.Tags``.
        '''
        props = CfnTaskProps(
            destination_location_arn=destination_location_arn,
            source_location_arn=source_location_arn,
            cloud_watch_log_group_arn=cloud_watch_log_group_arn,
            excludes=excludes,
            name=name,
            options=options,
            schedule=schedule,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDestinationNetworkInterfaceArns")
    def attr_destination_network_interface_arns(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: DestinationNetworkInterfaceArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDestinationNetworkInterfaceArns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrErrorCode")
    def attr_error_code(self) -> builtins.str:
        '''
        :cloudformationAttribute: ErrorCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrErrorCode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrErrorDetail")
    def attr_error_detail(self) -> builtins.str:
        '''
        :cloudformationAttribute: ErrorDetail
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrErrorDetail"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSourceNetworkInterfaceArns")
    def attr_source_network_interface_arns(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: SourceNetworkInterfaceArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrSourceNetworkInterfaceArns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTaskArn")
    def attr_task_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: TaskArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTaskArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::DataSync::Task.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="destinationLocationArn")
    def destination_location_arn(self) -> builtins.str:
        '''``AWS::DataSync::Task.DestinationLocationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-destinationlocationarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "destinationLocationArn"))

    @destination_location_arn.setter
    def destination_location_arn(self, value: builtins.str) -> None:
        jsii.set(self, "destinationLocationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceLocationArn")
    def source_location_arn(self) -> builtins.str:
        '''``AWS::DataSync::Task.SourceLocationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-sourcelocationarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "sourceLocationArn"))

    @source_location_arn.setter
    def source_location_arn(self, value: builtins.str) -> None:
        jsii.set(self, "sourceLocationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::Task.CloudWatchLogGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-cloudwatchloggrouparn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogGroupArn"))

    @cloud_watch_log_group_arn.setter
    def cloud_watch_log_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cloudWatchLogGroupArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludes")
    def excludes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTask.FilterRuleProperty"]]]]:
        '''``AWS::DataSync::Task.Excludes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-excludes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTask.FilterRuleProperty"]]]], jsii.get(self, "excludes"))

    @excludes.setter
    def excludes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTask.FilterRuleProperty"]]]],
    ) -> None:
        jsii.set(self, "excludes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::Task.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="options")
    def options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTask.OptionsProperty"]]:
        '''``AWS::DataSync::Task.Options``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-options
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTask.OptionsProperty"]], jsii.get(self, "options"))

    @options.setter
    def options(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTask.OptionsProperty"]],
    ) -> None:
        jsii.set(self, "options", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTask.TaskScheduleProperty"]]:
        '''``AWS::DataSync::Task.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-schedule
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTask.TaskScheduleProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTask.TaskScheduleProperty"]],
    ) -> None:
        jsii.set(self, "schedule", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-datasync.CfnTask.FilterRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"filter_type": "filterType", "value": "value"},
    )
    class FilterRuleProperty:
        def __init__(
            self,
            *,
            filter_type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param filter_type: ``CfnTask.FilterRuleProperty.FilterType``.
            :param value: ``CfnTask.FilterRuleProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if filter_type is not None:
                self._values["filter_type"] = filter_type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def filter_type(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.FilterRuleProperty.FilterType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-filtertype
            '''
            result = self._values.get("filter_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.FilterRuleProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-datasync.CfnTask.OptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "atime": "atime",
            "bytes_per_second": "bytesPerSecond",
            "gid": "gid",
            "log_level": "logLevel",
            "mtime": "mtime",
            "overwrite_mode": "overwriteMode",
            "posix_permissions": "posixPermissions",
            "preserve_deleted_files": "preserveDeletedFiles",
            "preserve_devices": "preserveDevices",
            "security_descriptor_copy_flags": "securityDescriptorCopyFlags",
            "task_queueing": "taskQueueing",
            "transfer_mode": "transferMode",
            "uid": "uid",
            "verify_mode": "verifyMode",
        },
    )
    class OptionsProperty:
        def __init__(
            self,
            *,
            atime: typing.Optional[builtins.str] = None,
            bytes_per_second: typing.Optional[jsii.Number] = None,
            gid: typing.Optional[builtins.str] = None,
            log_level: typing.Optional[builtins.str] = None,
            mtime: typing.Optional[builtins.str] = None,
            overwrite_mode: typing.Optional[builtins.str] = None,
            posix_permissions: typing.Optional[builtins.str] = None,
            preserve_deleted_files: typing.Optional[builtins.str] = None,
            preserve_devices: typing.Optional[builtins.str] = None,
            security_descriptor_copy_flags: typing.Optional[builtins.str] = None,
            task_queueing: typing.Optional[builtins.str] = None,
            transfer_mode: typing.Optional[builtins.str] = None,
            uid: typing.Optional[builtins.str] = None,
            verify_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param atime: ``CfnTask.OptionsProperty.Atime``.
            :param bytes_per_second: ``CfnTask.OptionsProperty.BytesPerSecond``.
            :param gid: ``CfnTask.OptionsProperty.Gid``.
            :param log_level: ``CfnTask.OptionsProperty.LogLevel``.
            :param mtime: ``CfnTask.OptionsProperty.Mtime``.
            :param overwrite_mode: ``CfnTask.OptionsProperty.OverwriteMode``.
            :param posix_permissions: ``CfnTask.OptionsProperty.PosixPermissions``.
            :param preserve_deleted_files: ``CfnTask.OptionsProperty.PreserveDeletedFiles``.
            :param preserve_devices: ``CfnTask.OptionsProperty.PreserveDevices``.
            :param security_descriptor_copy_flags: ``CfnTask.OptionsProperty.SecurityDescriptorCopyFlags``.
            :param task_queueing: ``CfnTask.OptionsProperty.TaskQueueing``.
            :param transfer_mode: ``CfnTask.OptionsProperty.TransferMode``.
            :param uid: ``CfnTask.OptionsProperty.Uid``.
            :param verify_mode: ``CfnTask.OptionsProperty.VerifyMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if atime is not None:
                self._values["atime"] = atime
            if bytes_per_second is not None:
                self._values["bytes_per_second"] = bytes_per_second
            if gid is not None:
                self._values["gid"] = gid
            if log_level is not None:
                self._values["log_level"] = log_level
            if mtime is not None:
                self._values["mtime"] = mtime
            if overwrite_mode is not None:
                self._values["overwrite_mode"] = overwrite_mode
            if posix_permissions is not None:
                self._values["posix_permissions"] = posix_permissions
            if preserve_deleted_files is not None:
                self._values["preserve_deleted_files"] = preserve_deleted_files
            if preserve_devices is not None:
                self._values["preserve_devices"] = preserve_devices
            if security_descriptor_copy_flags is not None:
                self._values["security_descriptor_copy_flags"] = security_descriptor_copy_flags
            if task_queueing is not None:
                self._values["task_queueing"] = task_queueing
            if transfer_mode is not None:
                self._values["transfer_mode"] = transfer_mode
            if uid is not None:
                self._values["uid"] = uid
            if verify_mode is not None:
                self._values["verify_mode"] = verify_mode

        @builtins.property
        def atime(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.Atime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-atime
            '''
            result = self._values.get("atime")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bytes_per_second(self) -> typing.Optional[jsii.Number]:
            '''``CfnTask.OptionsProperty.BytesPerSecond``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-bytespersecond
            '''
            result = self._values.get("bytes_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gid(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.Gid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-gid
            '''
            result = self._values.get("gid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.LogLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mtime(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.Mtime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-mtime
            '''
            result = self._values.get("mtime")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def overwrite_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.OverwriteMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-overwritemode
            '''
            result = self._values.get("overwrite_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def posix_permissions(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.PosixPermissions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-posixpermissions
            '''
            result = self._values.get("posix_permissions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preserve_deleted_files(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.PreserveDeletedFiles``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedeletedfiles
            '''
            result = self._values.get("preserve_deleted_files")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preserve_devices(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.PreserveDevices``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedevices
            '''
            result = self._values.get("preserve_devices")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_descriptor_copy_flags(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.SecurityDescriptorCopyFlags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-securitydescriptorcopyflags
            '''
            result = self._values.get("security_descriptor_copy_flags")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def task_queueing(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.TaskQueueing``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-taskqueueing
            '''
            result = self._values.get("task_queueing")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def transfer_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.TransferMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-transfermode
            '''
            result = self._values.get("transfer_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uid(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.Uid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-uid
            '''
            result = self._values.get("uid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def verify_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnTask.OptionsProperty.VerifyMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-verifymode
            '''
            result = self._values.get("verify_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-datasync.CfnTask.TaskScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule_expression": "scheduleExpression"},
    )
    class TaskScheduleProperty:
        def __init__(self, *, schedule_expression: builtins.str) -> None:
            '''
            :param schedule_expression: ``CfnTask.TaskScheduleProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''``CfnTask.TaskScheduleProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html#cfn-datasync-task-taskschedule-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-datasync.CfnTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_location_arn": "destinationLocationArn",
        "source_location_arn": "sourceLocationArn",
        "cloud_watch_log_group_arn": "cloudWatchLogGroupArn",
        "excludes": "excludes",
        "name": "name",
        "options": "options",
        "schedule": "schedule",
        "tags": "tags",
    },
)
class CfnTaskProps:
    def __init__(
        self,
        *,
        destination_location_arn: builtins.str,
        source_location_arn: builtins.str,
        cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
        excludes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnTask.FilterRuleProperty]]]] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTask.OptionsProperty]] = None,
        schedule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTask.TaskScheduleProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DataSync::Task``.

        :param destination_location_arn: ``AWS::DataSync::Task.DestinationLocationArn``.
        :param source_location_arn: ``AWS::DataSync::Task.SourceLocationArn``.
        :param cloud_watch_log_group_arn: ``AWS::DataSync::Task.CloudWatchLogGroupArn``.
        :param excludes: ``AWS::DataSync::Task.Excludes``.
        :param name: ``AWS::DataSync::Task.Name``.
        :param options: ``AWS::DataSync::Task.Options``.
        :param schedule: ``AWS::DataSync::Task.Schedule``.
        :param tags: ``AWS::DataSync::Task.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "destination_location_arn": destination_location_arn,
            "source_location_arn": source_location_arn,
        }
        if cloud_watch_log_group_arn is not None:
            self._values["cloud_watch_log_group_arn"] = cloud_watch_log_group_arn
        if excludes is not None:
            self._values["excludes"] = excludes
        if name is not None:
            self._values["name"] = name
        if options is not None:
            self._values["options"] = options
        if schedule is not None:
            self._values["schedule"] = schedule
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination_location_arn(self) -> builtins.str:
        '''``AWS::DataSync::Task.DestinationLocationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-destinationlocationarn
        '''
        result = self._values.get("destination_location_arn")
        assert result is not None, "Required property 'destination_location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_location_arn(self) -> builtins.str:
        '''``AWS::DataSync::Task.SourceLocationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-sourcelocationarn
        '''
        result = self._values.get("source_location_arn")
        assert result is not None, "Required property 'source_location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_watch_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::Task.CloudWatchLogGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-cloudwatchloggrouparn
        '''
        result = self._values.get("cloud_watch_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def excludes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTask.FilterRuleProperty]]]]:
        '''``AWS::DataSync::Task.Excludes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-excludes
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTask.FilterRuleProperty]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DataSync::Task.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTask.OptionsProperty]]:
        '''``AWS::DataSync::Task.Options``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-options
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTask.OptionsProperty]], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTask.TaskScheduleProperty]]:
        '''``AWS::DataSync::Task.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTask.TaskScheduleProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::DataSync::Task.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAgent",
    "CfnAgentProps",
    "CfnLocationEFS",
    "CfnLocationEFSProps",
    "CfnLocationFSxWindows",
    "CfnLocationFSxWindowsProps",
    "CfnLocationNFS",
    "CfnLocationNFSProps",
    "CfnLocationObjectStorage",
    "CfnLocationObjectStorageProps",
    "CfnLocationS3",
    "CfnLocationS3Props",
    "CfnLocationSMB",
    "CfnLocationSMBProps",
    "CfnTask",
    "CfnTaskProps",
]

publication.publish()
