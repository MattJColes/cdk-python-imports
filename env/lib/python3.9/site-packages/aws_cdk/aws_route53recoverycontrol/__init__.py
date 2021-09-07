'''
# AWS::Route53RecoveryControl Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_route53recoverycontrol as route53recoverycontrol
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
class CfnCluster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnCluster",
):
    '''A CloudFormation ``AWS::Route53RecoveryControl::Cluster``.

    :cloudformationResource: AWS::Route53RecoveryControl::Cluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Route53RecoveryControl::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Route53RecoveryControl::Cluster.Name``.
        '''
        props = CfnClusterProps(name=name)

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
    @jsii.member(jsii_name="attrClusterArn")
    def attr_cluster_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ClusterArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrClusterEndpoints")
    def attr_cluster_endpoints(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: ClusterEndpoints
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrClusterEndpoints"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryControl::Cluster.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnCluster.ClusterEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint": "endpoint", "region": "region"},
    )
    class ClusterEndpointProperty:
        def __init__(
            self,
            *,
            endpoint: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint: ``CfnCluster.ClusterEndpointProperty.Endpoint``.
            :param region: ``CfnCluster.ClusterEndpointProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if endpoint is not None:
                self._values["endpoint"] = endpoint
            if region is not None:
                self._values["region"] = region

        @builtins.property
        def endpoint(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.ClusterEndpointProperty.Endpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.ClusterEndpointProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class CfnClusterProps:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a ``AWS::Route53RecoveryControl::Cluster``.

        :param name: ``AWS::Route53RecoveryControl::Cluster.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryControl::Cluster.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnControlPanel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnControlPanel",
):
    '''A CloudFormation ``AWS::Route53RecoveryControl::ControlPanel``.

    :cloudformationResource: AWS::Route53RecoveryControl::ControlPanel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        cluster_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Route53RecoveryControl::ControlPanel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Route53RecoveryControl::ControlPanel.Name``.
        :param cluster_arn: ``AWS::Route53RecoveryControl::ControlPanel.ClusterArn``.
        '''
        props = CfnControlPanelProps(name=name, cluster_arn=cluster_arn)

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
    @jsii.member(jsii_name="attrControlPanelArn")
    def attr_control_panel_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ControlPanelArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrControlPanelArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDefaultControlPanel")
    def attr_default_control_panel(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: DefaultControlPanel
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrDefaultControlPanel"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRoutingControlCount")
    def attr_routing_control_count(self) -> jsii.Number:
        '''
        :cloudformationAttribute: RoutingControlCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRoutingControlCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Route53RecoveryControl::ControlPanel.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryControl::ControlPanel.ClusterArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-clusterarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterArn"))

    @cluster_arn.setter
    def cluster_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "clusterArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnControlPanelProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "cluster_arn": "clusterArn"},
)
class CfnControlPanelProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        cluster_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53RecoveryControl::ControlPanel``.

        :param name: ``AWS::Route53RecoveryControl::ControlPanel.Name``.
        :param cluster_arn: ``AWS::Route53RecoveryControl::ControlPanel.ClusterArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if cluster_arn is not None:
            self._values["cluster_arn"] = cluster_arn

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Route53RecoveryControl::ControlPanel.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryControl::ControlPanel.ClusterArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-clusterarn
        '''
        result = self._values.get("cluster_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnControlPanelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRoutingControl(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnRoutingControl",
):
    '''A CloudFormation ``AWS::Route53RecoveryControl::RoutingControl``.

    :cloudformationResource: AWS::Route53RecoveryControl::RoutingControl
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        cluster_arn: typing.Optional[builtins.str] = None,
        control_panel_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Route53RecoveryControl::RoutingControl``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Route53RecoveryControl::RoutingControl.Name``.
        :param cluster_arn: ``AWS::Route53RecoveryControl::RoutingControl.ClusterArn``.
        :param control_panel_arn: ``AWS::Route53RecoveryControl::RoutingControl.ControlPanelArn``.
        '''
        props = CfnRoutingControlProps(
            name=name, cluster_arn=cluster_arn, control_panel_arn=control_panel_arn
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
    @jsii.member(jsii_name="attrRoutingControlArn")
    def attr_routing_control_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: RoutingControlArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoutingControlArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Route53RecoveryControl::RoutingControl.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryControl::RoutingControl.ClusterArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-clusterarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterArn"))

    @cluster_arn.setter
    def cluster_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "clusterArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="controlPanelArn")
    def control_panel_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryControl::RoutingControl.ControlPanelArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-controlpanelarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "controlPanelArn"))

    @control_panel_arn.setter
    def control_panel_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "controlPanelArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnRoutingControlProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "cluster_arn": "clusterArn",
        "control_panel_arn": "controlPanelArn",
    },
)
class CfnRoutingControlProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        cluster_arn: typing.Optional[builtins.str] = None,
        control_panel_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53RecoveryControl::RoutingControl``.

        :param name: ``AWS::Route53RecoveryControl::RoutingControl.Name``.
        :param cluster_arn: ``AWS::Route53RecoveryControl::RoutingControl.ClusterArn``.
        :param control_panel_arn: ``AWS::Route53RecoveryControl::RoutingControl.ControlPanelArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if cluster_arn is not None:
            self._values["cluster_arn"] = cluster_arn
        if control_panel_arn is not None:
            self._values["control_panel_arn"] = control_panel_arn

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Route53RecoveryControl::RoutingControl.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryControl::RoutingControl.ClusterArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-clusterarn
        '''
        result = self._values.get("cluster_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def control_panel_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryControl::RoutingControl.ControlPanelArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-controlpanelarn
        '''
        result = self._values.get("control_panel_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRoutingControlProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSafetyRule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnSafetyRule",
):
    '''A CloudFormation ``AWS::Route53RecoveryControl::SafetyRule``.

    :cloudformationResource: AWS::Route53RecoveryControl::SafetyRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        control_panel_arn: builtins.str,
        name: builtins.str,
        rule_config: typing.Union["CfnSafetyRule.RuleConfigProperty", aws_cdk.core.IResolvable],
        assertion_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSafetyRule.AssertionRuleProperty"]] = None,
        gating_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSafetyRule.GatingRuleProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53RecoveryControl::SafetyRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param control_panel_arn: ``AWS::Route53RecoveryControl::SafetyRule.ControlPanelArn``.
        :param name: ``AWS::Route53RecoveryControl::SafetyRule.Name``.
        :param rule_config: ``AWS::Route53RecoveryControl::SafetyRule.RuleConfig``.
        :param assertion_rule: ``AWS::Route53RecoveryControl::SafetyRule.AssertionRule``.
        :param gating_rule: ``AWS::Route53RecoveryControl::SafetyRule.GatingRule``.
        '''
        props = CfnSafetyRuleProps(
            control_panel_arn=control_panel_arn,
            name=name,
            rule_config=rule_config,
            assertion_rule=assertion_rule,
            gating_rule=gating_rule,
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
    @jsii.member(jsii_name="attrSafetyRuleArn")
    def attr_safety_rule_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SafetyRuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSafetyRuleArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="controlPanelArn")
    def control_panel_arn(self) -> builtins.str:
        '''``AWS::Route53RecoveryControl::SafetyRule.ControlPanelArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-controlpanelarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "controlPanelArn"))

    @control_panel_arn.setter
    def control_panel_arn(self, value: builtins.str) -> None:
        jsii.set(self, "controlPanelArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Route53RecoveryControl::SafetyRule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleConfig")
    def rule_config(
        self,
    ) -> typing.Union["CfnSafetyRule.RuleConfigProperty", aws_cdk.core.IResolvable]:
        '''``AWS::Route53RecoveryControl::SafetyRule.RuleConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-ruleconfig
        '''
        return typing.cast(typing.Union["CfnSafetyRule.RuleConfigProperty", aws_cdk.core.IResolvable], jsii.get(self, "ruleConfig"))

    @rule_config.setter
    def rule_config(
        self,
        value: typing.Union["CfnSafetyRule.RuleConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "ruleConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assertionRule")
    def assertion_rule(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSafetyRule.AssertionRuleProperty"]]:
        '''``AWS::Route53RecoveryControl::SafetyRule.AssertionRule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSafetyRule.AssertionRuleProperty"]], jsii.get(self, "assertionRule"))

    @assertion_rule.setter
    def assertion_rule(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSafetyRule.AssertionRuleProperty"]],
    ) -> None:
        jsii.set(self, "assertionRule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatingRule")
    def gating_rule(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSafetyRule.GatingRuleProperty"]]:
        '''``AWS::Route53RecoveryControl::SafetyRule.GatingRule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSafetyRule.GatingRuleProperty"]], jsii.get(self, "gatingRule"))

    @gating_rule.setter
    def gating_rule(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSafetyRule.GatingRuleProperty"]],
    ) -> None:
        jsii.set(self, "gatingRule", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnSafetyRule.AssertionRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "asserted_controls": "assertedControls",
            "wait_period_ms": "waitPeriodMs",
        },
    )
    class AssertionRuleProperty:
        def __init__(
            self,
            *,
            asserted_controls: typing.Sequence[builtins.str],
            wait_period_ms: jsii.Number,
        ) -> None:
            '''
            :param asserted_controls: ``CfnSafetyRule.AssertionRuleProperty.AssertedControls``.
            :param wait_period_ms: ``CfnSafetyRule.AssertionRuleProperty.WaitPeriodMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "asserted_controls": asserted_controls,
                "wait_period_ms": wait_period_ms,
            }

        @builtins.property
        def asserted_controls(self) -> typing.List[builtins.str]:
            '''``CfnSafetyRule.AssertionRuleProperty.AssertedControls``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-assertedcontrols
            '''
            result = self._values.get("asserted_controls")
            assert result is not None, "Required property 'asserted_controls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def wait_period_ms(self) -> jsii.Number:
            '''``CfnSafetyRule.AssertionRuleProperty.WaitPeriodMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-waitperiodms
            '''
            result = self._values.get("wait_period_ms")
            assert result is not None, "Required property 'wait_period_ms' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssertionRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnSafetyRule.GatingRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "gating_controls": "gatingControls",
            "target_controls": "targetControls",
            "wait_period_ms": "waitPeriodMs",
        },
    )
    class GatingRuleProperty:
        def __init__(
            self,
            *,
            gating_controls: typing.Sequence[builtins.str],
            target_controls: typing.Sequence[builtins.str],
            wait_period_ms: jsii.Number,
        ) -> None:
            '''
            :param gating_controls: ``CfnSafetyRule.GatingRuleProperty.GatingControls``.
            :param target_controls: ``CfnSafetyRule.GatingRuleProperty.TargetControls``.
            :param wait_period_ms: ``CfnSafetyRule.GatingRuleProperty.WaitPeriodMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "gating_controls": gating_controls,
                "target_controls": target_controls,
                "wait_period_ms": wait_period_ms,
            }

        @builtins.property
        def gating_controls(self) -> typing.List[builtins.str]:
            '''``CfnSafetyRule.GatingRuleProperty.GatingControls``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-gatingcontrols
            '''
            result = self._values.get("gating_controls")
            assert result is not None, "Required property 'gating_controls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def target_controls(self) -> typing.List[builtins.str]:
            '''``CfnSafetyRule.GatingRuleProperty.TargetControls``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-targetcontrols
            '''
            result = self._values.get("target_controls")
            assert result is not None, "Required property 'target_controls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def wait_period_ms(self) -> jsii.Number:
            '''``CfnSafetyRule.GatingRuleProperty.WaitPeriodMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-waitperiodms
            '''
            result = self._values.get("wait_period_ms")
            assert result is not None, "Required property 'wait_period_ms' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatingRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnSafetyRule.RuleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "inverted": "inverted",
            "threshold": "threshold",
            "type": "type",
        },
    )
    class RuleConfigProperty:
        def __init__(
            self,
            *,
            inverted: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            threshold: jsii.Number,
            type: builtins.str,
        ) -> None:
            '''
            :param inverted: ``CfnSafetyRule.RuleConfigProperty.Inverted``.
            :param threshold: ``CfnSafetyRule.RuleConfigProperty.Threshold``.
            :param type: ``CfnSafetyRule.RuleConfigProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "inverted": inverted,
                "threshold": threshold,
                "type": type,
            }

        @builtins.property
        def inverted(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnSafetyRule.RuleConfigProperty.Inverted``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-inverted
            '''
            result = self._values.get("inverted")
            assert result is not None, "Required property 'inverted' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def threshold(self) -> jsii.Number:
            '''``CfnSafetyRule.RuleConfigProperty.Threshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnSafetyRule.RuleConfigProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53recoverycontrol.CfnSafetyRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "control_panel_arn": "controlPanelArn",
        "name": "name",
        "rule_config": "ruleConfig",
        "assertion_rule": "assertionRule",
        "gating_rule": "gatingRule",
    },
)
class CfnSafetyRuleProps:
    def __init__(
        self,
        *,
        control_panel_arn: builtins.str,
        name: builtins.str,
        rule_config: typing.Union[CfnSafetyRule.RuleConfigProperty, aws_cdk.core.IResolvable],
        assertion_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSafetyRule.AssertionRuleProperty]] = None,
        gating_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSafetyRule.GatingRuleProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53RecoveryControl::SafetyRule``.

        :param control_panel_arn: ``AWS::Route53RecoveryControl::SafetyRule.ControlPanelArn``.
        :param name: ``AWS::Route53RecoveryControl::SafetyRule.Name``.
        :param rule_config: ``AWS::Route53RecoveryControl::SafetyRule.RuleConfig``.
        :param assertion_rule: ``AWS::Route53RecoveryControl::SafetyRule.AssertionRule``.
        :param gating_rule: ``AWS::Route53RecoveryControl::SafetyRule.GatingRule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "control_panel_arn": control_panel_arn,
            "name": name,
            "rule_config": rule_config,
        }
        if assertion_rule is not None:
            self._values["assertion_rule"] = assertion_rule
        if gating_rule is not None:
            self._values["gating_rule"] = gating_rule

    @builtins.property
    def control_panel_arn(self) -> builtins.str:
        '''``AWS::Route53RecoveryControl::SafetyRule.ControlPanelArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-controlpanelarn
        '''
        result = self._values.get("control_panel_arn")
        assert result is not None, "Required property 'control_panel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Route53RecoveryControl::SafetyRule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_config(
        self,
    ) -> typing.Union[CfnSafetyRule.RuleConfigProperty, aws_cdk.core.IResolvable]:
        '''``AWS::Route53RecoveryControl::SafetyRule.RuleConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-ruleconfig
        '''
        result = self._values.get("rule_config")
        assert result is not None, "Required property 'rule_config' is missing"
        return typing.cast(typing.Union[CfnSafetyRule.RuleConfigProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def assertion_rule(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSafetyRule.AssertionRuleProperty]]:
        '''``AWS::Route53RecoveryControl::SafetyRule.AssertionRule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule
        '''
        result = self._values.get("assertion_rule")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSafetyRule.AssertionRuleProperty]], result)

    @builtins.property
    def gating_rule(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSafetyRule.GatingRuleProperty]]:
        '''``AWS::Route53RecoveryControl::SafetyRule.GatingRule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule
        '''
        result = self._values.get("gating_rule")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSafetyRule.GatingRuleProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSafetyRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
    "CfnControlPanel",
    "CfnControlPanelProps",
    "CfnRoutingControl",
    "CfnRoutingControlProps",
    "CfnSafetyRule",
    "CfnSafetyRuleProps",
]

publication.publish()
