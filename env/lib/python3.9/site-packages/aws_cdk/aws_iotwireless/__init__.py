'''
# AWS::IoTWireless Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iotwireless as iotwireless
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
class CfnDestination(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnDestination",
):
    '''A CloudFormation ``AWS::IoTWireless::Destination``.

    :cloudformationResource: AWS::IoTWireless::Destination
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        expression: builtins.str,
        expression_type: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::Destination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param expression: ``AWS::IoTWireless::Destination.Expression``.
        :param expression_type: ``AWS::IoTWireless::Destination.ExpressionType``.
        :param name: ``AWS::IoTWireless::Destination.Name``.
        :param role_arn: ``AWS::IoTWireless::Destination.RoleArn``.
        :param description: ``AWS::IoTWireless::Destination.Description``.
        :param tags: ``AWS::IoTWireless::Destination.Tags``.
        '''
        props = CfnDestinationProps(
            expression=expression,
            expression_type=expression_type,
            name=name,
            role_arn=role_arn,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTWireless::Destination.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        '''``AWS::IoTWireless::Destination.Expression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression
        '''
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        jsii.set(self, "expression", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="expressionType")
    def expression_type(self) -> builtins.str:
        '''``AWS::IoTWireless::Destination.ExpressionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype
        '''
        return typing.cast(builtins.str, jsii.get(self, "expressionType"))

    @expression_type.setter
    def expression_type(self, value: builtins.str) -> None:
        jsii.set(self, "expressionType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::IoTWireless::Destination.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::IoTWireless::Destination.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::Destination.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "expression_type": "expressionType",
        "name": "name",
        "role_arn": "roleArn",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDestinationProps:
    def __init__(
        self,
        *,
        expression: builtins.str,
        expression_type: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTWireless::Destination``.

        :param expression: ``AWS::IoTWireless::Destination.Expression``.
        :param expression_type: ``AWS::IoTWireless::Destination.ExpressionType``.
        :param name: ``AWS::IoTWireless::Destination.Name``.
        :param role_arn: ``AWS::IoTWireless::Destination.RoleArn``.
        :param description: ``AWS::IoTWireless::Destination.Description``.
        :param tags: ``AWS::IoTWireless::Destination.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
            "expression_type": expression_type,
            "name": name,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def expression(self) -> builtins.str:
        '''``AWS::IoTWireless::Destination.Expression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression_type(self) -> builtins.str:
        '''``AWS::IoTWireless::Destination.ExpressionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype
        '''
        result = self._values.get("expression_type")
        assert result is not None, "Required property 'expression_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::IoTWireless::Destination.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::IoTWireless::Destination.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::Destination.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTWireless::Destination.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDeviceProfile(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnDeviceProfile",
):
    '''A CloudFormation ``AWS::IoTWireless::DeviceProfile``.

    :cloudformationResource: AWS::IoTWireless::DeviceProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        lo_ra_wan: typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", aws_cdk.core.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::DeviceProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan: ``AWS::IoTWireless::DeviceProfile.LoRaWAN``.
        :param name: ``AWS::IoTWireless::DeviceProfile.Name``.
        :param tags: ``AWS::IoTWireless::DeviceProfile.Tags``.
        '''
        props = CfnDeviceProfileProps(lo_ra_wan=lo_ra_wan, name=name, tags=tags)

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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTWireless::DeviceProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::IoTWireless::DeviceProfile.LoRaWAN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawan
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", aws_cdk.core.IResolvable]], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "loRaWan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::DeviceProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "class_b_timeout": "classBTimeout",
            "class_c_timeout": "classCTimeout",
            "mac_version": "macVersion",
            "max_duty_cycle": "maxDutyCycle",
            "max_eirp": "maxEirp",
            "ping_slot_dr": "pingSlotDr",
            "ping_slot_freq": "pingSlotFreq",
            "ping_slot_period": "pingSlotPeriod",
            "reg_params_revision": "regParamsRevision",
            "rf_region": "rfRegion",
            "supports32_bit_f_cnt": "supports32BitFCnt",
            "supports_class_b": "supportsClassB",
            "supports_class_c": "supportsClassC",
            "supports_join": "supportsJoin",
        },
    )
    class LoRaWANDeviceProfileProperty:
        def __init__(
            self,
            *,
            class_b_timeout: typing.Optional[jsii.Number] = None,
            class_c_timeout: typing.Optional[jsii.Number] = None,
            mac_version: typing.Optional[builtins.str] = None,
            max_duty_cycle: typing.Optional[jsii.Number] = None,
            max_eirp: typing.Optional[jsii.Number] = None,
            ping_slot_dr: typing.Optional[jsii.Number] = None,
            ping_slot_freq: typing.Optional[jsii.Number] = None,
            ping_slot_period: typing.Optional[jsii.Number] = None,
            reg_params_revision: typing.Optional[builtins.str] = None,
            rf_region: typing.Optional[builtins.str] = None,
            supports32_bit_f_cnt: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            supports_class_b: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            supports_class_c: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            supports_join: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param class_b_timeout: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.ClassBTimeout``.
            :param class_c_timeout: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.ClassCTimeout``.
            :param mac_version: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MacVersion``.
            :param max_duty_cycle: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MaxDutyCycle``.
            :param max_eirp: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MaxEirp``.
            :param ping_slot_dr: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotDr``.
            :param ping_slot_freq: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotFreq``.
            :param ping_slot_period: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotPeriod``.
            :param reg_params_revision: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.RegParamsRevision``.
            :param rf_region: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.RfRegion``.
            :param supports32_bit_f_cnt: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.Supports32BitFCnt``.
            :param supports_class_b: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsClassB``.
            :param supports_class_c: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsClassC``.
            :param supports_join: ``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsJoin``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if class_b_timeout is not None:
                self._values["class_b_timeout"] = class_b_timeout
            if class_c_timeout is not None:
                self._values["class_c_timeout"] = class_c_timeout
            if mac_version is not None:
                self._values["mac_version"] = mac_version
            if max_duty_cycle is not None:
                self._values["max_duty_cycle"] = max_duty_cycle
            if max_eirp is not None:
                self._values["max_eirp"] = max_eirp
            if ping_slot_dr is not None:
                self._values["ping_slot_dr"] = ping_slot_dr
            if ping_slot_freq is not None:
                self._values["ping_slot_freq"] = ping_slot_freq
            if ping_slot_period is not None:
                self._values["ping_slot_period"] = ping_slot_period
            if reg_params_revision is not None:
                self._values["reg_params_revision"] = reg_params_revision
            if rf_region is not None:
                self._values["rf_region"] = rf_region
            if supports32_bit_f_cnt is not None:
                self._values["supports32_bit_f_cnt"] = supports32_bit_f_cnt
            if supports_class_b is not None:
                self._values["supports_class_b"] = supports_class_b
            if supports_class_c is not None:
                self._values["supports_class_c"] = supports_class_c
            if supports_join is not None:
                self._values["supports_join"] = supports_join

        @builtins.property
        def class_b_timeout(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.ClassBTimeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout
            '''
            result = self._values.get("class_b_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def class_c_timeout(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.ClassCTimeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout
            '''
            result = self._values.get("class_c_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mac_version(self) -> typing.Optional[builtins.str]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MacVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion
            '''
            result = self._values.get("mac_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_duty_cycle(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MaxDutyCycle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle
            '''
            result = self._values.get("max_duty_cycle")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_eirp(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.MaxEirp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp
            '''
            result = self._values.get("max_eirp")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ping_slot_dr(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotDr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr
            '''
            result = self._values.get("ping_slot_dr")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ping_slot_freq(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotFreq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq
            '''
            result = self._values.get("ping_slot_freq")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ping_slot_period(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.PingSlotPeriod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod
            '''
            result = self._values.get("ping_slot_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def reg_params_revision(self) -> typing.Optional[builtins.str]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.RegParamsRevision``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision
            '''
            result = self._values.get("reg_params_revision")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rf_region(self) -> typing.Optional[builtins.str]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.RfRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion
            '''
            result = self._values.get("rf_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def supports32_bit_f_cnt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.Supports32BitFCnt``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt
            '''
            result = self._values.get("supports32_bit_f_cnt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def supports_class_b(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsClassB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb
            '''
            result = self._values.get("supports_class_b")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def supports_class_c(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsClassC``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc
            '''
            result = self._values.get("supports_class_c")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def supports_join(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeviceProfile.LoRaWANDeviceProfileProperty.SupportsJoin``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin
            '''
            result = self._values.get("supports_join")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANDeviceProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnDeviceProfileProps",
    jsii_struct_bases=[],
    name_mapping={"lo_ra_wan": "loRaWan", "name": "name", "tags": "tags"},
)
class CfnDeviceProfileProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Optional[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, aws_cdk.core.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTWireless::DeviceProfile``.

        :param lo_ra_wan: ``AWS::IoTWireless::DeviceProfile.LoRaWAN``.
        :param name: ``AWS::IoTWireless::DeviceProfile.Name``.
        :param tags: ``AWS::IoTWireless::DeviceProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if lo_ra_wan is not None:
            self._values["lo_ra_wan"] = lo_ra_wan
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::IoTWireless::DeviceProfile.LoRaWAN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        return typing.cast(typing.Optional[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::DeviceProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTWireless::DeviceProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPartnerAccount(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnPartnerAccount",
):
    '''A CloudFormation ``AWS::IoTWireless::PartnerAccount``.

    :cloudformationResource: AWS::IoTWireless::PartnerAccount
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        account_linked: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        fingerprint: typing.Optional[builtins.str] = None,
        partner_account_id: typing.Optional[builtins.str] = None,
        partner_type: typing.Optional[builtins.str] = None,
        sidewalk: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPartnerAccount.SidewalkAccountInfoProperty"]] = None,
        sidewalk_update: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::PartnerAccount``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_linked: ``AWS::IoTWireless::PartnerAccount.AccountLinked``.
        :param fingerprint: ``AWS::IoTWireless::PartnerAccount.Fingerprint``.
        :param partner_account_id: ``AWS::IoTWireless::PartnerAccount.PartnerAccountId``.
        :param partner_type: ``AWS::IoTWireless::PartnerAccount.PartnerType``.
        :param sidewalk: ``AWS::IoTWireless::PartnerAccount.Sidewalk``.
        :param sidewalk_update: ``AWS::IoTWireless::PartnerAccount.SidewalkUpdate``.
        :param tags: ``AWS::IoTWireless::PartnerAccount.Tags``.
        '''
        props = CfnPartnerAccountProps(
            account_linked=account_linked,
            fingerprint=fingerprint,
            partner_account_id=partner_account_id,
            partner_type=partner_type,
            sidewalk=sidewalk,
            sidewalk_update=sidewalk_update,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTWireless::PartnerAccount.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accountLinked")
    def account_linked(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::IoTWireless::PartnerAccount.AccountLinked``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-accountlinked
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "accountLinked"))

    @account_linked.setter
    def account_linked(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "accountLinked", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.Fingerprint``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-fingerprint
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fingerprint"))

    @fingerprint.setter
    def fingerprint(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "fingerprint", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="partnerAccountId")
    def partner_account_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.PartnerAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partneraccountid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partnerAccountId"))

    @partner_account_id.setter
    def partner_account_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "partnerAccountId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="partnerType")
    def partner_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.PartnerType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partnertype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partnerType"))

    @partner_type.setter
    def partner_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "partnerType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sidewalk")
    def sidewalk(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPartnerAccount.SidewalkAccountInfoProperty"]]:
        '''``AWS::IoTWireless::PartnerAccount.Sidewalk``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalk
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPartnerAccount.SidewalkAccountInfoProperty"]], jsii.get(self, "sidewalk"))

    @sidewalk.setter
    def sidewalk(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPartnerAccount.SidewalkAccountInfoProperty"]],
    ) -> None:
        jsii.set(self, "sidewalk", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sidewalkUpdate")
    def sidewalk_update(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]]:
        '''``AWS::IoTWireless::PartnerAccount.SidewalkUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkupdate
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]], jsii.get(self, "sidewalkUpdate"))

    @sidewalk_update.setter
    def sidewalk_update(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]],
    ) -> None:
        jsii.set(self, "sidewalkUpdate", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnPartnerAccount.SidewalkAccountInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"app_server_private_key": "appServerPrivateKey"},
    )
    class SidewalkAccountInfoProperty:
        def __init__(self, *, app_server_private_key: builtins.str) -> None:
            '''
            :param app_server_private_key: ``CfnPartnerAccount.SidewalkAccountInfoProperty.AppServerPrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "app_server_private_key": app_server_private_key,
            }

        @builtins.property
        def app_server_private_key(self) -> builtins.str:
            '''``CfnPartnerAccount.SidewalkAccountInfoProperty.AppServerPrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html#cfn-iotwireless-partneraccount-sidewalkaccountinfo-appserverprivatekey
            '''
            result = self._values.get("app_server_private_key")
            assert result is not None, "Required property 'app_server_private_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SidewalkAccountInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnPartnerAccount.SidewalkUpdateAccountProperty",
        jsii_struct_bases=[],
        name_mapping={"app_server_private_key": "appServerPrivateKey"},
    )
    class SidewalkUpdateAccountProperty:
        def __init__(
            self,
            *,
            app_server_private_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param app_server_private_key: ``CfnPartnerAccount.SidewalkUpdateAccountProperty.AppServerPrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if app_server_private_key is not None:
                self._values["app_server_private_key"] = app_server_private_key

        @builtins.property
        def app_server_private_key(self) -> typing.Optional[builtins.str]:
            '''``CfnPartnerAccount.SidewalkUpdateAccountProperty.AppServerPrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html#cfn-iotwireless-partneraccount-sidewalkupdateaccount-appserverprivatekey
            '''
            result = self._values.get("app_server_private_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SidewalkUpdateAccountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnPartnerAccountProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_linked": "accountLinked",
        "fingerprint": "fingerprint",
        "partner_account_id": "partnerAccountId",
        "partner_type": "partnerType",
        "sidewalk": "sidewalk",
        "sidewalk_update": "sidewalkUpdate",
        "tags": "tags",
    },
)
class CfnPartnerAccountProps:
    def __init__(
        self,
        *,
        account_linked: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        fingerprint: typing.Optional[builtins.str] = None,
        partner_account_id: typing.Optional[builtins.str] = None,
        partner_type: typing.Optional[builtins.str] = None,
        sidewalk: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPartnerAccount.SidewalkAccountInfoProperty]] = None,
        sidewalk_update: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPartnerAccount.SidewalkUpdateAccountProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTWireless::PartnerAccount``.

        :param account_linked: ``AWS::IoTWireless::PartnerAccount.AccountLinked``.
        :param fingerprint: ``AWS::IoTWireless::PartnerAccount.Fingerprint``.
        :param partner_account_id: ``AWS::IoTWireless::PartnerAccount.PartnerAccountId``.
        :param partner_type: ``AWS::IoTWireless::PartnerAccount.PartnerType``.
        :param sidewalk: ``AWS::IoTWireless::PartnerAccount.Sidewalk``.
        :param sidewalk_update: ``AWS::IoTWireless::PartnerAccount.SidewalkUpdate``.
        :param tags: ``AWS::IoTWireless::PartnerAccount.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if account_linked is not None:
            self._values["account_linked"] = account_linked
        if fingerprint is not None:
            self._values["fingerprint"] = fingerprint
        if partner_account_id is not None:
            self._values["partner_account_id"] = partner_account_id
        if partner_type is not None:
            self._values["partner_type"] = partner_type
        if sidewalk is not None:
            self._values["sidewalk"] = sidewalk
        if sidewalk_update is not None:
            self._values["sidewalk_update"] = sidewalk_update
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def account_linked(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::IoTWireless::PartnerAccount.AccountLinked``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-accountlinked
        '''
        result = self._values.get("account_linked")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def fingerprint(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.Fingerprint``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-fingerprint
        '''
        result = self._values.get("fingerprint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partner_account_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.PartnerAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partneraccountid
        '''
        result = self._values.get("partner_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partner_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.PartnerType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partnertype
        '''
        result = self._values.get("partner_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sidewalk(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPartnerAccount.SidewalkAccountInfoProperty]]:
        '''``AWS::IoTWireless::PartnerAccount.Sidewalk``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalk
        '''
        result = self._values.get("sidewalk")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPartnerAccount.SidewalkAccountInfoProperty]], result)

    @builtins.property
    def sidewalk_update(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPartnerAccount.SidewalkUpdateAccountProperty]]:
        '''``AWS::IoTWireless::PartnerAccount.SidewalkUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkupdate
        '''
        result = self._values.get("sidewalk_update")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPartnerAccount.SidewalkUpdateAccountProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTWireless::PartnerAccount.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPartnerAccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnServiceProfile(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnServiceProfile",
):
    '''A CloudFormation ``AWS::IoTWireless::ServiceProfile``.

    :cloudformationResource: AWS::IoTWireless::ServiceProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        lo_ra_wan: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServiceProfile.LoRaWANServiceProfileProperty"]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::ServiceProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan: ``AWS::IoTWireless::ServiceProfile.LoRaWAN``.
        :param name: ``AWS::IoTWireless::ServiceProfile.Name``.
        :param tags: ``AWS::IoTWireless::ServiceProfile.Tags``.
        '''
        props = CfnServiceProfileProps(lo_ra_wan=lo_ra_wan, name=name, tags=tags)

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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanChannelMask")
    def attr_lo_ra_wan_channel_mask(self) -> builtins.str:
        '''
        :cloudformationAttribute: LoRaWAN.ChannelMask
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanChannelMask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanDevStatusReqFreq")
    def attr_lo_ra_wan_dev_status_req_freq(self) -> jsii.Number:
        '''
        :cloudformationAttribute: LoRaWAN.DevStatusReqFreq
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDevStatusReqFreq"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanDlBucketSize")
    def attr_lo_ra_wan_dl_bucket_size(self) -> jsii.Number:
        '''
        :cloudformationAttribute: LoRaWAN.DlBucketSize
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDlBucketSize"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanDlRate")
    def attr_lo_ra_wan_dl_rate(self) -> jsii.Number:
        '''
        :cloudformationAttribute: LoRaWAN.DlRate
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDlRate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanDlRatePolicy")
    def attr_lo_ra_wan_dl_rate_policy(self) -> builtins.str:
        '''
        :cloudformationAttribute: LoRaWAN.DlRatePolicy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanDlRatePolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanDrMax")
    def attr_lo_ra_wan_dr_max(self) -> jsii.Number:
        '''
        :cloudformationAttribute: LoRaWAN.DrMax
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDrMax"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanDrMin")
    def attr_lo_ra_wan_dr_min(self) -> jsii.Number:
        '''
        :cloudformationAttribute: LoRaWAN.DrMin
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDrMin"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanHrAllowed")
    def attr_lo_ra_wan_hr_allowed(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: LoRaWAN.HrAllowed
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrLoRaWanHrAllowed"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanMinGwDiversity")
    def attr_lo_ra_wan_min_gw_diversity(self) -> jsii.Number:
        '''
        :cloudformationAttribute: LoRaWAN.MinGwDiversity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanMinGwDiversity"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanNwkGeoLoc")
    def attr_lo_ra_wan_nwk_geo_loc(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: LoRaWAN.NwkGeoLoc
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrLoRaWanNwkGeoLoc"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanPrAllowed")
    def attr_lo_ra_wan_pr_allowed(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: LoRaWAN.PrAllowed
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrLoRaWanPrAllowed"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanRaAllowed")
    def attr_lo_ra_wan_ra_allowed(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: LoRaWAN.RaAllowed
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrLoRaWanRaAllowed"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanReportDevStatusBattery")
    def attr_lo_ra_wan_report_dev_status_battery(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: LoRaWAN.ReportDevStatusBattery
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrLoRaWanReportDevStatusBattery"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanReportDevStatusMargin")
    def attr_lo_ra_wan_report_dev_status_margin(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: LoRaWAN.ReportDevStatusMargin
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrLoRaWanReportDevStatusMargin"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanResponse")
    def attr_lo_ra_wan_response(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: LoRaWANResponse
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrLoRaWanResponse"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanTargetPer")
    def attr_lo_ra_wan_target_per(self) -> jsii.Number:
        '''
        :cloudformationAttribute: LoRaWAN.TargetPer
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanTargetPer"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanUlBucketSize")
    def attr_lo_ra_wan_ul_bucket_size(self) -> jsii.Number:
        '''
        :cloudformationAttribute: LoRaWAN.UlBucketSize
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanUlBucketSize"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanUlRate")
    def attr_lo_ra_wan_ul_rate(self) -> jsii.Number:
        '''
        :cloudformationAttribute: LoRaWAN.UlRate
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanUlRate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoRaWanUlRatePolicy")
    def attr_lo_ra_wan_ul_rate_policy(self) -> builtins.str:
        '''
        :cloudformationAttribute: LoRaWAN.UlRatePolicy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanUlRatePolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTWireless::ServiceProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServiceProfile.LoRaWANServiceProfileProperty"]]:
        '''``AWS::IoTWireless::ServiceProfile.LoRaWAN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawan
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServiceProfile.LoRaWANServiceProfileProperty"]], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServiceProfile.LoRaWANServiceProfileProperty"]],
    ) -> None:
        jsii.set(self, "loRaWan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::ServiceProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_gw_metadata": "addGwMetadata",
            "channel_mask": "channelMask",
            "dev_status_req_freq": "devStatusReqFreq",
            "dl_bucket_size": "dlBucketSize",
            "dl_rate": "dlRate",
            "dl_rate_policy": "dlRatePolicy",
            "dr_max": "drMax",
            "dr_min": "drMin",
            "hr_allowed": "hrAllowed",
            "min_gw_diversity": "minGwDiversity",
            "nwk_geo_loc": "nwkGeoLoc",
            "pr_allowed": "prAllowed",
            "ra_allowed": "raAllowed",
            "report_dev_status_battery": "reportDevStatusBattery",
            "report_dev_status_margin": "reportDevStatusMargin",
            "target_per": "targetPer",
            "ul_bucket_size": "ulBucketSize",
            "ul_rate": "ulRate",
            "ul_rate_policy": "ulRatePolicy",
        },
    )
    class LoRaWANServiceProfileProperty:
        def __init__(
            self,
            *,
            add_gw_metadata: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            channel_mask: typing.Optional[builtins.str] = None,
            dev_status_req_freq: typing.Optional[jsii.Number] = None,
            dl_bucket_size: typing.Optional[jsii.Number] = None,
            dl_rate: typing.Optional[jsii.Number] = None,
            dl_rate_policy: typing.Optional[builtins.str] = None,
            dr_max: typing.Optional[jsii.Number] = None,
            dr_min: typing.Optional[jsii.Number] = None,
            hr_allowed: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            min_gw_diversity: typing.Optional[jsii.Number] = None,
            nwk_geo_loc: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            pr_allowed: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            ra_allowed: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            report_dev_status_battery: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            report_dev_status_margin: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            target_per: typing.Optional[jsii.Number] = None,
            ul_bucket_size: typing.Optional[jsii.Number] = None,
            ul_rate: typing.Optional[jsii.Number] = None,
            ul_rate_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param add_gw_metadata: ``CfnServiceProfile.LoRaWANServiceProfileProperty.AddGwMetadata``.
            :param channel_mask: ``CfnServiceProfile.LoRaWANServiceProfileProperty.ChannelMask``.
            :param dev_status_req_freq: ``CfnServiceProfile.LoRaWANServiceProfileProperty.DevStatusReqFreq``.
            :param dl_bucket_size: ``CfnServiceProfile.LoRaWANServiceProfileProperty.DlBucketSize``.
            :param dl_rate: ``CfnServiceProfile.LoRaWANServiceProfileProperty.DlRate``.
            :param dl_rate_policy: ``CfnServiceProfile.LoRaWANServiceProfileProperty.DlRatePolicy``.
            :param dr_max: ``CfnServiceProfile.LoRaWANServiceProfileProperty.DrMax``.
            :param dr_min: ``CfnServiceProfile.LoRaWANServiceProfileProperty.DrMin``.
            :param hr_allowed: ``CfnServiceProfile.LoRaWANServiceProfileProperty.HrAllowed``.
            :param min_gw_diversity: ``CfnServiceProfile.LoRaWANServiceProfileProperty.MinGwDiversity``.
            :param nwk_geo_loc: ``CfnServiceProfile.LoRaWANServiceProfileProperty.NwkGeoLoc``.
            :param pr_allowed: ``CfnServiceProfile.LoRaWANServiceProfileProperty.PrAllowed``.
            :param ra_allowed: ``CfnServiceProfile.LoRaWANServiceProfileProperty.RaAllowed``.
            :param report_dev_status_battery: ``CfnServiceProfile.LoRaWANServiceProfileProperty.ReportDevStatusBattery``.
            :param report_dev_status_margin: ``CfnServiceProfile.LoRaWANServiceProfileProperty.ReportDevStatusMargin``.
            :param target_per: ``CfnServiceProfile.LoRaWANServiceProfileProperty.TargetPer``.
            :param ul_bucket_size: ``CfnServiceProfile.LoRaWANServiceProfileProperty.UlBucketSize``.
            :param ul_rate: ``CfnServiceProfile.LoRaWANServiceProfileProperty.UlRate``.
            :param ul_rate_policy: ``CfnServiceProfile.LoRaWANServiceProfileProperty.UlRatePolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if add_gw_metadata is not None:
                self._values["add_gw_metadata"] = add_gw_metadata
            if channel_mask is not None:
                self._values["channel_mask"] = channel_mask
            if dev_status_req_freq is not None:
                self._values["dev_status_req_freq"] = dev_status_req_freq
            if dl_bucket_size is not None:
                self._values["dl_bucket_size"] = dl_bucket_size
            if dl_rate is not None:
                self._values["dl_rate"] = dl_rate
            if dl_rate_policy is not None:
                self._values["dl_rate_policy"] = dl_rate_policy
            if dr_max is not None:
                self._values["dr_max"] = dr_max
            if dr_min is not None:
                self._values["dr_min"] = dr_min
            if hr_allowed is not None:
                self._values["hr_allowed"] = hr_allowed
            if min_gw_diversity is not None:
                self._values["min_gw_diversity"] = min_gw_diversity
            if nwk_geo_loc is not None:
                self._values["nwk_geo_loc"] = nwk_geo_loc
            if pr_allowed is not None:
                self._values["pr_allowed"] = pr_allowed
            if ra_allowed is not None:
                self._values["ra_allowed"] = ra_allowed
            if report_dev_status_battery is not None:
                self._values["report_dev_status_battery"] = report_dev_status_battery
            if report_dev_status_margin is not None:
                self._values["report_dev_status_margin"] = report_dev_status_margin
            if target_per is not None:
                self._values["target_per"] = target_per
            if ul_bucket_size is not None:
                self._values["ul_bucket_size"] = ul_bucket_size
            if ul_rate is not None:
                self._values["ul_rate"] = ul_rate
            if ul_rate_policy is not None:
                self._values["ul_rate_policy"] = ul_rate_policy

        @builtins.property
        def add_gw_metadata(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.AddGwMetadata``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata
            '''
            result = self._values.get("add_gw_metadata")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def channel_mask(self) -> typing.Optional[builtins.str]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.ChannelMask``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-channelmask
            '''
            result = self._values.get("channel_mask")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dev_status_req_freq(self) -> typing.Optional[jsii.Number]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.DevStatusReqFreq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-devstatusreqfreq
            '''
            result = self._values.get("dev_status_req_freq")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dl_bucket_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.DlBucketSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlbucketsize
            '''
            result = self._values.get("dl_bucket_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dl_rate(self) -> typing.Optional[jsii.Number]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.DlRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlrate
            '''
            result = self._values.get("dl_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dl_rate_policy(self) -> typing.Optional[builtins.str]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.DlRatePolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlratepolicy
            '''
            result = self._values.get("dl_rate_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dr_max(self) -> typing.Optional[jsii.Number]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.DrMax``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmax
            '''
            result = self._values.get("dr_max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dr_min(self) -> typing.Optional[jsii.Number]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.DrMin``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmin
            '''
            result = self._values.get("dr_min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def hr_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.HrAllowed``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-hrallowed
            '''
            result = self._values.get("hr_allowed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def min_gw_diversity(self) -> typing.Optional[jsii.Number]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.MinGwDiversity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-mingwdiversity
            '''
            result = self._values.get("min_gw_diversity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def nwk_geo_loc(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.NwkGeoLoc``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-nwkgeoloc
            '''
            result = self._values.get("nwk_geo_loc")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def pr_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.PrAllowed``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-prallowed
            '''
            result = self._values.get("pr_allowed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def ra_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.RaAllowed``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-raallowed
            '''
            result = self._values.get("ra_allowed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def report_dev_status_battery(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.ReportDevStatusBattery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusbattery
            '''
            result = self._values.get("report_dev_status_battery")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def report_dev_status_margin(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.ReportDevStatusMargin``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusmargin
            '''
            result = self._values.get("report_dev_status_margin")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def target_per(self) -> typing.Optional[jsii.Number]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.TargetPer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-targetper
            '''
            result = self._values.get("target_per")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ul_bucket_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.UlBucketSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulbucketsize
            '''
            result = self._values.get("ul_bucket_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ul_rate(self) -> typing.Optional[jsii.Number]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.UlRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulrate
            '''
            result = self._values.get("ul_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ul_rate_policy(self) -> typing.Optional[builtins.str]:
            '''``CfnServiceProfile.LoRaWANServiceProfileProperty.UlRatePolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulratepolicy
            '''
            result = self._values.get("ul_rate_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANServiceProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnServiceProfileProps",
    jsii_struct_bases=[],
    name_mapping={"lo_ra_wan": "loRaWan", "name": "name", "tags": "tags"},
)
class CfnServiceProfileProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServiceProfile.LoRaWANServiceProfileProperty]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTWireless::ServiceProfile``.

        :param lo_ra_wan: ``AWS::IoTWireless::ServiceProfile.LoRaWAN``.
        :param name: ``AWS::IoTWireless::ServiceProfile.Name``.
        :param tags: ``AWS::IoTWireless::ServiceProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if lo_ra_wan is not None:
            self._values["lo_ra_wan"] = lo_ra_wan
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServiceProfile.LoRaWANServiceProfileProperty]]:
        '''``AWS::IoTWireless::ServiceProfile.LoRaWAN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServiceProfile.LoRaWANServiceProfileProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::ServiceProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTWireless::ServiceProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTaskDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition",
):
    '''A CloudFormation ``AWS::IoTWireless::TaskDefinition``.

    :cloudformationResource: AWS::IoTWireless::TaskDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        auto_create_tasks: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        task_definition_type: typing.Optional[builtins.str] = None,
        update: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::TaskDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param auto_create_tasks: ``AWS::IoTWireless::TaskDefinition.AutoCreateTasks``.
        :param lo_ra_wan_update_gateway_task_entry: ``AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry``.
        :param name: ``AWS::IoTWireless::TaskDefinition.Name``.
        :param tags: ``AWS::IoTWireless::TaskDefinition.Tags``.
        :param task_definition_type: ``AWS::IoTWireless::TaskDefinition.TaskDefinitionType``.
        :param update: ``AWS::IoTWireless::TaskDefinition.Update``.
        '''
        props = CfnTaskDefinitionProps(
            auto_create_tasks=auto_create_tasks,
            lo_ra_wan_update_gateway_task_entry=lo_ra_wan_update_gateway_task_entry,
            name=name,
            tags=tags,
            task_definition_type=task_definition_type,
            update=update,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTWireless::TaskDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoCreateTasks")
    def auto_create_tasks(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::IoTWireless::TaskDefinition.AutoCreateTasks``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-autocreatetasks
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "autoCreateTasks"))

    @auto_create_tasks.setter
    def auto_create_tasks(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "autoCreateTasks", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loRaWanUpdateGatewayTaskEntry")
    def lo_ra_wan_update_gateway_task_entry(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]]:
        '''``AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]], jsii.get(self, "loRaWanUpdateGatewayTaskEntry"))

    @lo_ra_wan_update_gateway_task_entry.setter
    def lo_ra_wan_update_gateway_task_entry(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]],
    ) -> None:
        jsii.set(self, "loRaWanUpdateGatewayTaskEntry", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::TaskDefinition.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taskDefinitionType")
    def task_definition_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::TaskDefinition.TaskDefinitionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-taskdefinitiontype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionType"))

    @task_definition_type.setter
    def task_definition_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "taskDefinitionType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="update")
    def update(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]]:
        '''``AWS::IoTWireless::TaskDefinition.Update``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-update
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]], jsii.get(self, "update"))

    @update.setter
    def update(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]],
    ) -> None:
        jsii.set(self, "update", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "model": "model",
            "package_version": "packageVersion",
            "station": "station",
        },
    )
    class LoRaWANGatewayVersionProperty:
        def __init__(
            self,
            *,
            model: typing.Optional[builtins.str] = None,
            package_version: typing.Optional[builtins.str] = None,
            station: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param model: ``CfnTaskDefinition.LoRaWANGatewayVersionProperty.Model``.
            :param package_version: ``CfnTaskDefinition.LoRaWANGatewayVersionProperty.PackageVersion``.
            :param station: ``CfnTaskDefinition.LoRaWANGatewayVersionProperty.Station``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if model is not None:
                self._values["model"] = model
            if package_version is not None:
                self._values["package_version"] = package_version
            if station is not None:
                self._values["station"] = station

        @builtins.property
        def model(self) -> typing.Optional[builtins.str]:
            '''``CfnTaskDefinition.LoRaWANGatewayVersionProperty.Model``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-model
            '''
            result = self._values.get("model")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def package_version(self) -> typing.Optional[builtins.str]:
            '''``CfnTaskDefinition.LoRaWANGatewayVersionProperty.PackageVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-packageversion
            '''
            result = self._values.get("package_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def station(self) -> typing.Optional[builtins.str]:
            '''``CfnTaskDefinition.LoRaWANGatewayVersionProperty.Station``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-station
            '''
            result = self._values.get("station")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANGatewayVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "current_version": "currentVersion",
            "sig_key_crc": "sigKeyCrc",
            "update_signature": "updateSignature",
            "update_version": "updateVersion",
        },
    )
    class LoRaWANUpdateGatewayTaskCreateProperty:
        def __init__(
            self,
            *,
            current_version: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]] = None,
            sig_key_crc: typing.Optional[jsii.Number] = None,
            update_signature: typing.Optional[builtins.str] = None,
            update_version: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]] = None,
        ) -> None:
            '''
            :param current_version: ``CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty.CurrentVersion``.
            :param sig_key_crc: ``CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty.SigKeyCrc``.
            :param update_signature: ``CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty.UpdateSignature``.
            :param update_version: ``CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty.UpdateVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if current_version is not None:
                self._values["current_version"] = current_version
            if sig_key_crc is not None:
                self._values["sig_key_crc"] = sig_key_crc
            if update_signature is not None:
                self._values["update_signature"] = update_signature
            if update_version is not None:
                self._values["update_version"] = update_version

        @builtins.property
        def current_version(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''``CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty.CurrentVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-currentversion
            '''
            result = self._values.get("current_version")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        @builtins.property
        def sig_key_crc(self) -> typing.Optional[jsii.Number]:
            '''``CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty.SigKeyCrc``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-sigkeycrc
            '''
            result = self._values.get("sig_key_crc")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def update_signature(self) -> typing.Optional[builtins.str]:
            '''``CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty.UpdateSignature``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updatesignature
            '''
            result = self._values.get("update_signature")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def update_version(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''``CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty.UpdateVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updateversion
            '''
            result = self._values.get("update_version")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANUpdateGatewayTaskCreateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "current_version": "currentVersion",
            "update_version": "updateVersion",
        },
    )
    class LoRaWANUpdateGatewayTaskEntryProperty:
        def __init__(
            self,
            *,
            current_version: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]] = None,
            update_version: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]] = None,
        ) -> None:
            '''
            :param current_version: ``CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty.CurrentVersion``.
            :param update_version: ``CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty.UpdateVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if current_version is not None:
                self._values["current_version"] = current_version
            if update_version is not None:
                self._values["update_version"] = update_version

        @builtins.property
        def current_version(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''``CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty.CurrentVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-currentversion
            '''
            result = self._values.get("current_version")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        @builtins.property
        def update_version(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''``CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty.UpdateVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-updateversion
            '''
            result = self._values.get("update_version")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANUpdateGatewayTaskEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lo_ra_wan": "loRaWan",
            "update_data_role": "updateDataRole",
            "update_data_source": "updateDataSource",
        },
    )
    class UpdateWirelessGatewayTaskCreateProperty:
        def __init__(
            self,
            *,
            lo_ra_wan: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty"]] = None,
            update_data_role: typing.Optional[builtins.str] = None,
            update_data_source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param lo_ra_wan: ``CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty.LoRaWAN``.
            :param update_data_role: ``CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty.UpdateDataRole``.
            :param update_data_source: ``CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty.UpdateDataSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if lo_ra_wan is not None:
                self._values["lo_ra_wan"] = lo_ra_wan
            if update_data_role is not None:
                self._values["update_data_role"] = update_data_role
            if update_data_source is not None:
                self._values["update_data_source"] = update_data_source

        @builtins.property
        def lo_ra_wan(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty"]]:
            '''``CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty.LoRaWAN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-lorawan
            '''
            result = self._values.get("lo_ra_wan")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty"]], result)

        @builtins.property
        def update_data_role(self) -> typing.Optional[builtins.str]:
            '''``CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty.UpdateDataRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatarole
            '''
            result = self._values.get("update_data_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def update_data_source(self) -> typing.Optional[builtins.str]:
            '''``CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty.UpdateDataSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatasource
            '''
            result = self._values.get("update_data_source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateWirelessGatewayTaskCreateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_create_tasks": "autoCreateTasks",
        "lo_ra_wan_update_gateway_task_entry": "loRaWanUpdateGatewayTaskEntry",
        "name": "name",
        "tags": "tags",
        "task_definition_type": "taskDefinitionType",
        "update": "update",
    },
)
class CfnTaskDefinitionProps:
    def __init__(
        self,
        *,
        auto_create_tasks: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        task_definition_type: typing.Optional[builtins.str] = None,
        update: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTWireless::TaskDefinition``.

        :param auto_create_tasks: ``AWS::IoTWireless::TaskDefinition.AutoCreateTasks``.
        :param lo_ra_wan_update_gateway_task_entry: ``AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry``.
        :param name: ``AWS::IoTWireless::TaskDefinition.Name``.
        :param tags: ``AWS::IoTWireless::TaskDefinition.Tags``.
        :param task_definition_type: ``AWS::IoTWireless::TaskDefinition.TaskDefinitionType``.
        :param update: ``AWS::IoTWireless::TaskDefinition.Update``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "auto_create_tasks": auto_create_tasks,
        }
        if lo_ra_wan_update_gateway_task_entry is not None:
            self._values["lo_ra_wan_update_gateway_task_entry"] = lo_ra_wan_update_gateway_task_entry
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if task_definition_type is not None:
            self._values["task_definition_type"] = task_definition_type
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def auto_create_tasks(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::IoTWireless::TaskDefinition.AutoCreateTasks``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-autocreatetasks
        '''
        result = self._values.get("auto_create_tasks")
        assert result is not None, "Required property 'auto_create_tasks' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def lo_ra_wan_update_gateway_task_entry(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty]]:
        '''``AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry
        '''
        result = self._values.get("lo_ra_wan_update_gateway_task_entry")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::TaskDefinition.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTWireless::TaskDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def task_definition_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::TaskDefinition.TaskDefinitionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-taskdefinitiontype
        '''
        result = self._values.get("task_definition_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty]]:
        '''``AWS::IoTWireless::TaskDefinition.Update``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-update
        '''
        result = self._values.get("update")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTaskDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWirelessDevice(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice",
):
    '''A CloudFormation ``AWS::IoTWireless::WirelessDevice``.

    :cloudformationResource: AWS::IoTWireless::WirelessDevice
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        destination_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        lo_ra_wan: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.LoRaWANDeviceProperty"]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::WirelessDevice``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param destination_name: ``AWS::IoTWireless::WirelessDevice.DestinationName``.
        :param type: ``AWS::IoTWireless::WirelessDevice.Type``.
        :param description: ``AWS::IoTWireless::WirelessDevice.Description``.
        :param last_uplink_received_at: ``AWS::IoTWireless::WirelessDevice.LastUplinkReceivedAt``.
        :param lo_ra_wan: ``AWS::IoTWireless::WirelessDevice.LoRaWAN``.
        :param name: ``AWS::IoTWireless::WirelessDevice.Name``.
        :param tags: ``AWS::IoTWireless::WirelessDevice.Tags``.
        :param thing_arn: ``AWS::IoTWireless::WirelessDevice.ThingArn``.
        '''
        props = CfnWirelessDeviceProps(
            destination_name=destination_name,
            type=type,
            description=description,
            last_uplink_received_at=last_uplink_received_at,
            lo_ra_wan=lo_ra_wan,
            name=name,
            tags=tags,
            thing_arn=thing_arn,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrThingName")
    def attr_thing_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ThingName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrThingName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTWireless::WirelessDevice.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> builtins.str:
        '''``AWS::IoTWireless::WirelessDevice.DestinationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "destinationName"))

    @destination_name.setter
    def destination_name(self, value: builtins.str) -> None:
        jsii.set(self, "destinationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::IoTWireless::WirelessDevice.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessDevice.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lastUplinkReceivedAt")
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessDevice.LastUplinkReceivedAt``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lastuplinkreceivedat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastUplinkReceivedAt"))

    @last_uplink_received_at.setter
    def last_uplink_received_at(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "lastUplinkReceivedAt", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.LoRaWANDeviceProperty"]]:
        '''``AWS::IoTWireless::WirelessDevice.LoRaWAN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawan
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.LoRaWANDeviceProperty"]], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.LoRaWANDeviceProperty"]],
    ) -> None:
        jsii.set(self, "loRaWan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessDevice.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="thingArn")
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessDevice.ThingArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-thingarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingArn"))

    @thing_arn.setter
    def thing_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "thingArn", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.AbpV10xProperty",
        jsii_struct_bases=[],
        name_mapping={"dev_addr": "devAddr", "session_keys": "sessionKeys"},
    )
    class AbpV10xProperty:
        def __init__(
            self,
            *,
            dev_addr: builtins.str,
            session_keys: typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.SessionKeysAbpV10xProperty"],
        ) -> None:
            '''
            :param dev_addr: ``CfnWirelessDevice.AbpV10xProperty.DevAddr``.
            :param session_keys: ``CfnWirelessDevice.AbpV10xProperty.SessionKeys``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "dev_addr": dev_addr,
                "session_keys": session_keys,
            }

        @builtins.property
        def dev_addr(self) -> builtins.str:
            '''``CfnWirelessDevice.AbpV10xProperty.DevAddr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-devaddr
            '''
            result = self._values.get("dev_addr")
            assert result is not None, "Required property 'dev_addr' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def session_keys(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.SessionKeysAbpV10xProperty"]:
            '''``CfnWirelessDevice.AbpV10xProperty.SessionKeys``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-sessionkeys
            '''
            result = self._values.get("session_keys")
            assert result is not None, "Required property 'session_keys' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.SessionKeysAbpV10xProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbpV10xProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.AbpV11Property",
        jsii_struct_bases=[],
        name_mapping={"dev_addr": "devAddr", "session_keys": "sessionKeys"},
    )
    class AbpV11Property:
        def __init__(
            self,
            *,
            dev_addr: builtins.str,
            session_keys: typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.SessionKeysAbpV11Property"],
        ) -> None:
            '''
            :param dev_addr: ``CfnWirelessDevice.AbpV11Property.DevAddr``.
            :param session_keys: ``CfnWirelessDevice.AbpV11Property.SessionKeys``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "dev_addr": dev_addr,
                "session_keys": session_keys,
            }

        @builtins.property
        def dev_addr(self) -> builtins.str:
            '''``CfnWirelessDevice.AbpV11Property.DevAddr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-devaddr
            '''
            result = self._values.get("dev_addr")
            assert result is not None, "Required property 'dev_addr' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def session_keys(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.SessionKeysAbpV11Property"]:
            '''``CfnWirelessDevice.AbpV11Property.SessionKeys``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-sessionkeys
            '''
            result = self._values.get("session_keys")
            assert result is not None, "Required property 'session_keys' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.SessionKeysAbpV11Property"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbpV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "abp_v10_x": "abpV10X",
            "abp_v11": "abpV11",
            "dev_eui": "devEui",
            "device_profile_id": "deviceProfileId",
            "otaa_v10_x": "otaaV10X",
            "otaa_v11": "otaaV11",
            "service_profile_id": "serviceProfileId",
        },
    )
    class LoRaWANDeviceProperty:
        def __init__(
            self,
            *,
            abp_v10_x: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.AbpV10xProperty"]] = None,
            abp_v11: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.AbpV11Property"]] = None,
            dev_eui: typing.Optional[builtins.str] = None,
            device_profile_id: typing.Optional[builtins.str] = None,
            otaa_v10_x: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.OtaaV10xProperty"]] = None,
            otaa_v11: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.OtaaV11Property"]] = None,
            service_profile_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param abp_v10_x: ``CfnWirelessDevice.LoRaWANDeviceProperty.AbpV10x``.
            :param abp_v11: ``CfnWirelessDevice.LoRaWANDeviceProperty.AbpV11``.
            :param dev_eui: ``CfnWirelessDevice.LoRaWANDeviceProperty.DevEui``.
            :param device_profile_id: ``CfnWirelessDevice.LoRaWANDeviceProperty.DeviceProfileId``.
            :param otaa_v10_x: ``CfnWirelessDevice.LoRaWANDeviceProperty.OtaaV10x``.
            :param otaa_v11: ``CfnWirelessDevice.LoRaWANDeviceProperty.OtaaV11``.
            :param service_profile_id: ``CfnWirelessDevice.LoRaWANDeviceProperty.ServiceProfileId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if abp_v10_x is not None:
                self._values["abp_v10_x"] = abp_v10_x
            if abp_v11 is not None:
                self._values["abp_v11"] = abp_v11
            if dev_eui is not None:
                self._values["dev_eui"] = dev_eui
            if device_profile_id is not None:
                self._values["device_profile_id"] = device_profile_id
            if otaa_v10_x is not None:
                self._values["otaa_v10_x"] = otaa_v10_x
            if otaa_v11 is not None:
                self._values["otaa_v11"] = otaa_v11
            if service_profile_id is not None:
                self._values["service_profile_id"] = service_profile_id

        @builtins.property
        def abp_v10_x(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.AbpV10xProperty"]]:
            '''``CfnWirelessDevice.LoRaWANDeviceProperty.AbpV10x``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x
            '''
            result = self._values.get("abp_v10_x")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.AbpV10xProperty"]], result)

        @builtins.property
        def abp_v11(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.AbpV11Property"]]:
            '''``CfnWirelessDevice.LoRaWANDeviceProperty.AbpV11``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv11
            '''
            result = self._values.get("abp_v11")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.AbpV11Property"]], result)

        @builtins.property
        def dev_eui(self) -> typing.Optional[builtins.str]:
            '''``CfnWirelessDevice.LoRaWANDeviceProperty.DevEui``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deveui
            '''
            result = self._values.get("dev_eui")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_profile_id(self) -> typing.Optional[builtins.str]:
            '''``CfnWirelessDevice.LoRaWANDeviceProperty.DeviceProfileId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid
            '''
            result = self._values.get("device_profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def otaa_v10_x(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.OtaaV10xProperty"]]:
            '''``CfnWirelessDevice.LoRaWANDeviceProperty.OtaaV10x``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x
            '''
            result = self._values.get("otaa_v10_x")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.OtaaV10xProperty"]], result)

        @builtins.property
        def otaa_v11(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.OtaaV11Property"]]:
            '''``CfnWirelessDevice.LoRaWANDeviceProperty.OtaaV11``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav11
            '''
            result = self._values.get("otaa_v11")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWirelessDevice.OtaaV11Property"]], result)

        @builtins.property
        def service_profile_id(self) -> typing.Optional[builtins.str]:
            '''``CfnWirelessDevice.LoRaWANDeviceProperty.ServiceProfileId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid
            '''
            result = self._values.get("service_profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANDeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.OtaaV10xProperty",
        jsii_struct_bases=[],
        name_mapping={"app_eui": "appEui", "app_key": "appKey"},
    )
    class OtaaV10xProperty:
        def __init__(self, *, app_eui: builtins.str, app_key: builtins.str) -> None:
            '''
            :param app_eui: ``CfnWirelessDevice.OtaaV10xProperty.AppEui``.
            :param app_key: ``CfnWirelessDevice.OtaaV10xProperty.AppKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "app_eui": app_eui,
                "app_key": app_key,
            }

        @builtins.property
        def app_eui(self) -> builtins.str:
            '''``CfnWirelessDevice.OtaaV10xProperty.AppEui``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appeui
            '''
            result = self._values.get("app_eui")
            assert result is not None, "Required property 'app_eui' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def app_key(self) -> builtins.str:
            '''``CfnWirelessDevice.OtaaV10xProperty.AppKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appkey
            '''
            result = self._values.get("app_key")
            assert result is not None, "Required property 'app_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtaaV10xProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.OtaaV11Property",
        jsii_struct_bases=[],
        name_mapping={"app_key": "appKey", "join_eui": "joinEui", "nwk_key": "nwkKey"},
    )
    class OtaaV11Property:
        def __init__(
            self,
            *,
            app_key: builtins.str,
            join_eui: builtins.str,
            nwk_key: builtins.str,
        ) -> None:
            '''
            :param app_key: ``CfnWirelessDevice.OtaaV11Property.AppKey``.
            :param join_eui: ``CfnWirelessDevice.OtaaV11Property.JoinEui``.
            :param nwk_key: ``CfnWirelessDevice.OtaaV11Property.NwkKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "app_key": app_key,
                "join_eui": join_eui,
                "nwk_key": nwk_key,
            }

        @builtins.property
        def app_key(self) -> builtins.str:
            '''``CfnWirelessDevice.OtaaV11Property.AppKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-appkey
            '''
            result = self._values.get("app_key")
            assert result is not None, "Required property 'app_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def join_eui(self) -> builtins.str:
            '''``CfnWirelessDevice.OtaaV11Property.JoinEui``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-joineui
            '''
            result = self._values.get("join_eui")
            assert result is not None, "Required property 'join_eui' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nwk_key(self) -> builtins.str:
            '''``CfnWirelessDevice.OtaaV11Property.NwkKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-nwkkey
            '''
            result = self._values.get("nwk_key")
            assert result is not None, "Required property 'nwk_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtaaV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty",
        jsii_struct_bases=[],
        name_mapping={"app_s_key": "appSKey", "nwk_s_key": "nwkSKey"},
    )
    class SessionKeysAbpV10xProperty:
        def __init__(self, *, app_s_key: builtins.str, nwk_s_key: builtins.str) -> None:
            '''
            :param app_s_key: ``CfnWirelessDevice.SessionKeysAbpV10xProperty.AppSKey``.
            :param nwk_s_key: ``CfnWirelessDevice.SessionKeysAbpV10xProperty.NwkSKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "app_s_key": app_s_key,
                "nwk_s_key": nwk_s_key,
            }

        @builtins.property
        def app_s_key(self) -> builtins.str:
            '''``CfnWirelessDevice.SessionKeysAbpV10xProperty.AppSKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey
            '''
            result = self._values.get("app_s_key")
            assert result is not None, "Required property 'app_s_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nwk_s_key(self) -> builtins.str:
            '''``CfnWirelessDevice.SessionKeysAbpV10xProperty.NwkSKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey
            '''
            result = self._values.get("nwk_s_key")
            assert result is not None, "Required property 'nwk_s_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionKeysAbpV10xProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property",
        jsii_struct_bases=[],
        name_mapping={
            "app_s_key": "appSKey",
            "f_nwk_s_int_key": "fNwkSIntKey",
            "nwk_s_enc_key": "nwkSEncKey",
            "s_nwk_s_int_key": "sNwkSIntKey",
        },
    )
    class SessionKeysAbpV11Property:
        def __init__(
            self,
            *,
            app_s_key: builtins.str,
            f_nwk_s_int_key: builtins.str,
            nwk_s_enc_key: builtins.str,
            s_nwk_s_int_key: builtins.str,
        ) -> None:
            '''
            :param app_s_key: ``CfnWirelessDevice.SessionKeysAbpV11Property.AppSKey``.
            :param f_nwk_s_int_key: ``CfnWirelessDevice.SessionKeysAbpV11Property.FNwkSIntKey``.
            :param nwk_s_enc_key: ``CfnWirelessDevice.SessionKeysAbpV11Property.NwkSEncKey``.
            :param s_nwk_s_int_key: ``CfnWirelessDevice.SessionKeysAbpV11Property.SNwkSIntKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "app_s_key": app_s_key,
                "f_nwk_s_int_key": f_nwk_s_int_key,
                "nwk_s_enc_key": nwk_s_enc_key,
                "s_nwk_s_int_key": s_nwk_s_int_key,
            }

        @builtins.property
        def app_s_key(self) -> builtins.str:
            '''``CfnWirelessDevice.SessionKeysAbpV11Property.AppSKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey
            '''
            result = self._values.get("app_s_key")
            assert result is not None, "Required property 'app_s_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def f_nwk_s_int_key(self) -> builtins.str:
            '''``CfnWirelessDevice.SessionKeysAbpV11Property.FNwkSIntKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey
            '''
            result = self._values.get("f_nwk_s_int_key")
            assert result is not None, "Required property 'f_nwk_s_int_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nwk_s_enc_key(self) -> builtins.str:
            '''``CfnWirelessDevice.SessionKeysAbpV11Property.NwkSEncKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey
            '''
            result = self._values.get("nwk_s_enc_key")
            assert result is not None, "Required property 'nwk_s_enc_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s_nwk_s_int_key(self) -> builtins.str:
            '''``CfnWirelessDevice.SessionKeysAbpV11Property.SNwkSIntKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey
            '''
            result = self._values.get("s_nwk_s_int_key")
            assert result is not None, "Required property 's_nwk_s_int_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionKeysAbpV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_name": "destinationName",
        "type": "type",
        "description": "description",
        "last_uplink_received_at": "lastUplinkReceivedAt",
        "lo_ra_wan": "loRaWan",
        "name": "name",
        "tags": "tags",
        "thing_arn": "thingArn",
    },
)
class CfnWirelessDeviceProps:
    def __init__(
        self,
        *,
        destination_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        lo_ra_wan: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWirelessDevice.LoRaWANDeviceProperty]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTWireless::WirelessDevice``.

        :param destination_name: ``AWS::IoTWireless::WirelessDevice.DestinationName``.
        :param type: ``AWS::IoTWireless::WirelessDevice.Type``.
        :param description: ``AWS::IoTWireless::WirelessDevice.Description``.
        :param last_uplink_received_at: ``AWS::IoTWireless::WirelessDevice.LastUplinkReceivedAt``.
        :param lo_ra_wan: ``AWS::IoTWireless::WirelessDevice.LoRaWAN``.
        :param name: ``AWS::IoTWireless::WirelessDevice.Name``.
        :param tags: ``AWS::IoTWireless::WirelessDevice.Tags``.
        :param thing_arn: ``AWS::IoTWireless::WirelessDevice.ThingArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "destination_name": destination_name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if last_uplink_received_at is not None:
            self._values["last_uplink_received_at"] = last_uplink_received_at
        if lo_ra_wan is not None:
            self._values["lo_ra_wan"] = lo_ra_wan
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if thing_arn is not None:
            self._values["thing_arn"] = thing_arn

    @builtins.property
    def destination_name(self) -> builtins.str:
        '''``AWS::IoTWireless::WirelessDevice.DestinationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname
        '''
        result = self._values.get("destination_name")
        assert result is not None, "Required property 'destination_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::IoTWireless::WirelessDevice.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessDevice.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessDevice.LastUplinkReceivedAt``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lastuplinkreceivedat
        '''
        result = self._values.get("last_uplink_received_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWirelessDevice.LoRaWANDeviceProperty]]:
        '''``AWS::IoTWireless::WirelessDevice.LoRaWAN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWirelessDevice.LoRaWANDeviceProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessDevice.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTWireless::WirelessDevice.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessDevice.ThingArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-thingarn
        '''
        result = self._values.get("thing_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWirelessDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWirelessGateway(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessGateway",
):
    '''A CloudFormation ``AWS::IoTWireless::WirelessGateway``.

    :cloudformationResource: AWS::IoTWireless::WirelessGateway
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        lo_ra_wan: typing.Union[aws_cdk.core.IResolvable, "CfnWirelessGateway.LoRaWANGatewayProperty"],
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::WirelessGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan: ``AWS::IoTWireless::WirelessGateway.LoRaWAN``.
        :param description: ``AWS::IoTWireless::WirelessGateway.Description``.
        :param last_uplink_received_at: ``AWS::IoTWireless::WirelessGateway.LastUplinkReceivedAt``.
        :param name: ``AWS::IoTWireless::WirelessGateway.Name``.
        :param tags: ``AWS::IoTWireless::WirelessGateway.Tags``.
        :param thing_arn: ``AWS::IoTWireless::WirelessGateway.ThingArn``.
        '''
        props = CfnWirelessGatewayProps(
            lo_ra_wan=lo_ra_wan,
            description=description,
            last_uplink_received_at=last_uplink_received_at,
            name=name,
            tags=tags,
            thing_arn=thing_arn,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrThingName")
    def attr_thing_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ThingName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrThingName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTWireless::WirelessGateway.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWirelessGateway.LoRaWANGatewayProperty"]:
        '''``AWS::IoTWireless::WirelessGateway.LoRaWAN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawan
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWirelessGateway.LoRaWANGatewayProperty"], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnWirelessGateway.LoRaWANGatewayProperty"],
    ) -> None:
        jsii.set(self, "loRaWan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lastUplinkReceivedAt")
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.LastUplinkReceivedAt``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lastuplinkreceivedat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastUplinkReceivedAt"))

    @last_uplink_received_at.setter
    def last_uplink_received_at(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "lastUplinkReceivedAt", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="thingArn")
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.ThingArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingArn"))

    @thing_arn.setter
    def thing_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "thingArn", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty",
        jsii_struct_bases=[],
        name_mapping={"gateway_eui": "gatewayEui", "rf_region": "rfRegion"},
    )
    class LoRaWANGatewayProperty:
        def __init__(
            self,
            *,
            gateway_eui: builtins.str,
            rf_region: builtins.str,
        ) -> None:
            '''
            :param gateway_eui: ``CfnWirelessGateway.LoRaWANGatewayProperty.GatewayEui``.
            :param rf_region: ``CfnWirelessGateway.LoRaWANGatewayProperty.RfRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "gateway_eui": gateway_eui,
                "rf_region": rf_region,
            }

        @builtins.property
        def gateway_eui(self) -> builtins.str:
            '''``CfnWirelessGateway.LoRaWANGatewayProperty.GatewayEui``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui
            '''
            result = self._values.get("gateway_eui")
            assert result is not None, "Required property 'gateway_eui' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rf_region(self) -> builtins.str:
            '''``CfnWirelessGateway.LoRaWANGatewayProperty.RfRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-rfregion
            '''
            result = self._values.get("rf_region")
            assert result is not None, "Required property 'rf_region' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANGatewayProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "lo_ra_wan": "loRaWan",
        "description": "description",
        "last_uplink_received_at": "lastUplinkReceivedAt",
        "name": "name",
        "tags": "tags",
        "thing_arn": "thingArn",
    },
)
class CfnWirelessGatewayProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Union[aws_cdk.core.IResolvable, CfnWirelessGateway.LoRaWANGatewayProperty],
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTWireless::WirelessGateway``.

        :param lo_ra_wan: ``AWS::IoTWireless::WirelessGateway.LoRaWAN``.
        :param description: ``AWS::IoTWireless::WirelessGateway.Description``.
        :param last_uplink_received_at: ``AWS::IoTWireless::WirelessGateway.LastUplinkReceivedAt``.
        :param name: ``AWS::IoTWireless::WirelessGateway.Name``.
        :param tags: ``AWS::IoTWireless::WirelessGateway.Tags``.
        :param thing_arn: ``AWS::IoTWireless::WirelessGateway.ThingArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "lo_ra_wan": lo_ra_wan,
        }
        if description is not None:
            self._values["description"] = description
        if last_uplink_received_at is not None:
            self._values["last_uplink_received_at"] = last_uplink_received_at
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if thing_arn is not None:
            self._values["thing_arn"] = thing_arn

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnWirelessGateway.LoRaWANGatewayProperty]:
        '''``AWS::IoTWireless::WirelessGateway.LoRaWAN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        assert result is not None, "Required property 'lo_ra_wan' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnWirelessGateway.LoRaWANGatewayProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.LastUplinkReceivedAt``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lastuplinkreceivedat
        '''
        result = self._values.get("last_uplink_received_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTWireless::WirelessGateway.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.ThingArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingarn
        '''
        result = self._values.get("thing_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWirelessGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDestination",
    "CfnDestinationProps",
    "CfnDeviceProfile",
    "CfnDeviceProfileProps",
    "CfnPartnerAccount",
    "CfnPartnerAccountProps",
    "CfnServiceProfile",
    "CfnServiceProfileProps",
    "CfnTaskDefinition",
    "CfnTaskDefinitionProps",
    "CfnWirelessDevice",
    "CfnWirelessDeviceProps",
    "CfnWirelessGateway",
    "CfnWirelessGatewayProps",
]

publication.publish()
