'''
# AWS::XRay Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_xray as xray
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
class CfnGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-xray.CfnGroup",
):
    '''A CloudFormation ``AWS::XRay::Group``.

    :cloudformationResource: AWS::XRay::Group
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        filter_expression: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        insights_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.InsightsConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''Create a new ``AWS::XRay::Group``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param filter_expression: ``AWS::XRay::Group.FilterExpression``.
        :param group_name: ``AWS::XRay::Group.GroupName``.
        :param insights_configuration: ``AWS::XRay::Group.InsightsConfiguration``.
        :param tags: ``AWS::XRay::Group.Tags``.
        '''
        props = CfnGroupProps(
            filter_expression=filter_expression,
            group_name=group_name,
            insights_configuration=insights_configuration,
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
    @jsii.member(jsii_name="attrGroupArn")
    def attr_group_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: GroupARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="filterExpression")
    def filter_expression(self) -> typing.Optional[builtins.str]:
        '''``AWS::XRay::Group.FilterExpression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-filterexpression
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterExpression"))

    @filter_expression.setter
    def filter_expression(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "filterExpression", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::XRay::Group.GroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-groupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "groupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="insightsConfiguration")
    def insights_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.InsightsConfigurationProperty"]]:
        '''``AWS::XRay::Group.InsightsConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-insightsconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.InsightsConfigurationProperty"]], jsii.get(self, "insightsConfiguration"))

    @insights_configuration.setter
    def insights_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.InsightsConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "insightsConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[typing.Any]]:
        '''``AWS::XRay::Group.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-tags
        '''
        return typing.cast(typing.Optional[typing.List[typing.Any]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[typing.Any]]) -> None:
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-xray.CfnGroup.InsightsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "insights_enabled": "insightsEnabled",
            "notifications_enabled": "notificationsEnabled",
        },
    )
    class InsightsConfigurationProperty:
        def __init__(
            self,
            *,
            insights_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            notifications_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param insights_enabled: ``CfnGroup.InsightsConfigurationProperty.InsightsEnabled``.
            :param notifications_enabled: ``CfnGroup.InsightsConfigurationProperty.NotificationsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if insights_enabled is not None:
                self._values["insights_enabled"] = insights_enabled
            if notifications_enabled is not None:
                self._values["notifications_enabled"] = notifications_enabled

        @builtins.property
        def insights_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnGroup.InsightsConfigurationProperty.InsightsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html#cfn-xray-group-insightsconfiguration-insightsenabled
            '''
            result = self._values.get("insights_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def notifications_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnGroup.InsightsConfigurationProperty.NotificationsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html#cfn-xray-group-insightsconfiguration-notificationsenabled
            '''
            result = self._values.get("notifications_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InsightsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-xray.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "filter_expression": "filterExpression",
        "group_name": "groupName",
        "insights_configuration": "insightsConfiguration",
        "tags": "tags",
    },
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        filter_expression: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        insights_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnGroup.InsightsConfigurationProperty]] = None,
        tags: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::XRay::Group``.

        :param filter_expression: ``AWS::XRay::Group.FilterExpression``.
        :param group_name: ``AWS::XRay::Group.GroupName``.
        :param insights_configuration: ``AWS::XRay::Group.InsightsConfiguration``.
        :param tags: ``AWS::XRay::Group.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if filter_expression is not None:
            self._values["filter_expression"] = filter_expression
        if group_name is not None:
            self._values["group_name"] = group_name
        if insights_configuration is not None:
            self._values["insights_configuration"] = insights_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def filter_expression(self) -> typing.Optional[builtins.str]:
        '''``AWS::XRay::Group.FilterExpression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-filterexpression
        '''
        result = self._values.get("filter_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::XRay::Group.GroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-groupname
        '''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insights_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnGroup.InsightsConfigurationProperty]]:
        '''``AWS::XRay::Group.InsightsConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-insightsconfiguration
        '''
        result = self._values.get("insights_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnGroup.InsightsConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[typing.Any]]:
        '''``AWS::XRay::Group.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSamplingRule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-xray.CfnSamplingRule",
):
    '''A CloudFormation ``AWS::XRay::SamplingRule``.

    :cloudformationResource: AWS::XRay::SamplingRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        rule_name: typing.Optional[builtins.str] = None,
        sampling_rule: typing.Optional[typing.Union["CfnSamplingRule.SamplingRuleProperty", aws_cdk.core.IResolvable]] = None,
        sampling_rule_record: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSamplingRule.SamplingRuleRecordProperty"]] = None,
        sampling_rule_update: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSamplingRule.SamplingRuleUpdateProperty"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''Create a new ``AWS::XRay::SamplingRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param rule_name: ``AWS::XRay::SamplingRule.RuleName``.
        :param sampling_rule: ``AWS::XRay::SamplingRule.SamplingRule``.
        :param sampling_rule_record: ``AWS::XRay::SamplingRule.SamplingRuleRecord``.
        :param sampling_rule_update: ``AWS::XRay::SamplingRule.SamplingRuleUpdate``.
        :param tags: ``AWS::XRay::SamplingRule.Tags``.
        '''
        props = CfnSamplingRuleProps(
            rule_name=rule_name,
            sampling_rule=sampling_rule,
            sampling_rule_record=sampling_rule_record,
            sampling_rule_update=sampling_rule_update,
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
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: RuleARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::XRay::SamplingRule.RuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-rulename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ruleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="samplingRule")
    def sampling_rule(
        self,
    ) -> typing.Optional[typing.Union["CfnSamplingRule.SamplingRuleProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::XRay::SamplingRule.SamplingRule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingrule
        '''
        return typing.cast(typing.Optional[typing.Union["CfnSamplingRule.SamplingRuleProperty", aws_cdk.core.IResolvable]], jsii.get(self, "samplingRule"))

    @sampling_rule.setter
    def sampling_rule(
        self,
        value: typing.Optional[typing.Union["CfnSamplingRule.SamplingRuleProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "samplingRule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="samplingRuleRecord")
    def sampling_rule_record(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSamplingRule.SamplingRuleRecordProperty"]]:
        '''``AWS::XRay::SamplingRule.SamplingRuleRecord``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingrulerecord
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSamplingRule.SamplingRuleRecordProperty"]], jsii.get(self, "samplingRuleRecord"))

    @sampling_rule_record.setter
    def sampling_rule_record(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSamplingRule.SamplingRuleRecordProperty"]],
    ) -> None:
        jsii.set(self, "samplingRuleRecord", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="samplingRuleUpdate")
    def sampling_rule_update(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSamplingRule.SamplingRuleUpdateProperty"]]:
        '''``AWS::XRay::SamplingRule.SamplingRuleUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingruleupdate
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSamplingRule.SamplingRuleUpdateProperty"]], jsii.get(self, "samplingRuleUpdate"))

    @sampling_rule_update.setter
    def sampling_rule_update(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSamplingRule.SamplingRuleUpdateProperty"]],
    ) -> None:
        jsii.set(self, "samplingRuleUpdate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[typing.Any]]:
        '''``AWS::XRay::SamplingRule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-tags
        '''
        return typing.cast(typing.Optional[typing.List[typing.Any]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[typing.Any]]) -> None:
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-xray.CfnSamplingRule.SamplingRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attributes": "attributes",
            "fixed_rate": "fixedRate",
            "host": "host",
            "http_method": "httpMethod",
            "priority": "priority",
            "reservoir_size": "reservoirSize",
            "resource_arn": "resourceArn",
            "rule_arn": "ruleArn",
            "rule_name": "ruleName",
            "service_name": "serviceName",
            "service_type": "serviceType",
            "url_path": "urlPath",
            "version": "version",
        },
    )
    class SamplingRuleProperty:
        def __init__(
            self,
            *,
            attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            fixed_rate: typing.Optional[jsii.Number] = None,
            host: typing.Optional[builtins.str] = None,
            http_method: typing.Optional[builtins.str] = None,
            priority: typing.Optional[jsii.Number] = None,
            reservoir_size: typing.Optional[jsii.Number] = None,
            resource_arn: typing.Optional[builtins.str] = None,
            rule_arn: typing.Optional[builtins.str] = None,
            rule_name: typing.Optional[builtins.str] = None,
            service_name: typing.Optional[builtins.str] = None,
            service_type: typing.Optional[builtins.str] = None,
            url_path: typing.Optional[builtins.str] = None,
            version: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param attributes: ``CfnSamplingRule.SamplingRuleProperty.Attributes``.
            :param fixed_rate: ``CfnSamplingRule.SamplingRuleProperty.FixedRate``.
            :param host: ``CfnSamplingRule.SamplingRuleProperty.Host``.
            :param http_method: ``CfnSamplingRule.SamplingRuleProperty.HTTPMethod``.
            :param priority: ``CfnSamplingRule.SamplingRuleProperty.Priority``.
            :param reservoir_size: ``CfnSamplingRule.SamplingRuleProperty.ReservoirSize``.
            :param resource_arn: ``CfnSamplingRule.SamplingRuleProperty.ResourceARN``.
            :param rule_arn: ``CfnSamplingRule.SamplingRuleProperty.RuleARN``.
            :param rule_name: ``CfnSamplingRule.SamplingRuleProperty.RuleName``.
            :param service_name: ``CfnSamplingRule.SamplingRuleProperty.ServiceName``.
            :param service_type: ``CfnSamplingRule.SamplingRuleProperty.ServiceType``.
            :param url_path: ``CfnSamplingRule.SamplingRuleProperty.URLPath``.
            :param version: ``CfnSamplingRule.SamplingRuleProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if fixed_rate is not None:
                self._values["fixed_rate"] = fixed_rate
            if host is not None:
                self._values["host"] = host
            if http_method is not None:
                self._values["http_method"] = http_method
            if priority is not None:
                self._values["priority"] = priority
            if reservoir_size is not None:
                self._values["reservoir_size"] = reservoir_size
            if resource_arn is not None:
                self._values["resource_arn"] = resource_arn
            if rule_arn is not None:
                self._values["rule_arn"] = rule_arn
            if rule_name is not None:
                self._values["rule_name"] = rule_name
            if service_name is not None:
                self._values["service_name"] = service_name
            if service_type is not None:
                self._values["service_type"] = service_type
            if url_path is not None:
                self._values["url_path"] = url_path
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnSamplingRule.SamplingRuleProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def fixed_rate(self) -> typing.Optional[jsii.Number]:
            '''``CfnSamplingRule.SamplingRuleProperty.FixedRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-fixedrate
            '''
            result = self._values.get("fixed_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def host(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-host
            '''
            result = self._values.get("host")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def http_method(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleProperty.HTTPMethod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-httpmethod
            '''
            result = self._values.get("http_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            '''``CfnSamplingRule.SamplingRuleProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-priority
            '''
            result = self._values.get("priority")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def reservoir_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnSamplingRule.SamplingRuleProperty.ReservoirSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-reservoirsize
            '''
            result = self._values.get("reservoir_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def resource_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleProperty.ResourceARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-resourcearn
            '''
            result = self._values.get("resource_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleProperty.RuleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-rulearn
            '''
            result = self._values.get("rule_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_name(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleProperty.RuleName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-rulename
            '''
            result = self._values.get("rule_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_name(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleProperty.ServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-servicename
            '''
            result = self._values.get("service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_type(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleProperty.ServiceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-servicetype
            '''
            result = self._values.get("service_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url_path(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleProperty.URLPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-urlpath
            '''
            result = self._values.get("url_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[jsii.Number]:
            '''``CfnSamplingRule.SamplingRuleProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamplingRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-xray.CfnSamplingRule.SamplingRuleRecordProperty",
        jsii_struct_bases=[],
        name_mapping={
            "created_at": "createdAt",
            "modified_at": "modifiedAt",
            "sampling_rule": "samplingRule",
        },
    )
    class SamplingRuleRecordProperty:
        def __init__(
            self,
            *,
            created_at: typing.Optional[builtins.str] = None,
            modified_at: typing.Optional[builtins.str] = None,
            sampling_rule: typing.Optional[typing.Union["CfnSamplingRule.SamplingRuleProperty", aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param created_at: ``CfnSamplingRule.SamplingRuleRecordProperty.CreatedAt``.
            :param modified_at: ``CfnSamplingRule.SamplingRuleRecordProperty.ModifiedAt``.
            :param sampling_rule: ``CfnSamplingRule.SamplingRuleRecordProperty.SamplingRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if created_at is not None:
                self._values["created_at"] = created_at
            if modified_at is not None:
                self._values["modified_at"] = modified_at
            if sampling_rule is not None:
                self._values["sampling_rule"] = sampling_rule

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleRecordProperty.CreatedAt``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html#cfn-xray-samplingrule-samplingrulerecord-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def modified_at(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleRecordProperty.ModifiedAt``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html#cfn-xray-samplingrule-samplingrulerecord-modifiedat
            '''
            result = self._values.get("modified_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sampling_rule(
            self,
        ) -> typing.Optional[typing.Union["CfnSamplingRule.SamplingRuleProperty", aws_cdk.core.IResolvable]]:
            '''``CfnSamplingRule.SamplingRuleRecordProperty.SamplingRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html#cfn-xray-samplingrule-samplingrulerecord-samplingrule
            '''
            result = self._values.get("sampling_rule")
            return typing.cast(typing.Optional[typing.Union["CfnSamplingRule.SamplingRuleProperty", aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamplingRuleRecordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-xray.CfnSamplingRule.SamplingRuleUpdateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attributes": "attributes",
            "fixed_rate": "fixedRate",
            "host": "host",
            "http_method": "httpMethod",
            "priority": "priority",
            "reservoir_size": "reservoirSize",
            "resource_arn": "resourceArn",
            "rule_arn": "ruleArn",
            "rule_name": "ruleName",
            "service_name": "serviceName",
            "service_type": "serviceType",
            "url_path": "urlPath",
        },
    )
    class SamplingRuleUpdateProperty:
        def __init__(
            self,
            *,
            attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            fixed_rate: typing.Optional[jsii.Number] = None,
            host: typing.Optional[builtins.str] = None,
            http_method: typing.Optional[builtins.str] = None,
            priority: typing.Optional[jsii.Number] = None,
            reservoir_size: typing.Optional[jsii.Number] = None,
            resource_arn: typing.Optional[builtins.str] = None,
            rule_arn: typing.Optional[builtins.str] = None,
            rule_name: typing.Optional[builtins.str] = None,
            service_name: typing.Optional[builtins.str] = None,
            service_type: typing.Optional[builtins.str] = None,
            url_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attributes: ``CfnSamplingRule.SamplingRuleUpdateProperty.Attributes``.
            :param fixed_rate: ``CfnSamplingRule.SamplingRuleUpdateProperty.FixedRate``.
            :param host: ``CfnSamplingRule.SamplingRuleUpdateProperty.Host``.
            :param http_method: ``CfnSamplingRule.SamplingRuleUpdateProperty.HTTPMethod``.
            :param priority: ``CfnSamplingRule.SamplingRuleUpdateProperty.Priority``.
            :param reservoir_size: ``CfnSamplingRule.SamplingRuleUpdateProperty.ReservoirSize``.
            :param resource_arn: ``CfnSamplingRule.SamplingRuleUpdateProperty.ResourceARN``.
            :param rule_arn: ``CfnSamplingRule.SamplingRuleUpdateProperty.RuleARN``.
            :param rule_name: ``CfnSamplingRule.SamplingRuleUpdateProperty.RuleName``.
            :param service_name: ``CfnSamplingRule.SamplingRuleUpdateProperty.ServiceName``.
            :param service_type: ``CfnSamplingRule.SamplingRuleUpdateProperty.ServiceType``.
            :param url_path: ``CfnSamplingRule.SamplingRuleUpdateProperty.URLPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if fixed_rate is not None:
                self._values["fixed_rate"] = fixed_rate
            if host is not None:
                self._values["host"] = host
            if http_method is not None:
                self._values["http_method"] = http_method
            if priority is not None:
                self._values["priority"] = priority
            if reservoir_size is not None:
                self._values["reservoir_size"] = reservoir_size
            if resource_arn is not None:
                self._values["resource_arn"] = resource_arn
            if rule_arn is not None:
                self._values["rule_arn"] = rule_arn
            if rule_name is not None:
                self._values["rule_name"] = rule_name
            if service_name is not None:
                self._values["service_name"] = service_name
            if service_type is not None:
                self._values["service_type"] = service_type
            if url_path is not None:
                self._values["url_path"] = url_path

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def fixed_rate(self) -> typing.Optional[jsii.Number]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.FixedRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-fixedrate
            '''
            result = self._values.get("fixed_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def host(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-host
            '''
            result = self._values.get("host")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def http_method(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.HTTPMethod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-httpmethod
            '''
            result = self._values.get("http_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-priority
            '''
            result = self._values.get("priority")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def reservoir_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.ReservoirSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-reservoirsize
            '''
            result = self._values.get("reservoir_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def resource_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.ResourceARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-resourcearn
            '''
            result = self._values.get("resource_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.RuleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-rulearn
            '''
            result = self._values.get("rule_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_name(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.RuleName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-rulename
            '''
            result = self._values.get("rule_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_name(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.ServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-servicename
            '''
            result = self._values.get("service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_type(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.ServiceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-servicetype
            '''
            result = self._values.get("service_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url_path(self) -> typing.Optional[builtins.str]:
            '''``CfnSamplingRule.SamplingRuleUpdateProperty.URLPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html#cfn-xray-samplingrule-samplingruleupdate-urlpath
            '''
            result = self._values.get("url_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamplingRuleUpdateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-xray.CfnSamplingRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "rule_name": "ruleName",
        "sampling_rule": "samplingRule",
        "sampling_rule_record": "samplingRuleRecord",
        "sampling_rule_update": "samplingRuleUpdate",
        "tags": "tags",
    },
)
class CfnSamplingRuleProps:
    def __init__(
        self,
        *,
        rule_name: typing.Optional[builtins.str] = None,
        sampling_rule: typing.Optional[typing.Union[CfnSamplingRule.SamplingRuleProperty, aws_cdk.core.IResolvable]] = None,
        sampling_rule_record: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSamplingRule.SamplingRuleRecordProperty]] = None,
        sampling_rule_update: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSamplingRule.SamplingRuleUpdateProperty]] = None,
        tags: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::XRay::SamplingRule``.

        :param rule_name: ``AWS::XRay::SamplingRule.RuleName``.
        :param sampling_rule: ``AWS::XRay::SamplingRule.SamplingRule``.
        :param sampling_rule_record: ``AWS::XRay::SamplingRule.SamplingRuleRecord``.
        :param sampling_rule_update: ``AWS::XRay::SamplingRule.SamplingRuleUpdate``.
        :param tags: ``AWS::XRay::SamplingRule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if sampling_rule is not None:
            self._values["sampling_rule"] = sampling_rule
        if sampling_rule_record is not None:
            self._values["sampling_rule_record"] = sampling_rule_record
        if sampling_rule_update is not None:
            self._values["sampling_rule_update"] = sampling_rule_update
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::XRay::SamplingRule.RuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-rulename
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sampling_rule(
        self,
    ) -> typing.Optional[typing.Union[CfnSamplingRule.SamplingRuleProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::XRay::SamplingRule.SamplingRule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingrule
        '''
        result = self._values.get("sampling_rule")
        return typing.cast(typing.Optional[typing.Union[CfnSamplingRule.SamplingRuleProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def sampling_rule_record(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSamplingRule.SamplingRuleRecordProperty]]:
        '''``AWS::XRay::SamplingRule.SamplingRuleRecord``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingrulerecord
        '''
        result = self._values.get("sampling_rule_record")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSamplingRule.SamplingRuleRecordProperty]], result)

    @builtins.property
    def sampling_rule_update(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSamplingRule.SamplingRuleUpdateProperty]]:
        '''``AWS::XRay::SamplingRule.SamplingRuleUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingruleupdate
        '''
        result = self._values.get("sampling_rule_update")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSamplingRule.SamplingRuleUpdateProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[typing.Any]]:
        '''``AWS::XRay::SamplingRule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSamplingRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGroup",
    "CfnGroupProps",
    "CfnSamplingRule",
    "CfnSamplingRuleProps",
]

publication.publish()
