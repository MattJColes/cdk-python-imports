'''
# AWS::NetworkFirewall Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_networkfirewall as networkfirewall
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
class CfnFirewall(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewall",
):
    '''A CloudFormation ``AWS::NetworkFirewall::Firewall``.

    :cloudformationResource: AWS::NetworkFirewall::Firewall
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        firewall_name: builtins.str,
        firewall_policy_arn: builtins.str,
        subnet_mappings: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnFirewall.SubnetMappingProperty"]]],
        vpc_id: builtins.str,
        delete_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        firewall_policy_change_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        subnet_change_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkFirewall::Firewall``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param firewall_name: ``AWS::NetworkFirewall::Firewall.FirewallName``.
        :param firewall_policy_arn: ``AWS::NetworkFirewall::Firewall.FirewallPolicyArn``.
        :param subnet_mappings: ``AWS::NetworkFirewall::Firewall.SubnetMappings``.
        :param vpc_id: ``AWS::NetworkFirewall::Firewall.VpcId``.
        :param delete_protection: ``AWS::NetworkFirewall::Firewall.DeleteProtection``.
        :param description: ``AWS::NetworkFirewall::Firewall.Description``.
        :param firewall_policy_change_protection: ``AWS::NetworkFirewall::Firewall.FirewallPolicyChangeProtection``.
        :param subnet_change_protection: ``AWS::NetworkFirewall::Firewall.SubnetChangeProtection``.
        :param tags: ``AWS::NetworkFirewall::Firewall.Tags``.
        '''
        props = CfnFirewallProps(
            firewall_name=firewall_name,
            firewall_policy_arn=firewall_policy_arn,
            subnet_mappings=subnet_mappings,
            vpc_id=vpc_id,
            delete_protection=delete_protection,
            description=description,
            firewall_policy_change_protection=firewall_policy_change_protection,
            subnet_change_protection=subnet_change_protection,
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
    @jsii.member(jsii_name="attrEndpointIds")
    def attr_endpoint_ids(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: EndpointIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrEndpointIds"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrFirewallArn")
    def attr_firewall_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: FirewallArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrFirewallId")
    def attr_firewall_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: FirewallId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NetworkFirewall::Firewall.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallName")
    def firewall_name(self) -> builtins.str:
        '''``AWS::NetworkFirewall::Firewall.FirewallName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallname
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallName"))

    @firewall_name.setter
    def firewall_name(self, value: builtins.str) -> None:
        jsii.set(self, "firewallName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallPolicyArn")
    def firewall_policy_arn(self) -> builtins.str:
        '''``AWS::NetworkFirewall::Firewall.FirewallPolicyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicyarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicyArn"))

    @firewall_policy_arn.setter
    def firewall_policy_arn(self, value: builtins.str) -> None:
        jsii.set(self, "firewallPolicyArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetMappings")
    def subnet_mappings(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewall.SubnetMappingProperty"]]]:
        '''``AWS::NetworkFirewall::Firewall.SubnetMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetmappings
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewall.SubnetMappingProperty"]]], jsii.get(self, "subnetMappings"))

    @subnet_mappings.setter
    def subnet_mappings(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewall.SubnetMappingProperty"]]],
    ) -> None:
        jsii.set(self, "subnetMappings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''``AWS::NetworkFirewall::Firewall.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-vpcid
        '''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        jsii.set(self, "vpcId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deleteProtection")
    def delete_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::NetworkFirewall::Firewall.DeleteProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-deleteprotection
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "deleteProtection"))

    @delete_protection.setter
    def delete_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "deleteProtection", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkFirewall::Firewall.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallPolicyChangeProtection")
    def firewall_policy_change_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::NetworkFirewall::Firewall.FirewallPolicyChangeProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicychangeprotection
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "firewallPolicyChangeProtection"))

    @firewall_policy_change_protection.setter
    def firewall_policy_change_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "firewallPolicyChangeProtection", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetChangeProtection")
    def subnet_change_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::NetworkFirewall::Firewall.SubnetChangeProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetchangeprotection
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "subnetChangeProtection"))

    @subnet_change_protection.setter
    def subnet_change_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "subnetChangeProtection", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewall.SubnetMappingProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_id": "subnetId"},
    )
    class SubnetMappingProperty:
        def __init__(self, *, subnet_id: builtins.str) -> None:
            '''
            :param subnet_id: ``CfnFirewall.SubnetMappingProperty.SubnetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "subnet_id": subnet_id,
            }

        @builtins.property
        def subnet_id(self) -> builtins.str:
            '''``CfnFirewall.SubnetMappingProperty.SubnetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html#cfn-networkfirewall-firewall-subnetmapping-subnetid
            '''
            result = self._values.get("subnet_id")
            assert result is not None, "Required property 'subnet_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubnetMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFirewallPolicy(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallPolicy",
):
    '''A CloudFormation ``AWS::NetworkFirewall::FirewallPolicy``.

    :cloudformationResource: AWS::NetworkFirewall::FirewallPolicy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        firewall_policy: typing.Union["CfnFirewallPolicy.FirewallPolicyProperty", aws_cdk.core.IResolvable],
        firewall_policy_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkFirewall::FirewallPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param firewall_policy: ``AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy``.
        :param firewall_policy_name: ``AWS::NetworkFirewall::FirewallPolicy.FirewallPolicyName``.
        :param description: ``AWS::NetworkFirewall::FirewallPolicy.Description``.
        :param tags: ``AWS::NetworkFirewall::FirewallPolicy.Tags``.
        '''
        props = CfnFirewallPolicyProps(
            firewall_policy=firewall_policy,
            firewall_policy_name=firewall_policy_name,
            description=description,
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
    @jsii.member(jsii_name="attrFirewallPolicyArn")
    def attr_firewall_policy_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: FirewallPolicyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallPolicyArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrFirewallPolicyId")
    def attr_firewall_policy_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: FirewallPolicyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallPolicyId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NetworkFirewall::FirewallPolicy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallPolicy")
    def firewall_policy(
        self,
    ) -> typing.Union["CfnFirewallPolicy.FirewallPolicyProperty", aws_cdk.core.IResolvable]:
        '''``AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy
        '''
        return typing.cast(typing.Union["CfnFirewallPolicy.FirewallPolicyProperty", aws_cdk.core.IResolvable], jsii.get(self, "firewallPolicy"))

    @firewall_policy.setter
    def firewall_policy(
        self,
        value: typing.Union["CfnFirewallPolicy.FirewallPolicyProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "firewallPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallPolicyName")
    def firewall_policy_name(self) -> builtins.str:
        '''``AWS::NetworkFirewall::FirewallPolicy.FirewallPolicyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicyname
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicyName"))

    @firewall_policy_name.setter
    def firewall_policy_name(self, value: builtins.str) -> None:
        jsii.set(self, "firewallPolicyName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkFirewall::FirewallPolicy.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallPolicy.ActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"publish_metric_action": "publishMetricAction"},
    )
    class ActionDefinitionProperty:
        def __init__(
            self,
            *,
            publish_metric_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.PublishMetricActionProperty"]] = None,
        ) -> None:
            '''
            :param publish_metric_action: ``CfnFirewallPolicy.ActionDefinitionProperty.PublishMetricAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if publish_metric_action is not None:
                self._values["publish_metric_action"] = publish_metric_action

        @builtins.property
        def publish_metric_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.PublishMetricActionProperty"]]:
            '''``CfnFirewallPolicy.ActionDefinitionProperty.PublishMetricAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html#cfn-networkfirewall-firewallpolicy-actiondefinition-publishmetricaction
            '''
            result = self._values.get("publish_metric_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.PublishMetricActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallPolicy.CustomActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_definition": "actionDefinition",
            "action_name": "actionName",
        },
    )
    class CustomActionProperty:
        def __init__(
            self,
            *,
            action_definition: typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.ActionDefinitionProperty"],
            action_name: builtins.str,
        ) -> None:
            '''
            :param action_definition: ``CfnFirewallPolicy.CustomActionProperty.ActionDefinition``.
            :param action_name: ``CfnFirewallPolicy.CustomActionProperty.ActionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action_definition": action_definition,
                "action_name": action_name,
            }

        @builtins.property
        def action_definition(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.ActionDefinitionProperty"]:
            '''``CfnFirewallPolicy.CustomActionProperty.ActionDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actiondefinition
            '''
            result = self._values.get("action_definition")
            assert result is not None, "Required property 'action_definition' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.ActionDefinitionProperty"], result)

        @builtins.property
        def action_name(self) -> builtins.str:
            '''``CfnFirewallPolicy.CustomActionProperty.ActionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actionname
            '''
            result = self._values.get("action_name")
            assert result is not None, "Required property 'action_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallPolicy.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, value: builtins.str) -> None:
            '''
            :param value: ``CfnFirewallPolicy.DimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnFirewallPolicy.DimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html#cfn-networkfirewall-firewallpolicy-dimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallPolicy.FirewallPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "stateless_default_actions": "statelessDefaultActions",
            "stateless_fragment_default_actions": "statelessFragmentDefaultActions",
            "stateful_rule_group_references": "statefulRuleGroupReferences",
            "stateless_custom_actions": "statelessCustomActions",
            "stateless_rule_group_references": "statelessRuleGroupReferences",
        },
    )
    class FirewallPolicyProperty:
        def __init__(
            self,
            *,
            stateless_default_actions: typing.Sequence[builtins.str],
            stateless_fragment_default_actions: typing.Sequence[builtins.str],
            stateful_rule_group_references: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.StatefulRuleGroupReferenceProperty"]]]] = None,
            stateless_custom_actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.CustomActionProperty"]]]] = None,
            stateless_rule_group_references: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.StatelessRuleGroupReferenceProperty"]]]] = None,
        ) -> None:
            '''
            :param stateless_default_actions: ``CfnFirewallPolicy.FirewallPolicyProperty.StatelessDefaultActions``.
            :param stateless_fragment_default_actions: ``CfnFirewallPolicy.FirewallPolicyProperty.StatelessFragmentDefaultActions``.
            :param stateful_rule_group_references: ``CfnFirewallPolicy.FirewallPolicyProperty.StatefulRuleGroupReferences``.
            :param stateless_custom_actions: ``CfnFirewallPolicy.FirewallPolicyProperty.StatelessCustomActions``.
            :param stateless_rule_group_references: ``CfnFirewallPolicy.FirewallPolicyProperty.StatelessRuleGroupReferences``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "stateless_default_actions": stateless_default_actions,
                "stateless_fragment_default_actions": stateless_fragment_default_actions,
            }
            if stateful_rule_group_references is not None:
                self._values["stateful_rule_group_references"] = stateful_rule_group_references
            if stateless_custom_actions is not None:
                self._values["stateless_custom_actions"] = stateless_custom_actions
            if stateless_rule_group_references is not None:
                self._values["stateless_rule_group_references"] = stateless_rule_group_references

        @builtins.property
        def stateless_default_actions(self) -> typing.List[builtins.str]:
            '''``CfnFirewallPolicy.FirewallPolicyProperty.StatelessDefaultActions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessdefaultactions
            '''
            result = self._values.get("stateless_default_actions")
            assert result is not None, "Required property 'stateless_default_actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def stateless_fragment_default_actions(self) -> typing.List[builtins.str]:
            '''``CfnFirewallPolicy.FirewallPolicyProperty.StatelessFragmentDefaultActions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessfragmentdefaultactions
            '''
            result = self._values.get("stateless_fragment_default_actions")
            assert result is not None, "Required property 'stateless_fragment_default_actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def stateful_rule_group_references(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.StatefulRuleGroupReferenceProperty"]]]]:
            '''``CfnFirewallPolicy.FirewallPolicyProperty.StatefulRuleGroupReferences``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulrulegroupreferences
            '''
            result = self._values.get("stateful_rule_group_references")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.StatefulRuleGroupReferenceProperty"]]]], result)

        @builtins.property
        def stateless_custom_actions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.CustomActionProperty"]]]]:
            '''``CfnFirewallPolicy.FirewallPolicyProperty.StatelessCustomActions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelesscustomactions
            '''
            result = self._values.get("stateless_custom_actions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.CustomActionProperty"]]]], result)

        @builtins.property
        def stateless_rule_group_references(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.StatelessRuleGroupReferenceProperty"]]]]:
            '''``CfnFirewallPolicy.FirewallPolicyProperty.StatelessRuleGroupReferences``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessrulegroupreferences
            '''
            result = self._values.get("stateless_rule_group_references")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.StatelessRuleGroupReferenceProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirewallPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallPolicy.PublishMetricActionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimensions": "dimensions"},
    )
    class PublishMetricActionProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.DimensionProperty"]]],
        ) -> None:
            '''
            :param dimensions: ``CfnFirewallPolicy.PublishMetricActionProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "dimensions": dimensions,
            }

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.DimensionProperty"]]]:
            '''``CfnFirewallPolicy.PublishMetricActionProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html#cfn-networkfirewall-firewallpolicy-publishmetricaction-dimensions
            '''
            result = self._values.get("dimensions")
            assert result is not None, "Required property 'dimensions' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFirewallPolicy.DimensionProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublishMetricActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallPolicy.StatefulRuleGroupReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class StatefulRuleGroupReferenceProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''
            :param resource_arn: ``CfnFirewallPolicy.StatefulRuleGroupReferenceProperty.ResourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''``CfnFirewallPolicy.StatefulRuleGroupReferenceProperty.ResourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatefulRuleGroupReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallPolicy.StatelessRuleGroupReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"priority": "priority", "resource_arn": "resourceArn"},
    )
    class StatelessRuleGroupReferenceProperty:
        def __init__(
            self,
            *,
            priority: jsii.Number,
            resource_arn: builtins.str,
        ) -> None:
            '''
            :param priority: ``CfnFirewallPolicy.StatelessRuleGroupReferenceProperty.Priority``.
            :param resource_arn: ``CfnFirewallPolicy.StatelessRuleGroupReferenceProperty.ResourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "priority": priority,
                "resource_arn": resource_arn,
            }

        @builtins.property
        def priority(self) -> jsii.Number:
            '''``CfnFirewallPolicy.StatelessRuleGroupReferenceProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''``CfnFirewallPolicy.StatelessRuleGroupReferenceProperty.ResourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatelessRuleGroupReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_policy": "firewallPolicy",
        "firewall_policy_name": "firewallPolicyName",
        "description": "description",
        "tags": "tags",
    },
)
class CfnFirewallPolicyProps:
    def __init__(
        self,
        *,
        firewall_policy: typing.Union[CfnFirewallPolicy.FirewallPolicyProperty, aws_cdk.core.IResolvable],
        firewall_policy_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkFirewall::FirewallPolicy``.

        :param firewall_policy: ``AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy``.
        :param firewall_policy_name: ``AWS::NetworkFirewall::FirewallPolicy.FirewallPolicyName``.
        :param description: ``AWS::NetworkFirewall::FirewallPolicy.Description``.
        :param tags: ``AWS::NetworkFirewall::FirewallPolicy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "firewall_policy": firewall_policy,
            "firewall_policy_name": firewall_policy_name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firewall_policy(
        self,
    ) -> typing.Union[CfnFirewallPolicy.FirewallPolicyProperty, aws_cdk.core.IResolvable]:
        '''``AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy
        '''
        result = self._values.get("firewall_policy")
        assert result is not None, "Required property 'firewall_policy' is missing"
        return typing.cast(typing.Union[CfnFirewallPolicy.FirewallPolicyProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def firewall_policy_name(self) -> builtins.str:
        '''``AWS::NetworkFirewall::FirewallPolicy.FirewallPolicyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicyname
        '''
        result = self._values.get("firewall_policy_name")
        assert result is not None, "Required property 'firewall_policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkFirewall::FirewallPolicy.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::NetworkFirewall::FirewallPolicy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkfirewall.CfnFirewallProps",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_name": "firewallName",
        "firewall_policy_arn": "firewallPolicyArn",
        "subnet_mappings": "subnetMappings",
        "vpc_id": "vpcId",
        "delete_protection": "deleteProtection",
        "description": "description",
        "firewall_policy_change_protection": "firewallPolicyChangeProtection",
        "subnet_change_protection": "subnetChangeProtection",
        "tags": "tags",
    },
)
class CfnFirewallProps:
    def __init__(
        self,
        *,
        firewall_name: builtins.str,
        firewall_policy_arn: builtins.str,
        subnet_mappings: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnFirewall.SubnetMappingProperty]]],
        vpc_id: builtins.str,
        delete_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        firewall_policy_change_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        subnet_change_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkFirewall::Firewall``.

        :param firewall_name: ``AWS::NetworkFirewall::Firewall.FirewallName``.
        :param firewall_policy_arn: ``AWS::NetworkFirewall::Firewall.FirewallPolicyArn``.
        :param subnet_mappings: ``AWS::NetworkFirewall::Firewall.SubnetMappings``.
        :param vpc_id: ``AWS::NetworkFirewall::Firewall.VpcId``.
        :param delete_protection: ``AWS::NetworkFirewall::Firewall.DeleteProtection``.
        :param description: ``AWS::NetworkFirewall::Firewall.Description``.
        :param firewall_policy_change_protection: ``AWS::NetworkFirewall::Firewall.FirewallPolicyChangeProtection``.
        :param subnet_change_protection: ``AWS::NetworkFirewall::Firewall.SubnetChangeProtection``.
        :param tags: ``AWS::NetworkFirewall::Firewall.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "firewall_name": firewall_name,
            "firewall_policy_arn": firewall_policy_arn,
            "subnet_mappings": subnet_mappings,
            "vpc_id": vpc_id,
        }
        if delete_protection is not None:
            self._values["delete_protection"] = delete_protection
        if description is not None:
            self._values["description"] = description
        if firewall_policy_change_protection is not None:
            self._values["firewall_policy_change_protection"] = firewall_policy_change_protection
        if subnet_change_protection is not None:
            self._values["subnet_change_protection"] = subnet_change_protection
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firewall_name(self) -> builtins.str:
        '''``AWS::NetworkFirewall::Firewall.FirewallName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallname
        '''
        result = self._values.get("firewall_name")
        assert result is not None, "Required property 'firewall_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_policy_arn(self) -> builtins.str:
        '''``AWS::NetworkFirewall::Firewall.FirewallPolicyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicyarn
        '''
        result = self._values.get("firewall_policy_arn")
        assert result is not None, "Required property 'firewall_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_mappings(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnFirewall.SubnetMappingProperty]]]:
        '''``AWS::NetworkFirewall::Firewall.SubnetMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetmappings
        '''
        result = self._values.get("subnet_mappings")
        assert result is not None, "Required property 'subnet_mappings' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnFirewall.SubnetMappingProperty]]], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''``AWS::NetworkFirewall::Firewall.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::NetworkFirewall::Firewall.DeleteProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-deleteprotection
        '''
        result = self._values.get("delete_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkFirewall::Firewall.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def firewall_policy_change_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::NetworkFirewall::Firewall.FirewallPolicyChangeProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicychangeprotection
        '''
        result = self._values.get("firewall_policy_change_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def subnet_change_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::NetworkFirewall::Firewall.SubnetChangeProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetchangeprotection
        '''
        result = self._values.get("subnet_change_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::NetworkFirewall::Firewall.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLoggingConfiguration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkfirewall.CfnLoggingConfiguration",
):
    '''A CloudFormation ``AWS::NetworkFirewall::LoggingConfiguration``.

    :cloudformationResource: AWS::NetworkFirewall::LoggingConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        firewall_arn: builtins.str,
        logging_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.LoggingConfigurationProperty"],
        firewall_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkFirewall::LoggingConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param firewall_arn: ``AWS::NetworkFirewall::LoggingConfiguration.FirewallArn``.
        :param logging_configuration: ``AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration``.
        :param firewall_name: ``AWS::NetworkFirewall::LoggingConfiguration.FirewallName``.
        '''
        props = CfnLoggingConfigurationProps(
            firewall_arn=firewall_arn,
            logging_configuration=logging_configuration,
            firewall_name=firewall_name,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallArn")
    def firewall_arn(self) -> builtins.str:
        '''``AWS::NetworkFirewall::LoggingConfiguration.FirewallArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallArn"))

    @firewall_arn.setter
    def firewall_arn(self, value: builtins.str) -> None:
        jsii.set(self, "firewallArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.LoggingConfigurationProperty"]:
        '''``AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.LoggingConfigurationProperty"], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.LoggingConfigurationProperty"],
    ) -> None:
        jsii.set(self, "loggingConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallName")
    def firewall_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkFirewall::LoggingConfiguration.FirewallName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallName"))

    @firewall_name.setter
    def firewall_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "firewallName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnLoggingConfiguration.LogDestinationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_destination": "logDestination",
            "log_destination_type": "logDestinationType",
            "log_type": "logType",
        },
    )
    class LogDestinationConfigProperty:
        def __init__(
            self,
            *,
            log_destination: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]],
            log_destination_type: builtins.str,
            log_type: builtins.str,
        ) -> None:
            '''
            :param log_destination: ``CfnLoggingConfiguration.LogDestinationConfigProperty.LogDestination``.
            :param log_destination_type: ``CfnLoggingConfiguration.LogDestinationConfigProperty.LogDestinationType``.
            :param log_type: ``CfnLoggingConfiguration.LogDestinationConfigProperty.LogType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "log_destination": log_destination,
                "log_destination_type": log_destination_type,
                "log_type": log_type,
            }

        @builtins.property
        def log_destination(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]:
            '''``CfnLoggingConfiguration.LogDestinationConfigProperty.LogDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestination
            '''
            result = self._values.get("log_destination")
            assert result is not None, "Required property 'log_destination' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]], result)

        @builtins.property
        def log_destination_type(self) -> builtins.str:
            '''``CfnLoggingConfiguration.LogDestinationConfigProperty.LogDestinationType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestinationtype
            '''
            result = self._values.get("log_destination_type")
            assert result is not None, "Required property 'log_destination_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_type(self) -> builtins.str:
            '''``CfnLoggingConfiguration.LogDestinationConfigProperty.LogType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logtype
            '''
            result = self._values.get("log_type")
            assert result is not None, "Required property 'log_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDestinationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnLoggingConfiguration.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_destination_configs": "logDestinationConfigs"},
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            log_destination_configs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.LogDestinationConfigProperty"]]],
        ) -> None:
            '''
            :param log_destination_configs: ``CfnLoggingConfiguration.LoggingConfigurationProperty.LogDestinationConfigs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "log_destination_configs": log_destination_configs,
            }

        @builtins.property
        def log_destination_configs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.LogDestinationConfigProperty"]]]:
            '''``CfnLoggingConfiguration.LoggingConfigurationProperty.LogDestinationConfigs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration-logdestinationconfigs
            '''
            result = self._values.get("log_destination_configs")
            assert result is not None, "Required property 'log_destination_configs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.LogDestinationConfigProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkfirewall.CfnLoggingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_arn": "firewallArn",
        "logging_configuration": "loggingConfiguration",
        "firewall_name": "firewallName",
    },
)
class CfnLoggingConfigurationProps:
    def __init__(
        self,
        *,
        firewall_arn: builtins.str,
        logging_configuration: typing.Union[aws_cdk.core.IResolvable, CfnLoggingConfiguration.LoggingConfigurationProperty],
        firewall_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkFirewall::LoggingConfiguration``.

        :param firewall_arn: ``AWS::NetworkFirewall::LoggingConfiguration.FirewallArn``.
        :param logging_configuration: ``AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration``.
        :param firewall_name: ``AWS::NetworkFirewall::LoggingConfiguration.FirewallName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "firewall_arn": firewall_arn,
            "logging_configuration": logging_configuration,
        }
        if firewall_name is not None:
            self._values["firewall_name"] = firewall_name

    @builtins.property
    def firewall_arn(self) -> builtins.str:
        '''``AWS::NetworkFirewall::LoggingConfiguration.FirewallArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallarn
        '''
        result = self._values.get("firewall_arn")
        assert result is not None, "Required property 'firewall_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnLoggingConfiguration.LoggingConfigurationProperty]:
        '''``AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        assert result is not None, "Required property 'logging_configuration' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnLoggingConfiguration.LoggingConfigurationProperty], result)

    @builtins.property
    def firewall_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkFirewall::LoggingConfiguration.FirewallName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallname
        '''
        result = self._values.get("firewall_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoggingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRuleGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup",
):
    '''A CloudFormation ``AWS::NetworkFirewall::RuleGroup``.

    :cloudformationResource: AWS::NetworkFirewall::RuleGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        capacity: jsii.Number,
        rule_group_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rule_group: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleGroupProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkFirewall::RuleGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param capacity: ``AWS::NetworkFirewall::RuleGroup.Capacity``.
        :param rule_group_name: ``AWS::NetworkFirewall::RuleGroup.RuleGroupName``.
        :param type: ``AWS::NetworkFirewall::RuleGroup.Type``.
        :param description: ``AWS::NetworkFirewall::RuleGroup.Description``.
        :param rule_group: ``AWS::NetworkFirewall::RuleGroup.RuleGroup``.
        :param tags: ``AWS::NetworkFirewall::RuleGroup.Tags``.
        '''
        props = CfnRuleGroupProps(
            capacity=capacity,
            rule_group_name=rule_group_name,
            type=type,
            description=description,
            rule_group=rule_group,
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
    @jsii.member(jsii_name="attrRuleGroupArn")
    def attr_rule_group_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: RuleGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRuleGroupId")
    def attr_rule_group_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: RuleGroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleGroupId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NetworkFirewall::RuleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        '''``AWS::NetworkFirewall::RuleGroup.Capacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-capacity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        jsii.set(self, "capacity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleGroupName")
    def rule_group_name(self) -> builtins.str:
        '''``AWS::NetworkFirewall::RuleGroup.RuleGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "ruleGroupName"))

    @rule_group_name.setter
    def rule_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "ruleGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::NetworkFirewall::RuleGroup.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkFirewall::RuleGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleGroup")
    def rule_group(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleGroupProperty"]]:
        '''``AWS::NetworkFirewall::RuleGroup.RuleGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleGroupProperty"]], jsii.get(self, "ruleGroup"))

    @rule_group.setter
    def rule_group(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleGroupProperty"]],
    ) -> None:
        jsii.set(self, "ruleGroup", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.ActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"publish_metric_action": "publishMetricAction"},
    )
    class ActionDefinitionProperty:
        def __init__(
            self,
            *,
            publish_metric_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PublishMetricActionProperty"]] = None,
        ) -> None:
            '''
            :param publish_metric_action: ``CfnRuleGroup.ActionDefinitionProperty.PublishMetricAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if publish_metric_action is not None:
                self._values["publish_metric_action"] = publish_metric_action

        @builtins.property
        def publish_metric_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PublishMetricActionProperty"]]:
            '''``CfnRuleGroup.ActionDefinitionProperty.PublishMetricAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html#cfn-networkfirewall-rulegroup-actiondefinition-publishmetricaction
            '''
            result = self._values.get("publish_metric_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PublishMetricActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.AddressProperty",
        jsii_struct_bases=[],
        name_mapping={"address_definition": "addressDefinition"},
    )
    class AddressProperty:
        def __init__(self, *, address_definition: builtins.str) -> None:
            '''
            :param address_definition: ``CfnRuleGroup.AddressProperty.AddressDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "address_definition": address_definition,
            }

        @builtins.property
        def address_definition(self) -> builtins.str:
            '''``CfnRuleGroup.AddressProperty.AddressDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html#cfn-networkfirewall-rulegroup-address-addressdefinition
            '''
            result = self._values.get("address_definition")
            assert result is not None, "Required property 'address_definition' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.CustomActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_definition": "actionDefinition",
            "action_name": "actionName",
        },
    )
    class CustomActionProperty:
        def __init__(
            self,
            *,
            action_definition: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ActionDefinitionProperty"],
            action_name: builtins.str,
        ) -> None:
            '''
            :param action_definition: ``CfnRuleGroup.CustomActionProperty.ActionDefinition``.
            :param action_name: ``CfnRuleGroup.CustomActionProperty.ActionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action_definition": action_definition,
                "action_name": action_name,
            }

        @builtins.property
        def action_definition(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ActionDefinitionProperty"]:
            '''``CfnRuleGroup.CustomActionProperty.ActionDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actiondefinition
            '''
            result = self._values.get("action_definition")
            assert result is not None, "Required property 'action_definition' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ActionDefinitionProperty"], result)

        @builtins.property
        def action_name(self) -> builtins.str:
            '''``CfnRuleGroup.CustomActionProperty.ActionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actionname
            '''
            result = self._values.get("action_name")
            assert result is not None, "Required property 'action_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, value: builtins.str) -> None:
            '''
            :param value: ``CfnRuleGroup.DimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnRuleGroup.DimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html#cfn-networkfirewall-rulegroup-dimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.HeaderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "destination_port": "destinationPort",
            "direction": "direction",
            "protocol": "protocol",
            "source": "source",
            "source_port": "sourcePort",
        },
    )
    class HeaderProperty:
        def __init__(
            self,
            *,
            destination: builtins.str,
            destination_port: builtins.str,
            direction: builtins.str,
            protocol: builtins.str,
            source: builtins.str,
            source_port: builtins.str,
        ) -> None:
            '''
            :param destination: ``CfnRuleGroup.HeaderProperty.Destination``.
            :param destination_port: ``CfnRuleGroup.HeaderProperty.DestinationPort``.
            :param direction: ``CfnRuleGroup.HeaderProperty.Direction``.
            :param protocol: ``CfnRuleGroup.HeaderProperty.Protocol``.
            :param source: ``CfnRuleGroup.HeaderProperty.Source``.
            :param source_port: ``CfnRuleGroup.HeaderProperty.SourcePort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "destination": destination,
                "destination_port": destination_port,
                "direction": direction,
                "protocol": protocol,
                "source": source,
                "source_port": source_port,
            }

        @builtins.property
        def destination(self) -> builtins.str:
            '''``CfnRuleGroup.HeaderProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_port(self) -> builtins.str:
            '''``CfnRuleGroup.HeaderProperty.DestinationPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destinationport
            '''
            result = self._values.get("destination_port")
            assert result is not None, "Required property 'destination_port' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def direction(self) -> builtins.str:
            '''``CfnRuleGroup.HeaderProperty.Direction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-direction
            '''
            result = self._values.get("direction")
            assert result is not None, "Required property 'direction' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''``CfnRuleGroup.HeaderProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''``CfnRuleGroup.HeaderProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_port(self) -> builtins.str:
            '''``CfnRuleGroup.HeaderProperty.SourcePort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-sourceport
            '''
            result = self._values.get("source_port")
            assert result is not None, "Required property 'source_port' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.interface(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.IPSetProperty"
    )
    class IPSetProperty(typing_extensions.Protocol):
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html
        '''

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="definition")
        def definition(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRuleGroup.IPSetProperty.Definition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html#cfn-networkfirewall-rulegroup-ipset-definition
            '''
            ...


    class _IPSetPropertyProxy:
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html
        '''

        __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-networkfirewall.CfnRuleGroup.IPSetProperty"

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="definition")
        def definition(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRuleGroup.IPSetProperty.Definition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html#cfn-networkfirewall-rulegroup-ipset-definition
            '''
            return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "definition"))

    # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
    typing.cast(typing.Any, IPSetProperty).__jsii_proxy_class__ = lambda : _IPSetPropertyProxy

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.MatchAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_ports": "destinationPorts",
            "destinations": "destinations",
            "protocols": "protocols",
            "source_ports": "sourcePorts",
            "sources": "sources",
            "tcp_flags": "tcpFlags",
        },
    )
    class MatchAttributesProperty:
        def __init__(
            self,
            *,
            destination_ports: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PortRangeProperty"]]]] = None,
            destinations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.AddressProperty"]]]] = None,
            protocols: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[jsii.Number]]] = None,
            source_ports: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PortRangeProperty"]]]] = None,
            sources: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.AddressProperty"]]]] = None,
            tcp_flags: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TCPFlagFieldProperty"]]]] = None,
        ) -> None:
            '''
            :param destination_ports: ``CfnRuleGroup.MatchAttributesProperty.DestinationPorts``.
            :param destinations: ``CfnRuleGroup.MatchAttributesProperty.Destinations``.
            :param protocols: ``CfnRuleGroup.MatchAttributesProperty.Protocols``.
            :param source_ports: ``CfnRuleGroup.MatchAttributesProperty.SourcePorts``.
            :param sources: ``CfnRuleGroup.MatchAttributesProperty.Sources``.
            :param tcp_flags: ``CfnRuleGroup.MatchAttributesProperty.TCPFlags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if destination_ports is not None:
                self._values["destination_ports"] = destination_ports
            if destinations is not None:
                self._values["destinations"] = destinations
            if protocols is not None:
                self._values["protocols"] = protocols
            if source_ports is not None:
                self._values["source_ports"] = source_ports
            if sources is not None:
                self._values["sources"] = sources
            if tcp_flags is not None:
                self._values["tcp_flags"] = tcp_flags

        @builtins.property
        def destination_ports(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PortRangeProperty"]]]]:
            '''``CfnRuleGroup.MatchAttributesProperty.DestinationPorts``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinationports
            '''
            result = self._values.get("destination_ports")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PortRangeProperty"]]]], result)

        @builtins.property
        def destinations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.AddressProperty"]]]]:
            '''``CfnRuleGroup.MatchAttributesProperty.Destinations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinations
            '''
            result = self._values.get("destinations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.AddressProperty"]]]], result)

        @builtins.property
        def protocols(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]]:
            '''``CfnRuleGroup.MatchAttributesProperty.Protocols``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-protocols
            '''
            result = self._values.get("protocols")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]], result)

        @builtins.property
        def source_ports(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PortRangeProperty"]]]]:
            '''``CfnRuleGroup.MatchAttributesProperty.SourcePorts``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sourceports
            '''
            result = self._values.get("source_ports")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PortRangeProperty"]]]], result)

        @builtins.property
        def sources(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.AddressProperty"]]]]:
            '''``CfnRuleGroup.MatchAttributesProperty.Sources``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sources
            '''
            result = self._values.get("sources")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.AddressProperty"]]]], result)

        @builtins.property
        def tcp_flags(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TCPFlagFieldProperty"]]]]:
            '''``CfnRuleGroup.MatchAttributesProperty.TCPFlags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-tcpflags
            '''
            result = self._values.get("tcp_flags")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TCPFlagFieldProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MatchAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.PortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"from_port": "fromPort", "to_port": "toPort"},
    )
    class PortRangeProperty:
        def __init__(self, *, from_port: jsii.Number, to_port: jsii.Number) -> None:
            '''
            :param from_port: ``CfnRuleGroup.PortRangeProperty.FromPort``.
            :param to_port: ``CfnRuleGroup.PortRangeProperty.ToPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "from_port": from_port,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''``CfnRuleGroup.PortRangeProperty.FromPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''``CfnRuleGroup.PortRangeProperty.ToPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.PortSetProperty",
        jsii_struct_bases=[],
        name_mapping={"definition": "definition"},
    )
    class PortSetProperty:
        def __init__(
            self,
            *,
            definition: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param definition: ``CfnRuleGroup.PortSetProperty.Definition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if definition is not None:
                self._values["definition"] = definition

        @builtins.property
        def definition(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRuleGroup.PortSetProperty.Definition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html#cfn-networkfirewall-rulegroup-portset-definition
            '''
            result = self._values.get("definition")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.PublishMetricActionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimensions": "dimensions"},
    )
    class PublishMetricActionProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.DimensionProperty"]]],
        ) -> None:
            '''
            :param dimensions: ``CfnRuleGroup.PublishMetricActionProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "dimensions": dimensions,
            }

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.DimensionProperty"]]]:
            '''``CfnRuleGroup.PublishMetricActionProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html#cfn-networkfirewall-rulegroup-publishmetricaction-dimensions
            '''
            result = self._values.get("dimensions")
            assert result is not None, "Required property 'dimensions' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.DimensionProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublishMetricActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.RuleDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "match_attributes": "matchAttributes"},
    )
    class RuleDefinitionProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            match_attributes: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.MatchAttributesProperty"],
        ) -> None:
            '''
            :param actions: ``CfnRuleGroup.RuleDefinitionProperty.Actions``.
            :param match_attributes: ``CfnRuleGroup.RuleDefinitionProperty.MatchAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "match_attributes": match_attributes,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''``CfnRuleGroup.RuleDefinitionProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def match_attributes(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.MatchAttributesProperty"]:
            '''``CfnRuleGroup.RuleDefinitionProperty.MatchAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-matchattributes
            '''
            result = self._values.get("match_attributes")
            assert result is not None, "Required property 'match_attributes' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.MatchAttributesProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.RuleGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rules_source": "rulesSource",
            "rule_variables": "ruleVariables",
        },
    )
    class RuleGroupProperty:
        def __init__(
            self,
            *,
            rules_source: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RulesSourceProperty"],
            rule_variables: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleVariablesProperty"]] = None,
        ) -> None:
            '''
            :param rules_source: ``CfnRuleGroup.RuleGroupProperty.RulesSource``.
            :param rule_variables: ``CfnRuleGroup.RuleGroupProperty.RuleVariables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "rules_source": rules_source,
            }
            if rule_variables is not None:
                self._values["rule_variables"] = rule_variables

        @builtins.property
        def rules_source(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RulesSourceProperty"]:
            '''``CfnRuleGroup.RuleGroupProperty.RulesSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulessource
            '''
            result = self._values.get("rules_source")
            assert result is not None, "Required property 'rules_source' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RulesSourceProperty"], result)

        @builtins.property
        def rule_variables(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleVariablesProperty"]]:
            '''``CfnRuleGroup.RuleGroupProperty.RuleVariables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulevariables
            '''
            result = self._values.get("rule_variables")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleVariablesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.RuleOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"keyword": "keyword", "settings": "settings"},
    )
    class RuleOptionProperty:
        def __init__(
            self,
            *,
            keyword: builtins.str,
            settings: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param keyword: ``CfnRuleGroup.RuleOptionProperty.Keyword``.
            :param settings: ``CfnRuleGroup.RuleOptionProperty.Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "keyword": keyword,
            }
            if settings is not None:
                self._values["settings"] = settings

        @builtins.property
        def keyword(self) -> builtins.str:
            '''``CfnRuleGroup.RuleOptionProperty.Keyword``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-keyword
            '''
            result = self._values.get("keyword")
            assert result is not None, "Required property 'keyword' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def settings(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRuleGroup.RuleOptionProperty.Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-settings
            '''
            result = self._values.get("settings")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.RuleVariablesProperty",
        jsii_struct_bases=[],
        name_mapping={"ip_sets": "ipSets", "port_sets": "portSets"},
    )
    class RuleVariablesProperty:
        def __init__(
            self,
            *,
            ip_sets: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.IPSetProperty"]]]] = None,
            port_sets: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PortSetProperty"]]]] = None,
        ) -> None:
            '''
            :param ip_sets: ``CfnRuleGroup.RuleVariablesProperty.IPSets``.
            :param port_sets: ``CfnRuleGroup.RuleVariablesProperty.PortSets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ip_sets is not None:
                self._values["ip_sets"] = ip_sets
            if port_sets is not None:
                self._values["port_sets"] = port_sets

        @builtins.property
        def ip_sets(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.IPSetProperty"]]]]:
            '''``CfnRuleGroup.RuleVariablesProperty.IPSets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-ipsets
            '''
            result = self._values.get("ip_sets")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.IPSetProperty"]]]], result)

        @builtins.property
        def port_sets(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PortSetProperty"]]]]:
            '''``CfnRuleGroup.RuleVariablesProperty.PortSets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-portsets
            '''
            result = self._values.get("port_sets")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.PortSetProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleVariablesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.RulesSourceListProperty",
        jsii_struct_bases=[],
        name_mapping={
            "generated_rules_type": "generatedRulesType",
            "targets": "targets",
            "target_types": "targetTypes",
        },
    )
    class RulesSourceListProperty:
        def __init__(
            self,
            *,
            generated_rules_type: builtins.str,
            targets: typing.Sequence[builtins.str],
            target_types: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param generated_rules_type: ``CfnRuleGroup.RulesSourceListProperty.GeneratedRulesType``.
            :param targets: ``CfnRuleGroup.RulesSourceListProperty.Targets``.
            :param target_types: ``CfnRuleGroup.RulesSourceListProperty.TargetTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "generated_rules_type": generated_rules_type,
                "targets": targets,
                "target_types": target_types,
            }

        @builtins.property
        def generated_rules_type(self) -> builtins.str:
            '''``CfnRuleGroup.RulesSourceListProperty.GeneratedRulesType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-generatedrulestype
            '''
            result = self._values.get("generated_rules_type")
            assert result is not None, "Required property 'generated_rules_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def targets(self) -> typing.List[builtins.str]:
            '''``CfnRuleGroup.RulesSourceListProperty.Targets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targets
            '''
            result = self._values.get("targets")
            assert result is not None, "Required property 'targets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def target_types(self) -> typing.List[builtins.str]:
            '''``CfnRuleGroup.RulesSourceListProperty.TargetTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targettypes
            '''
            result = self._values.get("target_types")
            assert result is not None, "Required property 'target_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RulesSourceListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.RulesSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rules_source_list": "rulesSourceList",
            "rules_string": "rulesString",
            "stateful_rules": "statefulRules",
            "stateless_rules_and_custom_actions": "statelessRulesAndCustomActions",
        },
    )
    class RulesSourceProperty:
        def __init__(
            self,
            *,
            rules_source_list: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RulesSourceListProperty"]] = None,
            rules_string: typing.Optional[builtins.str] = None,
            stateful_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatefulRuleProperty"]]]] = None,
            stateless_rules_and_custom_actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatelessRulesAndCustomActionsProperty"]] = None,
        ) -> None:
            '''
            :param rules_source_list: ``CfnRuleGroup.RulesSourceProperty.RulesSourceList``.
            :param rules_string: ``CfnRuleGroup.RulesSourceProperty.RulesString``.
            :param stateful_rules: ``CfnRuleGroup.RulesSourceProperty.StatefulRules``.
            :param stateless_rules_and_custom_actions: ``CfnRuleGroup.RulesSourceProperty.StatelessRulesAndCustomActions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if rules_source_list is not None:
                self._values["rules_source_list"] = rules_source_list
            if rules_string is not None:
                self._values["rules_string"] = rules_string
            if stateful_rules is not None:
                self._values["stateful_rules"] = stateful_rules
            if stateless_rules_and_custom_actions is not None:
                self._values["stateless_rules_and_custom_actions"] = stateless_rules_and_custom_actions

        @builtins.property
        def rules_source_list(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RulesSourceListProperty"]]:
            '''``CfnRuleGroup.RulesSourceProperty.RulesSourceList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulessourcelist
            '''
            result = self._values.get("rules_source_list")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RulesSourceListProperty"]], result)

        @builtins.property
        def rules_string(self) -> typing.Optional[builtins.str]:
            '''``CfnRuleGroup.RulesSourceProperty.RulesString``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulesstring
            '''
            result = self._values.get("rules_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stateful_rules(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatefulRuleProperty"]]]]:
            '''``CfnRuleGroup.RulesSourceProperty.StatefulRules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statefulrules
            '''
            result = self._values.get("stateful_rules")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatefulRuleProperty"]]]], result)

        @builtins.property
        def stateless_rules_and_custom_actions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatelessRulesAndCustomActionsProperty"]]:
            '''``CfnRuleGroup.RulesSourceProperty.StatelessRulesAndCustomActions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statelessrulesandcustomactions
            '''
            result = self._values.get("stateless_rules_and_custom_actions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatelessRulesAndCustomActionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RulesSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.StatefulRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "header": "header",
            "rule_options": "ruleOptions",
        },
    )
    class StatefulRuleProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            header: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.HeaderProperty"],
            rule_options: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleOptionProperty"]]],
        ) -> None:
            '''
            :param action: ``CfnRuleGroup.StatefulRuleProperty.Action``.
            :param header: ``CfnRuleGroup.StatefulRuleProperty.Header``.
            :param rule_options: ``CfnRuleGroup.StatefulRuleProperty.RuleOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
                "header": header,
                "rule_options": rule_options,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''``CfnRuleGroup.StatefulRuleProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def header(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.HeaderProperty"]:
            '''``CfnRuleGroup.StatefulRuleProperty.Header``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-header
            '''
            result = self._values.get("header")
            assert result is not None, "Required property 'header' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.HeaderProperty"], result)

        @builtins.property
        def rule_options(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleOptionProperty"]]]:
            '''``CfnRuleGroup.StatefulRuleProperty.RuleOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-ruleoptions
            '''
            result = self._values.get("rule_options")
            assert result is not None, "Required property 'rule_options' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleOptionProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatefulRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.StatelessRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"priority": "priority", "rule_definition": "ruleDefinition"},
    )
    class StatelessRuleProperty:
        def __init__(
            self,
            *,
            priority: jsii.Number,
            rule_definition: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleDefinitionProperty"],
        ) -> None:
            '''
            :param priority: ``CfnRuleGroup.StatelessRuleProperty.Priority``.
            :param rule_definition: ``CfnRuleGroup.StatelessRuleProperty.RuleDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "priority": priority,
                "rule_definition": rule_definition,
            }

        @builtins.property
        def priority(self) -> jsii.Number:
            '''``CfnRuleGroup.StatelessRuleProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rule_definition(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleDefinitionProperty"]:
            '''``CfnRuleGroup.StatelessRuleProperty.RuleDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-ruledefinition
            '''
            result = self._values.get("rule_definition")
            assert result is not None, "Required property 'rule_definition' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleDefinitionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatelessRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.StatelessRulesAndCustomActionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "stateless_rules": "statelessRules",
            "custom_actions": "customActions",
        },
    )
    class StatelessRulesAndCustomActionsProperty:
        def __init__(
            self,
            *,
            stateless_rules: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatelessRuleProperty"]]],
            custom_actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.CustomActionProperty"]]]] = None,
        ) -> None:
            '''
            :param stateless_rules: ``CfnRuleGroup.StatelessRulesAndCustomActionsProperty.StatelessRules``.
            :param custom_actions: ``CfnRuleGroup.StatelessRulesAndCustomActionsProperty.CustomActions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "stateless_rules": stateless_rules,
            }
            if custom_actions is not None:
                self._values["custom_actions"] = custom_actions

        @builtins.property
        def stateless_rules(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatelessRuleProperty"]]]:
            '''``CfnRuleGroup.StatelessRulesAndCustomActionsProperty.StatelessRules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-statelessrules
            '''
            result = self._values.get("stateless_rules")
            assert result is not None, "Required property 'stateless_rules' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatelessRuleProperty"]]], result)

        @builtins.property
        def custom_actions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.CustomActionProperty"]]]]:
            '''``CfnRuleGroup.StatelessRulesAndCustomActionsProperty.CustomActions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-customactions
            '''
            result = self._values.get("custom_actions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.CustomActionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatelessRulesAndCustomActionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroup.TCPFlagFieldProperty",
        jsii_struct_bases=[],
        name_mapping={"flags": "flags", "masks": "masks"},
    )
    class TCPFlagFieldProperty:
        def __init__(
            self,
            *,
            flags: typing.Sequence[builtins.str],
            masks: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param flags: ``CfnRuleGroup.TCPFlagFieldProperty.Flags``.
            :param masks: ``CfnRuleGroup.TCPFlagFieldProperty.Masks``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "flags": flags,
            }
            if masks is not None:
                self._values["masks"] = masks

        @builtins.property
        def flags(self) -> typing.List[builtins.str]:
            '''``CfnRuleGroup.TCPFlagFieldProperty.Flags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-flags
            '''
            result = self._values.get("flags")
            assert result is not None, "Required property 'flags' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def masks(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRuleGroup.TCPFlagFieldProperty.Masks``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-masks
            '''
            result = self._values.get("masks")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TCPFlagFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkfirewall.CfnRuleGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "capacity": "capacity",
        "rule_group_name": "ruleGroupName",
        "type": "type",
        "description": "description",
        "rule_group": "ruleGroup",
        "tags": "tags",
    },
)
class CfnRuleGroupProps:
    def __init__(
        self,
        *,
        capacity: jsii.Number,
        rule_group_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rule_group: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.RuleGroupProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkFirewall::RuleGroup``.

        :param capacity: ``AWS::NetworkFirewall::RuleGroup.Capacity``.
        :param rule_group_name: ``AWS::NetworkFirewall::RuleGroup.RuleGroupName``.
        :param type: ``AWS::NetworkFirewall::RuleGroup.Type``.
        :param description: ``AWS::NetworkFirewall::RuleGroup.Description``.
        :param rule_group: ``AWS::NetworkFirewall::RuleGroup.RuleGroup``.
        :param tags: ``AWS::NetworkFirewall::RuleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "rule_group_name": rule_group_name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if rule_group is not None:
            self._values["rule_group"] = rule_group
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def capacity(self) -> jsii.Number:
        '''``AWS::NetworkFirewall::RuleGroup.Capacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-capacity
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule_group_name(self) -> builtins.str:
        '''``AWS::NetworkFirewall::RuleGroup.RuleGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroupname
        '''
        result = self._values.get("rule_group_name")
        assert result is not None, "Required property 'rule_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::NetworkFirewall::RuleGroup.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkFirewall::RuleGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_group(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.RuleGroupProperty]]:
        '''``AWS::NetworkFirewall::RuleGroup.RuleGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup
        '''
        result = self._values.get("rule_group")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.RuleGroupProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::NetworkFirewall::RuleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFirewall",
    "CfnFirewallPolicy",
    "CfnFirewallPolicyProps",
    "CfnFirewallProps",
    "CfnLoggingConfiguration",
    "CfnLoggingConfigurationProps",
    "CfnRuleGroup",
    "CfnRuleGroupProps",
]

publication.publish()
