'''
# AWS::SSMContacts Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_ssmcontacts as ssmcontacts
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
class CfnContact(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ssmcontacts.CfnContact",
):
    '''A CloudFormation ``AWS::SSMContacts::Contact``.

    :cloudformationResource: AWS::SSMContacts::Contact
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        alias: builtins.str,
        display_name: builtins.str,
        plan: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnContact.StageProperty", aws_cdk.core.IResolvable]]],
        type: builtins.str,
    ) -> None:
        '''Create a new ``AWS::SSMContacts::Contact``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param alias: ``AWS::SSMContacts::Contact.Alias``.
        :param display_name: ``AWS::SSMContacts::Contact.DisplayName``.
        :param plan: ``AWS::SSMContacts::Contact.Plan``.
        :param type: ``AWS::SSMContacts::Contact.Type``.
        '''
        props = CfnContactProps(
            alias=alias, display_name=display_name, plan=plan, type=type
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
    @jsii.member(jsii_name="alias")
    def alias(self) -> builtins.str:
        '''``AWS::SSMContacts::Contact.Alias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: builtins.str) -> None:
        jsii.set(self, "alias", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''``AWS::SSMContacts::Contact.DisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-displayname
        '''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        jsii.set(self, "displayName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="plan")
    def plan(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnContact.StageProperty", aws_cdk.core.IResolvable]]]:
        '''``AWS::SSMContacts::Contact.Plan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-plan
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnContact.StageProperty", aws_cdk.core.IResolvable]]], jsii.get(self, "plan"))

    @plan.setter
    def plan(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnContact.StageProperty", aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "plan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::SSMContacts::Contact.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmcontacts.CfnContact.ChannelTargetInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_id": "channelId",
            "retry_interval_in_minutes": "retryIntervalInMinutes",
        },
    )
    class ChannelTargetInfoProperty:
        def __init__(
            self,
            *,
            channel_id: builtins.str,
            retry_interval_in_minutes: jsii.Number,
        ) -> None:
            '''
            :param channel_id: ``CfnContact.ChannelTargetInfoProperty.ChannelId``.
            :param retry_interval_in_minutes: ``CfnContact.ChannelTargetInfoProperty.RetryIntervalInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "channel_id": channel_id,
                "retry_interval_in_minutes": retry_interval_in_minutes,
            }

        @builtins.property
        def channel_id(self) -> builtins.str:
            '''``CfnContact.ChannelTargetInfoProperty.ChannelId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html#cfn-ssmcontacts-contact-channeltargetinfo-channelid
            '''
            result = self._values.get("channel_id")
            assert result is not None, "Required property 'channel_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def retry_interval_in_minutes(self) -> jsii.Number:
            '''``CfnContact.ChannelTargetInfoProperty.RetryIntervalInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html#cfn-ssmcontacts-contact-channeltargetinfo-retryintervalinminutes
            '''
            result = self._values.get("retry_interval_in_minutes")
            assert result is not None, "Required property 'retry_interval_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChannelTargetInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmcontacts.CfnContact.ContactTargetInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_id": "contactId", "is_essential": "isEssential"},
    )
    class ContactTargetInfoProperty:
        def __init__(
            self,
            *,
            contact_id: builtins.str,
            is_essential: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''
            :param contact_id: ``CfnContact.ContactTargetInfoProperty.ContactId``.
            :param is_essential: ``CfnContact.ContactTargetInfoProperty.IsEssential``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "contact_id": contact_id,
                "is_essential": is_essential,
            }

        @builtins.property
        def contact_id(self) -> builtins.str:
            '''``CfnContact.ContactTargetInfoProperty.ContactId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html#cfn-ssmcontacts-contact-contacttargetinfo-contactid
            '''
            result = self._values.get("contact_id")
            assert result is not None, "Required property 'contact_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def is_essential(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnContact.ContactTargetInfoProperty.IsEssential``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html#cfn-ssmcontacts-contact-contacttargetinfo-isessential
            '''
            result = self._values.get("is_essential")
            assert result is not None, "Required property 'is_essential' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContactTargetInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmcontacts.CfnContact.StageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "duration_in_minutes": "durationInMinutes",
            "targets": "targets",
        },
    )
    class StageProperty:
        def __init__(
            self,
            *,
            duration_in_minutes: jsii.Number,
            targets: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnContact.TargetsProperty"]]]] = None,
        ) -> None:
            '''
            :param duration_in_minutes: ``CfnContact.StageProperty.DurationInMinutes``.
            :param targets: ``CfnContact.StageProperty.Targets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "duration_in_minutes": duration_in_minutes,
            }
            if targets is not None:
                self._values["targets"] = targets

        @builtins.property
        def duration_in_minutes(self) -> jsii.Number:
            '''``CfnContact.StageProperty.DurationInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html#cfn-ssmcontacts-contact-stage-durationinminutes
            '''
            result = self._values.get("duration_in_minutes")
            assert result is not None, "Required property 'duration_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def targets(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnContact.TargetsProperty"]]]]:
            '''``CfnContact.StageProperty.Targets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html#cfn-ssmcontacts-contact-stage-targets
            '''
            result = self._values.get("targets")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnContact.TargetsProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmcontacts.CfnContact.TargetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_target_info": "channelTargetInfo",
            "contact_target_info": "contactTargetInfo",
        },
    )
    class TargetsProperty:
        def __init__(
            self,
            *,
            channel_target_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContact.ChannelTargetInfoProperty"]] = None,
            contact_target_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContact.ContactTargetInfoProperty"]] = None,
        ) -> None:
            '''
            :param channel_target_info: ``CfnContact.TargetsProperty.ChannelTargetInfo``.
            :param contact_target_info: ``CfnContact.TargetsProperty.ContactTargetInfo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if channel_target_info is not None:
                self._values["channel_target_info"] = channel_target_info
            if contact_target_info is not None:
                self._values["contact_target_info"] = contact_target_info

        @builtins.property
        def channel_target_info(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContact.ChannelTargetInfoProperty"]]:
            '''``CfnContact.TargetsProperty.ChannelTargetInfo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html#cfn-ssmcontacts-contact-targets-channeltargetinfo
            '''
            result = self._values.get("channel_target_info")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContact.ChannelTargetInfoProperty"]], result)

        @builtins.property
        def contact_target_info(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContact.ContactTargetInfoProperty"]]:
            '''``CfnContact.TargetsProperty.ContactTargetInfo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html#cfn-ssmcontacts-contact-targets-contacttargetinfo
            '''
            result = self._values.get("contact_target_info")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContact.ContactTargetInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnContactChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ssmcontacts.CfnContactChannel",
):
    '''A CloudFormation ``AWS::SSMContacts::ContactChannel``.

    :cloudformationResource: AWS::SSMContacts::ContactChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        channel_address: builtins.str,
        channel_name: builtins.str,
        channel_type: builtins.str,
        contact_id: builtins.str,
        defer_activation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Create a new ``AWS::SSMContacts::ContactChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param channel_address: ``AWS::SSMContacts::ContactChannel.ChannelAddress``.
        :param channel_name: ``AWS::SSMContacts::ContactChannel.ChannelName``.
        :param channel_type: ``AWS::SSMContacts::ContactChannel.ChannelType``.
        :param contact_id: ``AWS::SSMContacts::ContactChannel.ContactId``.
        :param defer_activation: ``AWS::SSMContacts::ContactChannel.DeferActivation``.
        '''
        props = CfnContactChannelProps(
            channel_address=channel_address,
            channel_name=channel_name,
            channel_type=channel_type,
            contact_id=contact_id,
            defer_activation=defer_activation,
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
    @jsii.member(jsii_name="channelAddress")
    def channel_address(self) -> builtins.str:
        '''``AWS::SSMContacts::ContactChannel.ChannelAddress``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeladdress
        '''
        return typing.cast(builtins.str, jsii.get(self, "channelAddress"))

    @channel_address.setter
    def channel_address(self, value: builtins.str) -> None:
        jsii.set(self, "channelAddress", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        '''``AWS::SSMContacts::ContactChannel.ChannelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channelname
        '''
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        jsii.set(self, "channelName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="channelType")
    def channel_type(self) -> builtins.str:
        '''``AWS::SSMContacts::ContactChannel.ChannelType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeltype
        '''
        return typing.cast(builtins.str, jsii.get(self, "channelType"))

    @channel_type.setter
    def channel_type(self, value: builtins.str) -> None:
        jsii.set(self, "channelType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactId")
    def contact_id(self) -> builtins.str:
        '''``AWS::SSMContacts::ContactChannel.ContactId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-contactid
        '''
        return typing.cast(builtins.str, jsii.get(self, "contactId"))

    @contact_id.setter
    def contact_id(self, value: builtins.str) -> None:
        jsii.set(self, "contactId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deferActivation")
    def defer_activation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SSMContacts::ContactChannel.DeferActivation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-deferactivation
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "deferActivation"))

    @defer_activation.setter
    def defer_activation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "deferActivation", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ssmcontacts.CfnContactChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_address": "channelAddress",
        "channel_name": "channelName",
        "channel_type": "channelType",
        "contact_id": "contactId",
        "defer_activation": "deferActivation",
    },
)
class CfnContactChannelProps:
    def __init__(
        self,
        *,
        channel_address: builtins.str,
        channel_name: builtins.str,
        channel_type: builtins.str,
        contact_id: builtins.str,
        defer_activation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSMContacts::ContactChannel``.

        :param channel_address: ``AWS::SSMContacts::ContactChannel.ChannelAddress``.
        :param channel_name: ``AWS::SSMContacts::ContactChannel.ChannelName``.
        :param channel_type: ``AWS::SSMContacts::ContactChannel.ChannelType``.
        :param contact_id: ``AWS::SSMContacts::ContactChannel.ContactId``.
        :param defer_activation: ``AWS::SSMContacts::ContactChannel.DeferActivation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "channel_address": channel_address,
            "channel_name": channel_name,
            "channel_type": channel_type,
            "contact_id": contact_id,
        }
        if defer_activation is not None:
            self._values["defer_activation"] = defer_activation

    @builtins.property
    def channel_address(self) -> builtins.str:
        '''``AWS::SSMContacts::ContactChannel.ChannelAddress``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeladdress
        '''
        result = self._values.get("channel_address")
        assert result is not None, "Required property 'channel_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''``AWS::SSMContacts::ContactChannel.ChannelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channelname
        '''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_type(self) -> builtins.str:
        '''``AWS::SSMContacts::ContactChannel.ChannelType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeltype
        '''
        result = self._values.get("channel_type")
        assert result is not None, "Required property 'channel_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contact_id(self) -> builtins.str:
        '''``AWS::SSMContacts::ContactChannel.ContactId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-contactid
        '''
        result = self._values.get("contact_id")
        assert result is not None, "Required property 'contact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def defer_activation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SSMContacts::ContactChannel.DeferActivation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-deferactivation
        '''
        result = self._values.get("defer_activation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ssmcontacts.CfnContactProps",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "display_name": "displayName",
        "plan": "plan",
        "type": "type",
    },
)
class CfnContactProps:
    def __init__(
        self,
        *,
        alias: builtins.str,
        display_name: builtins.str,
        plan: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnContact.StageProperty, aws_cdk.core.IResolvable]]],
        type: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::SSMContacts::Contact``.

        :param alias: ``AWS::SSMContacts::Contact.Alias``.
        :param display_name: ``AWS::SSMContacts::Contact.DisplayName``.
        :param plan: ``AWS::SSMContacts::Contact.Plan``.
        :param type: ``AWS::SSMContacts::Contact.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alias": alias,
            "display_name": display_name,
            "plan": plan,
            "type": type,
        }

    @builtins.property
    def alias(self) -> builtins.str:
        '''``AWS::SSMContacts::Contact.Alias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-alias
        '''
        result = self._values.get("alias")
        assert result is not None, "Required property 'alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''``AWS::SSMContacts::Contact.DisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plan(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnContact.StageProperty, aws_cdk.core.IResolvable]]]:
        '''``AWS::SSMContacts::Contact.Plan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-plan
        '''
        result = self._values.get("plan")
        assert result is not None, "Required property 'plan' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnContact.StageProperty, aws_cdk.core.IResolvable]]], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::SSMContacts::Contact.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnContact",
    "CfnContactChannel",
    "CfnContactChannelProps",
    "CfnContactProps",
]

publication.publish()
