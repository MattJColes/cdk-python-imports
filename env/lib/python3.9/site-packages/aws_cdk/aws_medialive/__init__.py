'''
# AWS Elemental MediaLive Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_medialive as medialive
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
class CfnChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-medialive.CfnChannel",
):
    '''A CloudFormation ``AWS::MediaLive::Channel``.

    :cloudformationResource: AWS::MediaLive::Channel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cdi_input_specification: typing.Optional[typing.Union["CfnChannel.CdiInputSpecificationProperty", aws_cdk.core.IResolvable]] = None,
        channel_class: typing.Optional[builtins.str] = None,
        destinations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputDestinationProperty"]]]] = None,
        encoder_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EncoderSettingsProperty"]] = None,
        input_attachments: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputAttachmentProperty"]]]] = None,
        input_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputSpecificationProperty"]] = None,
        log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        vpc: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VpcOutputSettingsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaLive::Channel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cdi_input_specification: ``AWS::MediaLive::Channel.CdiInputSpecification``.
        :param channel_class: ``AWS::MediaLive::Channel.ChannelClass``.
        :param destinations: ``AWS::MediaLive::Channel.Destinations``.
        :param encoder_settings: ``AWS::MediaLive::Channel.EncoderSettings``.
        :param input_attachments: ``AWS::MediaLive::Channel.InputAttachments``.
        :param input_specification: ``AWS::MediaLive::Channel.InputSpecification``.
        :param log_level: ``AWS::MediaLive::Channel.LogLevel``.
        :param name: ``AWS::MediaLive::Channel.Name``.
        :param role_arn: ``AWS::MediaLive::Channel.RoleArn``.
        :param tags: ``AWS::MediaLive::Channel.Tags``.
        :param vpc: ``AWS::MediaLive::Channel.Vpc``.
        '''
        props = CfnChannelProps(
            cdi_input_specification=cdi_input_specification,
            channel_class=channel_class,
            destinations=destinations,
            encoder_settings=encoder_settings,
            input_attachments=input_attachments,
            input_specification=input_specification,
            log_level=log_level,
            name=name,
            role_arn=role_arn,
            tags=tags,
            vpc=vpc,
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
    @jsii.member(jsii_name="attrInputs")
    def attr_inputs(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: Inputs
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrInputs"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::MediaLive::Channel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cdiInputSpecification")
    def cdi_input_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnChannel.CdiInputSpecificationProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::MediaLive::Channel.CdiInputSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-cdiinputspecification
        '''
        return typing.cast(typing.Optional[typing.Union["CfnChannel.CdiInputSpecificationProperty", aws_cdk.core.IResolvable]], jsii.get(self, "cdiInputSpecification"))

    @cdi_input_specification.setter
    def cdi_input_specification(
        self,
        value: typing.Optional[typing.Union["CfnChannel.CdiInputSpecificationProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "cdiInputSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="channelClass")
    def channel_class(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Channel.ChannelClass``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-channelclass
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelClass"))

    @channel_class.setter
    def channel_class(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "channelClass", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="destinations")
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputDestinationProperty"]]]]:
        '''``AWS::MediaLive::Channel.Destinations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-destinations
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputDestinationProperty"]]]], jsii.get(self, "destinations"))

    @destinations.setter
    def destinations(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputDestinationProperty"]]]],
    ) -> None:
        jsii.set(self, "destinations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encoderSettings")
    def encoder_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EncoderSettingsProperty"]]:
        '''``AWS::MediaLive::Channel.EncoderSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-encodersettings
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EncoderSettingsProperty"]], jsii.get(self, "encoderSettings"))

    @encoder_settings.setter
    def encoder_settings(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EncoderSettingsProperty"]],
    ) -> None:
        jsii.set(self, "encoderSettings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inputAttachments")
    def input_attachments(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputAttachmentProperty"]]]]:
        '''``AWS::MediaLive::Channel.InputAttachments``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputattachments
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputAttachmentProperty"]]]], jsii.get(self, "inputAttachments"))

    @input_attachments.setter
    def input_attachments(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputAttachmentProperty"]]]],
    ) -> None:
        jsii.set(self, "inputAttachments", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inputSpecification")
    def input_specification(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputSpecificationProperty"]]:
        '''``AWS::MediaLive::Channel.InputSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputspecification
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputSpecificationProperty"]], jsii.get(self, "inputSpecification"))

    @input_specification.setter
    def input_specification(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputSpecificationProperty"]],
    ) -> None:
        jsii.set(self, "inputSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Channel.LogLevel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-loglevel
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logLevel", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Channel.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Channel.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpc")
    def vpc(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VpcOutputSettingsProperty"]]:
        '''``AWS::MediaLive::Channel.Vpc``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-vpc
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VpcOutputSettingsProperty"]], jsii.get(self, "vpc"))

    @vpc.setter
    def vpc(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VpcOutputSettingsProperty"]],
    ) -> None:
        jsii.set(self, "vpc", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AacSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bitrate": "bitrate",
            "coding_mode": "codingMode",
            "input_type": "inputType",
            "profile": "profile",
            "rate_control_mode": "rateControlMode",
            "raw_format": "rawFormat",
            "sample_rate": "sampleRate",
            "spec": "spec",
            "vbr_quality": "vbrQuality",
        },
    )
    class AacSettingsProperty:
        def __init__(
            self,
            *,
            bitrate: typing.Optional[jsii.Number] = None,
            coding_mode: typing.Optional[builtins.str] = None,
            input_type: typing.Optional[builtins.str] = None,
            profile: typing.Optional[builtins.str] = None,
            rate_control_mode: typing.Optional[builtins.str] = None,
            raw_format: typing.Optional[builtins.str] = None,
            sample_rate: typing.Optional[jsii.Number] = None,
            spec: typing.Optional[builtins.str] = None,
            vbr_quality: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bitrate: ``CfnChannel.AacSettingsProperty.Bitrate``.
            :param coding_mode: ``CfnChannel.AacSettingsProperty.CodingMode``.
            :param input_type: ``CfnChannel.AacSettingsProperty.InputType``.
            :param profile: ``CfnChannel.AacSettingsProperty.Profile``.
            :param rate_control_mode: ``CfnChannel.AacSettingsProperty.RateControlMode``.
            :param raw_format: ``CfnChannel.AacSettingsProperty.RawFormat``.
            :param sample_rate: ``CfnChannel.AacSettingsProperty.SampleRate``.
            :param spec: ``CfnChannel.AacSettingsProperty.Spec``.
            :param vbr_quality: ``CfnChannel.AacSettingsProperty.VbrQuality``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if coding_mode is not None:
                self._values["coding_mode"] = coding_mode
            if input_type is not None:
                self._values["input_type"] = input_type
            if profile is not None:
                self._values["profile"] = profile
            if rate_control_mode is not None:
                self._values["rate_control_mode"] = rate_control_mode
            if raw_format is not None:
                self._values["raw_format"] = raw_format
            if sample_rate is not None:
                self._values["sample_rate"] = sample_rate
            if spec is not None:
                self._values["spec"] = spec
            if vbr_quality is not None:
                self._values["vbr_quality"] = vbr_quality

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.AacSettingsProperty.Bitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-bitrate
            '''
            result = self._values.get("bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def coding_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AacSettingsProperty.CodingMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-codingmode
            '''
            result = self._values.get("coding_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AacSettingsProperty.InputType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-inputtype
            '''
            result = self._values.get("input_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AacSettingsProperty.Profile``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-profile
            '''
            result = self._values.get("profile")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rate_control_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AacSettingsProperty.RateControlMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-ratecontrolmode
            '''
            result = self._values.get("rate_control_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def raw_format(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AacSettingsProperty.RawFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-rawformat
            '''
            result = self._values.get("raw_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sample_rate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.AacSettingsProperty.SampleRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-samplerate
            '''
            result = self._values.get("sample_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def spec(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AacSettingsProperty.Spec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-spec
            '''
            result = self._values.get("spec")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vbr_quality(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AacSettingsProperty.VbrQuality``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-vbrquality
            '''
            result = self._values.get("vbr_quality")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AacSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Ac3SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bitrate": "bitrate",
            "bitstream_mode": "bitstreamMode",
            "coding_mode": "codingMode",
            "dialnorm": "dialnorm",
            "drc_profile": "drcProfile",
            "lfe_filter": "lfeFilter",
            "metadata_control": "metadataControl",
        },
    )
    class Ac3SettingsProperty:
        def __init__(
            self,
            *,
            bitrate: typing.Optional[jsii.Number] = None,
            bitstream_mode: typing.Optional[builtins.str] = None,
            coding_mode: typing.Optional[builtins.str] = None,
            dialnorm: typing.Optional[jsii.Number] = None,
            drc_profile: typing.Optional[builtins.str] = None,
            lfe_filter: typing.Optional[builtins.str] = None,
            metadata_control: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bitrate: ``CfnChannel.Ac3SettingsProperty.Bitrate``.
            :param bitstream_mode: ``CfnChannel.Ac3SettingsProperty.BitstreamMode``.
            :param coding_mode: ``CfnChannel.Ac3SettingsProperty.CodingMode``.
            :param dialnorm: ``CfnChannel.Ac3SettingsProperty.Dialnorm``.
            :param drc_profile: ``CfnChannel.Ac3SettingsProperty.DrcProfile``.
            :param lfe_filter: ``CfnChannel.Ac3SettingsProperty.LfeFilter``.
            :param metadata_control: ``CfnChannel.Ac3SettingsProperty.MetadataControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if bitstream_mode is not None:
                self._values["bitstream_mode"] = bitstream_mode
            if coding_mode is not None:
                self._values["coding_mode"] = coding_mode
            if dialnorm is not None:
                self._values["dialnorm"] = dialnorm
            if drc_profile is not None:
                self._values["drc_profile"] = drc_profile
            if lfe_filter is not None:
                self._values["lfe_filter"] = lfe_filter
            if metadata_control is not None:
                self._values["metadata_control"] = metadata_control

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Ac3SettingsProperty.Bitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-bitrate
            '''
            result = self._values.get("bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def bitstream_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Ac3SettingsProperty.BitstreamMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-bitstreammode
            '''
            result = self._values.get("bitstream_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def coding_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Ac3SettingsProperty.CodingMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-codingmode
            '''
            result = self._values.get("coding_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dialnorm(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Ac3SettingsProperty.Dialnorm``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-dialnorm
            '''
            result = self._values.get("dialnorm")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def drc_profile(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Ac3SettingsProperty.DrcProfile``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-drcprofile
            '''
            result = self._values.get("drc_profile")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lfe_filter(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Ac3SettingsProperty.LfeFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-lfefilter
            '''
            result = self._values.get("lfe_filter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metadata_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Ac3SettingsProperty.MetadataControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-metadatacontrol
            '''
            result = self._values.get("metadata_control")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Ac3SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AncillarySourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_ancillary_channel_number": "sourceAncillaryChannelNumber",
        },
    )
    class AncillarySourceSettingsProperty:
        def __init__(
            self,
            *,
            source_ancillary_channel_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param source_ancillary_channel_number: ``CfnChannel.AncillarySourceSettingsProperty.SourceAncillaryChannelNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ancillarysourcesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if source_ancillary_channel_number is not None:
                self._values["source_ancillary_channel_number"] = source_ancillary_channel_number

        @builtins.property
        def source_ancillary_channel_number(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.AncillarySourceSettingsProperty.SourceAncillaryChannelNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ancillarysourcesettings.html#cfn-medialive-channel-ancillarysourcesettings-sourceancillarychannelnumber
            '''
            result = self._values.get("source_ancillary_channel_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AncillarySourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.ArchiveCdnSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"archive_s3_settings": "archiveS3Settings"},
    )
    class ArchiveCdnSettingsProperty:
        def __init__(
            self,
            *,
            archive_s3_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveS3SettingsProperty"]] = None,
        ) -> None:
            '''
            :param archive_s3_settings: ``CfnChannel.ArchiveCdnSettingsProperty.ArchiveS3Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecdnsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if archive_s3_settings is not None:
                self._values["archive_s3_settings"] = archive_s3_settings

        @builtins.property
        def archive_s3_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveS3SettingsProperty"]]:
            '''``CfnChannel.ArchiveCdnSettingsProperty.ArchiveS3Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecdnsettings.html#cfn-medialive-channel-archivecdnsettings-archives3settings
            '''
            result = self._values.get("archive_s3_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveS3SettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveCdnSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.ArchiveContainerSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"m2_ts_settings": "m2TsSettings", "raw_settings": "rawSettings"},
    )
    class ArchiveContainerSettingsProperty:
        def __init__(
            self,
            *,
            m2_ts_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.M2tsSettingsProperty"]] = None,
            raw_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RawSettingsProperty"]] = None,
        ) -> None:
            '''
            :param m2_ts_settings: ``CfnChannel.ArchiveContainerSettingsProperty.M2tsSettings``.
            :param raw_settings: ``CfnChannel.ArchiveContainerSettingsProperty.RawSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if m2_ts_settings is not None:
                self._values["m2_ts_settings"] = m2_ts_settings
            if raw_settings is not None:
                self._values["raw_settings"] = raw_settings

        @builtins.property
        def m2_ts_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.M2tsSettingsProperty"]]:
            '''``CfnChannel.ArchiveContainerSettingsProperty.M2tsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html#cfn-medialive-channel-archivecontainersettings-m2tssettings
            '''
            result = self._values.get("m2_ts_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.M2tsSettingsProperty"]], result)

        @builtins.property
        def raw_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RawSettingsProperty"]]:
            '''``CfnChannel.ArchiveContainerSettingsProperty.RawSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html#cfn-medialive-channel-archivecontainersettings-rawsettings
            '''
            result = self._values.get("raw_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RawSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveContainerSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.ArchiveGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "archive_cdn_settings": "archiveCdnSettings",
            "destination": "destination",
            "rollover_interval": "rolloverInterval",
        },
    )
    class ArchiveGroupSettingsProperty:
        def __init__(
            self,
            *,
            archive_cdn_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveCdnSettingsProperty"]] = None,
            destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]] = None,
            rollover_interval: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param archive_cdn_settings: ``CfnChannel.ArchiveGroupSettingsProperty.ArchiveCdnSettings``.
            :param destination: ``CfnChannel.ArchiveGroupSettingsProperty.Destination``.
            :param rollover_interval: ``CfnChannel.ArchiveGroupSettingsProperty.RolloverInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if archive_cdn_settings is not None:
                self._values["archive_cdn_settings"] = archive_cdn_settings
            if destination is not None:
                self._values["destination"] = destination
            if rollover_interval is not None:
                self._values["rollover_interval"] = rollover_interval

        @builtins.property
        def archive_cdn_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveCdnSettingsProperty"]]:
            '''``CfnChannel.ArchiveGroupSettingsProperty.ArchiveCdnSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html#cfn-medialive-channel-archivegroupsettings-archivecdnsettings
            '''
            result = self._values.get("archive_cdn_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveCdnSettingsProperty"]], result)

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]]:
            '''``CfnChannel.ArchiveGroupSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html#cfn-medialive-channel-archivegroupsettings-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]], result)

        @builtins.property
        def rollover_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.ArchiveGroupSettingsProperty.RolloverInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html#cfn-medialive-channel-archivegroupsettings-rolloverinterval
            '''
            result = self._values.get("rollover_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.ArchiveOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_settings": "containerSettings",
            "extension": "extension",
            "name_modifier": "nameModifier",
        },
    )
    class ArchiveOutputSettingsProperty:
        def __init__(
            self,
            *,
            container_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveContainerSettingsProperty"]] = None,
            extension: typing.Optional[builtins.str] = None,
            name_modifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param container_settings: ``CfnChannel.ArchiveOutputSettingsProperty.ContainerSettings``.
            :param extension: ``CfnChannel.ArchiveOutputSettingsProperty.Extension``.
            :param name_modifier: ``CfnChannel.ArchiveOutputSettingsProperty.NameModifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if container_settings is not None:
                self._values["container_settings"] = container_settings
            if extension is not None:
                self._values["extension"] = extension
            if name_modifier is not None:
                self._values["name_modifier"] = name_modifier

        @builtins.property
        def container_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveContainerSettingsProperty"]]:
            '''``CfnChannel.ArchiveOutputSettingsProperty.ContainerSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html#cfn-medialive-channel-archiveoutputsettings-containersettings
            '''
            result = self._values.get("container_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveContainerSettingsProperty"]], result)

        @builtins.property
        def extension(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.ArchiveOutputSettingsProperty.Extension``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html#cfn-medialive-channel-archiveoutputsettings-extension
            '''
            result = self._values.get("extension")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name_modifier(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.ArchiveOutputSettingsProperty.NameModifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html#cfn-medialive-channel-archiveoutputsettings-namemodifier
            '''
            result = self._values.get("name_modifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.ArchiveS3SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"canned_acl": "cannedAcl"},
    )
    class ArchiveS3SettingsProperty:
        def __init__(self, *, canned_acl: typing.Optional[builtins.str] = None) -> None:
            '''
            :param canned_acl: ``CfnChannel.ArchiveS3SettingsProperty.CannedAcl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archives3settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if canned_acl is not None:
                self._values["canned_acl"] = canned_acl

        @builtins.property
        def canned_acl(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.ArchiveS3SettingsProperty.CannedAcl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archives3settings.html#cfn-medialive-channel-archives3settings-cannedacl
            '''
            result = self._values.get("canned_acl")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveS3SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AribDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class AribDestinationSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribdestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AribDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AribSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class AribSourceSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribsourcesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AribSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioChannelMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_channel_levels": "inputChannelLevels",
            "output_channel": "outputChannel",
        },
    )
    class AudioChannelMappingProperty:
        def __init__(
            self,
            *,
            input_channel_levels: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputChannelLevelProperty"]]]] = None,
            output_channel: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param input_channel_levels: ``CfnChannel.AudioChannelMappingProperty.InputChannelLevels``.
            :param output_channel: ``CfnChannel.AudioChannelMappingProperty.OutputChannel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if input_channel_levels is not None:
                self._values["input_channel_levels"] = input_channel_levels
            if output_channel is not None:
                self._values["output_channel"] = output_channel

        @builtins.property
        def input_channel_levels(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputChannelLevelProperty"]]]]:
            '''``CfnChannel.AudioChannelMappingProperty.InputChannelLevels``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html#cfn-medialive-channel-audiochannelmapping-inputchannellevels
            '''
            result = self._values.get("input_channel_levels")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputChannelLevelProperty"]]]], result)

        @builtins.property
        def output_channel(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.AudioChannelMappingProperty.OutputChannel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html#cfn-medialive-channel-audiochannelmapping-outputchannel
            '''
            result = self._values.get("output_channel")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioChannelMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioCodecSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aac_settings": "aacSettings",
            "ac3_settings": "ac3Settings",
            "eac3_settings": "eac3Settings",
            "mp2_settings": "mp2Settings",
            "pass_through_settings": "passThroughSettings",
            "wav_settings": "wavSettings",
        },
    )
    class AudioCodecSettingsProperty:
        def __init__(
            self,
            *,
            aac_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AacSettingsProperty"]] = None,
            ac3_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Ac3SettingsProperty"]] = None,
            eac3_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Eac3SettingsProperty"]] = None,
            mp2_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Mp2SettingsProperty"]] = None,
            pass_through_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.PassThroughSettingsProperty"]] = None,
            wav_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.WavSettingsProperty"]] = None,
        ) -> None:
            '''
            :param aac_settings: ``CfnChannel.AudioCodecSettingsProperty.AacSettings``.
            :param ac3_settings: ``CfnChannel.AudioCodecSettingsProperty.Ac3Settings``.
            :param eac3_settings: ``CfnChannel.AudioCodecSettingsProperty.Eac3Settings``.
            :param mp2_settings: ``CfnChannel.AudioCodecSettingsProperty.Mp2Settings``.
            :param pass_through_settings: ``CfnChannel.AudioCodecSettingsProperty.PassThroughSettings``.
            :param wav_settings: ``CfnChannel.AudioCodecSettingsProperty.WavSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if aac_settings is not None:
                self._values["aac_settings"] = aac_settings
            if ac3_settings is not None:
                self._values["ac3_settings"] = ac3_settings
            if eac3_settings is not None:
                self._values["eac3_settings"] = eac3_settings
            if mp2_settings is not None:
                self._values["mp2_settings"] = mp2_settings
            if pass_through_settings is not None:
                self._values["pass_through_settings"] = pass_through_settings
            if wav_settings is not None:
                self._values["wav_settings"] = wav_settings

        @builtins.property
        def aac_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AacSettingsProperty"]]:
            '''``CfnChannel.AudioCodecSettingsProperty.AacSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-aacsettings
            '''
            result = self._values.get("aac_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AacSettingsProperty"]], result)

        @builtins.property
        def ac3_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Ac3SettingsProperty"]]:
            '''``CfnChannel.AudioCodecSettingsProperty.Ac3Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-ac3settings
            '''
            result = self._values.get("ac3_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Ac3SettingsProperty"]], result)

        @builtins.property
        def eac3_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Eac3SettingsProperty"]]:
            '''``CfnChannel.AudioCodecSettingsProperty.Eac3Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-eac3settings
            '''
            result = self._values.get("eac3_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Eac3SettingsProperty"]], result)

        @builtins.property
        def mp2_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Mp2SettingsProperty"]]:
            '''``CfnChannel.AudioCodecSettingsProperty.Mp2Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-mp2settings
            '''
            result = self._values.get("mp2_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Mp2SettingsProperty"]], result)

        @builtins.property
        def pass_through_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.PassThroughSettingsProperty"]]:
            '''``CfnChannel.AudioCodecSettingsProperty.PassThroughSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-passthroughsettings
            '''
            result = self._values.get("pass_through_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.PassThroughSettingsProperty"]], result)

        @builtins.property
        def wav_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.WavSettingsProperty"]]:
            '''``CfnChannel.AudioCodecSettingsProperty.WavSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-wavsettings
            '''
            result = self._values.get("wav_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.WavSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioCodecSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_normalization_settings": "audioNormalizationSettings",
            "audio_selector_name": "audioSelectorName",
            "audio_type": "audioType",
            "audio_type_control": "audioTypeControl",
            "codec_settings": "codecSettings",
            "language_code": "languageCode",
            "language_code_control": "languageCodeControl",
            "name": "name",
            "remix_settings": "remixSettings",
            "stream_name": "streamName",
        },
    )
    class AudioDescriptionProperty:
        def __init__(
            self,
            *,
            audio_normalization_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioNormalizationSettingsProperty"]] = None,
            audio_selector_name: typing.Optional[builtins.str] = None,
            audio_type: typing.Optional[builtins.str] = None,
            audio_type_control: typing.Optional[builtins.str] = None,
            codec_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioCodecSettingsProperty"]] = None,
            language_code: typing.Optional[builtins.str] = None,
            language_code_control: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            remix_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RemixSettingsProperty"]] = None,
            stream_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param audio_normalization_settings: ``CfnChannel.AudioDescriptionProperty.AudioNormalizationSettings``.
            :param audio_selector_name: ``CfnChannel.AudioDescriptionProperty.AudioSelectorName``.
            :param audio_type: ``CfnChannel.AudioDescriptionProperty.AudioType``.
            :param audio_type_control: ``CfnChannel.AudioDescriptionProperty.AudioTypeControl``.
            :param codec_settings: ``CfnChannel.AudioDescriptionProperty.CodecSettings``.
            :param language_code: ``CfnChannel.AudioDescriptionProperty.LanguageCode``.
            :param language_code_control: ``CfnChannel.AudioDescriptionProperty.LanguageCodeControl``.
            :param name: ``CfnChannel.AudioDescriptionProperty.Name``.
            :param remix_settings: ``CfnChannel.AudioDescriptionProperty.RemixSettings``.
            :param stream_name: ``CfnChannel.AudioDescriptionProperty.StreamName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_normalization_settings is not None:
                self._values["audio_normalization_settings"] = audio_normalization_settings
            if audio_selector_name is not None:
                self._values["audio_selector_name"] = audio_selector_name
            if audio_type is not None:
                self._values["audio_type"] = audio_type
            if audio_type_control is not None:
                self._values["audio_type_control"] = audio_type_control
            if codec_settings is not None:
                self._values["codec_settings"] = codec_settings
            if language_code is not None:
                self._values["language_code"] = language_code
            if language_code_control is not None:
                self._values["language_code_control"] = language_code_control
            if name is not None:
                self._values["name"] = name
            if remix_settings is not None:
                self._values["remix_settings"] = remix_settings
            if stream_name is not None:
                self._values["stream_name"] = stream_name

        @builtins.property
        def audio_normalization_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioNormalizationSettingsProperty"]]:
            '''``CfnChannel.AudioDescriptionProperty.AudioNormalizationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audionormalizationsettings
            '''
            result = self._values.get("audio_normalization_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioNormalizationSettingsProperty"]], result)

        @builtins.property
        def audio_selector_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioDescriptionProperty.AudioSelectorName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audioselectorname
            '''
            result = self._values.get("audio_selector_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def audio_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioDescriptionProperty.AudioType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audiotype
            '''
            result = self._values.get("audio_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def audio_type_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioDescriptionProperty.AudioTypeControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audiotypecontrol
            '''
            result = self._values.get("audio_type_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def codec_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioCodecSettingsProperty"]]:
            '''``CfnChannel.AudioDescriptionProperty.CodecSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-codecsettings
            '''
            result = self._values.get("codec_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioCodecSettingsProperty"]], result)

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioDescriptionProperty.LanguageCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-languagecode
            '''
            result = self._values.get("language_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def language_code_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioDescriptionProperty.LanguageCodeControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-languagecodecontrol
            '''
            result = self._values.get("language_code_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioDescriptionProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remix_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RemixSettingsProperty"]]:
            '''``CfnChannel.AudioDescriptionProperty.RemixSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-remixsettings
            '''
            result = self._values.get("remix_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RemixSettingsProperty"]], result)

        @builtins.property
        def stream_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioDescriptionProperty.StreamName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-streamname
            '''
            result = self._values.get("stream_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioLanguageSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "language_code": "languageCode",
            "language_selection_policy": "languageSelectionPolicy",
        },
    )
    class AudioLanguageSelectionProperty:
        def __init__(
            self,
            *,
            language_code: typing.Optional[builtins.str] = None,
            language_selection_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param language_code: ``CfnChannel.AudioLanguageSelectionProperty.LanguageCode``.
            :param language_selection_policy: ``CfnChannel.AudioLanguageSelectionProperty.LanguageSelectionPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if language_code is not None:
                self._values["language_code"] = language_code
            if language_selection_policy is not None:
                self._values["language_selection_policy"] = language_selection_policy

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioLanguageSelectionProperty.LanguageCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html#cfn-medialive-channel-audiolanguageselection-languagecode
            '''
            result = self._values.get("language_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def language_selection_policy(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioLanguageSelectionProperty.LanguageSelectionPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html#cfn-medialive-channel-audiolanguageselection-languageselectionpolicy
            '''
            result = self._values.get("language_selection_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioLanguageSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioNormalizationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "algorithm_control": "algorithmControl",
            "target_lkfs": "targetLkfs",
        },
    )
    class AudioNormalizationSettingsProperty:
        def __init__(
            self,
            *,
            algorithm: typing.Optional[builtins.str] = None,
            algorithm_control: typing.Optional[builtins.str] = None,
            target_lkfs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param algorithm: ``CfnChannel.AudioNormalizationSettingsProperty.Algorithm``.
            :param algorithm_control: ``CfnChannel.AudioNormalizationSettingsProperty.AlgorithmControl``.
            :param target_lkfs: ``CfnChannel.AudioNormalizationSettingsProperty.TargetLkfs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if algorithm is not None:
                self._values["algorithm"] = algorithm
            if algorithm_control is not None:
                self._values["algorithm_control"] = algorithm_control
            if target_lkfs is not None:
                self._values["target_lkfs"] = target_lkfs

        @builtins.property
        def algorithm(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioNormalizationSettingsProperty.Algorithm``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html#cfn-medialive-channel-audionormalizationsettings-algorithm
            '''
            result = self._values.get("algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def algorithm_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioNormalizationSettingsProperty.AlgorithmControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html#cfn-medialive-channel-audionormalizationsettings-algorithmcontrol
            '''
            result = self._values.get("algorithm_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_lkfs(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.AudioNormalizationSettingsProperty.TargetLkfs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html#cfn-medialive-channel-audionormalizationsettings-targetlkfs
            '''
            result = self._values.get("target_lkfs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioNormalizationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioOnlyHlsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_group_id": "audioGroupId",
            "audio_only_image": "audioOnlyImage",
            "audio_track_type": "audioTrackType",
            "segment_type": "segmentType",
        },
    )
    class AudioOnlyHlsSettingsProperty:
        def __init__(
            self,
            *,
            audio_group_id: typing.Optional[builtins.str] = None,
            audio_only_image: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]] = None,
            audio_track_type: typing.Optional[builtins.str] = None,
            segment_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param audio_group_id: ``CfnChannel.AudioOnlyHlsSettingsProperty.AudioGroupId``.
            :param audio_only_image: ``CfnChannel.AudioOnlyHlsSettingsProperty.AudioOnlyImage``.
            :param audio_track_type: ``CfnChannel.AudioOnlyHlsSettingsProperty.AudioTrackType``.
            :param segment_type: ``CfnChannel.AudioOnlyHlsSettingsProperty.SegmentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_group_id is not None:
                self._values["audio_group_id"] = audio_group_id
            if audio_only_image is not None:
                self._values["audio_only_image"] = audio_only_image
            if audio_track_type is not None:
                self._values["audio_track_type"] = audio_track_type
            if segment_type is not None:
                self._values["segment_type"] = segment_type

        @builtins.property
        def audio_group_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioOnlyHlsSettingsProperty.AudioGroupId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-audiogroupid
            '''
            result = self._values.get("audio_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def audio_only_image(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]]:
            '''``CfnChannel.AudioOnlyHlsSettingsProperty.AudioOnlyImage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-audioonlyimage
            '''
            result = self._values.get("audio_only_image")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]], result)

        @builtins.property
        def audio_track_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioOnlyHlsSettingsProperty.AudioTrackType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-audiotracktype
            '''
            result = self._values.get("audio_track_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segment_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioOnlyHlsSettingsProperty.SegmentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-segmenttype
            '''
            result = self._values.get("segment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioOnlyHlsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioPidSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={"pid": "pid"},
    )
    class AudioPidSelectionProperty:
        def __init__(self, *, pid: typing.Optional[jsii.Number] = None) -> None:
            '''
            :param pid: ``CfnChannel.AudioPidSelectionProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiopidselection.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if pid is not None:
                self._values["pid"] = pid

        @builtins.property
        def pid(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.AudioPidSelectionProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiopidselection.html#cfn-medialive-channel-audiopidselection-pid
            '''
            result = self._values.get("pid")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioPidSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "selector_settings": "selectorSettings"},
    )
    class AudioSelectorProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            selector_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioSelectorSettingsProperty"]] = None,
        ) -> None:
            '''
            :param name: ``CfnChannel.AudioSelectorProperty.Name``.
            :param selector_settings: ``CfnChannel.AudioSelectorProperty.SelectorSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if selector_settings is not None:
                self._values["selector_settings"] = selector_settings

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioSelectorProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html#cfn-medialive-channel-audioselector-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def selector_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioSelectorSettingsProperty"]]:
            '''``CfnChannel.AudioSelectorProperty.SelectorSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html#cfn-medialive-channel-audioselector-selectorsettings
            '''
            result = self._values.get("selector_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioSelectorSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioSelectorSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_language_selection": "audioLanguageSelection",
            "audio_pid_selection": "audioPidSelection",
            "audio_track_selection": "audioTrackSelection",
        },
    )
    class AudioSelectorSettingsProperty:
        def __init__(
            self,
            *,
            audio_language_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioLanguageSelectionProperty"]] = None,
            audio_pid_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioPidSelectionProperty"]] = None,
            audio_track_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioTrackSelectionProperty"]] = None,
        ) -> None:
            '''
            :param audio_language_selection: ``CfnChannel.AudioSelectorSettingsProperty.AudioLanguageSelection``.
            :param audio_pid_selection: ``CfnChannel.AudioSelectorSettingsProperty.AudioPidSelection``.
            :param audio_track_selection: ``CfnChannel.AudioSelectorSettingsProperty.AudioTrackSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_language_selection is not None:
                self._values["audio_language_selection"] = audio_language_selection
            if audio_pid_selection is not None:
                self._values["audio_pid_selection"] = audio_pid_selection
            if audio_track_selection is not None:
                self._values["audio_track_selection"] = audio_track_selection

        @builtins.property
        def audio_language_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioLanguageSelectionProperty"]]:
            '''``CfnChannel.AudioSelectorSettingsProperty.AudioLanguageSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiolanguageselection
            '''
            result = self._values.get("audio_language_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioLanguageSelectionProperty"]], result)

        @builtins.property
        def audio_pid_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioPidSelectionProperty"]]:
            '''``CfnChannel.AudioSelectorSettingsProperty.AudioPidSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiopidselection
            '''
            result = self._values.get("audio_pid_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioPidSelectionProperty"]], result)

        @builtins.property
        def audio_track_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioTrackSelectionProperty"]]:
            '''``CfnChannel.AudioSelectorSettingsProperty.AudioTrackSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiotrackselection
            '''
            result = self._values.get("audio_track_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioTrackSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioSelectorSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioSilenceFailoverSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_selector_name": "audioSelectorName",
            "audio_silence_threshold_msec": "audioSilenceThresholdMsec",
        },
    )
    class AudioSilenceFailoverSettingsProperty:
        def __init__(
            self,
            *,
            audio_selector_name: typing.Optional[builtins.str] = None,
            audio_silence_threshold_msec: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param audio_selector_name: ``CfnChannel.AudioSilenceFailoverSettingsProperty.AudioSelectorName``.
            :param audio_silence_threshold_msec: ``CfnChannel.AudioSilenceFailoverSettingsProperty.AudioSilenceThresholdMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiosilencefailoversettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_selector_name is not None:
                self._values["audio_selector_name"] = audio_selector_name
            if audio_silence_threshold_msec is not None:
                self._values["audio_silence_threshold_msec"] = audio_silence_threshold_msec

        @builtins.property
        def audio_selector_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AudioSilenceFailoverSettingsProperty.AudioSelectorName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiosilencefailoversettings.html#cfn-medialive-channel-audiosilencefailoversettings-audioselectorname
            '''
            result = self._values.get("audio_selector_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def audio_silence_threshold_msec(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.AudioSilenceFailoverSettingsProperty.AudioSilenceThresholdMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiosilencefailoversettings.html#cfn-medialive-channel-audiosilencefailoversettings-audiosilencethresholdmsec
            '''
            result = self._values.get("audio_silence_threshold_msec")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioSilenceFailoverSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioTrackProperty",
        jsii_struct_bases=[],
        name_mapping={"track": "track"},
    )
    class AudioTrackProperty:
        def __init__(self, *, track: typing.Optional[jsii.Number] = None) -> None:
            '''
            :param track: ``CfnChannel.AudioTrackProperty.Track``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if track is not None:
                self._values["track"] = track

        @builtins.property
        def track(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.AudioTrackProperty.Track``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html#cfn-medialive-channel-audiotrack-track
            '''
            result = self._values.get("track")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioTrackProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AudioTrackSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={"tracks": "tracks"},
    )
    class AudioTrackSelectionProperty:
        def __init__(
            self,
            *,
            tracks: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioTrackProperty"]]]] = None,
        ) -> None:
            '''
            :param tracks: ``CfnChannel.AudioTrackSelectionProperty.Tracks``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if tracks is not None:
                self._values["tracks"] = tracks

        @builtins.property
        def tracks(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioTrackProperty"]]]]:
            '''``CfnChannel.AudioTrackSelectionProperty.Tracks``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html#cfn-medialive-channel-audiotrackselection-tracks
            '''
            result = self._values.get("tracks")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioTrackProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioTrackSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AutomaticInputFailoverSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "error_clear_time_msec": "errorClearTimeMsec",
            "failover_conditions": "failoverConditions",
            "input_preference": "inputPreference",
            "secondary_input_id": "secondaryInputId",
        },
    )
    class AutomaticInputFailoverSettingsProperty:
        def __init__(
            self,
            *,
            error_clear_time_msec: typing.Optional[jsii.Number] = None,
            failover_conditions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FailoverConditionProperty"]]]] = None,
            input_preference: typing.Optional[builtins.str] = None,
            secondary_input_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param error_clear_time_msec: ``CfnChannel.AutomaticInputFailoverSettingsProperty.ErrorClearTimeMsec``.
            :param failover_conditions: ``CfnChannel.AutomaticInputFailoverSettingsProperty.FailoverConditions``.
            :param input_preference: ``CfnChannel.AutomaticInputFailoverSettingsProperty.InputPreference``.
            :param secondary_input_id: ``CfnChannel.AutomaticInputFailoverSettingsProperty.SecondaryInputId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if error_clear_time_msec is not None:
                self._values["error_clear_time_msec"] = error_clear_time_msec
            if failover_conditions is not None:
                self._values["failover_conditions"] = failover_conditions
            if input_preference is not None:
                self._values["input_preference"] = input_preference
            if secondary_input_id is not None:
                self._values["secondary_input_id"] = secondary_input_id

        @builtins.property
        def error_clear_time_msec(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.AutomaticInputFailoverSettingsProperty.ErrorClearTimeMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-errorcleartimemsec
            '''
            result = self._values.get("error_clear_time_msec")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def failover_conditions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FailoverConditionProperty"]]]]:
            '''``CfnChannel.AutomaticInputFailoverSettingsProperty.FailoverConditions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-failoverconditions
            '''
            result = self._values.get("failover_conditions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FailoverConditionProperty"]]]], result)

        @builtins.property
        def input_preference(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AutomaticInputFailoverSettingsProperty.InputPreference``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-inputpreference
            '''
            result = self._values.get("input_preference")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secondary_input_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AutomaticInputFailoverSettingsProperty.SecondaryInputId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-secondaryinputid
            '''
            result = self._values.get("secondary_input_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutomaticInputFailoverSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AvailBlankingProperty",
        jsii_struct_bases=[],
        name_mapping={"avail_blanking_image": "availBlankingImage", "state": "state"},
    )
    class AvailBlankingProperty:
        def __init__(
            self,
            *,
            avail_blanking_image: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param avail_blanking_image: ``CfnChannel.AvailBlankingProperty.AvailBlankingImage``.
            :param state: ``CfnChannel.AvailBlankingProperty.State``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if avail_blanking_image is not None:
                self._values["avail_blanking_image"] = avail_blanking_image
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def avail_blanking_image(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]]:
            '''``CfnChannel.AvailBlankingProperty.AvailBlankingImage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html#cfn-medialive-channel-availblanking-availblankingimage
            '''
            result = self._values.get("avail_blanking_image")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.AvailBlankingProperty.State``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html#cfn-medialive-channel-availblanking-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AvailBlankingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AvailConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"avail_settings": "availSettings"},
    )
    class AvailConfigurationProperty:
        def __init__(
            self,
            *,
            avail_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AvailSettingsProperty"]] = None,
        ) -> None:
            '''
            :param avail_settings: ``CfnChannel.AvailConfigurationProperty.AvailSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if avail_settings is not None:
                self._values["avail_settings"] = avail_settings

        @builtins.property
        def avail_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AvailSettingsProperty"]]:
            '''``CfnChannel.AvailConfigurationProperty.AvailSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html#cfn-medialive-channel-availconfiguration-availsettings
            '''
            result = self._values.get("avail_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AvailSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AvailConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.AvailSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scte35_splice_insert": "scte35SpliceInsert",
            "scte35_time_signal_apos": "scte35TimeSignalApos",
        },
    )
    class AvailSettingsProperty:
        def __init__(
            self,
            *,
            scte35_splice_insert: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte35SpliceInsertProperty"]] = None,
            scte35_time_signal_apos: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte35TimeSignalAposProperty"]] = None,
        ) -> None:
            '''
            :param scte35_splice_insert: ``CfnChannel.AvailSettingsProperty.Scte35SpliceInsert``.
            :param scte35_time_signal_apos: ``CfnChannel.AvailSettingsProperty.Scte35TimeSignalApos``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if scte35_splice_insert is not None:
                self._values["scte35_splice_insert"] = scte35_splice_insert
            if scte35_time_signal_apos is not None:
                self._values["scte35_time_signal_apos"] = scte35_time_signal_apos

        @builtins.property
        def scte35_splice_insert(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte35SpliceInsertProperty"]]:
            '''``CfnChannel.AvailSettingsProperty.Scte35SpliceInsert``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html#cfn-medialive-channel-availsettings-scte35spliceinsert
            '''
            result = self._values.get("scte35_splice_insert")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte35SpliceInsertProperty"]], result)

        @builtins.property
        def scte35_time_signal_apos(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte35TimeSignalAposProperty"]]:
            '''``CfnChannel.AvailSettingsProperty.Scte35TimeSignalApos``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html#cfn-medialive-channel-availsettings-scte35timesignalapos
            '''
            result = self._values.get("scte35_time_signal_apos")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte35TimeSignalAposProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AvailSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.BlackoutSlateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "blackout_slate_image": "blackoutSlateImage",
            "network_end_blackout": "networkEndBlackout",
            "network_end_blackout_image": "networkEndBlackoutImage",
            "network_id": "networkId",
            "state": "state",
        },
    )
    class BlackoutSlateProperty:
        def __init__(
            self,
            *,
            blackout_slate_image: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]] = None,
            network_end_blackout: typing.Optional[builtins.str] = None,
            network_end_blackout_image: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]] = None,
            network_id: typing.Optional[builtins.str] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param blackout_slate_image: ``CfnChannel.BlackoutSlateProperty.BlackoutSlateImage``.
            :param network_end_blackout: ``CfnChannel.BlackoutSlateProperty.NetworkEndBlackout``.
            :param network_end_blackout_image: ``CfnChannel.BlackoutSlateProperty.NetworkEndBlackoutImage``.
            :param network_id: ``CfnChannel.BlackoutSlateProperty.NetworkId``.
            :param state: ``CfnChannel.BlackoutSlateProperty.State``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if blackout_slate_image is not None:
                self._values["blackout_slate_image"] = blackout_slate_image
            if network_end_blackout is not None:
                self._values["network_end_blackout"] = network_end_blackout
            if network_end_blackout_image is not None:
                self._values["network_end_blackout_image"] = network_end_blackout_image
            if network_id is not None:
                self._values["network_id"] = network_id
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def blackout_slate_image(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]]:
            '''``CfnChannel.BlackoutSlateProperty.BlackoutSlateImage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-blackoutslateimage
            '''
            result = self._values.get("blackout_slate_image")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]], result)

        @builtins.property
        def network_end_blackout(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BlackoutSlateProperty.NetworkEndBlackout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-networkendblackout
            '''
            result = self._values.get("network_end_blackout")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def network_end_blackout_image(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]]:
            '''``CfnChannel.BlackoutSlateProperty.NetworkEndBlackoutImage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-networkendblackoutimage
            '''
            result = self._values.get("network_end_blackout_image")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]], result)

        @builtins.property
        def network_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BlackoutSlateProperty.NetworkId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-networkid
            '''
            result = self._values.get("network_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BlackoutSlateProperty.State``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlackoutSlateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.BurnInDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alignment": "alignment",
            "background_color": "backgroundColor",
            "background_opacity": "backgroundOpacity",
            "font": "font",
            "font_color": "fontColor",
            "font_opacity": "fontOpacity",
            "font_resolution": "fontResolution",
            "font_size": "fontSize",
            "outline_color": "outlineColor",
            "outline_size": "outlineSize",
            "shadow_color": "shadowColor",
            "shadow_opacity": "shadowOpacity",
            "shadow_x_offset": "shadowXOffset",
            "shadow_y_offset": "shadowYOffset",
            "teletext_grid_control": "teletextGridControl",
            "x_position": "xPosition",
            "y_position": "yPosition",
        },
    )
    class BurnInDestinationSettingsProperty:
        def __init__(
            self,
            *,
            alignment: typing.Optional[builtins.str] = None,
            background_color: typing.Optional[builtins.str] = None,
            background_opacity: typing.Optional[jsii.Number] = None,
            font: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]] = None,
            font_color: typing.Optional[builtins.str] = None,
            font_opacity: typing.Optional[jsii.Number] = None,
            font_resolution: typing.Optional[jsii.Number] = None,
            font_size: typing.Optional[builtins.str] = None,
            outline_color: typing.Optional[builtins.str] = None,
            outline_size: typing.Optional[jsii.Number] = None,
            shadow_color: typing.Optional[builtins.str] = None,
            shadow_opacity: typing.Optional[jsii.Number] = None,
            shadow_x_offset: typing.Optional[jsii.Number] = None,
            shadow_y_offset: typing.Optional[jsii.Number] = None,
            teletext_grid_control: typing.Optional[builtins.str] = None,
            x_position: typing.Optional[jsii.Number] = None,
            y_position: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param alignment: ``CfnChannel.BurnInDestinationSettingsProperty.Alignment``.
            :param background_color: ``CfnChannel.BurnInDestinationSettingsProperty.BackgroundColor``.
            :param background_opacity: ``CfnChannel.BurnInDestinationSettingsProperty.BackgroundOpacity``.
            :param font: ``CfnChannel.BurnInDestinationSettingsProperty.Font``.
            :param font_color: ``CfnChannel.BurnInDestinationSettingsProperty.FontColor``.
            :param font_opacity: ``CfnChannel.BurnInDestinationSettingsProperty.FontOpacity``.
            :param font_resolution: ``CfnChannel.BurnInDestinationSettingsProperty.FontResolution``.
            :param font_size: ``CfnChannel.BurnInDestinationSettingsProperty.FontSize``.
            :param outline_color: ``CfnChannel.BurnInDestinationSettingsProperty.OutlineColor``.
            :param outline_size: ``CfnChannel.BurnInDestinationSettingsProperty.OutlineSize``.
            :param shadow_color: ``CfnChannel.BurnInDestinationSettingsProperty.ShadowColor``.
            :param shadow_opacity: ``CfnChannel.BurnInDestinationSettingsProperty.ShadowOpacity``.
            :param shadow_x_offset: ``CfnChannel.BurnInDestinationSettingsProperty.ShadowXOffset``.
            :param shadow_y_offset: ``CfnChannel.BurnInDestinationSettingsProperty.ShadowYOffset``.
            :param teletext_grid_control: ``CfnChannel.BurnInDestinationSettingsProperty.TeletextGridControl``.
            :param x_position: ``CfnChannel.BurnInDestinationSettingsProperty.XPosition``.
            :param y_position: ``CfnChannel.BurnInDestinationSettingsProperty.YPosition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if alignment is not None:
                self._values["alignment"] = alignment
            if background_color is not None:
                self._values["background_color"] = background_color
            if background_opacity is not None:
                self._values["background_opacity"] = background_opacity
            if font is not None:
                self._values["font"] = font
            if font_color is not None:
                self._values["font_color"] = font_color
            if font_opacity is not None:
                self._values["font_opacity"] = font_opacity
            if font_resolution is not None:
                self._values["font_resolution"] = font_resolution
            if font_size is not None:
                self._values["font_size"] = font_size
            if outline_color is not None:
                self._values["outline_color"] = outline_color
            if outline_size is not None:
                self._values["outline_size"] = outline_size
            if shadow_color is not None:
                self._values["shadow_color"] = shadow_color
            if shadow_opacity is not None:
                self._values["shadow_opacity"] = shadow_opacity
            if shadow_x_offset is not None:
                self._values["shadow_x_offset"] = shadow_x_offset
            if shadow_y_offset is not None:
                self._values["shadow_y_offset"] = shadow_y_offset
            if teletext_grid_control is not None:
                self._values["teletext_grid_control"] = teletext_grid_control
            if x_position is not None:
                self._values["x_position"] = x_position
            if y_position is not None:
                self._values["y_position"] = y_position

        @builtins.property
        def alignment(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.Alignment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-alignment
            '''
            result = self._values.get("alignment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def background_color(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.BackgroundColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-backgroundcolor
            '''
            result = self._values.get("background_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def background_opacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.BackgroundOpacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-backgroundopacity
            '''
            result = self._values.get("background_opacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def font(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.Font``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-font
            '''
            result = self._values.get("font")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]], result)

        @builtins.property
        def font_color(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.FontColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontcolor
            '''
            result = self._values.get("font_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def font_opacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.FontOpacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontopacity
            '''
            result = self._values.get("font_opacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def font_resolution(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.FontResolution``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontresolution
            '''
            result = self._values.get("font_resolution")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def font_size(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.FontSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontsize
            '''
            result = self._values.get("font_size")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def outline_color(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.OutlineColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-outlinecolor
            '''
            result = self._values.get("outline_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def outline_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.OutlineSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-outlinesize
            '''
            result = self._values.get("outline_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def shadow_color(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.ShadowColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowcolor
            '''
            result = self._values.get("shadow_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shadow_opacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.ShadowOpacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowopacity
            '''
            result = self._values.get("shadow_opacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def shadow_x_offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.ShadowXOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowxoffset
            '''
            result = self._values.get("shadow_x_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def shadow_y_offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.ShadowYOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowyoffset
            '''
            result = self._values.get("shadow_y_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def teletext_grid_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.TeletextGridControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-teletextgridcontrol
            '''
            result = self._values.get("teletext_grid_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def x_position(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.XPosition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-xposition
            '''
            result = self._values.get("x_position")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def y_position(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.BurnInDestinationSettingsProperty.YPosition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-yposition
            '''
            result = self._values.get("y_position")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BurnInDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.CaptionDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "caption_selector_name": "captionSelectorName",
            "destination_settings": "destinationSettings",
            "language_code": "languageCode",
            "language_description": "languageDescription",
            "name": "name",
        },
    )
    class CaptionDescriptionProperty:
        def __init__(
            self,
            *,
            caption_selector_name: typing.Optional[builtins.str] = None,
            destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionDestinationSettingsProperty"]] = None,
            language_code: typing.Optional[builtins.str] = None,
            language_description: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param caption_selector_name: ``CfnChannel.CaptionDescriptionProperty.CaptionSelectorName``.
            :param destination_settings: ``CfnChannel.CaptionDescriptionProperty.DestinationSettings``.
            :param language_code: ``CfnChannel.CaptionDescriptionProperty.LanguageCode``.
            :param language_description: ``CfnChannel.CaptionDescriptionProperty.LanguageDescription``.
            :param name: ``CfnChannel.CaptionDescriptionProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if caption_selector_name is not None:
                self._values["caption_selector_name"] = caption_selector_name
            if destination_settings is not None:
                self._values["destination_settings"] = destination_settings
            if language_code is not None:
                self._values["language_code"] = language_code
            if language_description is not None:
                self._values["language_description"] = language_description
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def caption_selector_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CaptionDescriptionProperty.CaptionSelectorName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-captionselectorname
            '''
            result = self._values.get("caption_selector_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDescriptionProperty.DestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-destinationsettings
            '''
            result = self._values.get("destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionDestinationSettingsProperty"]], result)

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CaptionDescriptionProperty.LanguageCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-languagecode
            '''
            result = self._values.get("language_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def language_description(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CaptionDescriptionProperty.LanguageDescription``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-languagedescription
            '''
            result = self._values.get("language_description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CaptionDescriptionProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.CaptionDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arib_destination_settings": "aribDestinationSettings",
            "burn_in_destination_settings": "burnInDestinationSettings",
            "dvb_sub_destination_settings": "dvbSubDestinationSettings",
            "ebu_tt_d_destination_settings": "ebuTtDDestinationSettings",
            "embedded_destination_settings": "embeddedDestinationSettings",
            "embedded_plus_scte20_destination_settings": "embeddedPlusScte20DestinationSettings",
            "rtmp_caption_info_destination_settings": "rtmpCaptionInfoDestinationSettings",
            "scte20_plus_embedded_destination_settings": "scte20PlusEmbeddedDestinationSettings",
            "scte27_destination_settings": "scte27DestinationSettings",
            "smpte_tt_destination_settings": "smpteTtDestinationSettings",
            "teletext_destination_settings": "teletextDestinationSettings",
            "ttml_destination_settings": "ttmlDestinationSettings",
            "webvtt_destination_settings": "webvttDestinationSettings",
        },
    )
    class CaptionDestinationSettingsProperty:
        def __init__(
            self,
            *,
            arib_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AribDestinationSettingsProperty"]] = None,
            burn_in_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.BurnInDestinationSettingsProperty"]] = None,
            dvb_sub_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbSubDestinationSettingsProperty"]] = None,
            ebu_tt_d_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EbuTtDDestinationSettingsProperty"]] = None,
            embedded_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EmbeddedDestinationSettingsProperty"]] = None,
            embedded_plus_scte20_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EmbeddedPlusScte20DestinationSettingsProperty"]] = None,
            rtmp_caption_info_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RtmpCaptionInfoDestinationSettingsProperty"]] = None,
            scte20_plus_embedded_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte20PlusEmbeddedDestinationSettingsProperty"]] = None,
            scte27_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte27DestinationSettingsProperty"]] = None,
            smpte_tt_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.SmpteTtDestinationSettingsProperty"]] = None,
            teletext_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TeletextDestinationSettingsProperty"]] = None,
            ttml_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TtmlDestinationSettingsProperty"]] = None,
            webvtt_destination_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.WebvttDestinationSettingsProperty"]] = None,
        ) -> None:
            '''
            :param arib_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.AribDestinationSettings``.
            :param burn_in_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.BurnInDestinationSettings``.
            :param dvb_sub_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.DvbSubDestinationSettings``.
            :param ebu_tt_d_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.EbuTtDDestinationSettings``.
            :param embedded_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.EmbeddedDestinationSettings``.
            :param embedded_plus_scte20_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.EmbeddedPlusScte20DestinationSettings``.
            :param rtmp_caption_info_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.RtmpCaptionInfoDestinationSettings``.
            :param scte20_plus_embedded_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.Scte20PlusEmbeddedDestinationSettings``.
            :param scte27_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.Scte27DestinationSettings``.
            :param smpte_tt_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.SmpteTtDestinationSettings``.
            :param teletext_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.TeletextDestinationSettings``.
            :param ttml_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.TtmlDestinationSettings``.
            :param webvtt_destination_settings: ``CfnChannel.CaptionDestinationSettingsProperty.WebvttDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arib_destination_settings is not None:
                self._values["arib_destination_settings"] = arib_destination_settings
            if burn_in_destination_settings is not None:
                self._values["burn_in_destination_settings"] = burn_in_destination_settings
            if dvb_sub_destination_settings is not None:
                self._values["dvb_sub_destination_settings"] = dvb_sub_destination_settings
            if ebu_tt_d_destination_settings is not None:
                self._values["ebu_tt_d_destination_settings"] = ebu_tt_d_destination_settings
            if embedded_destination_settings is not None:
                self._values["embedded_destination_settings"] = embedded_destination_settings
            if embedded_plus_scte20_destination_settings is not None:
                self._values["embedded_plus_scte20_destination_settings"] = embedded_plus_scte20_destination_settings
            if rtmp_caption_info_destination_settings is not None:
                self._values["rtmp_caption_info_destination_settings"] = rtmp_caption_info_destination_settings
            if scte20_plus_embedded_destination_settings is not None:
                self._values["scte20_plus_embedded_destination_settings"] = scte20_plus_embedded_destination_settings
            if scte27_destination_settings is not None:
                self._values["scte27_destination_settings"] = scte27_destination_settings
            if smpte_tt_destination_settings is not None:
                self._values["smpte_tt_destination_settings"] = smpte_tt_destination_settings
            if teletext_destination_settings is not None:
                self._values["teletext_destination_settings"] = teletext_destination_settings
            if ttml_destination_settings is not None:
                self._values["ttml_destination_settings"] = ttml_destination_settings
            if webvtt_destination_settings is not None:
                self._values["webvtt_destination_settings"] = webvtt_destination_settings

        @builtins.property
        def arib_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AribDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.AribDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-aribdestinationsettings
            '''
            result = self._values.get("arib_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AribDestinationSettingsProperty"]], result)

        @builtins.property
        def burn_in_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.BurnInDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.BurnInDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-burnindestinationsettings
            '''
            result = self._values.get("burn_in_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.BurnInDestinationSettingsProperty"]], result)

        @builtins.property
        def dvb_sub_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbSubDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.DvbSubDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-dvbsubdestinationsettings
            '''
            result = self._values.get("dvb_sub_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbSubDestinationSettingsProperty"]], result)

        @builtins.property
        def ebu_tt_d_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EbuTtDDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.EbuTtDDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-ebuttddestinationsettings
            '''
            result = self._values.get("ebu_tt_d_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EbuTtDDestinationSettingsProperty"]], result)

        @builtins.property
        def embedded_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EmbeddedDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.EmbeddedDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-embeddeddestinationsettings
            '''
            result = self._values.get("embedded_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EmbeddedDestinationSettingsProperty"]], result)

        @builtins.property
        def embedded_plus_scte20_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EmbeddedPlusScte20DestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.EmbeddedPlusScte20DestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-embeddedplusscte20destinationsettings
            '''
            result = self._values.get("embedded_plus_scte20_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EmbeddedPlusScte20DestinationSettingsProperty"]], result)

        @builtins.property
        def rtmp_caption_info_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RtmpCaptionInfoDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.RtmpCaptionInfoDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-rtmpcaptioninfodestinationsettings
            '''
            result = self._values.get("rtmp_caption_info_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RtmpCaptionInfoDestinationSettingsProperty"]], result)

        @builtins.property
        def scte20_plus_embedded_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte20PlusEmbeddedDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.Scte20PlusEmbeddedDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-scte20plusembeddeddestinationsettings
            '''
            result = self._values.get("scte20_plus_embedded_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte20PlusEmbeddedDestinationSettingsProperty"]], result)

        @builtins.property
        def scte27_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte27DestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.Scte27DestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-scte27destinationsettings
            '''
            result = self._values.get("scte27_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte27DestinationSettingsProperty"]], result)

        @builtins.property
        def smpte_tt_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.SmpteTtDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.SmpteTtDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-smptettdestinationsettings
            '''
            result = self._values.get("smpte_tt_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.SmpteTtDestinationSettingsProperty"]], result)

        @builtins.property
        def teletext_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TeletextDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.TeletextDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-teletextdestinationsettings
            '''
            result = self._values.get("teletext_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TeletextDestinationSettingsProperty"]], result)

        @builtins.property
        def ttml_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TtmlDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.TtmlDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-ttmldestinationsettings
            '''
            result = self._values.get("ttml_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TtmlDestinationSettingsProperty"]], result)

        @builtins.property
        def webvtt_destination_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.WebvttDestinationSettingsProperty"]]:
            '''``CfnChannel.CaptionDestinationSettingsProperty.WebvttDestinationSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-webvttdestinationsettings
            '''
            result = self._values.get("webvtt_destination_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.WebvttDestinationSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.CaptionLanguageMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "caption_channel": "captionChannel",
            "language_code": "languageCode",
            "language_description": "languageDescription",
        },
    )
    class CaptionLanguageMappingProperty:
        def __init__(
            self,
            *,
            caption_channel: typing.Optional[jsii.Number] = None,
            language_code: typing.Optional[builtins.str] = None,
            language_description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param caption_channel: ``CfnChannel.CaptionLanguageMappingProperty.CaptionChannel``.
            :param language_code: ``CfnChannel.CaptionLanguageMappingProperty.LanguageCode``.
            :param language_description: ``CfnChannel.CaptionLanguageMappingProperty.LanguageDescription``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if caption_channel is not None:
                self._values["caption_channel"] = caption_channel
            if language_code is not None:
                self._values["language_code"] = language_code
            if language_description is not None:
                self._values["language_description"] = language_description

        @builtins.property
        def caption_channel(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.CaptionLanguageMappingProperty.CaptionChannel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html#cfn-medialive-channel-captionlanguagemapping-captionchannel
            '''
            result = self._values.get("caption_channel")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CaptionLanguageMappingProperty.LanguageCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html#cfn-medialive-channel-captionlanguagemapping-languagecode
            '''
            result = self._values.get("language_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def language_description(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CaptionLanguageMappingProperty.LanguageDescription``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html#cfn-medialive-channel-captionlanguagemapping-languagedescription
            '''
            result = self._values.get("language_description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionLanguageMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.CaptionRectangleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "height": "height",
            "left_offset": "leftOffset",
            "top_offset": "topOffset",
            "width": "width",
        },
    )
    class CaptionRectangleProperty:
        def __init__(
            self,
            *,
            height: typing.Optional[jsii.Number] = None,
            left_offset: typing.Optional[jsii.Number] = None,
            top_offset: typing.Optional[jsii.Number] = None,
            width: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param height: ``CfnChannel.CaptionRectangleProperty.Height``.
            :param left_offset: ``CfnChannel.CaptionRectangleProperty.LeftOffset``.
            :param top_offset: ``CfnChannel.CaptionRectangleProperty.TopOffset``.
            :param width: ``CfnChannel.CaptionRectangleProperty.Width``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if height is not None:
                self._values["height"] = height
            if left_offset is not None:
                self._values["left_offset"] = left_offset
            if top_offset is not None:
                self._values["top_offset"] = top_offset
            if width is not None:
                self._values["width"] = width

        @builtins.property
        def height(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.CaptionRectangleProperty.Height``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html#cfn-medialive-channel-captionrectangle-height
            '''
            result = self._values.get("height")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def left_offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.CaptionRectangleProperty.LeftOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html#cfn-medialive-channel-captionrectangle-leftoffset
            '''
            result = self._values.get("left_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def top_offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.CaptionRectangleProperty.TopOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html#cfn-medialive-channel-captionrectangle-topoffset
            '''
            result = self._values.get("top_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def width(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.CaptionRectangleProperty.Width``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html#cfn-medialive-channel-captionrectangle-width
            '''
            result = self._values.get("width")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionRectangleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.CaptionSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "language_code": "languageCode",
            "name": "name",
            "selector_settings": "selectorSettings",
        },
    )
    class CaptionSelectorProperty:
        def __init__(
            self,
            *,
            language_code: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            selector_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionSelectorSettingsProperty"]] = None,
        ) -> None:
            '''
            :param language_code: ``CfnChannel.CaptionSelectorProperty.LanguageCode``.
            :param name: ``CfnChannel.CaptionSelectorProperty.Name``.
            :param selector_settings: ``CfnChannel.CaptionSelectorProperty.SelectorSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if language_code is not None:
                self._values["language_code"] = language_code
            if name is not None:
                self._values["name"] = name
            if selector_settings is not None:
                self._values["selector_settings"] = selector_settings

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CaptionSelectorProperty.LanguageCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html#cfn-medialive-channel-captionselector-languagecode
            '''
            result = self._values.get("language_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CaptionSelectorProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html#cfn-medialive-channel-captionselector-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def selector_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionSelectorSettingsProperty"]]:
            '''``CfnChannel.CaptionSelectorProperty.SelectorSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html#cfn-medialive-channel-captionselector-selectorsettings
            '''
            result = self._values.get("selector_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionSelectorSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.CaptionSelectorSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ancillary_source_settings": "ancillarySourceSettings",
            "arib_source_settings": "aribSourceSettings",
            "dvb_sub_source_settings": "dvbSubSourceSettings",
            "embedded_source_settings": "embeddedSourceSettings",
            "scte20_source_settings": "scte20SourceSettings",
            "scte27_source_settings": "scte27SourceSettings",
            "teletext_source_settings": "teletextSourceSettings",
        },
    )
    class CaptionSelectorSettingsProperty:
        def __init__(
            self,
            *,
            ancillary_source_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AncillarySourceSettingsProperty"]] = None,
            arib_source_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AribSourceSettingsProperty"]] = None,
            dvb_sub_source_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbSubSourceSettingsProperty"]] = None,
            embedded_source_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EmbeddedSourceSettingsProperty"]] = None,
            scte20_source_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte20SourceSettingsProperty"]] = None,
            scte27_source_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte27SourceSettingsProperty"]] = None,
            teletext_source_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TeletextSourceSettingsProperty"]] = None,
        ) -> None:
            '''
            :param ancillary_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.AncillarySourceSettings``.
            :param arib_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.AribSourceSettings``.
            :param dvb_sub_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.DvbSubSourceSettings``.
            :param embedded_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.EmbeddedSourceSettings``.
            :param scte20_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.Scte20SourceSettings``.
            :param scte27_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.Scte27SourceSettings``.
            :param teletext_source_settings: ``CfnChannel.CaptionSelectorSettingsProperty.TeletextSourceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ancillary_source_settings is not None:
                self._values["ancillary_source_settings"] = ancillary_source_settings
            if arib_source_settings is not None:
                self._values["arib_source_settings"] = arib_source_settings
            if dvb_sub_source_settings is not None:
                self._values["dvb_sub_source_settings"] = dvb_sub_source_settings
            if embedded_source_settings is not None:
                self._values["embedded_source_settings"] = embedded_source_settings
            if scte20_source_settings is not None:
                self._values["scte20_source_settings"] = scte20_source_settings
            if scte27_source_settings is not None:
                self._values["scte27_source_settings"] = scte27_source_settings
            if teletext_source_settings is not None:
                self._values["teletext_source_settings"] = teletext_source_settings

        @builtins.property
        def ancillary_source_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AncillarySourceSettingsProperty"]]:
            '''``CfnChannel.CaptionSelectorSettingsProperty.AncillarySourceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-ancillarysourcesettings
            '''
            result = self._values.get("ancillary_source_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AncillarySourceSettingsProperty"]], result)

        @builtins.property
        def arib_source_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AribSourceSettingsProperty"]]:
            '''``CfnChannel.CaptionSelectorSettingsProperty.AribSourceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-aribsourcesettings
            '''
            result = self._values.get("arib_source_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AribSourceSettingsProperty"]], result)

        @builtins.property
        def dvb_sub_source_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbSubSourceSettingsProperty"]]:
            '''``CfnChannel.CaptionSelectorSettingsProperty.DvbSubSourceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-dvbsubsourcesettings
            '''
            result = self._values.get("dvb_sub_source_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbSubSourceSettingsProperty"]], result)

        @builtins.property
        def embedded_source_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EmbeddedSourceSettingsProperty"]]:
            '''``CfnChannel.CaptionSelectorSettingsProperty.EmbeddedSourceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-embeddedsourcesettings
            '''
            result = self._values.get("embedded_source_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.EmbeddedSourceSettingsProperty"]], result)

        @builtins.property
        def scte20_source_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte20SourceSettingsProperty"]]:
            '''``CfnChannel.CaptionSelectorSettingsProperty.Scte20SourceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-scte20sourcesettings
            '''
            result = self._values.get("scte20_source_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte20SourceSettingsProperty"]], result)

        @builtins.property
        def scte27_source_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte27SourceSettingsProperty"]]:
            '''``CfnChannel.CaptionSelectorSettingsProperty.Scte27SourceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-scte27sourcesettings
            '''
            result = self._values.get("scte27_source_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Scte27SourceSettingsProperty"]], result)

        @builtins.property
        def teletext_source_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TeletextSourceSettingsProperty"]]:
            '''``CfnChannel.CaptionSelectorSettingsProperty.TeletextSourceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-teletextsourcesettings
            '''
            result = self._values.get("teletext_source_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TeletextSourceSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptionSelectorSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.CdiInputSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"resolution": "resolution"},
    )
    class CdiInputSpecificationProperty:
        def __init__(self, *, resolution: typing.Optional[builtins.str] = None) -> None:
            '''
            :param resolution: ``CfnChannel.CdiInputSpecificationProperty.Resolution``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-cdiinputspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if resolution is not None:
                self._values["resolution"] = resolution

        @builtins.property
        def resolution(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CdiInputSpecificationProperty.Resolution``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-cdiinputspecification.html#cfn-medialive-channel-cdiinputspecification-resolution
            '''
            result = self._values.get("resolution")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CdiInputSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.ColorSpacePassthroughSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class ColorSpacePassthroughSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-colorspacepassthroughsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColorSpacePassthroughSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.DvbNitSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_id": "networkId",
            "network_name": "networkName",
            "rep_interval": "repInterval",
        },
    )
    class DvbNitSettingsProperty:
        def __init__(
            self,
            *,
            network_id: typing.Optional[jsii.Number] = None,
            network_name: typing.Optional[builtins.str] = None,
            rep_interval: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param network_id: ``CfnChannel.DvbNitSettingsProperty.NetworkId``.
            :param network_name: ``CfnChannel.DvbNitSettingsProperty.NetworkName``.
            :param rep_interval: ``CfnChannel.DvbNitSettingsProperty.RepInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if network_id is not None:
                self._values["network_id"] = network_id
            if network_name is not None:
                self._values["network_name"] = network_name
            if rep_interval is not None:
                self._values["rep_interval"] = rep_interval

        @builtins.property
        def network_id(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbNitSettingsProperty.NetworkId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html#cfn-medialive-channel-dvbnitsettings-networkid
            '''
            result = self._values.get("network_id")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def network_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbNitSettingsProperty.NetworkName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html#cfn-medialive-channel-dvbnitsettings-networkname
            '''
            result = self._values.get("network_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rep_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbNitSettingsProperty.RepInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html#cfn-medialive-channel-dvbnitsettings-repinterval
            '''
            result = self._values.get("rep_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbNitSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.DvbSdtSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "output_sdt": "outputSdt",
            "rep_interval": "repInterval",
            "service_name": "serviceName",
            "service_provider_name": "serviceProviderName",
        },
    )
    class DvbSdtSettingsProperty:
        def __init__(
            self,
            *,
            output_sdt: typing.Optional[builtins.str] = None,
            rep_interval: typing.Optional[jsii.Number] = None,
            service_name: typing.Optional[builtins.str] = None,
            service_provider_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param output_sdt: ``CfnChannel.DvbSdtSettingsProperty.OutputSdt``.
            :param rep_interval: ``CfnChannel.DvbSdtSettingsProperty.RepInterval``.
            :param service_name: ``CfnChannel.DvbSdtSettingsProperty.ServiceName``.
            :param service_provider_name: ``CfnChannel.DvbSdtSettingsProperty.ServiceProviderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if output_sdt is not None:
                self._values["output_sdt"] = output_sdt
            if rep_interval is not None:
                self._values["rep_interval"] = rep_interval
            if service_name is not None:
                self._values["service_name"] = service_name
            if service_provider_name is not None:
                self._values["service_provider_name"] = service_provider_name

        @builtins.property
        def output_sdt(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSdtSettingsProperty.OutputSdt``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-outputsdt
            '''
            result = self._values.get("output_sdt")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rep_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSdtSettingsProperty.RepInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-repinterval
            '''
            result = self._values.get("rep_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def service_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSdtSettingsProperty.ServiceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-servicename
            '''
            result = self._values.get("service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_provider_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSdtSettingsProperty.ServiceProviderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-serviceprovidername
            '''
            result = self._values.get("service_provider_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbSdtSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.DvbSubDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alignment": "alignment",
            "background_color": "backgroundColor",
            "background_opacity": "backgroundOpacity",
            "font": "font",
            "font_color": "fontColor",
            "font_opacity": "fontOpacity",
            "font_resolution": "fontResolution",
            "font_size": "fontSize",
            "outline_color": "outlineColor",
            "outline_size": "outlineSize",
            "shadow_color": "shadowColor",
            "shadow_opacity": "shadowOpacity",
            "shadow_x_offset": "shadowXOffset",
            "shadow_y_offset": "shadowYOffset",
            "teletext_grid_control": "teletextGridControl",
            "x_position": "xPosition",
            "y_position": "yPosition",
        },
    )
    class DvbSubDestinationSettingsProperty:
        def __init__(
            self,
            *,
            alignment: typing.Optional[builtins.str] = None,
            background_color: typing.Optional[builtins.str] = None,
            background_opacity: typing.Optional[jsii.Number] = None,
            font: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]] = None,
            font_color: typing.Optional[builtins.str] = None,
            font_opacity: typing.Optional[jsii.Number] = None,
            font_resolution: typing.Optional[jsii.Number] = None,
            font_size: typing.Optional[builtins.str] = None,
            outline_color: typing.Optional[builtins.str] = None,
            outline_size: typing.Optional[jsii.Number] = None,
            shadow_color: typing.Optional[builtins.str] = None,
            shadow_opacity: typing.Optional[jsii.Number] = None,
            shadow_x_offset: typing.Optional[jsii.Number] = None,
            shadow_y_offset: typing.Optional[jsii.Number] = None,
            teletext_grid_control: typing.Optional[builtins.str] = None,
            x_position: typing.Optional[jsii.Number] = None,
            y_position: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param alignment: ``CfnChannel.DvbSubDestinationSettingsProperty.Alignment``.
            :param background_color: ``CfnChannel.DvbSubDestinationSettingsProperty.BackgroundColor``.
            :param background_opacity: ``CfnChannel.DvbSubDestinationSettingsProperty.BackgroundOpacity``.
            :param font: ``CfnChannel.DvbSubDestinationSettingsProperty.Font``.
            :param font_color: ``CfnChannel.DvbSubDestinationSettingsProperty.FontColor``.
            :param font_opacity: ``CfnChannel.DvbSubDestinationSettingsProperty.FontOpacity``.
            :param font_resolution: ``CfnChannel.DvbSubDestinationSettingsProperty.FontResolution``.
            :param font_size: ``CfnChannel.DvbSubDestinationSettingsProperty.FontSize``.
            :param outline_color: ``CfnChannel.DvbSubDestinationSettingsProperty.OutlineColor``.
            :param outline_size: ``CfnChannel.DvbSubDestinationSettingsProperty.OutlineSize``.
            :param shadow_color: ``CfnChannel.DvbSubDestinationSettingsProperty.ShadowColor``.
            :param shadow_opacity: ``CfnChannel.DvbSubDestinationSettingsProperty.ShadowOpacity``.
            :param shadow_x_offset: ``CfnChannel.DvbSubDestinationSettingsProperty.ShadowXOffset``.
            :param shadow_y_offset: ``CfnChannel.DvbSubDestinationSettingsProperty.ShadowYOffset``.
            :param teletext_grid_control: ``CfnChannel.DvbSubDestinationSettingsProperty.TeletextGridControl``.
            :param x_position: ``CfnChannel.DvbSubDestinationSettingsProperty.XPosition``.
            :param y_position: ``CfnChannel.DvbSubDestinationSettingsProperty.YPosition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if alignment is not None:
                self._values["alignment"] = alignment
            if background_color is not None:
                self._values["background_color"] = background_color
            if background_opacity is not None:
                self._values["background_opacity"] = background_opacity
            if font is not None:
                self._values["font"] = font
            if font_color is not None:
                self._values["font_color"] = font_color
            if font_opacity is not None:
                self._values["font_opacity"] = font_opacity
            if font_resolution is not None:
                self._values["font_resolution"] = font_resolution
            if font_size is not None:
                self._values["font_size"] = font_size
            if outline_color is not None:
                self._values["outline_color"] = outline_color
            if outline_size is not None:
                self._values["outline_size"] = outline_size
            if shadow_color is not None:
                self._values["shadow_color"] = shadow_color
            if shadow_opacity is not None:
                self._values["shadow_opacity"] = shadow_opacity
            if shadow_x_offset is not None:
                self._values["shadow_x_offset"] = shadow_x_offset
            if shadow_y_offset is not None:
                self._values["shadow_y_offset"] = shadow_y_offset
            if teletext_grid_control is not None:
                self._values["teletext_grid_control"] = teletext_grid_control
            if x_position is not None:
                self._values["x_position"] = x_position
            if y_position is not None:
                self._values["y_position"] = y_position

        @builtins.property
        def alignment(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.Alignment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-alignment
            '''
            result = self._values.get("alignment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def background_color(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.BackgroundColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-backgroundcolor
            '''
            result = self._values.get("background_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def background_opacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.BackgroundOpacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-backgroundopacity
            '''
            result = self._values.get("background_opacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def font(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.Font``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-font
            '''
            result = self._values.get("font")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]], result)

        @builtins.property
        def font_color(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.FontColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontcolor
            '''
            result = self._values.get("font_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def font_opacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.FontOpacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontopacity
            '''
            result = self._values.get("font_opacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def font_resolution(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.FontResolution``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontresolution
            '''
            result = self._values.get("font_resolution")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def font_size(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.FontSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontsize
            '''
            result = self._values.get("font_size")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def outline_color(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.OutlineColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-outlinecolor
            '''
            result = self._values.get("outline_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def outline_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.OutlineSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-outlinesize
            '''
            result = self._values.get("outline_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def shadow_color(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.ShadowColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowcolor
            '''
            result = self._values.get("shadow_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shadow_opacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.ShadowOpacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowopacity
            '''
            result = self._values.get("shadow_opacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def shadow_x_offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.ShadowXOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowxoffset
            '''
            result = self._values.get("shadow_x_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def shadow_y_offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.ShadowYOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowyoffset
            '''
            result = self._values.get("shadow_y_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def teletext_grid_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.TeletextGridControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-teletextgridcontrol
            '''
            result = self._values.get("teletext_grid_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def x_position(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.XPosition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-xposition
            '''
            result = self._values.get("x_position")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def y_position(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubDestinationSettingsProperty.YPosition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-yposition
            '''
            result = self._values.get("y_position")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbSubDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.DvbSubSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"pid": "pid"},
    )
    class DvbSubSourceSettingsProperty:
        def __init__(self, *, pid: typing.Optional[jsii.Number] = None) -> None:
            '''
            :param pid: ``CfnChannel.DvbSubSourceSettingsProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubsourcesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if pid is not None:
                self._values["pid"] = pid

        @builtins.property
        def pid(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbSubSourceSettingsProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubsourcesettings.html#cfn-medialive-channel-dvbsubsourcesettings-pid
            '''
            result = self._values.get("pid")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbSubSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.DvbTdtSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"rep_interval": "repInterval"},
    )
    class DvbTdtSettingsProperty:
        def __init__(
            self,
            *,
            rep_interval: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param rep_interval: ``CfnChannel.DvbTdtSettingsProperty.RepInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if rep_interval is not None:
                self._values["rep_interval"] = rep_interval

        @builtins.property
        def rep_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.DvbTdtSettingsProperty.RepInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html#cfn-medialive-channel-dvbtdtsettings-repinterval
            '''
            result = self._values.get("rep_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DvbTdtSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Eac3SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attenuation_control": "attenuationControl",
            "bitrate": "bitrate",
            "bitstream_mode": "bitstreamMode",
            "coding_mode": "codingMode",
            "dc_filter": "dcFilter",
            "dialnorm": "dialnorm",
            "drc_line": "drcLine",
            "drc_rf": "drcRf",
            "lfe_control": "lfeControl",
            "lfe_filter": "lfeFilter",
            "lo_ro_center_mix_level": "loRoCenterMixLevel",
            "lo_ro_surround_mix_level": "loRoSurroundMixLevel",
            "lt_rt_center_mix_level": "ltRtCenterMixLevel",
            "lt_rt_surround_mix_level": "ltRtSurroundMixLevel",
            "metadata_control": "metadataControl",
            "passthrough_control": "passthroughControl",
            "phase_control": "phaseControl",
            "stereo_downmix": "stereoDownmix",
            "surround_ex_mode": "surroundExMode",
            "surround_mode": "surroundMode",
        },
    )
    class Eac3SettingsProperty:
        def __init__(
            self,
            *,
            attenuation_control: typing.Optional[builtins.str] = None,
            bitrate: typing.Optional[jsii.Number] = None,
            bitstream_mode: typing.Optional[builtins.str] = None,
            coding_mode: typing.Optional[builtins.str] = None,
            dc_filter: typing.Optional[builtins.str] = None,
            dialnorm: typing.Optional[jsii.Number] = None,
            drc_line: typing.Optional[builtins.str] = None,
            drc_rf: typing.Optional[builtins.str] = None,
            lfe_control: typing.Optional[builtins.str] = None,
            lfe_filter: typing.Optional[builtins.str] = None,
            lo_ro_center_mix_level: typing.Optional[jsii.Number] = None,
            lo_ro_surround_mix_level: typing.Optional[jsii.Number] = None,
            lt_rt_center_mix_level: typing.Optional[jsii.Number] = None,
            lt_rt_surround_mix_level: typing.Optional[jsii.Number] = None,
            metadata_control: typing.Optional[builtins.str] = None,
            passthrough_control: typing.Optional[builtins.str] = None,
            phase_control: typing.Optional[builtins.str] = None,
            stereo_downmix: typing.Optional[builtins.str] = None,
            surround_ex_mode: typing.Optional[builtins.str] = None,
            surround_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attenuation_control: ``CfnChannel.Eac3SettingsProperty.AttenuationControl``.
            :param bitrate: ``CfnChannel.Eac3SettingsProperty.Bitrate``.
            :param bitstream_mode: ``CfnChannel.Eac3SettingsProperty.BitstreamMode``.
            :param coding_mode: ``CfnChannel.Eac3SettingsProperty.CodingMode``.
            :param dc_filter: ``CfnChannel.Eac3SettingsProperty.DcFilter``.
            :param dialnorm: ``CfnChannel.Eac3SettingsProperty.Dialnorm``.
            :param drc_line: ``CfnChannel.Eac3SettingsProperty.DrcLine``.
            :param drc_rf: ``CfnChannel.Eac3SettingsProperty.DrcRf``.
            :param lfe_control: ``CfnChannel.Eac3SettingsProperty.LfeControl``.
            :param lfe_filter: ``CfnChannel.Eac3SettingsProperty.LfeFilter``.
            :param lo_ro_center_mix_level: ``CfnChannel.Eac3SettingsProperty.LoRoCenterMixLevel``.
            :param lo_ro_surround_mix_level: ``CfnChannel.Eac3SettingsProperty.LoRoSurroundMixLevel``.
            :param lt_rt_center_mix_level: ``CfnChannel.Eac3SettingsProperty.LtRtCenterMixLevel``.
            :param lt_rt_surround_mix_level: ``CfnChannel.Eac3SettingsProperty.LtRtSurroundMixLevel``.
            :param metadata_control: ``CfnChannel.Eac3SettingsProperty.MetadataControl``.
            :param passthrough_control: ``CfnChannel.Eac3SettingsProperty.PassthroughControl``.
            :param phase_control: ``CfnChannel.Eac3SettingsProperty.PhaseControl``.
            :param stereo_downmix: ``CfnChannel.Eac3SettingsProperty.StereoDownmix``.
            :param surround_ex_mode: ``CfnChannel.Eac3SettingsProperty.SurroundExMode``.
            :param surround_mode: ``CfnChannel.Eac3SettingsProperty.SurroundMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attenuation_control is not None:
                self._values["attenuation_control"] = attenuation_control
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if bitstream_mode is not None:
                self._values["bitstream_mode"] = bitstream_mode
            if coding_mode is not None:
                self._values["coding_mode"] = coding_mode
            if dc_filter is not None:
                self._values["dc_filter"] = dc_filter
            if dialnorm is not None:
                self._values["dialnorm"] = dialnorm
            if drc_line is not None:
                self._values["drc_line"] = drc_line
            if drc_rf is not None:
                self._values["drc_rf"] = drc_rf
            if lfe_control is not None:
                self._values["lfe_control"] = lfe_control
            if lfe_filter is not None:
                self._values["lfe_filter"] = lfe_filter
            if lo_ro_center_mix_level is not None:
                self._values["lo_ro_center_mix_level"] = lo_ro_center_mix_level
            if lo_ro_surround_mix_level is not None:
                self._values["lo_ro_surround_mix_level"] = lo_ro_surround_mix_level
            if lt_rt_center_mix_level is not None:
                self._values["lt_rt_center_mix_level"] = lt_rt_center_mix_level
            if lt_rt_surround_mix_level is not None:
                self._values["lt_rt_surround_mix_level"] = lt_rt_surround_mix_level
            if metadata_control is not None:
                self._values["metadata_control"] = metadata_control
            if passthrough_control is not None:
                self._values["passthrough_control"] = passthrough_control
            if phase_control is not None:
                self._values["phase_control"] = phase_control
            if stereo_downmix is not None:
                self._values["stereo_downmix"] = stereo_downmix
            if surround_ex_mode is not None:
                self._values["surround_ex_mode"] = surround_ex_mode
            if surround_mode is not None:
                self._values["surround_mode"] = surround_mode

        @builtins.property
        def attenuation_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.AttenuationControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-attenuationcontrol
            '''
            result = self._values.get("attenuation_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Eac3SettingsProperty.Bitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-bitrate
            '''
            result = self._values.get("bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def bitstream_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.BitstreamMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-bitstreammode
            '''
            result = self._values.get("bitstream_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def coding_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.CodingMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-codingmode
            '''
            result = self._values.get("coding_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dc_filter(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.DcFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-dcfilter
            '''
            result = self._values.get("dc_filter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dialnorm(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Eac3SettingsProperty.Dialnorm``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-dialnorm
            '''
            result = self._values.get("dialnorm")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def drc_line(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.DrcLine``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-drcline
            '''
            result = self._values.get("drc_line")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def drc_rf(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.DrcRf``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-drcrf
            '''
            result = self._values.get("drc_rf")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lfe_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.LfeControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lfecontrol
            '''
            result = self._values.get("lfe_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lfe_filter(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.LfeFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lfefilter
            '''
            result = self._values.get("lfe_filter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lo_ro_center_mix_level(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Eac3SettingsProperty.LoRoCenterMixLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lorocentermixlevel
            '''
            result = self._values.get("lo_ro_center_mix_level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lo_ro_surround_mix_level(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Eac3SettingsProperty.LoRoSurroundMixLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lorosurroundmixlevel
            '''
            result = self._values.get("lo_ro_surround_mix_level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lt_rt_center_mix_level(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Eac3SettingsProperty.LtRtCenterMixLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-ltrtcentermixlevel
            '''
            result = self._values.get("lt_rt_center_mix_level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lt_rt_surround_mix_level(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Eac3SettingsProperty.LtRtSurroundMixLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-ltrtsurroundmixlevel
            '''
            result = self._values.get("lt_rt_surround_mix_level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def metadata_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.MetadataControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-metadatacontrol
            '''
            result = self._values.get("metadata_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def passthrough_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.PassthroughControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-passthroughcontrol
            '''
            result = self._values.get("passthrough_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def phase_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.PhaseControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-phasecontrol
            '''
            result = self._values.get("phase_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stereo_downmix(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.StereoDownmix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-stereodownmix
            '''
            result = self._values.get("stereo_downmix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def surround_ex_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.SurroundExMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-surroundexmode
            '''
            result = self._values.get("surround_ex_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def surround_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Eac3SettingsProperty.SurroundMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-surroundmode
            '''
            result = self._values.get("surround_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Eac3SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.EbuTtDDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "copyright_holder": "copyrightHolder",
            "fill_line_gap": "fillLineGap",
            "font_family": "fontFamily",
            "style_control": "styleControl",
        },
    )
    class EbuTtDDestinationSettingsProperty:
        def __init__(
            self,
            *,
            copyright_holder: typing.Optional[builtins.str] = None,
            fill_line_gap: typing.Optional[builtins.str] = None,
            font_family: typing.Optional[builtins.str] = None,
            style_control: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param copyright_holder: ``CfnChannel.EbuTtDDestinationSettingsProperty.CopyrightHolder``.
            :param fill_line_gap: ``CfnChannel.EbuTtDDestinationSettingsProperty.FillLineGap``.
            :param font_family: ``CfnChannel.EbuTtDDestinationSettingsProperty.FontFamily``.
            :param style_control: ``CfnChannel.EbuTtDDestinationSettingsProperty.StyleControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if copyright_holder is not None:
                self._values["copyright_holder"] = copyright_holder
            if fill_line_gap is not None:
                self._values["fill_line_gap"] = fill_line_gap
            if font_family is not None:
                self._values["font_family"] = font_family
            if style_control is not None:
                self._values["style_control"] = style_control

        @builtins.property
        def copyright_holder(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.EbuTtDDestinationSettingsProperty.CopyrightHolder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-copyrightholder
            '''
            result = self._values.get("copyright_holder")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fill_line_gap(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.EbuTtDDestinationSettingsProperty.FillLineGap``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-filllinegap
            '''
            result = self._values.get("fill_line_gap")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def font_family(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.EbuTtDDestinationSettingsProperty.FontFamily``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-fontfamily
            '''
            result = self._values.get("font_family")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def style_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.EbuTtDDestinationSettingsProperty.StyleControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-stylecontrol
            '''
            result = self._values.get("style_control")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbuTtDDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.EmbeddedDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EmbeddedDestinationSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddeddestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmbeddedDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.EmbeddedPlusScte20DestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EmbeddedPlusScte20DestinationSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedplusscte20destinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmbeddedPlusScte20DestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.EmbeddedSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "convert608_to708": "convert608To708",
            "scte20_detection": "scte20Detection",
            "source608_channel_number": "source608ChannelNumber",
            "source608_track_number": "source608TrackNumber",
        },
    )
    class EmbeddedSourceSettingsProperty:
        def __init__(
            self,
            *,
            convert608_to708: typing.Optional[builtins.str] = None,
            scte20_detection: typing.Optional[builtins.str] = None,
            source608_channel_number: typing.Optional[jsii.Number] = None,
            source608_track_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param convert608_to708: ``CfnChannel.EmbeddedSourceSettingsProperty.Convert608To708``.
            :param scte20_detection: ``CfnChannel.EmbeddedSourceSettingsProperty.Scte20Detection``.
            :param source608_channel_number: ``CfnChannel.EmbeddedSourceSettingsProperty.Source608ChannelNumber``.
            :param source608_track_number: ``CfnChannel.EmbeddedSourceSettingsProperty.Source608TrackNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if convert608_to708 is not None:
                self._values["convert608_to708"] = convert608_to708
            if scte20_detection is not None:
                self._values["scte20_detection"] = scte20_detection
            if source608_channel_number is not None:
                self._values["source608_channel_number"] = source608_channel_number
            if source608_track_number is not None:
                self._values["source608_track_number"] = source608_track_number

        @builtins.property
        def convert608_to708(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.EmbeddedSourceSettingsProperty.Convert608To708``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-convert608to708
            '''
            result = self._values.get("convert608_to708")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scte20_detection(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.EmbeddedSourceSettingsProperty.Scte20Detection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-scte20detection
            '''
            result = self._values.get("scte20_detection")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source608_channel_number(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.EmbeddedSourceSettingsProperty.Source608ChannelNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-source608channelnumber
            '''
            result = self._values.get("source608_channel_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def source608_track_number(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.EmbeddedSourceSettingsProperty.Source608TrackNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-source608tracknumber
            '''
            result = self._values.get("source608_track_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmbeddedSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.EncoderSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_descriptions": "audioDescriptions",
            "avail_blanking": "availBlanking",
            "avail_configuration": "availConfiguration",
            "blackout_slate": "blackoutSlate",
            "caption_descriptions": "captionDescriptions",
            "feature_activations": "featureActivations",
            "global_configuration": "globalConfiguration",
            "motion_graphics_configuration": "motionGraphicsConfiguration",
            "nielsen_configuration": "nielsenConfiguration",
            "output_groups": "outputGroups",
            "timecode_config": "timecodeConfig",
            "video_descriptions": "videoDescriptions",
        },
    )
    class EncoderSettingsProperty:
        def __init__(
            self,
            *,
            audio_descriptions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioDescriptionProperty"]]]] = None,
            avail_blanking: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AvailBlankingProperty"]] = None,
            avail_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AvailConfigurationProperty"]] = None,
            blackout_slate: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.BlackoutSlateProperty"]] = None,
            caption_descriptions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionDescriptionProperty"]]]] = None,
            feature_activations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FeatureActivationsProperty"]] = None,
            global_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.GlobalConfigurationProperty"]] = None,
            motion_graphics_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MotionGraphicsConfigurationProperty"]] = None,
            nielsen_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.NielsenConfigurationProperty"]] = None,
            output_groups: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputGroupProperty"]]]] = None,
            timecode_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TimecodeConfigProperty"]] = None,
            video_descriptions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoDescriptionProperty"]]]] = None,
        ) -> None:
            '''
            :param audio_descriptions: ``CfnChannel.EncoderSettingsProperty.AudioDescriptions``.
            :param avail_blanking: ``CfnChannel.EncoderSettingsProperty.AvailBlanking``.
            :param avail_configuration: ``CfnChannel.EncoderSettingsProperty.AvailConfiguration``.
            :param blackout_slate: ``CfnChannel.EncoderSettingsProperty.BlackoutSlate``.
            :param caption_descriptions: ``CfnChannel.EncoderSettingsProperty.CaptionDescriptions``.
            :param feature_activations: ``CfnChannel.EncoderSettingsProperty.FeatureActivations``.
            :param global_configuration: ``CfnChannel.EncoderSettingsProperty.GlobalConfiguration``.
            :param motion_graphics_configuration: ``CfnChannel.EncoderSettingsProperty.MotionGraphicsConfiguration``.
            :param nielsen_configuration: ``CfnChannel.EncoderSettingsProperty.NielsenConfiguration``.
            :param output_groups: ``CfnChannel.EncoderSettingsProperty.OutputGroups``.
            :param timecode_config: ``CfnChannel.EncoderSettingsProperty.TimecodeConfig``.
            :param video_descriptions: ``CfnChannel.EncoderSettingsProperty.VideoDescriptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_descriptions is not None:
                self._values["audio_descriptions"] = audio_descriptions
            if avail_blanking is not None:
                self._values["avail_blanking"] = avail_blanking
            if avail_configuration is not None:
                self._values["avail_configuration"] = avail_configuration
            if blackout_slate is not None:
                self._values["blackout_slate"] = blackout_slate
            if caption_descriptions is not None:
                self._values["caption_descriptions"] = caption_descriptions
            if feature_activations is not None:
                self._values["feature_activations"] = feature_activations
            if global_configuration is not None:
                self._values["global_configuration"] = global_configuration
            if motion_graphics_configuration is not None:
                self._values["motion_graphics_configuration"] = motion_graphics_configuration
            if nielsen_configuration is not None:
                self._values["nielsen_configuration"] = nielsen_configuration
            if output_groups is not None:
                self._values["output_groups"] = output_groups
            if timecode_config is not None:
                self._values["timecode_config"] = timecode_config
            if video_descriptions is not None:
                self._values["video_descriptions"] = video_descriptions

        @builtins.property
        def audio_descriptions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioDescriptionProperty"]]]]:
            '''``CfnChannel.EncoderSettingsProperty.AudioDescriptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-audiodescriptions
            '''
            result = self._values.get("audio_descriptions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioDescriptionProperty"]]]], result)

        @builtins.property
        def avail_blanking(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AvailBlankingProperty"]]:
            '''``CfnChannel.EncoderSettingsProperty.AvailBlanking``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-availblanking
            '''
            result = self._values.get("avail_blanking")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AvailBlankingProperty"]], result)

        @builtins.property
        def avail_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AvailConfigurationProperty"]]:
            '''``CfnChannel.EncoderSettingsProperty.AvailConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-availconfiguration
            '''
            result = self._values.get("avail_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AvailConfigurationProperty"]], result)

        @builtins.property
        def blackout_slate(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.BlackoutSlateProperty"]]:
            '''``CfnChannel.EncoderSettingsProperty.BlackoutSlate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-blackoutslate
            '''
            result = self._values.get("blackout_slate")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.BlackoutSlateProperty"]], result)

        @builtins.property
        def caption_descriptions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionDescriptionProperty"]]]]:
            '''``CfnChannel.EncoderSettingsProperty.CaptionDescriptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-captiondescriptions
            '''
            result = self._values.get("caption_descriptions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionDescriptionProperty"]]]], result)

        @builtins.property
        def feature_activations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FeatureActivationsProperty"]]:
            '''``CfnChannel.EncoderSettingsProperty.FeatureActivations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-featureactivations
            '''
            result = self._values.get("feature_activations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FeatureActivationsProperty"]], result)

        @builtins.property
        def global_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.GlobalConfigurationProperty"]]:
            '''``CfnChannel.EncoderSettingsProperty.GlobalConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-globalconfiguration
            '''
            result = self._values.get("global_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.GlobalConfigurationProperty"]], result)

        @builtins.property
        def motion_graphics_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MotionGraphicsConfigurationProperty"]]:
            '''``CfnChannel.EncoderSettingsProperty.MotionGraphicsConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-motiongraphicsconfiguration
            '''
            result = self._values.get("motion_graphics_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MotionGraphicsConfigurationProperty"]], result)

        @builtins.property
        def nielsen_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.NielsenConfigurationProperty"]]:
            '''``CfnChannel.EncoderSettingsProperty.NielsenConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-nielsenconfiguration
            '''
            result = self._values.get("nielsen_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.NielsenConfigurationProperty"]], result)

        @builtins.property
        def output_groups(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputGroupProperty"]]]]:
            '''``CfnChannel.EncoderSettingsProperty.OutputGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-outputgroups
            '''
            result = self._values.get("output_groups")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputGroupProperty"]]]], result)

        @builtins.property
        def timecode_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TimecodeConfigProperty"]]:
            '''``CfnChannel.EncoderSettingsProperty.TimecodeConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-timecodeconfig
            '''
            result = self._values.get("timecode_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TimecodeConfigProperty"]], result)

        @builtins.property
        def video_descriptions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoDescriptionProperty"]]]]:
            '''``CfnChannel.EncoderSettingsProperty.VideoDescriptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-videodescriptions
            '''
            result = self._values.get("video_descriptions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoDescriptionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncoderSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FailoverConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"failover_condition_settings": "failoverConditionSettings"},
    )
    class FailoverConditionProperty:
        def __init__(
            self,
            *,
            failover_condition_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FailoverConditionSettingsProperty"]] = None,
        ) -> None:
            '''
            :param failover_condition_settings: ``CfnChannel.FailoverConditionProperty.FailoverConditionSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failovercondition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if failover_condition_settings is not None:
                self._values["failover_condition_settings"] = failover_condition_settings

        @builtins.property
        def failover_condition_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FailoverConditionSettingsProperty"]]:
            '''``CfnChannel.FailoverConditionProperty.FailoverConditionSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failovercondition.html#cfn-medialive-channel-failovercondition-failoverconditionsettings
            '''
            result = self._values.get("failover_condition_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FailoverConditionSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailoverConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FailoverConditionSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_silence_settings": "audioSilenceSettings",
            "input_loss_settings": "inputLossSettings",
            "video_black_settings": "videoBlackSettings",
        },
    )
    class FailoverConditionSettingsProperty:
        def __init__(
            self,
            *,
            audio_silence_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioSilenceFailoverSettingsProperty"]] = None,
            input_loss_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLossFailoverSettingsProperty"]] = None,
            video_black_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoBlackFailoverSettingsProperty"]] = None,
        ) -> None:
            '''
            :param audio_silence_settings: ``CfnChannel.FailoverConditionSettingsProperty.AudioSilenceSettings``.
            :param input_loss_settings: ``CfnChannel.FailoverConditionSettingsProperty.InputLossSettings``.
            :param video_black_settings: ``CfnChannel.FailoverConditionSettingsProperty.VideoBlackSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failoverconditionsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_silence_settings is not None:
                self._values["audio_silence_settings"] = audio_silence_settings
            if input_loss_settings is not None:
                self._values["input_loss_settings"] = input_loss_settings
            if video_black_settings is not None:
                self._values["video_black_settings"] = video_black_settings

        @builtins.property
        def audio_silence_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioSilenceFailoverSettingsProperty"]]:
            '''``CfnChannel.FailoverConditionSettingsProperty.AudioSilenceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failoverconditionsettings.html#cfn-medialive-channel-failoverconditionsettings-audiosilencesettings
            '''
            result = self._values.get("audio_silence_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioSilenceFailoverSettingsProperty"]], result)

        @builtins.property
        def input_loss_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLossFailoverSettingsProperty"]]:
            '''``CfnChannel.FailoverConditionSettingsProperty.InputLossSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failoverconditionsettings.html#cfn-medialive-channel-failoverconditionsettings-inputlosssettings
            '''
            result = self._values.get("input_loss_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLossFailoverSettingsProperty"]], result)

        @builtins.property
        def video_black_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoBlackFailoverSettingsProperty"]]:
            '''``CfnChannel.FailoverConditionSettingsProperty.VideoBlackSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failoverconditionsettings.html#cfn-medialive-channel-failoverconditionsettings-videoblacksettings
            '''
            result = self._values.get("video_black_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoBlackFailoverSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailoverConditionSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FeatureActivationsProperty",
        jsii_struct_bases=[],
        name_mapping={"input_prepare_schedule_actions": "inputPrepareScheduleActions"},
    )
    class FeatureActivationsProperty:
        def __init__(
            self,
            *,
            input_prepare_schedule_actions: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param input_prepare_schedule_actions: ``CfnChannel.FeatureActivationsProperty.InputPrepareScheduleActions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if input_prepare_schedule_actions is not None:
                self._values["input_prepare_schedule_actions"] = input_prepare_schedule_actions

        @builtins.property
        def input_prepare_schedule_actions(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.FeatureActivationsProperty.InputPrepareScheduleActions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html#cfn-medialive-channel-featureactivations-inputpreparescheduleactions
            '''
            result = self._values.get("input_prepare_schedule_actions")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FeatureActivationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FecOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_depth": "columnDepth",
            "include_fec": "includeFec",
            "row_length": "rowLength",
        },
    )
    class FecOutputSettingsProperty:
        def __init__(
            self,
            *,
            column_depth: typing.Optional[jsii.Number] = None,
            include_fec: typing.Optional[builtins.str] = None,
            row_length: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param column_depth: ``CfnChannel.FecOutputSettingsProperty.ColumnDepth``.
            :param include_fec: ``CfnChannel.FecOutputSettingsProperty.IncludeFec``.
            :param row_length: ``CfnChannel.FecOutputSettingsProperty.RowLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if column_depth is not None:
                self._values["column_depth"] = column_depth
            if include_fec is not None:
                self._values["include_fec"] = include_fec
            if row_length is not None:
                self._values["row_length"] = row_length

        @builtins.property
        def column_depth(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.FecOutputSettingsProperty.ColumnDepth``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html#cfn-medialive-channel-fecoutputsettings-columndepth
            '''
            result = self._values.get("column_depth")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def include_fec(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.FecOutputSettingsProperty.IncludeFec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html#cfn-medialive-channel-fecoutputsettings-includefec
            '''
            result = self._values.get("include_fec")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def row_length(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.FecOutputSettingsProperty.RowLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html#cfn-medialive-channel-fecoutputsettings-rowlength
            '''
            result = self._values.get("row_length")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FecOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Fmp4HlsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_rendition_sets": "audioRenditionSets",
            "nielsen_id3_behavior": "nielsenId3Behavior",
            "timed_metadata_behavior": "timedMetadataBehavior",
        },
    )
    class Fmp4HlsSettingsProperty:
        def __init__(
            self,
            *,
            audio_rendition_sets: typing.Optional[builtins.str] = None,
            nielsen_id3_behavior: typing.Optional[builtins.str] = None,
            timed_metadata_behavior: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param audio_rendition_sets: ``CfnChannel.Fmp4HlsSettingsProperty.AudioRenditionSets``.
            :param nielsen_id3_behavior: ``CfnChannel.Fmp4HlsSettingsProperty.NielsenId3Behavior``.
            :param timed_metadata_behavior: ``CfnChannel.Fmp4HlsSettingsProperty.TimedMetadataBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_rendition_sets is not None:
                self._values["audio_rendition_sets"] = audio_rendition_sets
            if nielsen_id3_behavior is not None:
                self._values["nielsen_id3_behavior"] = nielsen_id3_behavior
            if timed_metadata_behavior is not None:
                self._values["timed_metadata_behavior"] = timed_metadata_behavior

        @builtins.property
        def audio_rendition_sets(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Fmp4HlsSettingsProperty.AudioRenditionSets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html#cfn-medialive-channel-fmp4hlssettings-audiorenditionsets
            '''
            result = self._values.get("audio_rendition_sets")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def nielsen_id3_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Fmp4HlsSettingsProperty.NielsenId3Behavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html#cfn-medialive-channel-fmp4hlssettings-nielsenid3behavior
            '''
            result = self._values.get("nielsen_id3_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timed_metadata_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Fmp4HlsSettingsProperty.TimedMetadataBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html#cfn-medialive-channel-fmp4hlssettings-timedmetadatabehavior
            '''
            result = self._values.get("timed_metadata_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Fmp4HlsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FrameCaptureCdnSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"frame_capture_s3_settings": "frameCaptureS3Settings"},
    )
    class FrameCaptureCdnSettingsProperty:
        def __init__(
            self,
            *,
            frame_capture_s3_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureS3SettingsProperty"]] = None,
        ) -> None:
            '''
            :param frame_capture_s3_settings: ``CfnChannel.FrameCaptureCdnSettingsProperty.FrameCaptureS3Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturecdnsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if frame_capture_s3_settings is not None:
                self._values["frame_capture_s3_settings"] = frame_capture_s3_settings

        @builtins.property
        def frame_capture_s3_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureS3SettingsProperty"]]:
            '''``CfnChannel.FrameCaptureCdnSettingsProperty.FrameCaptureS3Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturecdnsettings.html#cfn-medialive-channel-framecapturecdnsettings-framecaptures3settings
            '''
            result = self._values.get("frame_capture_s3_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureS3SettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameCaptureCdnSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FrameCaptureGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "frame_capture_cdn_settings": "frameCaptureCdnSettings",
        },
    )
    class FrameCaptureGroupSettingsProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]] = None,
            frame_capture_cdn_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureCdnSettingsProperty"]] = None,
        ) -> None:
            '''
            :param destination: ``CfnChannel.FrameCaptureGroupSettingsProperty.Destination``.
            :param frame_capture_cdn_settings: ``CfnChannel.FrameCaptureGroupSettingsProperty.FrameCaptureCdnSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if frame_capture_cdn_settings is not None:
                self._values["frame_capture_cdn_settings"] = frame_capture_cdn_settings

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]]:
            '''``CfnChannel.FrameCaptureGroupSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html#cfn-medialive-channel-framecapturegroupsettings-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]], result)

        @builtins.property
        def frame_capture_cdn_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureCdnSettingsProperty"]]:
            '''``CfnChannel.FrameCaptureGroupSettingsProperty.FrameCaptureCdnSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html#cfn-medialive-channel-framecapturegroupsettings-framecapturecdnsettings
            '''
            result = self._values.get("frame_capture_cdn_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureCdnSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameCaptureGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FrameCaptureHlsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class FrameCaptureHlsSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturehlssettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameCaptureHlsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FrameCaptureOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"name_modifier": "nameModifier"},
    )
    class FrameCaptureOutputSettingsProperty:
        def __init__(
            self,
            *,
            name_modifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name_modifier: ``CfnChannel.FrameCaptureOutputSettingsProperty.NameModifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name_modifier is not None:
                self._values["name_modifier"] = name_modifier

        @builtins.property
        def name_modifier(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.FrameCaptureOutputSettingsProperty.NameModifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html#cfn-medialive-channel-framecaptureoutputsettings-namemodifier
            '''
            result = self._values.get("name_modifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameCaptureOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FrameCaptureS3SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"canned_acl": "cannedAcl"},
    )
    class FrameCaptureS3SettingsProperty:
        def __init__(self, *, canned_acl: typing.Optional[builtins.str] = None) -> None:
            '''
            :param canned_acl: ``CfnChannel.FrameCaptureS3SettingsProperty.CannedAcl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptures3settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if canned_acl is not None:
                self._values["canned_acl"] = canned_acl

        @builtins.property
        def canned_acl(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.FrameCaptureS3SettingsProperty.CannedAcl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptures3settings.html#cfn-medialive-channel-framecaptures3settings-cannedacl
            '''
            result = self._values.get("canned_acl")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameCaptureS3SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.FrameCaptureSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capture_interval": "captureInterval",
            "capture_interval_units": "captureIntervalUnits",
        },
    )
    class FrameCaptureSettingsProperty:
        def __init__(
            self,
            *,
            capture_interval: typing.Optional[jsii.Number] = None,
            capture_interval_units: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param capture_interval: ``CfnChannel.FrameCaptureSettingsProperty.CaptureInterval``.
            :param capture_interval_units: ``CfnChannel.FrameCaptureSettingsProperty.CaptureIntervalUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if capture_interval is not None:
                self._values["capture_interval"] = capture_interval
            if capture_interval_units is not None:
                self._values["capture_interval_units"] = capture_interval_units

        @builtins.property
        def capture_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.FrameCaptureSettingsProperty.CaptureInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html#cfn-medialive-channel-framecapturesettings-captureinterval
            '''
            result = self._values.get("capture_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def capture_interval_units(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.FrameCaptureSettingsProperty.CaptureIntervalUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html#cfn-medialive-channel-framecapturesettings-captureintervalunits
            '''
            result = self._values.get("capture_interval_units")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameCaptureSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.GlobalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "initial_audio_gain": "initialAudioGain",
            "input_end_action": "inputEndAction",
            "input_loss_behavior": "inputLossBehavior",
            "output_locking_mode": "outputLockingMode",
            "output_timing_source": "outputTimingSource",
            "support_low_framerate_inputs": "supportLowFramerateInputs",
        },
    )
    class GlobalConfigurationProperty:
        def __init__(
            self,
            *,
            initial_audio_gain: typing.Optional[jsii.Number] = None,
            input_end_action: typing.Optional[builtins.str] = None,
            input_loss_behavior: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLossBehaviorProperty"]] = None,
            output_locking_mode: typing.Optional[builtins.str] = None,
            output_timing_source: typing.Optional[builtins.str] = None,
            support_low_framerate_inputs: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param initial_audio_gain: ``CfnChannel.GlobalConfigurationProperty.InitialAudioGain``.
            :param input_end_action: ``CfnChannel.GlobalConfigurationProperty.InputEndAction``.
            :param input_loss_behavior: ``CfnChannel.GlobalConfigurationProperty.InputLossBehavior``.
            :param output_locking_mode: ``CfnChannel.GlobalConfigurationProperty.OutputLockingMode``.
            :param output_timing_source: ``CfnChannel.GlobalConfigurationProperty.OutputTimingSource``.
            :param support_low_framerate_inputs: ``CfnChannel.GlobalConfigurationProperty.SupportLowFramerateInputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if initial_audio_gain is not None:
                self._values["initial_audio_gain"] = initial_audio_gain
            if input_end_action is not None:
                self._values["input_end_action"] = input_end_action
            if input_loss_behavior is not None:
                self._values["input_loss_behavior"] = input_loss_behavior
            if output_locking_mode is not None:
                self._values["output_locking_mode"] = output_locking_mode
            if output_timing_source is not None:
                self._values["output_timing_source"] = output_timing_source
            if support_low_framerate_inputs is not None:
                self._values["support_low_framerate_inputs"] = support_low_framerate_inputs

        @builtins.property
        def initial_audio_gain(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.GlobalConfigurationProperty.InitialAudioGain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-initialaudiogain
            '''
            result = self._values.get("initial_audio_gain")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def input_end_action(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.GlobalConfigurationProperty.InputEndAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-inputendaction
            '''
            result = self._values.get("input_end_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_loss_behavior(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLossBehaviorProperty"]]:
            '''``CfnChannel.GlobalConfigurationProperty.InputLossBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-inputlossbehavior
            '''
            result = self._values.get("input_loss_behavior")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLossBehaviorProperty"]], result)

        @builtins.property
        def output_locking_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.GlobalConfigurationProperty.OutputLockingMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-outputlockingmode
            '''
            result = self._values.get("output_locking_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_timing_source(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.GlobalConfigurationProperty.OutputTimingSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-outputtimingsource
            '''
            result = self._values.get("output_timing_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def support_low_framerate_inputs(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.GlobalConfigurationProperty.SupportLowFramerateInputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-supportlowframerateinputs
            '''
            result = self._values.get("support_low_framerate_inputs")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlobalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.H264ColorSpaceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "color_space_passthrough_settings": "colorSpacePassthroughSettings",
            "rec601_settings": "rec601Settings",
            "rec709_settings": "rec709Settings",
        },
    )
    class H264ColorSpaceSettingsProperty:
        def __init__(
            self,
            *,
            color_space_passthrough_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ColorSpacePassthroughSettingsProperty"]] = None,
            rec601_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec601SettingsProperty"]] = None,
            rec709_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec709SettingsProperty"]] = None,
        ) -> None:
            '''
            :param color_space_passthrough_settings: ``CfnChannel.H264ColorSpaceSettingsProperty.ColorSpacePassthroughSettings``.
            :param rec601_settings: ``CfnChannel.H264ColorSpaceSettingsProperty.Rec601Settings``.
            :param rec709_settings: ``CfnChannel.H264ColorSpaceSettingsProperty.Rec709Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if color_space_passthrough_settings is not None:
                self._values["color_space_passthrough_settings"] = color_space_passthrough_settings
            if rec601_settings is not None:
                self._values["rec601_settings"] = rec601_settings
            if rec709_settings is not None:
                self._values["rec709_settings"] = rec709_settings

        @builtins.property
        def color_space_passthrough_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ColorSpacePassthroughSettingsProperty"]]:
            '''``CfnChannel.H264ColorSpaceSettingsProperty.ColorSpacePassthroughSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html#cfn-medialive-channel-h264colorspacesettings-colorspacepassthroughsettings
            '''
            result = self._values.get("color_space_passthrough_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ColorSpacePassthroughSettingsProperty"]], result)

        @builtins.property
        def rec601_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec601SettingsProperty"]]:
            '''``CfnChannel.H264ColorSpaceSettingsProperty.Rec601Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html#cfn-medialive-channel-h264colorspacesettings-rec601settings
            '''
            result = self._values.get("rec601_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec601SettingsProperty"]], result)

        @builtins.property
        def rec709_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec709SettingsProperty"]]:
            '''``CfnChannel.H264ColorSpaceSettingsProperty.Rec709Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html#cfn-medialive-channel-h264colorspacesettings-rec709settings
            '''
            result = self._values.get("rec709_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec709SettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H264ColorSpaceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.H264FilterSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"temporal_filter_settings": "temporalFilterSettings"},
    )
    class H264FilterSettingsProperty:
        def __init__(
            self,
            *,
            temporal_filter_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TemporalFilterSettingsProperty"]] = None,
        ) -> None:
            '''
            :param temporal_filter_settings: ``CfnChannel.H264FilterSettingsProperty.TemporalFilterSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if temporal_filter_settings is not None:
                self._values["temporal_filter_settings"] = temporal_filter_settings

        @builtins.property
        def temporal_filter_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TemporalFilterSettingsProperty"]]:
            '''``CfnChannel.H264FilterSettingsProperty.TemporalFilterSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html#cfn-medialive-channel-h264filtersettings-temporalfiltersettings
            '''
            result = self._values.get("temporal_filter_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TemporalFilterSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H264FilterSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.H264SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adaptive_quantization": "adaptiveQuantization",
            "afd_signaling": "afdSignaling",
            "bitrate": "bitrate",
            "buf_fill_pct": "bufFillPct",
            "buf_size": "bufSize",
            "color_metadata": "colorMetadata",
            "color_space_settings": "colorSpaceSettings",
            "entropy_encoding": "entropyEncoding",
            "filter_settings": "filterSettings",
            "fixed_afd": "fixedAfd",
            "flicker_aq": "flickerAq",
            "force_field_pictures": "forceFieldPictures",
            "framerate_control": "framerateControl",
            "framerate_denominator": "framerateDenominator",
            "framerate_numerator": "framerateNumerator",
            "gop_b_reference": "gopBReference",
            "gop_closed_cadence": "gopClosedCadence",
            "gop_num_b_frames": "gopNumBFrames",
            "gop_size": "gopSize",
            "gop_size_units": "gopSizeUnits",
            "level": "level",
            "look_ahead_rate_control": "lookAheadRateControl",
            "max_bitrate": "maxBitrate",
            "min_i_interval": "minIInterval",
            "num_ref_frames": "numRefFrames",
            "par_control": "parControl",
            "par_denominator": "parDenominator",
            "par_numerator": "parNumerator",
            "profile": "profile",
            "quality_level": "qualityLevel",
            "qvbr_quality_level": "qvbrQualityLevel",
            "rate_control_mode": "rateControlMode",
            "scan_type": "scanType",
            "scene_change_detect": "sceneChangeDetect",
            "slices": "slices",
            "softness": "softness",
            "spatial_aq": "spatialAq",
            "subgop_length": "subgopLength",
            "syntax": "syntax",
            "temporal_aq": "temporalAq",
            "timecode_insertion": "timecodeInsertion",
        },
    )
    class H264SettingsProperty:
        def __init__(
            self,
            *,
            adaptive_quantization: typing.Optional[builtins.str] = None,
            afd_signaling: typing.Optional[builtins.str] = None,
            bitrate: typing.Optional[jsii.Number] = None,
            buf_fill_pct: typing.Optional[jsii.Number] = None,
            buf_size: typing.Optional[jsii.Number] = None,
            color_metadata: typing.Optional[builtins.str] = None,
            color_space_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H264ColorSpaceSettingsProperty"]] = None,
            entropy_encoding: typing.Optional[builtins.str] = None,
            filter_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H264FilterSettingsProperty"]] = None,
            fixed_afd: typing.Optional[builtins.str] = None,
            flicker_aq: typing.Optional[builtins.str] = None,
            force_field_pictures: typing.Optional[builtins.str] = None,
            framerate_control: typing.Optional[builtins.str] = None,
            framerate_denominator: typing.Optional[jsii.Number] = None,
            framerate_numerator: typing.Optional[jsii.Number] = None,
            gop_b_reference: typing.Optional[builtins.str] = None,
            gop_closed_cadence: typing.Optional[jsii.Number] = None,
            gop_num_b_frames: typing.Optional[jsii.Number] = None,
            gop_size: typing.Optional[jsii.Number] = None,
            gop_size_units: typing.Optional[builtins.str] = None,
            level: typing.Optional[builtins.str] = None,
            look_ahead_rate_control: typing.Optional[builtins.str] = None,
            max_bitrate: typing.Optional[jsii.Number] = None,
            min_i_interval: typing.Optional[jsii.Number] = None,
            num_ref_frames: typing.Optional[jsii.Number] = None,
            par_control: typing.Optional[builtins.str] = None,
            par_denominator: typing.Optional[jsii.Number] = None,
            par_numerator: typing.Optional[jsii.Number] = None,
            profile: typing.Optional[builtins.str] = None,
            quality_level: typing.Optional[builtins.str] = None,
            qvbr_quality_level: typing.Optional[jsii.Number] = None,
            rate_control_mode: typing.Optional[builtins.str] = None,
            scan_type: typing.Optional[builtins.str] = None,
            scene_change_detect: typing.Optional[builtins.str] = None,
            slices: typing.Optional[jsii.Number] = None,
            softness: typing.Optional[jsii.Number] = None,
            spatial_aq: typing.Optional[builtins.str] = None,
            subgop_length: typing.Optional[builtins.str] = None,
            syntax: typing.Optional[builtins.str] = None,
            temporal_aq: typing.Optional[builtins.str] = None,
            timecode_insertion: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param adaptive_quantization: ``CfnChannel.H264SettingsProperty.AdaptiveQuantization``.
            :param afd_signaling: ``CfnChannel.H264SettingsProperty.AfdSignaling``.
            :param bitrate: ``CfnChannel.H264SettingsProperty.Bitrate``.
            :param buf_fill_pct: ``CfnChannel.H264SettingsProperty.BufFillPct``.
            :param buf_size: ``CfnChannel.H264SettingsProperty.BufSize``.
            :param color_metadata: ``CfnChannel.H264SettingsProperty.ColorMetadata``.
            :param color_space_settings: ``CfnChannel.H264SettingsProperty.ColorSpaceSettings``.
            :param entropy_encoding: ``CfnChannel.H264SettingsProperty.EntropyEncoding``.
            :param filter_settings: ``CfnChannel.H264SettingsProperty.FilterSettings``.
            :param fixed_afd: ``CfnChannel.H264SettingsProperty.FixedAfd``.
            :param flicker_aq: ``CfnChannel.H264SettingsProperty.FlickerAq``.
            :param force_field_pictures: ``CfnChannel.H264SettingsProperty.ForceFieldPictures``.
            :param framerate_control: ``CfnChannel.H264SettingsProperty.FramerateControl``.
            :param framerate_denominator: ``CfnChannel.H264SettingsProperty.FramerateDenominator``.
            :param framerate_numerator: ``CfnChannel.H264SettingsProperty.FramerateNumerator``.
            :param gop_b_reference: ``CfnChannel.H264SettingsProperty.GopBReference``.
            :param gop_closed_cadence: ``CfnChannel.H264SettingsProperty.GopClosedCadence``.
            :param gop_num_b_frames: ``CfnChannel.H264SettingsProperty.GopNumBFrames``.
            :param gop_size: ``CfnChannel.H264SettingsProperty.GopSize``.
            :param gop_size_units: ``CfnChannel.H264SettingsProperty.GopSizeUnits``.
            :param level: ``CfnChannel.H264SettingsProperty.Level``.
            :param look_ahead_rate_control: ``CfnChannel.H264SettingsProperty.LookAheadRateControl``.
            :param max_bitrate: ``CfnChannel.H264SettingsProperty.MaxBitrate``.
            :param min_i_interval: ``CfnChannel.H264SettingsProperty.MinIInterval``.
            :param num_ref_frames: ``CfnChannel.H264SettingsProperty.NumRefFrames``.
            :param par_control: ``CfnChannel.H264SettingsProperty.ParControl``.
            :param par_denominator: ``CfnChannel.H264SettingsProperty.ParDenominator``.
            :param par_numerator: ``CfnChannel.H264SettingsProperty.ParNumerator``.
            :param profile: ``CfnChannel.H264SettingsProperty.Profile``.
            :param quality_level: ``CfnChannel.H264SettingsProperty.QualityLevel``.
            :param qvbr_quality_level: ``CfnChannel.H264SettingsProperty.QvbrQualityLevel``.
            :param rate_control_mode: ``CfnChannel.H264SettingsProperty.RateControlMode``.
            :param scan_type: ``CfnChannel.H264SettingsProperty.ScanType``.
            :param scene_change_detect: ``CfnChannel.H264SettingsProperty.SceneChangeDetect``.
            :param slices: ``CfnChannel.H264SettingsProperty.Slices``.
            :param softness: ``CfnChannel.H264SettingsProperty.Softness``.
            :param spatial_aq: ``CfnChannel.H264SettingsProperty.SpatialAq``.
            :param subgop_length: ``CfnChannel.H264SettingsProperty.SubgopLength``.
            :param syntax: ``CfnChannel.H264SettingsProperty.Syntax``.
            :param temporal_aq: ``CfnChannel.H264SettingsProperty.TemporalAq``.
            :param timecode_insertion: ``CfnChannel.H264SettingsProperty.TimecodeInsertion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if adaptive_quantization is not None:
                self._values["adaptive_quantization"] = adaptive_quantization
            if afd_signaling is not None:
                self._values["afd_signaling"] = afd_signaling
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if buf_fill_pct is not None:
                self._values["buf_fill_pct"] = buf_fill_pct
            if buf_size is not None:
                self._values["buf_size"] = buf_size
            if color_metadata is not None:
                self._values["color_metadata"] = color_metadata
            if color_space_settings is not None:
                self._values["color_space_settings"] = color_space_settings
            if entropy_encoding is not None:
                self._values["entropy_encoding"] = entropy_encoding
            if filter_settings is not None:
                self._values["filter_settings"] = filter_settings
            if fixed_afd is not None:
                self._values["fixed_afd"] = fixed_afd
            if flicker_aq is not None:
                self._values["flicker_aq"] = flicker_aq
            if force_field_pictures is not None:
                self._values["force_field_pictures"] = force_field_pictures
            if framerate_control is not None:
                self._values["framerate_control"] = framerate_control
            if framerate_denominator is not None:
                self._values["framerate_denominator"] = framerate_denominator
            if framerate_numerator is not None:
                self._values["framerate_numerator"] = framerate_numerator
            if gop_b_reference is not None:
                self._values["gop_b_reference"] = gop_b_reference
            if gop_closed_cadence is not None:
                self._values["gop_closed_cadence"] = gop_closed_cadence
            if gop_num_b_frames is not None:
                self._values["gop_num_b_frames"] = gop_num_b_frames
            if gop_size is not None:
                self._values["gop_size"] = gop_size
            if gop_size_units is not None:
                self._values["gop_size_units"] = gop_size_units
            if level is not None:
                self._values["level"] = level
            if look_ahead_rate_control is not None:
                self._values["look_ahead_rate_control"] = look_ahead_rate_control
            if max_bitrate is not None:
                self._values["max_bitrate"] = max_bitrate
            if min_i_interval is not None:
                self._values["min_i_interval"] = min_i_interval
            if num_ref_frames is not None:
                self._values["num_ref_frames"] = num_ref_frames
            if par_control is not None:
                self._values["par_control"] = par_control
            if par_denominator is not None:
                self._values["par_denominator"] = par_denominator
            if par_numerator is not None:
                self._values["par_numerator"] = par_numerator
            if profile is not None:
                self._values["profile"] = profile
            if quality_level is not None:
                self._values["quality_level"] = quality_level
            if qvbr_quality_level is not None:
                self._values["qvbr_quality_level"] = qvbr_quality_level
            if rate_control_mode is not None:
                self._values["rate_control_mode"] = rate_control_mode
            if scan_type is not None:
                self._values["scan_type"] = scan_type
            if scene_change_detect is not None:
                self._values["scene_change_detect"] = scene_change_detect
            if slices is not None:
                self._values["slices"] = slices
            if softness is not None:
                self._values["softness"] = softness
            if spatial_aq is not None:
                self._values["spatial_aq"] = spatial_aq
            if subgop_length is not None:
                self._values["subgop_length"] = subgop_length
            if syntax is not None:
                self._values["syntax"] = syntax
            if temporal_aq is not None:
                self._values["temporal_aq"] = temporal_aq
            if timecode_insertion is not None:
                self._values["timecode_insertion"] = timecode_insertion

        @builtins.property
        def adaptive_quantization(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.AdaptiveQuantization``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-adaptivequantization
            '''
            result = self._values.get("adaptive_quantization")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def afd_signaling(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.AfdSignaling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-afdsignaling
            '''
            result = self._values.get("afd_signaling")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.Bitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-bitrate
            '''
            result = self._values.get("bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def buf_fill_pct(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.BufFillPct``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-buffillpct
            '''
            result = self._values.get("buf_fill_pct")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def buf_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.BufSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-bufsize
            '''
            result = self._values.get("buf_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def color_metadata(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.ColorMetadata``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-colormetadata
            '''
            result = self._values.get("color_metadata")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def color_space_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H264ColorSpaceSettingsProperty"]]:
            '''``CfnChannel.H264SettingsProperty.ColorSpaceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-colorspacesettings
            '''
            result = self._values.get("color_space_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H264ColorSpaceSettingsProperty"]], result)

        @builtins.property
        def entropy_encoding(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.EntropyEncoding``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-entropyencoding
            '''
            result = self._values.get("entropy_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def filter_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H264FilterSettingsProperty"]]:
            '''``CfnChannel.H264SettingsProperty.FilterSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-filtersettings
            '''
            result = self._values.get("filter_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H264FilterSettingsProperty"]], result)

        @builtins.property
        def fixed_afd(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.FixedAfd``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-fixedafd
            '''
            result = self._values.get("fixed_afd")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def flicker_aq(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.FlickerAq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-flickeraq
            '''
            result = self._values.get("flicker_aq")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def force_field_pictures(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.ForceFieldPictures``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-forcefieldpictures
            '''
            result = self._values.get("force_field_pictures")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def framerate_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.FramerateControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-frameratecontrol
            '''
            result = self._values.get("framerate_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def framerate_denominator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.FramerateDenominator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-frameratedenominator
            '''
            result = self._values.get("framerate_denominator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def framerate_numerator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.FramerateNumerator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-frameratenumerator
            '''
            result = self._values.get("framerate_numerator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_b_reference(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.GopBReference``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopbreference
            '''
            result = self._values.get("gop_b_reference")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def gop_closed_cadence(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.GopClosedCadence``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopclosedcadence
            '''
            result = self._values.get("gop_closed_cadence")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_num_b_frames(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.GopNumBFrames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopnumbframes
            '''
            result = self._values.get("gop_num_b_frames")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.GopSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopsize
            '''
            result = self._values.get("gop_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_size_units(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.GopSizeUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopsizeunits
            '''
            result = self._values.get("gop_size_units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def level(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.Level``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-level
            '''
            result = self._values.get("level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def look_ahead_rate_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.LookAheadRateControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-lookaheadratecontrol
            '''
            result = self._values.get("look_ahead_rate_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.MaxBitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-maxbitrate
            '''
            result = self._values.get("max_bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_i_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.MinIInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-miniinterval
            '''
            result = self._values.get("min_i_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def num_ref_frames(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.NumRefFrames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-numrefframes
            '''
            result = self._values.get("num_ref_frames")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def par_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.ParControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-parcontrol
            '''
            result = self._values.get("par_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def par_denominator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.ParDenominator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-pardenominator
            '''
            result = self._values.get("par_denominator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def par_numerator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.ParNumerator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-parnumerator
            '''
            result = self._values.get("par_numerator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.Profile``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-profile
            '''
            result = self._values.get("profile")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def quality_level(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.QualityLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-qualitylevel
            '''
            result = self._values.get("quality_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def qvbr_quality_level(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.QvbrQualityLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-qvbrqualitylevel
            '''
            result = self._values.get("qvbr_quality_level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rate_control_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.RateControlMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-ratecontrolmode
            '''
            result = self._values.get("rate_control_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scan_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.ScanType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-scantype
            '''
            result = self._values.get("scan_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scene_change_detect(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.SceneChangeDetect``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-scenechangedetect
            '''
            result = self._values.get("scene_change_detect")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def slices(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.Slices``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-slices
            '''
            result = self._values.get("slices")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def softness(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H264SettingsProperty.Softness``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-softness
            '''
            result = self._values.get("softness")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def spatial_aq(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.SpatialAq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-spatialaq
            '''
            result = self._values.get("spatial_aq")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subgop_length(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.SubgopLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-subgoplength
            '''
            result = self._values.get("subgop_length")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def syntax(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.Syntax``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-syntax
            '''
            result = self._values.get("syntax")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def temporal_aq(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.TemporalAq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-temporalaq
            '''
            result = self._values.get("temporal_aq")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timecode_insertion(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H264SettingsProperty.TimecodeInsertion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-timecodeinsertion
            '''
            result = self._values.get("timecode_insertion")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H264SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.H265ColorSpaceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "color_space_passthrough_settings": "colorSpacePassthroughSettings",
            "hdr10_settings": "hdr10Settings",
            "rec601_settings": "rec601Settings",
            "rec709_settings": "rec709Settings",
        },
    )
    class H265ColorSpaceSettingsProperty:
        def __init__(
            self,
            *,
            color_space_passthrough_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ColorSpacePassthroughSettingsProperty"]] = None,
            hdr10_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Hdr10SettingsProperty"]] = None,
            rec601_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec601SettingsProperty"]] = None,
            rec709_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec709SettingsProperty"]] = None,
        ) -> None:
            '''
            :param color_space_passthrough_settings: ``CfnChannel.H265ColorSpaceSettingsProperty.ColorSpacePassthroughSettings``.
            :param hdr10_settings: ``CfnChannel.H265ColorSpaceSettingsProperty.Hdr10Settings``.
            :param rec601_settings: ``CfnChannel.H265ColorSpaceSettingsProperty.Rec601Settings``.
            :param rec709_settings: ``CfnChannel.H265ColorSpaceSettingsProperty.Rec709Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if color_space_passthrough_settings is not None:
                self._values["color_space_passthrough_settings"] = color_space_passthrough_settings
            if hdr10_settings is not None:
                self._values["hdr10_settings"] = hdr10_settings
            if rec601_settings is not None:
                self._values["rec601_settings"] = rec601_settings
            if rec709_settings is not None:
                self._values["rec709_settings"] = rec709_settings

        @builtins.property
        def color_space_passthrough_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ColorSpacePassthroughSettingsProperty"]]:
            '''``CfnChannel.H265ColorSpaceSettingsProperty.ColorSpacePassthroughSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-colorspacepassthroughsettings
            '''
            result = self._values.get("color_space_passthrough_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ColorSpacePassthroughSettingsProperty"]], result)

        @builtins.property
        def hdr10_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Hdr10SettingsProperty"]]:
            '''``CfnChannel.H265ColorSpaceSettingsProperty.Hdr10Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-hdr10settings
            '''
            result = self._values.get("hdr10_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Hdr10SettingsProperty"]], result)

        @builtins.property
        def rec601_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec601SettingsProperty"]]:
            '''``CfnChannel.H265ColorSpaceSettingsProperty.Rec601Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-rec601settings
            '''
            result = self._values.get("rec601_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec601SettingsProperty"]], result)

        @builtins.property
        def rec709_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec709SettingsProperty"]]:
            '''``CfnChannel.H265ColorSpaceSettingsProperty.Rec709Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-rec709settings
            '''
            result = self._values.get("rec709_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Rec709SettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H265ColorSpaceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.H265FilterSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"temporal_filter_settings": "temporalFilterSettings"},
    )
    class H265FilterSettingsProperty:
        def __init__(
            self,
            *,
            temporal_filter_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TemporalFilterSettingsProperty"]] = None,
        ) -> None:
            '''
            :param temporal_filter_settings: ``CfnChannel.H265FilterSettingsProperty.TemporalFilterSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if temporal_filter_settings is not None:
                self._values["temporal_filter_settings"] = temporal_filter_settings

        @builtins.property
        def temporal_filter_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TemporalFilterSettingsProperty"]]:
            '''``CfnChannel.H265FilterSettingsProperty.TemporalFilterSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html#cfn-medialive-channel-h265filtersettings-temporalfiltersettings
            '''
            result = self._values.get("temporal_filter_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TemporalFilterSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H265FilterSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.H265SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adaptive_quantization": "adaptiveQuantization",
            "afd_signaling": "afdSignaling",
            "alternative_transfer_function": "alternativeTransferFunction",
            "bitrate": "bitrate",
            "buf_size": "bufSize",
            "color_metadata": "colorMetadata",
            "color_space_settings": "colorSpaceSettings",
            "filter_settings": "filterSettings",
            "fixed_afd": "fixedAfd",
            "flicker_aq": "flickerAq",
            "framerate_denominator": "framerateDenominator",
            "framerate_numerator": "framerateNumerator",
            "gop_closed_cadence": "gopClosedCadence",
            "gop_size": "gopSize",
            "gop_size_units": "gopSizeUnits",
            "level": "level",
            "look_ahead_rate_control": "lookAheadRateControl",
            "max_bitrate": "maxBitrate",
            "min_i_interval": "minIInterval",
            "par_denominator": "parDenominator",
            "par_numerator": "parNumerator",
            "profile": "profile",
            "qvbr_quality_level": "qvbrQualityLevel",
            "rate_control_mode": "rateControlMode",
            "scan_type": "scanType",
            "scene_change_detect": "sceneChangeDetect",
            "slices": "slices",
            "tier": "tier",
            "timecode_insertion": "timecodeInsertion",
        },
    )
    class H265SettingsProperty:
        def __init__(
            self,
            *,
            adaptive_quantization: typing.Optional[builtins.str] = None,
            afd_signaling: typing.Optional[builtins.str] = None,
            alternative_transfer_function: typing.Optional[builtins.str] = None,
            bitrate: typing.Optional[jsii.Number] = None,
            buf_size: typing.Optional[jsii.Number] = None,
            color_metadata: typing.Optional[builtins.str] = None,
            color_space_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H265ColorSpaceSettingsProperty"]] = None,
            filter_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H265FilterSettingsProperty"]] = None,
            fixed_afd: typing.Optional[builtins.str] = None,
            flicker_aq: typing.Optional[builtins.str] = None,
            framerate_denominator: typing.Optional[jsii.Number] = None,
            framerate_numerator: typing.Optional[jsii.Number] = None,
            gop_closed_cadence: typing.Optional[jsii.Number] = None,
            gop_size: typing.Optional[jsii.Number] = None,
            gop_size_units: typing.Optional[builtins.str] = None,
            level: typing.Optional[builtins.str] = None,
            look_ahead_rate_control: typing.Optional[builtins.str] = None,
            max_bitrate: typing.Optional[jsii.Number] = None,
            min_i_interval: typing.Optional[jsii.Number] = None,
            par_denominator: typing.Optional[jsii.Number] = None,
            par_numerator: typing.Optional[jsii.Number] = None,
            profile: typing.Optional[builtins.str] = None,
            qvbr_quality_level: typing.Optional[jsii.Number] = None,
            rate_control_mode: typing.Optional[builtins.str] = None,
            scan_type: typing.Optional[builtins.str] = None,
            scene_change_detect: typing.Optional[builtins.str] = None,
            slices: typing.Optional[jsii.Number] = None,
            tier: typing.Optional[builtins.str] = None,
            timecode_insertion: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param adaptive_quantization: ``CfnChannel.H265SettingsProperty.AdaptiveQuantization``.
            :param afd_signaling: ``CfnChannel.H265SettingsProperty.AfdSignaling``.
            :param alternative_transfer_function: ``CfnChannel.H265SettingsProperty.AlternativeTransferFunction``.
            :param bitrate: ``CfnChannel.H265SettingsProperty.Bitrate``.
            :param buf_size: ``CfnChannel.H265SettingsProperty.BufSize``.
            :param color_metadata: ``CfnChannel.H265SettingsProperty.ColorMetadata``.
            :param color_space_settings: ``CfnChannel.H265SettingsProperty.ColorSpaceSettings``.
            :param filter_settings: ``CfnChannel.H265SettingsProperty.FilterSettings``.
            :param fixed_afd: ``CfnChannel.H265SettingsProperty.FixedAfd``.
            :param flicker_aq: ``CfnChannel.H265SettingsProperty.FlickerAq``.
            :param framerate_denominator: ``CfnChannel.H265SettingsProperty.FramerateDenominator``.
            :param framerate_numerator: ``CfnChannel.H265SettingsProperty.FramerateNumerator``.
            :param gop_closed_cadence: ``CfnChannel.H265SettingsProperty.GopClosedCadence``.
            :param gop_size: ``CfnChannel.H265SettingsProperty.GopSize``.
            :param gop_size_units: ``CfnChannel.H265SettingsProperty.GopSizeUnits``.
            :param level: ``CfnChannel.H265SettingsProperty.Level``.
            :param look_ahead_rate_control: ``CfnChannel.H265SettingsProperty.LookAheadRateControl``.
            :param max_bitrate: ``CfnChannel.H265SettingsProperty.MaxBitrate``.
            :param min_i_interval: ``CfnChannel.H265SettingsProperty.MinIInterval``.
            :param par_denominator: ``CfnChannel.H265SettingsProperty.ParDenominator``.
            :param par_numerator: ``CfnChannel.H265SettingsProperty.ParNumerator``.
            :param profile: ``CfnChannel.H265SettingsProperty.Profile``.
            :param qvbr_quality_level: ``CfnChannel.H265SettingsProperty.QvbrQualityLevel``.
            :param rate_control_mode: ``CfnChannel.H265SettingsProperty.RateControlMode``.
            :param scan_type: ``CfnChannel.H265SettingsProperty.ScanType``.
            :param scene_change_detect: ``CfnChannel.H265SettingsProperty.SceneChangeDetect``.
            :param slices: ``CfnChannel.H265SettingsProperty.Slices``.
            :param tier: ``CfnChannel.H265SettingsProperty.Tier``.
            :param timecode_insertion: ``CfnChannel.H265SettingsProperty.TimecodeInsertion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if adaptive_quantization is not None:
                self._values["adaptive_quantization"] = adaptive_quantization
            if afd_signaling is not None:
                self._values["afd_signaling"] = afd_signaling
            if alternative_transfer_function is not None:
                self._values["alternative_transfer_function"] = alternative_transfer_function
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if buf_size is not None:
                self._values["buf_size"] = buf_size
            if color_metadata is not None:
                self._values["color_metadata"] = color_metadata
            if color_space_settings is not None:
                self._values["color_space_settings"] = color_space_settings
            if filter_settings is not None:
                self._values["filter_settings"] = filter_settings
            if fixed_afd is not None:
                self._values["fixed_afd"] = fixed_afd
            if flicker_aq is not None:
                self._values["flicker_aq"] = flicker_aq
            if framerate_denominator is not None:
                self._values["framerate_denominator"] = framerate_denominator
            if framerate_numerator is not None:
                self._values["framerate_numerator"] = framerate_numerator
            if gop_closed_cadence is not None:
                self._values["gop_closed_cadence"] = gop_closed_cadence
            if gop_size is not None:
                self._values["gop_size"] = gop_size
            if gop_size_units is not None:
                self._values["gop_size_units"] = gop_size_units
            if level is not None:
                self._values["level"] = level
            if look_ahead_rate_control is not None:
                self._values["look_ahead_rate_control"] = look_ahead_rate_control
            if max_bitrate is not None:
                self._values["max_bitrate"] = max_bitrate
            if min_i_interval is not None:
                self._values["min_i_interval"] = min_i_interval
            if par_denominator is not None:
                self._values["par_denominator"] = par_denominator
            if par_numerator is not None:
                self._values["par_numerator"] = par_numerator
            if profile is not None:
                self._values["profile"] = profile
            if qvbr_quality_level is not None:
                self._values["qvbr_quality_level"] = qvbr_quality_level
            if rate_control_mode is not None:
                self._values["rate_control_mode"] = rate_control_mode
            if scan_type is not None:
                self._values["scan_type"] = scan_type
            if scene_change_detect is not None:
                self._values["scene_change_detect"] = scene_change_detect
            if slices is not None:
                self._values["slices"] = slices
            if tier is not None:
                self._values["tier"] = tier
            if timecode_insertion is not None:
                self._values["timecode_insertion"] = timecode_insertion

        @builtins.property
        def adaptive_quantization(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.AdaptiveQuantization``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-adaptivequantization
            '''
            result = self._values.get("adaptive_quantization")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def afd_signaling(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.AfdSignaling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-afdsignaling
            '''
            result = self._values.get("afd_signaling")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def alternative_transfer_function(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.AlternativeTransferFunction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-alternativetransferfunction
            '''
            result = self._values.get("alternative_transfer_function")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.Bitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-bitrate
            '''
            result = self._values.get("bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def buf_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.BufSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-bufsize
            '''
            result = self._values.get("buf_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def color_metadata(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.ColorMetadata``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-colormetadata
            '''
            result = self._values.get("color_metadata")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def color_space_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H265ColorSpaceSettingsProperty"]]:
            '''``CfnChannel.H265SettingsProperty.ColorSpaceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-colorspacesettings
            '''
            result = self._values.get("color_space_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H265ColorSpaceSettingsProperty"]], result)

        @builtins.property
        def filter_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H265FilterSettingsProperty"]]:
            '''``CfnChannel.H265SettingsProperty.FilterSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-filtersettings
            '''
            result = self._values.get("filter_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H265FilterSettingsProperty"]], result)

        @builtins.property
        def fixed_afd(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.FixedAfd``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-fixedafd
            '''
            result = self._values.get("fixed_afd")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def flicker_aq(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.FlickerAq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-flickeraq
            '''
            result = self._values.get("flicker_aq")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def framerate_denominator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.FramerateDenominator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-frameratedenominator
            '''
            result = self._values.get("framerate_denominator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def framerate_numerator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.FramerateNumerator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-frameratenumerator
            '''
            result = self._values.get("framerate_numerator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_closed_cadence(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.GopClosedCadence``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-gopclosedcadence
            '''
            result = self._values.get("gop_closed_cadence")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.GopSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-gopsize
            '''
            result = self._values.get("gop_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_size_units(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.GopSizeUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-gopsizeunits
            '''
            result = self._values.get("gop_size_units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def level(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.Level``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-level
            '''
            result = self._values.get("level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def look_ahead_rate_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.LookAheadRateControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-lookaheadratecontrol
            '''
            result = self._values.get("look_ahead_rate_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.MaxBitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-maxbitrate
            '''
            result = self._values.get("max_bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_i_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.MinIInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-miniinterval
            '''
            result = self._values.get("min_i_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def par_denominator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.ParDenominator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-pardenominator
            '''
            result = self._values.get("par_denominator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def par_numerator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.ParNumerator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-parnumerator
            '''
            result = self._values.get("par_numerator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.Profile``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-profile
            '''
            result = self._values.get("profile")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def qvbr_quality_level(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.QvbrQualityLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-qvbrqualitylevel
            '''
            result = self._values.get("qvbr_quality_level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rate_control_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.RateControlMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-ratecontrolmode
            '''
            result = self._values.get("rate_control_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scan_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.ScanType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-scantype
            '''
            result = self._values.get("scan_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scene_change_detect(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.SceneChangeDetect``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-scenechangedetect
            '''
            result = self._values.get("scene_change_detect")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def slices(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.H265SettingsProperty.Slices``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-slices
            '''
            result = self._values.get("slices")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def tier(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.Tier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-tier
            '''
            result = self._values.get("tier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timecode_insertion(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.H265SettingsProperty.TimecodeInsertion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-timecodeinsertion
            '''
            result = self._values.get("timecode_insertion")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "H265SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Hdr10SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"max_cll": "maxCll", "max_fall": "maxFall"},
    )
    class Hdr10SettingsProperty:
        def __init__(
            self,
            *,
            max_cll: typing.Optional[jsii.Number] = None,
            max_fall: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param max_cll: ``CfnChannel.Hdr10SettingsProperty.MaxCll``.
            :param max_fall: ``CfnChannel.Hdr10SettingsProperty.MaxFall``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if max_cll is not None:
                self._values["max_cll"] = max_cll
            if max_fall is not None:
                self._values["max_fall"] = max_fall

        @builtins.property
        def max_cll(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Hdr10SettingsProperty.MaxCll``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html#cfn-medialive-channel-hdr10settings-maxcll
            '''
            result = self._values.get("max_cll")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_fall(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Hdr10SettingsProperty.MaxFall``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html#cfn-medialive-channel-hdr10settings-maxfall
            '''
            result = self._values.get("max_fall")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Hdr10SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsAkamaiSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_retry_interval": "connectionRetryInterval",
            "filecache_duration": "filecacheDuration",
            "http_transfer_mode": "httpTransferMode",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
            "salt": "salt",
            "token": "token",
        },
    )
    class HlsAkamaiSettingsProperty:
        def __init__(
            self,
            *,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            http_transfer_mode: typing.Optional[builtins.str] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
            salt: typing.Optional[builtins.str] = None,
            token: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param connection_retry_interval: ``CfnChannel.HlsAkamaiSettingsProperty.ConnectionRetryInterval``.
            :param filecache_duration: ``CfnChannel.HlsAkamaiSettingsProperty.FilecacheDuration``.
            :param http_transfer_mode: ``CfnChannel.HlsAkamaiSettingsProperty.HttpTransferMode``.
            :param num_retries: ``CfnChannel.HlsAkamaiSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.HlsAkamaiSettingsProperty.RestartDelay``.
            :param salt: ``CfnChannel.HlsAkamaiSettingsProperty.Salt``.
            :param token: ``CfnChannel.HlsAkamaiSettingsProperty.Token``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if http_transfer_mode is not None:
                self._values["http_transfer_mode"] = http_transfer_mode
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay
            if salt is not None:
                self._values["salt"] = salt
            if token is not None:
                self._values["token"] = token

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsAkamaiSettingsProperty.ConnectionRetryInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-connectionretryinterval
            '''
            result = self._values.get("connection_retry_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsAkamaiSettingsProperty.FilecacheDuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-filecacheduration
            '''
            result = self._values.get("filecache_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def http_transfer_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsAkamaiSettingsProperty.HttpTransferMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-httptransfermode
            '''
            result = self._values.get("http_transfer_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsAkamaiSettingsProperty.NumRetries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-numretries
            '''
            result = self._values.get("num_retries")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsAkamaiSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-restartdelay
            '''
            result = self._values.get("restart_delay")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def salt(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsAkamaiSettingsProperty.Salt``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-salt
            '''
            result = self._values.get("salt")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def token(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsAkamaiSettingsProperty.Token``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-token
            '''
            result = self._values.get("token")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsAkamaiSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsBasicPutSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_retry_interval": "connectionRetryInterval",
            "filecache_duration": "filecacheDuration",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
        },
    )
    class HlsBasicPutSettingsProperty:
        def __init__(
            self,
            *,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param connection_retry_interval: ``CfnChannel.HlsBasicPutSettingsProperty.ConnectionRetryInterval``.
            :param filecache_duration: ``CfnChannel.HlsBasicPutSettingsProperty.FilecacheDuration``.
            :param num_retries: ``CfnChannel.HlsBasicPutSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.HlsBasicPutSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsBasicPutSettingsProperty.ConnectionRetryInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-connectionretryinterval
            '''
            result = self._values.get("connection_retry_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsBasicPutSettingsProperty.FilecacheDuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-filecacheduration
            '''
            result = self._values.get("filecache_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsBasicPutSettingsProperty.NumRetries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-numretries
            '''
            result = self._values.get("num_retries")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsBasicPutSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-restartdelay
            '''
            result = self._values.get("restart_delay")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsBasicPutSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsCdnSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hls_akamai_settings": "hlsAkamaiSettings",
            "hls_basic_put_settings": "hlsBasicPutSettings",
            "hls_media_store_settings": "hlsMediaStoreSettings",
            "hls_s3_settings": "hlsS3Settings",
            "hls_webdav_settings": "hlsWebdavSettings",
        },
    )
    class HlsCdnSettingsProperty:
        def __init__(
            self,
            *,
            hls_akamai_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsAkamaiSettingsProperty"]] = None,
            hls_basic_put_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsBasicPutSettingsProperty"]] = None,
            hls_media_store_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsMediaStoreSettingsProperty"]] = None,
            hls_s3_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsS3SettingsProperty"]] = None,
            hls_webdav_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsWebdavSettingsProperty"]] = None,
        ) -> None:
            '''
            :param hls_akamai_settings: ``CfnChannel.HlsCdnSettingsProperty.HlsAkamaiSettings``.
            :param hls_basic_put_settings: ``CfnChannel.HlsCdnSettingsProperty.HlsBasicPutSettings``.
            :param hls_media_store_settings: ``CfnChannel.HlsCdnSettingsProperty.HlsMediaStoreSettings``.
            :param hls_s3_settings: ``CfnChannel.HlsCdnSettingsProperty.HlsS3Settings``.
            :param hls_webdav_settings: ``CfnChannel.HlsCdnSettingsProperty.HlsWebdavSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if hls_akamai_settings is not None:
                self._values["hls_akamai_settings"] = hls_akamai_settings
            if hls_basic_put_settings is not None:
                self._values["hls_basic_put_settings"] = hls_basic_put_settings
            if hls_media_store_settings is not None:
                self._values["hls_media_store_settings"] = hls_media_store_settings
            if hls_s3_settings is not None:
                self._values["hls_s3_settings"] = hls_s3_settings
            if hls_webdav_settings is not None:
                self._values["hls_webdav_settings"] = hls_webdav_settings

        @builtins.property
        def hls_akamai_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsAkamaiSettingsProperty"]]:
            '''``CfnChannel.HlsCdnSettingsProperty.HlsAkamaiSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlsakamaisettings
            '''
            result = self._values.get("hls_akamai_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsAkamaiSettingsProperty"]], result)

        @builtins.property
        def hls_basic_put_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsBasicPutSettingsProperty"]]:
            '''``CfnChannel.HlsCdnSettingsProperty.HlsBasicPutSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlsbasicputsettings
            '''
            result = self._values.get("hls_basic_put_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsBasicPutSettingsProperty"]], result)

        @builtins.property
        def hls_media_store_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsMediaStoreSettingsProperty"]]:
            '''``CfnChannel.HlsCdnSettingsProperty.HlsMediaStoreSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlsmediastoresettings
            '''
            result = self._values.get("hls_media_store_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsMediaStoreSettingsProperty"]], result)

        @builtins.property
        def hls_s3_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsS3SettingsProperty"]]:
            '''``CfnChannel.HlsCdnSettingsProperty.HlsS3Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlss3settings
            '''
            result = self._values.get("hls_s3_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsS3SettingsProperty"]], result)

        @builtins.property
        def hls_webdav_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsWebdavSettingsProperty"]]:
            '''``CfnChannel.HlsCdnSettingsProperty.HlsWebdavSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlswebdavsettings
            '''
            result = self._values.get("hls_webdav_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsWebdavSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsCdnSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_markers": "adMarkers",
            "base_url_content": "baseUrlContent",
            "base_url_content1": "baseUrlContent1",
            "base_url_manifest": "baseUrlManifest",
            "base_url_manifest1": "baseUrlManifest1",
            "caption_language_mappings": "captionLanguageMappings",
            "caption_language_setting": "captionLanguageSetting",
            "client_cache": "clientCache",
            "codec_specification": "codecSpecification",
            "constant_iv": "constantIv",
            "destination": "destination",
            "directory_structure": "directoryStructure",
            "discontinuity_tags": "discontinuityTags",
            "encryption_type": "encryptionType",
            "hls_cdn_settings": "hlsCdnSettings",
            "hls_id3_segment_tagging": "hlsId3SegmentTagging",
            "i_frame_only_playlists": "iFrameOnlyPlaylists",
            "incomplete_segment_behavior": "incompleteSegmentBehavior",
            "index_n_segments": "indexNSegments",
            "input_loss_action": "inputLossAction",
            "iv_in_manifest": "ivInManifest",
            "iv_source": "ivSource",
            "keep_segments": "keepSegments",
            "key_format": "keyFormat",
            "key_format_versions": "keyFormatVersions",
            "key_provider_settings": "keyProviderSettings",
            "manifest_compression": "manifestCompression",
            "manifest_duration_format": "manifestDurationFormat",
            "min_segment_length": "minSegmentLength",
            "mode": "mode",
            "output_selection": "outputSelection",
            "program_date_time": "programDateTime",
            "program_date_time_period": "programDateTimePeriod",
            "redundant_manifest": "redundantManifest",
            "segmentation_mode": "segmentationMode",
            "segment_length": "segmentLength",
            "segments_per_subdirectory": "segmentsPerSubdirectory",
            "stream_inf_resolution": "streamInfResolution",
            "timed_metadata_id3_frame": "timedMetadataId3Frame",
            "timed_metadata_id3_period": "timedMetadataId3Period",
            "timestamp_delta_milliseconds": "timestampDeltaMilliseconds",
            "ts_file_mode": "tsFileMode",
        },
    )
    class HlsGroupSettingsProperty:
        def __init__(
            self,
            *,
            ad_markers: typing.Optional[typing.Sequence[builtins.str]] = None,
            base_url_content: typing.Optional[builtins.str] = None,
            base_url_content1: typing.Optional[builtins.str] = None,
            base_url_manifest: typing.Optional[builtins.str] = None,
            base_url_manifest1: typing.Optional[builtins.str] = None,
            caption_language_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionLanguageMappingProperty"]]]] = None,
            caption_language_setting: typing.Optional[builtins.str] = None,
            client_cache: typing.Optional[builtins.str] = None,
            codec_specification: typing.Optional[builtins.str] = None,
            constant_iv: typing.Optional[builtins.str] = None,
            destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]] = None,
            directory_structure: typing.Optional[builtins.str] = None,
            discontinuity_tags: typing.Optional[builtins.str] = None,
            encryption_type: typing.Optional[builtins.str] = None,
            hls_cdn_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsCdnSettingsProperty"]] = None,
            hls_id3_segment_tagging: typing.Optional[builtins.str] = None,
            i_frame_only_playlists: typing.Optional[builtins.str] = None,
            incomplete_segment_behavior: typing.Optional[builtins.str] = None,
            index_n_segments: typing.Optional[jsii.Number] = None,
            input_loss_action: typing.Optional[builtins.str] = None,
            iv_in_manifest: typing.Optional[builtins.str] = None,
            iv_source: typing.Optional[builtins.str] = None,
            keep_segments: typing.Optional[jsii.Number] = None,
            key_format: typing.Optional[builtins.str] = None,
            key_format_versions: typing.Optional[builtins.str] = None,
            key_provider_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.KeyProviderSettingsProperty"]] = None,
            manifest_compression: typing.Optional[builtins.str] = None,
            manifest_duration_format: typing.Optional[builtins.str] = None,
            min_segment_length: typing.Optional[jsii.Number] = None,
            mode: typing.Optional[builtins.str] = None,
            output_selection: typing.Optional[builtins.str] = None,
            program_date_time: typing.Optional[builtins.str] = None,
            program_date_time_period: typing.Optional[jsii.Number] = None,
            redundant_manifest: typing.Optional[builtins.str] = None,
            segmentation_mode: typing.Optional[builtins.str] = None,
            segment_length: typing.Optional[jsii.Number] = None,
            segments_per_subdirectory: typing.Optional[jsii.Number] = None,
            stream_inf_resolution: typing.Optional[builtins.str] = None,
            timed_metadata_id3_frame: typing.Optional[builtins.str] = None,
            timed_metadata_id3_period: typing.Optional[jsii.Number] = None,
            timestamp_delta_milliseconds: typing.Optional[jsii.Number] = None,
            ts_file_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param ad_markers: ``CfnChannel.HlsGroupSettingsProperty.AdMarkers``.
            :param base_url_content: ``CfnChannel.HlsGroupSettingsProperty.BaseUrlContent``.
            :param base_url_content1: ``CfnChannel.HlsGroupSettingsProperty.BaseUrlContent1``.
            :param base_url_manifest: ``CfnChannel.HlsGroupSettingsProperty.BaseUrlManifest``.
            :param base_url_manifest1: ``CfnChannel.HlsGroupSettingsProperty.BaseUrlManifest1``.
            :param caption_language_mappings: ``CfnChannel.HlsGroupSettingsProperty.CaptionLanguageMappings``.
            :param caption_language_setting: ``CfnChannel.HlsGroupSettingsProperty.CaptionLanguageSetting``.
            :param client_cache: ``CfnChannel.HlsGroupSettingsProperty.ClientCache``.
            :param codec_specification: ``CfnChannel.HlsGroupSettingsProperty.CodecSpecification``.
            :param constant_iv: ``CfnChannel.HlsGroupSettingsProperty.ConstantIv``.
            :param destination: ``CfnChannel.HlsGroupSettingsProperty.Destination``.
            :param directory_structure: ``CfnChannel.HlsGroupSettingsProperty.DirectoryStructure``.
            :param discontinuity_tags: ``CfnChannel.HlsGroupSettingsProperty.DiscontinuityTags``.
            :param encryption_type: ``CfnChannel.HlsGroupSettingsProperty.EncryptionType``.
            :param hls_cdn_settings: ``CfnChannel.HlsGroupSettingsProperty.HlsCdnSettings``.
            :param hls_id3_segment_tagging: ``CfnChannel.HlsGroupSettingsProperty.HlsId3SegmentTagging``.
            :param i_frame_only_playlists: ``CfnChannel.HlsGroupSettingsProperty.IFrameOnlyPlaylists``.
            :param incomplete_segment_behavior: ``CfnChannel.HlsGroupSettingsProperty.IncompleteSegmentBehavior``.
            :param index_n_segments: ``CfnChannel.HlsGroupSettingsProperty.IndexNSegments``.
            :param input_loss_action: ``CfnChannel.HlsGroupSettingsProperty.InputLossAction``.
            :param iv_in_manifest: ``CfnChannel.HlsGroupSettingsProperty.IvInManifest``.
            :param iv_source: ``CfnChannel.HlsGroupSettingsProperty.IvSource``.
            :param keep_segments: ``CfnChannel.HlsGroupSettingsProperty.KeepSegments``.
            :param key_format: ``CfnChannel.HlsGroupSettingsProperty.KeyFormat``.
            :param key_format_versions: ``CfnChannel.HlsGroupSettingsProperty.KeyFormatVersions``.
            :param key_provider_settings: ``CfnChannel.HlsGroupSettingsProperty.KeyProviderSettings``.
            :param manifest_compression: ``CfnChannel.HlsGroupSettingsProperty.ManifestCompression``.
            :param manifest_duration_format: ``CfnChannel.HlsGroupSettingsProperty.ManifestDurationFormat``.
            :param min_segment_length: ``CfnChannel.HlsGroupSettingsProperty.MinSegmentLength``.
            :param mode: ``CfnChannel.HlsGroupSettingsProperty.Mode``.
            :param output_selection: ``CfnChannel.HlsGroupSettingsProperty.OutputSelection``.
            :param program_date_time: ``CfnChannel.HlsGroupSettingsProperty.ProgramDateTime``.
            :param program_date_time_period: ``CfnChannel.HlsGroupSettingsProperty.ProgramDateTimePeriod``.
            :param redundant_manifest: ``CfnChannel.HlsGroupSettingsProperty.RedundantManifest``.
            :param segmentation_mode: ``CfnChannel.HlsGroupSettingsProperty.SegmentationMode``.
            :param segment_length: ``CfnChannel.HlsGroupSettingsProperty.SegmentLength``.
            :param segments_per_subdirectory: ``CfnChannel.HlsGroupSettingsProperty.SegmentsPerSubdirectory``.
            :param stream_inf_resolution: ``CfnChannel.HlsGroupSettingsProperty.StreamInfResolution``.
            :param timed_metadata_id3_frame: ``CfnChannel.HlsGroupSettingsProperty.TimedMetadataId3Frame``.
            :param timed_metadata_id3_period: ``CfnChannel.HlsGroupSettingsProperty.TimedMetadataId3Period``.
            :param timestamp_delta_milliseconds: ``CfnChannel.HlsGroupSettingsProperty.TimestampDeltaMilliseconds``.
            :param ts_file_mode: ``CfnChannel.HlsGroupSettingsProperty.TsFileMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_markers is not None:
                self._values["ad_markers"] = ad_markers
            if base_url_content is not None:
                self._values["base_url_content"] = base_url_content
            if base_url_content1 is not None:
                self._values["base_url_content1"] = base_url_content1
            if base_url_manifest is not None:
                self._values["base_url_manifest"] = base_url_manifest
            if base_url_manifest1 is not None:
                self._values["base_url_manifest1"] = base_url_manifest1
            if caption_language_mappings is not None:
                self._values["caption_language_mappings"] = caption_language_mappings
            if caption_language_setting is not None:
                self._values["caption_language_setting"] = caption_language_setting
            if client_cache is not None:
                self._values["client_cache"] = client_cache
            if codec_specification is not None:
                self._values["codec_specification"] = codec_specification
            if constant_iv is not None:
                self._values["constant_iv"] = constant_iv
            if destination is not None:
                self._values["destination"] = destination
            if directory_structure is not None:
                self._values["directory_structure"] = directory_structure
            if discontinuity_tags is not None:
                self._values["discontinuity_tags"] = discontinuity_tags
            if encryption_type is not None:
                self._values["encryption_type"] = encryption_type
            if hls_cdn_settings is not None:
                self._values["hls_cdn_settings"] = hls_cdn_settings
            if hls_id3_segment_tagging is not None:
                self._values["hls_id3_segment_tagging"] = hls_id3_segment_tagging
            if i_frame_only_playlists is not None:
                self._values["i_frame_only_playlists"] = i_frame_only_playlists
            if incomplete_segment_behavior is not None:
                self._values["incomplete_segment_behavior"] = incomplete_segment_behavior
            if index_n_segments is not None:
                self._values["index_n_segments"] = index_n_segments
            if input_loss_action is not None:
                self._values["input_loss_action"] = input_loss_action
            if iv_in_manifest is not None:
                self._values["iv_in_manifest"] = iv_in_manifest
            if iv_source is not None:
                self._values["iv_source"] = iv_source
            if keep_segments is not None:
                self._values["keep_segments"] = keep_segments
            if key_format is not None:
                self._values["key_format"] = key_format
            if key_format_versions is not None:
                self._values["key_format_versions"] = key_format_versions
            if key_provider_settings is not None:
                self._values["key_provider_settings"] = key_provider_settings
            if manifest_compression is not None:
                self._values["manifest_compression"] = manifest_compression
            if manifest_duration_format is not None:
                self._values["manifest_duration_format"] = manifest_duration_format
            if min_segment_length is not None:
                self._values["min_segment_length"] = min_segment_length
            if mode is not None:
                self._values["mode"] = mode
            if output_selection is not None:
                self._values["output_selection"] = output_selection
            if program_date_time is not None:
                self._values["program_date_time"] = program_date_time
            if program_date_time_period is not None:
                self._values["program_date_time_period"] = program_date_time_period
            if redundant_manifest is not None:
                self._values["redundant_manifest"] = redundant_manifest
            if segmentation_mode is not None:
                self._values["segmentation_mode"] = segmentation_mode
            if segment_length is not None:
                self._values["segment_length"] = segment_length
            if segments_per_subdirectory is not None:
                self._values["segments_per_subdirectory"] = segments_per_subdirectory
            if stream_inf_resolution is not None:
                self._values["stream_inf_resolution"] = stream_inf_resolution
            if timed_metadata_id3_frame is not None:
                self._values["timed_metadata_id3_frame"] = timed_metadata_id3_frame
            if timed_metadata_id3_period is not None:
                self._values["timed_metadata_id3_period"] = timed_metadata_id3_period
            if timestamp_delta_milliseconds is not None:
                self._values["timestamp_delta_milliseconds"] = timestamp_delta_milliseconds
            if ts_file_mode is not None:
                self._values["ts_file_mode"] = ts_file_mode

        @builtins.property
        def ad_markers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnChannel.HlsGroupSettingsProperty.AdMarkers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-admarkers
            '''
            result = self._values.get("ad_markers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def base_url_content(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.BaseUrlContent``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlcontent
            '''
            result = self._values.get("base_url_content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def base_url_content1(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.BaseUrlContent1``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlcontent1
            '''
            result = self._values.get("base_url_content1")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def base_url_manifest(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.BaseUrlManifest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlmanifest
            '''
            result = self._values.get("base_url_manifest")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def base_url_manifest1(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.BaseUrlManifest1``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlmanifest1
            '''
            result = self._values.get("base_url_manifest1")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def caption_language_mappings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionLanguageMappingProperty"]]]]:
            '''``CfnChannel.HlsGroupSettingsProperty.CaptionLanguageMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-captionlanguagemappings
            '''
            result = self._values.get("caption_language_mappings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionLanguageMappingProperty"]]]], result)

        @builtins.property
        def caption_language_setting(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.CaptionLanguageSetting``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-captionlanguagesetting
            '''
            result = self._values.get("caption_language_setting")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def client_cache(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.ClientCache``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-clientcache
            '''
            result = self._values.get("client_cache")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def codec_specification(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.CodecSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-codecspecification
            '''
            result = self._values.get("codec_specification")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constant_iv(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.ConstantIv``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-constantiv
            '''
            result = self._values.get("constant_iv")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]]:
            '''``CfnChannel.HlsGroupSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]], result)

        @builtins.property
        def directory_structure(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.DirectoryStructure``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-directorystructure
            '''
            result = self._values.get("directory_structure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def discontinuity_tags(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.DiscontinuityTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-discontinuitytags
            '''
            result = self._values.get("discontinuity_tags")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.EncryptionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-encryptiontype
            '''
            result = self._values.get("encryption_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hls_cdn_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsCdnSettingsProperty"]]:
            '''``CfnChannel.HlsGroupSettingsProperty.HlsCdnSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-hlscdnsettings
            '''
            result = self._values.get("hls_cdn_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsCdnSettingsProperty"]], result)

        @builtins.property
        def hls_id3_segment_tagging(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.HlsId3SegmentTagging``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-hlsid3segmenttagging
            '''
            result = self._values.get("hls_id3_segment_tagging")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def i_frame_only_playlists(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.IFrameOnlyPlaylists``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-iframeonlyplaylists
            '''
            result = self._values.get("i_frame_only_playlists")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def incomplete_segment_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.IncompleteSegmentBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-incompletesegmentbehavior
            '''
            result = self._values.get("incomplete_segment_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_n_segments(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsGroupSettingsProperty.IndexNSegments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-indexnsegments
            '''
            result = self._values.get("index_n_segments")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def input_loss_action(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.InputLossAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-inputlossaction
            '''
            result = self._values.get("input_loss_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iv_in_manifest(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.IvInManifest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-ivinmanifest
            '''
            result = self._values.get("iv_in_manifest")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iv_source(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.IvSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-ivsource
            '''
            result = self._values.get("iv_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def keep_segments(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsGroupSettingsProperty.KeepSegments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keepsegments
            '''
            result = self._values.get("keep_segments")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def key_format(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.KeyFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keyformat
            '''
            result = self._values.get("key_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_format_versions(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.KeyFormatVersions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keyformatversions
            '''
            result = self._values.get("key_format_versions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_provider_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.KeyProviderSettingsProperty"]]:
            '''``CfnChannel.HlsGroupSettingsProperty.KeyProviderSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keyprovidersettings
            '''
            result = self._values.get("key_provider_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.KeyProviderSettingsProperty"]], result)

        @builtins.property
        def manifest_compression(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.ManifestCompression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-manifestcompression
            '''
            result = self._values.get("manifest_compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manifest_duration_format(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.ManifestDurationFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-manifestdurationformat
            '''
            result = self._values.get("manifest_duration_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def min_segment_length(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsGroupSettingsProperty.MinSegmentLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-minsegmentlength
            '''
            result = self._values.get("min_segment_length")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_selection(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.OutputSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-outputselection
            '''
            result = self._values.get("output_selection")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def program_date_time(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.ProgramDateTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-programdatetime
            '''
            result = self._values.get("program_date_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def program_date_time_period(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsGroupSettingsProperty.ProgramDateTimePeriod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-programdatetimeperiod
            '''
            result = self._values.get("program_date_time_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def redundant_manifest(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.RedundantManifest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-redundantmanifest
            '''
            result = self._values.get("redundant_manifest")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segmentation_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.SegmentationMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-segmentationmode
            '''
            result = self._values.get("segmentation_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segment_length(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsGroupSettingsProperty.SegmentLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-segmentlength
            '''
            result = self._values.get("segment_length")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segments_per_subdirectory(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsGroupSettingsProperty.SegmentsPerSubdirectory``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-segmentspersubdirectory
            '''
            result = self._values.get("segments_per_subdirectory")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_inf_resolution(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.StreamInfResolution``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-streaminfresolution
            '''
            result = self._values.get("stream_inf_resolution")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timed_metadata_id3_frame(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.TimedMetadataId3Frame``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-timedmetadataid3frame
            '''
            result = self._values.get("timed_metadata_id3_frame")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timed_metadata_id3_period(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsGroupSettingsProperty.TimedMetadataId3Period``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-timedmetadataid3period
            '''
            result = self._values.get("timed_metadata_id3_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timestamp_delta_milliseconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsGroupSettingsProperty.TimestampDeltaMilliseconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-timestampdeltamilliseconds
            '''
            result = self._values.get("timestamp_delta_milliseconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ts_file_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsGroupSettingsProperty.TsFileMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-tsfilemode
            '''
            result = self._values.get("ts_file_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsInputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bandwidth": "bandwidth",
            "buffer_segments": "bufferSegments",
            "retries": "retries",
            "retry_interval": "retryInterval",
        },
    )
    class HlsInputSettingsProperty:
        def __init__(
            self,
            *,
            bandwidth: typing.Optional[jsii.Number] = None,
            buffer_segments: typing.Optional[jsii.Number] = None,
            retries: typing.Optional[jsii.Number] = None,
            retry_interval: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param bandwidth: ``CfnChannel.HlsInputSettingsProperty.Bandwidth``.
            :param buffer_segments: ``CfnChannel.HlsInputSettingsProperty.BufferSegments``.
            :param retries: ``CfnChannel.HlsInputSettingsProperty.Retries``.
            :param retry_interval: ``CfnChannel.HlsInputSettingsProperty.RetryInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if bandwidth is not None:
                self._values["bandwidth"] = bandwidth
            if buffer_segments is not None:
                self._values["buffer_segments"] = buffer_segments
            if retries is not None:
                self._values["retries"] = retries
            if retry_interval is not None:
                self._values["retry_interval"] = retry_interval

        @builtins.property
        def bandwidth(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsInputSettingsProperty.Bandwidth``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-bandwidth
            '''
            result = self._values.get("bandwidth")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def buffer_segments(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsInputSettingsProperty.BufferSegments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-buffersegments
            '''
            result = self._values.get("buffer_segments")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def retries(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsInputSettingsProperty.Retries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-retries
            '''
            result = self._values.get("retries")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def retry_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsInputSettingsProperty.RetryInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-retryinterval
            '''
            result = self._values.get("retry_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsInputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsMediaStoreSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_retry_interval": "connectionRetryInterval",
            "filecache_duration": "filecacheDuration",
            "media_store_storage_class": "mediaStoreStorageClass",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
        },
    )
    class HlsMediaStoreSettingsProperty:
        def __init__(
            self,
            *,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            media_store_storage_class: typing.Optional[builtins.str] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param connection_retry_interval: ``CfnChannel.HlsMediaStoreSettingsProperty.ConnectionRetryInterval``.
            :param filecache_duration: ``CfnChannel.HlsMediaStoreSettingsProperty.FilecacheDuration``.
            :param media_store_storage_class: ``CfnChannel.HlsMediaStoreSettingsProperty.MediaStoreStorageClass``.
            :param num_retries: ``CfnChannel.HlsMediaStoreSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.HlsMediaStoreSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if media_store_storage_class is not None:
                self._values["media_store_storage_class"] = media_store_storage_class
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsMediaStoreSettingsProperty.ConnectionRetryInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-connectionretryinterval
            '''
            result = self._values.get("connection_retry_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsMediaStoreSettingsProperty.FilecacheDuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-filecacheduration
            '''
            result = self._values.get("filecache_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def media_store_storage_class(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsMediaStoreSettingsProperty.MediaStoreStorageClass``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-mediastorestorageclass
            '''
            result = self._values.get("media_store_storage_class")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsMediaStoreSettingsProperty.NumRetries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-numretries
            '''
            result = self._values.get("num_retries")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsMediaStoreSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-restartdelay
            '''
            result = self._values.get("restart_delay")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsMediaStoreSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "h265_packaging_type": "h265PackagingType",
            "hls_settings": "hlsSettings",
            "name_modifier": "nameModifier",
            "segment_modifier": "segmentModifier",
        },
    )
    class HlsOutputSettingsProperty:
        def __init__(
            self,
            *,
            h265_packaging_type: typing.Optional[builtins.str] = None,
            hls_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsSettingsProperty"]] = None,
            name_modifier: typing.Optional[builtins.str] = None,
            segment_modifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param h265_packaging_type: ``CfnChannel.HlsOutputSettingsProperty.H265PackagingType``.
            :param hls_settings: ``CfnChannel.HlsOutputSettingsProperty.HlsSettings``.
            :param name_modifier: ``CfnChannel.HlsOutputSettingsProperty.NameModifier``.
            :param segment_modifier: ``CfnChannel.HlsOutputSettingsProperty.SegmentModifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if h265_packaging_type is not None:
                self._values["h265_packaging_type"] = h265_packaging_type
            if hls_settings is not None:
                self._values["hls_settings"] = hls_settings
            if name_modifier is not None:
                self._values["name_modifier"] = name_modifier
            if segment_modifier is not None:
                self._values["segment_modifier"] = segment_modifier

        @builtins.property
        def h265_packaging_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsOutputSettingsProperty.H265PackagingType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-h265packagingtype
            '''
            result = self._values.get("h265_packaging_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hls_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsSettingsProperty"]]:
            '''``CfnChannel.HlsOutputSettingsProperty.HlsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-hlssettings
            '''
            result = self._values.get("hls_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsSettingsProperty"]], result)

        @builtins.property
        def name_modifier(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsOutputSettingsProperty.NameModifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-namemodifier
            '''
            result = self._values.get("name_modifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segment_modifier(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsOutputSettingsProperty.SegmentModifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-segmentmodifier
            '''
            result = self._values.get("segment_modifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsS3SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"canned_acl": "cannedAcl"},
    )
    class HlsS3SettingsProperty:
        def __init__(self, *, canned_acl: typing.Optional[builtins.str] = None) -> None:
            '''
            :param canned_acl: ``CfnChannel.HlsS3SettingsProperty.CannedAcl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlss3settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if canned_acl is not None:
                self._values["canned_acl"] = canned_acl

        @builtins.property
        def canned_acl(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsS3SettingsProperty.CannedAcl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlss3settings.html#cfn-medialive-channel-hlss3settings-cannedacl
            '''
            result = self._values.get("canned_acl")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsS3SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_only_hls_settings": "audioOnlyHlsSettings",
            "fmp4_hls_settings": "fmp4HlsSettings",
            "frame_capture_hls_settings": "frameCaptureHlsSettings",
            "standard_hls_settings": "standardHlsSettings",
        },
    )
    class HlsSettingsProperty:
        def __init__(
            self,
            *,
            audio_only_hls_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioOnlyHlsSettingsProperty"]] = None,
            fmp4_hls_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Fmp4HlsSettingsProperty"]] = None,
            frame_capture_hls_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureHlsSettingsProperty"]] = None,
            standard_hls_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.StandardHlsSettingsProperty"]] = None,
        ) -> None:
            '''
            :param audio_only_hls_settings: ``CfnChannel.HlsSettingsProperty.AudioOnlyHlsSettings``.
            :param fmp4_hls_settings: ``CfnChannel.HlsSettingsProperty.Fmp4HlsSettings``.
            :param frame_capture_hls_settings: ``CfnChannel.HlsSettingsProperty.FrameCaptureHlsSettings``.
            :param standard_hls_settings: ``CfnChannel.HlsSettingsProperty.StandardHlsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_only_hls_settings is not None:
                self._values["audio_only_hls_settings"] = audio_only_hls_settings
            if fmp4_hls_settings is not None:
                self._values["fmp4_hls_settings"] = fmp4_hls_settings
            if frame_capture_hls_settings is not None:
                self._values["frame_capture_hls_settings"] = frame_capture_hls_settings
            if standard_hls_settings is not None:
                self._values["standard_hls_settings"] = standard_hls_settings

        @builtins.property
        def audio_only_hls_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioOnlyHlsSettingsProperty"]]:
            '''``CfnChannel.HlsSettingsProperty.AudioOnlyHlsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-audioonlyhlssettings
            '''
            result = self._values.get("audio_only_hls_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioOnlyHlsSettingsProperty"]], result)

        @builtins.property
        def fmp4_hls_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Fmp4HlsSettingsProperty"]]:
            '''``CfnChannel.HlsSettingsProperty.Fmp4HlsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-fmp4hlssettings
            '''
            result = self._values.get("fmp4_hls_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Fmp4HlsSettingsProperty"]], result)

        @builtins.property
        def frame_capture_hls_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureHlsSettingsProperty"]]:
            '''``CfnChannel.HlsSettingsProperty.FrameCaptureHlsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-framecapturehlssettings
            '''
            result = self._values.get("frame_capture_hls_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureHlsSettingsProperty"]], result)

        @builtins.property
        def standard_hls_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.StandardHlsSettingsProperty"]]:
            '''``CfnChannel.HlsSettingsProperty.StandardHlsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-standardhlssettings
            '''
            result = self._values.get("standard_hls_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.StandardHlsSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HlsWebdavSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_retry_interval": "connectionRetryInterval",
            "filecache_duration": "filecacheDuration",
            "http_transfer_mode": "httpTransferMode",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
        },
    )
    class HlsWebdavSettingsProperty:
        def __init__(
            self,
            *,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            http_transfer_mode: typing.Optional[builtins.str] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param connection_retry_interval: ``CfnChannel.HlsWebdavSettingsProperty.ConnectionRetryInterval``.
            :param filecache_duration: ``CfnChannel.HlsWebdavSettingsProperty.FilecacheDuration``.
            :param http_transfer_mode: ``CfnChannel.HlsWebdavSettingsProperty.HttpTransferMode``.
            :param num_retries: ``CfnChannel.HlsWebdavSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.HlsWebdavSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if http_transfer_mode is not None:
                self._values["http_transfer_mode"] = http_transfer_mode
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsWebdavSettingsProperty.ConnectionRetryInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-connectionretryinterval
            '''
            result = self._values.get("connection_retry_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsWebdavSettingsProperty.FilecacheDuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-filecacheduration
            '''
            result = self._values.get("filecache_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def http_transfer_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.HlsWebdavSettingsProperty.HttpTransferMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-httptransfermode
            '''
            result = self._values.get("http_transfer_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsWebdavSettingsProperty.NumRetries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-numretries
            '''
            result = self._values.get("num_retries")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.HlsWebdavSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-restartdelay
            '''
            result = self._values.get("restart_delay")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsWebdavSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.HtmlMotionGraphicsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class HtmlMotionGraphicsSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-htmlmotiongraphicssettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HtmlMotionGraphicsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.InputAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "automatic_input_failover_settings": "automaticInputFailoverSettings",
            "input_attachment_name": "inputAttachmentName",
            "input_id": "inputId",
            "input_settings": "inputSettings",
        },
    )
    class InputAttachmentProperty:
        def __init__(
            self,
            *,
            automatic_input_failover_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AutomaticInputFailoverSettingsProperty"]] = None,
            input_attachment_name: typing.Optional[builtins.str] = None,
            input_id: typing.Optional[builtins.str] = None,
            input_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputSettingsProperty"]] = None,
        ) -> None:
            '''
            :param automatic_input_failover_settings: ``CfnChannel.InputAttachmentProperty.AutomaticInputFailoverSettings``.
            :param input_attachment_name: ``CfnChannel.InputAttachmentProperty.InputAttachmentName``.
            :param input_id: ``CfnChannel.InputAttachmentProperty.InputId``.
            :param input_settings: ``CfnChannel.InputAttachmentProperty.InputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if automatic_input_failover_settings is not None:
                self._values["automatic_input_failover_settings"] = automatic_input_failover_settings
            if input_attachment_name is not None:
                self._values["input_attachment_name"] = input_attachment_name
            if input_id is not None:
                self._values["input_id"] = input_id
            if input_settings is not None:
                self._values["input_settings"] = input_settings

        @builtins.property
        def automatic_input_failover_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AutomaticInputFailoverSettingsProperty"]]:
            '''``CfnChannel.InputAttachmentProperty.AutomaticInputFailoverSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-automaticinputfailoversettings
            '''
            result = self._values.get("automatic_input_failover_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AutomaticInputFailoverSettingsProperty"]], result)

        @builtins.property
        def input_attachment_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputAttachmentProperty.InputAttachmentName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-inputattachmentname
            '''
            result = self._values.get("input_attachment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputAttachmentProperty.InputId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-inputid
            '''
            result = self._values.get("input_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputSettingsProperty"]]:
            '''``CfnChannel.InputAttachmentProperty.InputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-inputsettings
            '''
            result = self._values.get("input_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.InputChannelLevelProperty",
        jsii_struct_bases=[],
        name_mapping={"gain": "gain", "input_channel": "inputChannel"},
    )
    class InputChannelLevelProperty:
        def __init__(
            self,
            *,
            gain: typing.Optional[jsii.Number] = None,
            input_channel: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param gain: ``CfnChannel.InputChannelLevelProperty.Gain``.
            :param input_channel: ``CfnChannel.InputChannelLevelProperty.InputChannel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if gain is not None:
                self._values["gain"] = gain
            if input_channel is not None:
                self._values["input_channel"] = input_channel

        @builtins.property
        def gain(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.InputChannelLevelProperty.Gain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html#cfn-medialive-channel-inputchannellevel-gain
            '''
            result = self._values.get("gain")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def input_channel(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.InputChannelLevelProperty.InputChannel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html#cfn-medialive-channel-inputchannellevel-inputchannel
            '''
            result = self._values.get("input_channel")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputChannelLevelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.InputLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password_param": "passwordParam",
            "uri": "uri",
            "username": "username",
        },
    )
    class InputLocationProperty:
        def __init__(
            self,
            *,
            password_param: typing.Optional[builtins.str] = None,
            uri: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param password_param: ``CfnChannel.InputLocationProperty.PasswordParam``.
            :param uri: ``CfnChannel.InputLocationProperty.Uri``.
            :param username: ``CfnChannel.InputLocationProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if password_param is not None:
                self._values["password_param"] = password_param
            if uri is not None:
                self._values["uri"] = uri
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password_param(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputLocationProperty.PasswordParam``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html#cfn-medialive-channel-inputlocation-passwordparam
            '''
            result = self._values.get("password_param")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uri(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputLocationProperty.Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html#cfn-medialive-channel-inputlocation-uri
            '''
            result = self._values.get("uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputLocationProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html#cfn-medialive-channel-inputlocation-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.InputLossBehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "black_frame_msec": "blackFrameMsec",
            "input_loss_image_color": "inputLossImageColor",
            "input_loss_image_slate": "inputLossImageSlate",
            "input_loss_image_type": "inputLossImageType",
            "repeat_frame_msec": "repeatFrameMsec",
        },
    )
    class InputLossBehaviorProperty:
        def __init__(
            self,
            *,
            black_frame_msec: typing.Optional[jsii.Number] = None,
            input_loss_image_color: typing.Optional[builtins.str] = None,
            input_loss_image_slate: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]] = None,
            input_loss_image_type: typing.Optional[builtins.str] = None,
            repeat_frame_msec: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param black_frame_msec: ``CfnChannel.InputLossBehaviorProperty.BlackFrameMsec``.
            :param input_loss_image_color: ``CfnChannel.InputLossBehaviorProperty.InputLossImageColor``.
            :param input_loss_image_slate: ``CfnChannel.InputLossBehaviorProperty.InputLossImageSlate``.
            :param input_loss_image_type: ``CfnChannel.InputLossBehaviorProperty.InputLossImageType``.
            :param repeat_frame_msec: ``CfnChannel.InputLossBehaviorProperty.RepeatFrameMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if black_frame_msec is not None:
                self._values["black_frame_msec"] = black_frame_msec
            if input_loss_image_color is not None:
                self._values["input_loss_image_color"] = input_loss_image_color
            if input_loss_image_slate is not None:
                self._values["input_loss_image_slate"] = input_loss_image_slate
            if input_loss_image_type is not None:
                self._values["input_loss_image_type"] = input_loss_image_type
            if repeat_frame_msec is not None:
                self._values["repeat_frame_msec"] = repeat_frame_msec

        @builtins.property
        def black_frame_msec(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.InputLossBehaviorProperty.BlackFrameMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-blackframemsec
            '''
            result = self._values.get("black_frame_msec")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def input_loss_image_color(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputLossBehaviorProperty.InputLossImageColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-inputlossimagecolor
            '''
            result = self._values.get("input_loss_image_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_loss_image_slate(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]]:
            '''``CfnChannel.InputLossBehaviorProperty.InputLossImageSlate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-inputlossimageslate
            '''
            result = self._values.get("input_loss_image_slate")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]], result)

        @builtins.property
        def input_loss_image_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputLossBehaviorProperty.InputLossImageType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-inputlossimagetype
            '''
            result = self._values.get("input_loss_image_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def repeat_frame_msec(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.InputLossBehaviorProperty.RepeatFrameMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-repeatframemsec
            '''
            result = self._values.get("repeat_frame_msec")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputLossBehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.InputLossFailoverSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"input_loss_threshold_msec": "inputLossThresholdMsec"},
    )
    class InputLossFailoverSettingsProperty:
        def __init__(
            self,
            *,
            input_loss_threshold_msec: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param input_loss_threshold_msec: ``CfnChannel.InputLossFailoverSettingsProperty.InputLossThresholdMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossfailoversettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if input_loss_threshold_msec is not None:
                self._values["input_loss_threshold_msec"] = input_loss_threshold_msec

        @builtins.property
        def input_loss_threshold_msec(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.InputLossFailoverSettingsProperty.InputLossThresholdMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossfailoversettings.html#cfn-medialive-channel-inputlossfailoversettings-inputlossthresholdmsec
            '''
            result = self._values.get("input_loss_threshold_msec")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputLossFailoverSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.InputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_selectors": "audioSelectors",
            "caption_selectors": "captionSelectors",
            "deblock_filter": "deblockFilter",
            "denoise_filter": "denoiseFilter",
            "filter_strength": "filterStrength",
            "input_filter": "inputFilter",
            "network_input_settings": "networkInputSettings",
            "smpte2038_data_preference": "smpte2038DataPreference",
            "source_end_behavior": "sourceEndBehavior",
            "video_selector": "videoSelector",
        },
    )
    class InputSettingsProperty:
        def __init__(
            self,
            *,
            audio_selectors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioSelectorProperty"]]]] = None,
            caption_selectors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionSelectorProperty"]]]] = None,
            deblock_filter: typing.Optional[builtins.str] = None,
            denoise_filter: typing.Optional[builtins.str] = None,
            filter_strength: typing.Optional[jsii.Number] = None,
            input_filter: typing.Optional[builtins.str] = None,
            network_input_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.NetworkInputSettingsProperty"]] = None,
            smpte2038_data_preference: typing.Optional[builtins.str] = None,
            source_end_behavior: typing.Optional[builtins.str] = None,
            video_selector: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorProperty"]] = None,
        ) -> None:
            '''
            :param audio_selectors: ``CfnChannel.InputSettingsProperty.AudioSelectors``.
            :param caption_selectors: ``CfnChannel.InputSettingsProperty.CaptionSelectors``.
            :param deblock_filter: ``CfnChannel.InputSettingsProperty.DeblockFilter``.
            :param denoise_filter: ``CfnChannel.InputSettingsProperty.DenoiseFilter``.
            :param filter_strength: ``CfnChannel.InputSettingsProperty.FilterStrength``.
            :param input_filter: ``CfnChannel.InputSettingsProperty.InputFilter``.
            :param network_input_settings: ``CfnChannel.InputSettingsProperty.NetworkInputSettings``.
            :param smpte2038_data_preference: ``CfnChannel.InputSettingsProperty.Smpte2038DataPreference``.
            :param source_end_behavior: ``CfnChannel.InputSettingsProperty.SourceEndBehavior``.
            :param video_selector: ``CfnChannel.InputSettingsProperty.VideoSelector``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_selectors is not None:
                self._values["audio_selectors"] = audio_selectors
            if caption_selectors is not None:
                self._values["caption_selectors"] = caption_selectors
            if deblock_filter is not None:
                self._values["deblock_filter"] = deblock_filter
            if denoise_filter is not None:
                self._values["denoise_filter"] = denoise_filter
            if filter_strength is not None:
                self._values["filter_strength"] = filter_strength
            if input_filter is not None:
                self._values["input_filter"] = input_filter
            if network_input_settings is not None:
                self._values["network_input_settings"] = network_input_settings
            if smpte2038_data_preference is not None:
                self._values["smpte2038_data_preference"] = smpte2038_data_preference
            if source_end_behavior is not None:
                self._values["source_end_behavior"] = source_end_behavior
            if video_selector is not None:
                self._values["video_selector"] = video_selector

        @builtins.property
        def audio_selectors(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioSelectorProperty"]]]]:
            '''``CfnChannel.InputSettingsProperty.AudioSelectors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-audioselectors
            '''
            result = self._values.get("audio_selectors")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioSelectorProperty"]]]], result)

        @builtins.property
        def caption_selectors(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionSelectorProperty"]]]]:
            '''``CfnChannel.InputSettingsProperty.CaptionSelectors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-captionselectors
            '''
            result = self._values.get("caption_selectors")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionSelectorProperty"]]]], result)

        @builtins.property
        def deblock_filter(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputSettingsProperty.DeblockFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-deblockfilter
            '''
            result = self._values.get("deblock_filter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def denoise_filter(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputSettingsProperty.DenoiseFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-denoisefilter
            '''
            result = self._values.get("denoise_filter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def filter_strength(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.InputSettingsProperty.FilterStrength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-filterstrength
            '''
            result = self._values.get("filter_strength")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def input_filter(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputSettingsProperty.InputFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-inputfilter
            '''
            result = self._values.get("input_filter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def network_input_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.NetworkInputSettingsProperty"]]:
            '''``CfnChannel.InputSettingsProperty.NetworkInputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-networkinputsettings
            '''
            result = self._values.get("network_input_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.NetworkInputSettingsProperty"]], result)

        @builtins.property
        def smpte2038_data_preference(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputSettingsProperty.Smpte2038DataPreference``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-smpte2038datapreference
            '''
            result = self._values.get("smpte2038_data_preference")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_end_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputSettingsProperty.SourceEndBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-sourceendbehavior
            '''
            result = self._values.get("source_end_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def video_selector(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorProperty"]]:
            '''``CfnChannel.InputSettingsProperty.VideoSelector``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-videoselector
            '''
            result = self._values.get("video_selector")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.InputSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "codec": "codec",
            "maximum_bitrate": "maximumBitrate",
            "resolution": "resolution",
        },
    )
    class InputSpecificationProperty:
        def __init__(
            self,
            *,
            codec: typing.Optional[builtins.str] = None,
            maximum_bitrate: typing.Optional[builtins.str] = None,
            resolution: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param codec: ``CfnChannel.InputSpecificationProperty.Codec``.
            :param maximum_bitrate: ``CfnChannel.InputSpecificationProperty.MaximumBitrate``.
            :param resolution: ``CfnChannel.InputSpecificationProperty.Resolution``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if codec is not None:
                self._values["codec"] = codec
            if maximum_bitrate is not None:
                self._values["maximum_bitrate"] = maximum_bitrate
            if resolution is not None:
                self._values["resolution"] = resolution

        @builtins.property
        def codec(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputSpecificationProperty.Codec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html#cfn-medialive-channel-inputspecification-codec
            '''
            result = self._values.get("codec")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def maximum_bitrate(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputSpecificationProperty.MaximumBitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html#cfn-medialive-channel-inputspecification-maximumbitrate
            '''
            result = self._values.get("maximum_bitrate")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resolution(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.InputSpecificationProperty.Resolution``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html#cfn-medialive-channel-inputspecification-resolution
            '''
            result = self._values.get("resolution")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.KeyProviderSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"static_key_settings": "staticKeySettings"},
    )
    class KeyProviderSettingsProperty:
        def __init__(
            self,
            *,
            static_key_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.StaticKeySettingsProperty"]] = None,
        ) -> None:
            '''
            :param static_key_settings: ``CfnChannel.KeyProviderSettingsProperty.StaticKeySettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if static_key_settings is not None:
                self._values["static_key_settings"] = static_key_settings

        @builtins.property
        def static_key_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.StaticKeySettingsProperty"]]:
            '''``CfnChannel.KeyProviderSettingsProperty.StaticKeySettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html#cfn-medialive-channel-keyprovidersettings-statickeysettings
            '''
            result = self._values.get("static_key_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.StaticKeySettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyProviderSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.M2tsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "absent_input_audio_behavior": "absentInputAudioBehavior",
            "arib": "arib",
            "arib_captions_pid": "aribCaptionsPid",
            "arib_captions_pid_control": "aribCaptionsPidControl",
            "audio_buffer_model": "audioBufferModel",
            "audio_frames_per_pes": "audioFramesPerPes",
            "audio_pids": "audioPids",
            "audio_stream_type": "audioStreamType",
            "bitrate": "bitrate",
            "buffer_model": "bufferModel",
            "cc_descriptor": "ccDescriptor",
            "dvb_nit_settings": "dvbNitSettings",
            "dvb_sdt_settings": "dvbSdtSettings",
            "dvb_sub_pids": "dvbSubPids",
            "dvb_tdt_settings": "dvbTdtSettings",
            "dvb_teletext_pid": "dvbTeletextPid",
            "ebif": "ebif",
            "ebp_audio_interval": "ebpAudioInterval",
            "ebp_lookahead_ms": "ebpLookaheadMs",
            "ebp_placement": "ebpPlacement",
            "ecm_pid": "ecmPid",
            "es_rate_in_pes": "esRateInPes",
            "etv_platform_pid": "etvPlatformPid",
            "etv_signal_pid": "etvSignalPid",
            "fragment_time": "fragmentTime",
            "klv": "klv",
            "klv_data_pids": "klvDataPids",
            "nielsen_id3_behavior": "nielsenId3Behavior",
            "null_packet_bitrate": "nullPacketBitrate",
            "pat_interval": "patInterval",
            "pcr_control": "pcrControl",
            "pcr_period": "pcrPeriod",
            "pcr_pid": "pcrPid",
            "pmt_interval": "pmtInterval",
            "pmt_pid": "pmtPid",
            "program_num": "programNum",
            "rate_mode": "rateMode",
            "scte27_pids": "scte27Pids",
            "scte35_control": "scte35Control",
            "scte35_pid": "scte35Pid",
            "segmentation_markers": "segmentationMarkers",
            "segmentation_style": "segmentationStyle",
            "segmentation_time": "segmentationTime",
            "timed_metadata_behavior": "timedMetadataBehavior",
            "timed_metadata_pid": "timedMetadataPid",
            "transport_stream_id": "transportStreamId",
            "video_pid": "videoPid",
        },
    )
    class M2tsSettingsProperty:
        def __init__(
            self,
            *,
            absent_input_audio_behavior: typing.Optional[builtins.str] = None,
            arib: typing.Optional[builtins.str] = None,
            arib_captions_pid: typing.Optional[builtins.str] = None,
            arib_captions_pid_control: typing.Optional[builtins.str] = None,
            audio_buffer_model: typing.Optional[builtins.str] = None,
            audio_frames_per_pes: typing.Optional[jsii.Number] = None,
            audio_pids: typing.Optional[builtins.str] = None,
            audio_stream_type: typing.Optional[builtins.str] = None,
            bitrate: typing.Optional[jsii.Number] = None,
            buffer_model: typing.Optional[builtins.str] = None,
            cc_descriptor: typing.Optional[builtins.str] = None,
            dvb_nit_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbNitSettingsProperty"]] = None,
            dvb_sdt_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbSdtSettingsProperty"]] = None,
            dvb_sub_pids: typing.Optional[builtins.str] = None,
            dvb_tdt_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbTdtSettingsProperty"]] = None,
            dvb_teletext_pid: typing.Optional[builtins.str] = None,
            ebif: typing.Optional[builtins.str] = None,
            ebp_audio_interval: typing.Optional[builtins.str] = None,
            ebp_lookahead_ms: typing.Optional[jsii.Number] = None,
            ebp_placement: typing.Optional[builtins.str] = None,
            ecm_pid: typing.Optional[builtins.str] = None,
            es_rate_in_pes: typing.Optional[builtins.str] = None,
            etv_platform_pid: typing.Optional[builtins.str] = None,
            etv_signal_pid: typing.Optional[builtins.str] = None,
            fragment_time: typing.Optional[jsii.Number] = None,
            klv: typing.Optional[builtins.str] = None,
            klv_data_pids: typing.Optional[builtins.str] = None,
            nielsen_id3_behavior: typing.Optional[builtins.str] = None,
            null_packet_bitrate: typing.Optional[jsii.Number] = None,
            pat_interval: typing.Optional[jsii.Number] = None,
            pcr_control: typing.Optional[builtins.str] = None,
            pcr_period: typing.Optional[jsii.Number] = None,
            pcr_pid: typing.Optional[builtins.str] = None,
            pmt_interval: typing.Optional[jsii.Number] = None,
            pmt_pid: typing.Optional[builtins.str] = None,
            program_num: typing.Optional[jsii.Number] = None,
            rate_mode: typing.Optional[builtins.str] = None,
            scte27_pids: typing.Optional[builtins.str] = None,
            scte35_control: typing.Optional[builtins.str] = None,
            scte35_pid: typing.Optional[builtins.str] = None,
            segmentation_markers: typing.Optional[builtins.str] = None,
            segmentation_style: typing.Optional[builtins.str] = None,
            segmentation_time: typing.Optional[jsii.Number] = None,
            timed_metadata_behavior: typing.Optional[builtins.str] = None,
            timed_metadata_pid: typing.Optional[builtins.str] = None,
            transport_stream_id: typing.Optional[jsii.Number] = None,
            video_pid: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param absent_input_audio_behavior: ``CfnChannel.M2tsSettingsProperty.AbsentInputAudioBehavior``.
            :param arib: ``CfnChannel.M2tsSettingsProperty.Arib``.
            :param arib_captions_pid: ``CfnChannel.M2tsSettingsProperty.AribCaptionsPid``.
            :param arib_captions_pid_control: ``CfnChannel.M2tsSettingsProperty.AribCaptionsPidControl``.
            :param audio_buffer_model: ``CfnChannel.M2tsSettingsProperty.AudioBufferModel``.
            :param audio_frames_per_pes: ``CfnChannel.M2tsSettingsProperty.AudioFramesPerPes``.
            :param audio_pids: ``CfnChannel.M2tsSettingsProperty.AudioPids``.
            :param audio_stream_type: ``CfnChannel.M2tsSettingsProperty.AudioStreamType``.
            :param bitrate: ``CfnChannel.M2tsSettingsProperty.Bitrate``.
            :param buffer_model: ``CfnChannel.M2tsSettingsProperty.BufferModel``.
            :param cc_descriptor: ``CfnChannel.M2tsSettingsProperty.CcDescriptor``.
            :param dvb_nit_settings: ``CfnChannel.M2tsSettingsProperty.DvbNitSettings``.
            :param dvb_sdt_settings: ``CfnChannel.M2tsSettingsProperty.DvbSdtSettings``.
            :param dvb_sub_pids: ``CfnChannel.M2tsSettingsProperty.DvbSubPids``.
            :param dvb_tdt_settings: ``CfnChannel.M2tsSettingsProperty.DvbTdtSettings``.
            :param dvb_teletext_pid: ``CfnChannel.M2tsSettingsProperty.DvbTeletextPid``.
            :param ebif: ``CfnChannel.M2tsSettingsProperty.Ebif``.
            :param ebp_audio_interval: ``CfnChannel.M2tsSettingsProperty.EbpAudioInterval``.
            :param ebp_lookahead_ms: ``CfnChannel.M2tsSettingsProperty.EbpLookaheadMs``.
            :param ebp_placement: ``CfnChannel.M2tsSettingsProperty.EbpPlacement``.
            :param ecm_pid: ``CfnChannel.M2tsSettingsProperty.EcmPid``.
            :param es_rate_in_pes: ``CfnChannel.M2tsSettingsProperty.EsRateInPes``.
            :param etv_platform_pid: ``CfnChannel.M2tsSettingsProperty.EtvPlatformPid``.
            :param etv_signal_pid: ``CfnChannel.M2tsSettingsProperty.EtvSignalPid``.
            :param fragment_time: ``CfnChannel.M2tsSettingsProperty.FragmentTime``.
            :param klv: ``CfnChannel.M2tsSettingsProperty.Klv``.
            :param klv_data_pids: ``CfnChannel.M2tsSettingsProperty.KlvDataPids``.
            :param nielsen_id3_behavior: ``CfnChannel.M2tsSettingsProperty.NielsenId3Behavior``.
            :param null_packet_bitrate: ``CfnChannel.M2tsSettingsProperty.NullPacketBitrate``.
            :param pat_interval: ``CfnChannel.M2tsSettingsProperty.PatInterval``.
            :param pcr_control: ``CfnChannel.M2tsSettingsProperty.PcrControl``.
            :param pcr_period: ``CfnChannel.M2tsSettingsProperty.PcrPeriod``.
            :param pcr_pid: ``CfnChannel.M2tsSettingsProperty.PcrPid``.
            :param pmt_interval: ``CfnChannel.M2tsSettingsProperty.PmtInterval``.
            :param pmt_pid: ``CfnChannel.M2tsSettingsProperty.PmtPid``.
            :param program_num: ``CfnChannel.M2tsSettingsProperty.ProgramNum``.
            :param rate_mode: ``CfnChannel.M2tsSettingsProperty.RateMode``.
            :param scte27_pids: ``CfnChannel.M2tsSettingsProperty.Scte27Pids``.
            :param scte35_control: ``CfnChannel.M2tsSettingsProperty.Scte35Control``.
            :param scte35_pid: ``CfnChannel.M2tsSettingsProperty.Scte35Pid``.
            :param segmentation_markers: ``CfnChannel.M2tsSettingsProperty.SegmentationMarkers``.
            :param segmentation_style: ``CfnChannel.M2tsSettingsProperty.SegmentationStyle``.
            :param segmentation_time: ``CfnChannel.M2tsSettingsProperty.SegmentationTime``.
            :param timed_metadata_behavior: ``CfnChannel.M2tsSettingsProperty.TimedMetadataBehavior``.
            :param timed_metadata_pid: ``CfnChannel.M2tsSettingsProperty.TimedMetadataPid``.
            :param transport_stream_id: ``CfnChannel.M2tsSettingsProperty.TransportStreamId``.
            :param video_pid: ``CfnChannel.M2tsSettingsProperty.VideoPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if absent_input_audio_behavior is not None:
                self._values["absent_input_audio_behavior"] = absent_input_audio_behavior
            if arib is not None:
                self._values["arib"] = arib
            if arib_captions_pid is not None:
                self._values["arib_captions_pid"] = arib_captions_pid
            if arib_captions_pid_control is not None:
                self._values["arib_captions_pid_control"] = arib_captions_pid_control
            if audio_buffer_model is not None:
                self._values["audio_buffer_model"] = audio_buffer_model
            if audio_frames_per_pes is not None:
                self._values["audio_frames_per_pes"] = audio_frames_per_pes
            if audio_pids is not None:
                self._values["audio_pids"] = audio_pids
            if audio_stream_type is not None:
                self._values["audio_stream_type"] = audio_stream_type
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if buffer_model is not None:
                self._values["buffer_model"] = buffer_model
            if cc_descriptor is not None:
                self._values["cc_descriptor"] = cc_descriptor
            if dvb_nit_settings is not None:
                self._values["dvb_nit_settings"] = dvb_nit_settings
            if dvb_sdt_settings is not None:
                self._values["dvb_sdt_settings"] = dvb_sdt_settings
            if dvb_sub_pids is not None:
                self._values["dvb_sub_pids"] = dvb_sub_pids
            if dvb_tdt_settings is not None:
                self._values["dvb_tdt_settings"] = dvb_tdt_settings
            if dvb_teletext_pid is not None:
                self._values["dvb_teletext_pid"] = dvb_teletext_pid
            if ebif is not None:
                self._values["ebif"] = ebif
            if ebp_audio_interval is not None:
                self._values["ebp_audio_interval"] = ebp_audio_interval
            if ebp_lookahead_ms is not None:
                self._values["ebp_lookahead_ms"] = ebp_lookahead_ms
            if ebp_placement is not None:
                self._values["ebp_placement"] = ebp_placement
            if ecm_pid is not None:
                self._values["ecm_pid"] = ecm_pid
            if es_rate_in_pes is not None:
                self._values["es_rate_in_pes"] = es_rate_in_pes
            if etv_platform_pid is not None:
                self._values["etv_platform_pid"] = etv_platform_pid
            if etv_signal_pid is not None:
                self._values["etv_signal_pid"] = etv_signal_pid
            if fragment_time is not None:
                self._values["fragment_time"] = fragment_time
            if klv is not None:
                self._values["klv"] = klv
            if klv_data_pids is not None:
                self._values["klv_data_pids"] = klv_data_pids
            if nielsen_id3_behavior is not None:
                self._values["nielsen_id3_behavior"] = nielsen_id3_behavior
            if null_packet_bitrate is not None:
                self._values["null_packet_bitrate"] = null_packet_bitrate
            if pat_interval is not None:
                self._values["pat_interval"] = pat_interval
            if pcr_control is not None:
                self._values["pcr_control"] = pcr_control
            if pcr_period is not None:
                self._values["pcr_period"] = pcr_period
            if pcr_pid is not None:
                self._values["pcr_pid"] = pcr_pid
            if pmt_interval is not None:
                self._values["pmt_interval"] = pmt_interval
            if pmt_pid is not None:
                self._values["pmt_pid"] = pmt_pid
            if program_num is not None:
                self._values["program_num"] = program_num
            if rate_mode is not None:
                self._values["rate_mode"] = rate_mode
            if scte27_pids is not None:
                self._values["scte27_pids"] = scte27_pids
            if scte35_control is not None:
                self._values["scte35_control"] = scte35_control
            if scte35_pid is not None:
                self._values["scte35_pid"] = scte35_pid
            if segmentation_markers is not None:
                self._values["segmentation_markers"] = segmentation_markers
            if segmentation_style is not None:
                self._values["segmentation_style"] = segmentation_style
            if segmentation_time is not None:
                self._values["segmentation_time"] = segmentation_time
            if timed_metadata_behavior is not None:
                self._values["timed_metadata_behavior"] = timed_metadata_behavior
            if timed_metadata_pid is not None:
                self._values["timed_metadata_pid"] = timed_metadata_pid
            if transport_stream_id is not None:
                self._values["transport_stream_id"] = transport_stream_id
            if video_pid is not None:
                self._values["video_pid"] = video_pid

        @builtins.property
        def absent_input_audio_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.AbsentInputAudioBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-absentinputaudiobehavior
            '''
            result = self._values.get("absent_input_audio_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def arib(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.Arib``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-arib
            '''
            result = self._values.get("arib")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def arib_captions_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.AribCaptionsPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-aribcaptionspid
            '''
            result = self._values.get("arib_captions_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def arib_captions_pid_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.AribCaptionsPidControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-aribcaptionspidcontrol
            '''
            result = self._values.get("arib_captions_pid_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def audio_buffer_model(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.AudioBufferModel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audiobuffermodel
            '''
            result = self._values.get("audio_buffer_model")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def audio_frames_per_pes(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.AudioFramesPerPes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audioframesperpes
            '''
            result = self._values.get("audio_frames_per_pes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def audio_pids(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.AudioPids``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audiopids
            '''
            result = self._values.get("audio_pids")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def audio_stream_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.AudioStreamType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audiostreamtype
            '''
            result = self._values.get("audio_stream_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.Bitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-bitrate
            '''
            result = self._values.get("bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def buffer_model(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.BufferModel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-buffermodel
            '''
            result = self._values.get("buffer_model")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cc_descriptor(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.CcDescriptor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ccdescriptor
            '''
            result = self._values.get("cc_descriptor")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dvb_nit_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbNitSettingsProperty"]]:
            '''``CfnChannel.M2tsSettingsProperty.DvbNitSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbnitsettings
            '''
            result = self._values.get("dvb_nit_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbNitSettingsProperty"]], result)

        @builtins.property
        def dvb_sdt_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbSdtSettingsProperty"]]:
            '''``CfnChannel.M2tsSettingsProperty.DvbSdtSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbsdtsettings
            '''
            result = self._values.get("dvb_sdt_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbSdtSettingsProperty"]], result)

        @builtins.property
        def dvb_sub_pids(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.DvbSubPids``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbsubpids
            '''
            result = self._values.get("dvb_sub_pids")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dvb_tdt_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbTdtSettingsProperty"]]:
            '''``CfnChannel.M2tsSettingsProperty.DvbTdtSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbtdtsettings
            '''
            result = self._values.get("dvb_tdt_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.DvbTdtSettingsProperty"]], result)

        @builtins.property
        def dvb_teletext_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.DvbTeletextPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbteletextpid
            '''
            result = self._values.get("dvb_teletext_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebif(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.Ebif``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebif
            '''
            result = self._values.get("ebif")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebp_audio_interval(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.EbpAudioInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebpaudiointerval
            '''
            result = self._values.get("ebp_audio_interval")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebp_lookahead_ms(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.EbpLookaheadMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebplookaheadms
            '''
            result = self._values.get("ebp_lookahead_ms")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ebp_placement(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.EbpPlacement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebpplacement
            '''
            result = self._values.get("ebp_placement")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ecm_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.EcmPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ecmpid
            '''
            result = self._values.get("ecm_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def es_rate_in_pes(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.EsRateInPes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-esrateinpes
            '''
            result = self._values.get("es_rate_in_pes")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def etv_platform_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.EtvPlatformPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-etvplatformpid
            '''
            result = self._values.get("etv_platform_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def etv_signal_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.EtvSignalPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-etvsignalpid
            '''
            result = self._values.get("etv_signal_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fragment_time(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.FragmentTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-fragmenttime
            '''
            result = self._values.get("fragment_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def klv(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.Klv``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-klv
            '''
            result = self._values.get("klv")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def klv_data_pids(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.KlvDataPids``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-klvdatapids
            '''
            result = self._values.get("klv_data_pids")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def nielsen_id3_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.NielsenId3Behavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-nielsenid3behavior
            '''
            result = self._values.get("nielsen_id3_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def null_packet_bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.NullPacketBitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-nullpacketbitrate
            '''
            result = self._values.get("null_packet_bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pat_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.PatInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-patinterval
            '''
            result = self._values.get("pat_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pcr_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.PcrControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pcrcontrol
            '''
            result = self._values.get("pcr_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pcr_period(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.PcrPeriod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pcrperiod
            '''
            result = self._values.get("pcr_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pcr_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.PcrPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pcrpid
            '''
            result = self._values.get("pcr_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pmt_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.PmtInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pmtinterval
            '''
            result = self._values.get("pmt_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pmt_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.PmtPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pmtpid
            '''
            result = self._values.get("pmt_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def program_num(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.ProgramNum``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-programnum
            '''
            result = self._values.get("program_num")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rate_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.RateMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ratemode
            '''
            result = self._values.get("rate_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scte27_pids(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.Scte27Pids``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte27pids
            '''
            result = self._values.get("scte27_pids")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scte35_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.Scte35Control``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte35control
            '''
            result = self._values.get("scte35_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scte35_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.Scte35Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte35pid
            '''
            result = self._values.get("scte35_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segmentation_markers(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.SegmentationMarkers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-segmentationmarkers
            '''
            result = self._values.get("segmentation_markers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segmentation_style(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.SegmentationStyle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-segmentationstyle
            '''
            result = self._values.get("segmentation_style")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segmentation_time(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.SegmentationTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-segmentationtime
            '''
            result = self._values.get("segmentation_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timed_metadata_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.TimedMetadataBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-timedmetadatabehavior
            '''
            result = self._values.get("timed_metadata_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timed_metadata_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.TimedMetadataPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-timedmetadatapid
            '''
            result = self._values.get("timed_metadata_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def transport_stream_id(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M2tsSettingsProperty.TransportStreamId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-transportstreamid
            '''
            result = self._values.get("transport_stream_id")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def video_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M2tsSettingsProperty.VideoPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-videopid
            '''
            result = self._values.get("video_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "M2tsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.M3u8SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_frames_per_pes": "audioFramesPerPes",
            "audio_pids": "audioPids",
            "ecm_pid": "ecmPid",
            "nielsen_id3_behavior": "nielsenId3Behavior",
            "pat_interval": "patInterval",
            "pcr_control": "pcrControl",
            "pcr_period": "pcrPeriod",
            "pcr_pid": "pcrPid",
            "pmt_interval": "pmtInterval",
            "pmt_pid": "pmtPid",
            "program_num": "programNum",
            "scte35_behavior": "scte35Behavior",
            "scte35_pid": "scte35Pid",
            "timed_metadata_behavior": "timedMetadataBehavior",
            "timed_metadata_pid": "timedMetadataPid",
            "transport_stream_id": "transportStreamId",
            "video_pid": "videoPid",
        },
    )
    class M3u8SettingsProperty:
        def __init__(
            self,
            *,
            audio_frames_per_pes: typing.Optional[jsii.Number] = None,
            audio_pids: typing.Optional[builtins.str] = None,
            ecm_pid: typing.Optional[builtins.str] = None,
            nielsen_id3_behavior: typing.Optional[builtins.str] = None,
            pat_interval: typing.Optional[jsii.Number] = None,
            pcr_control: typing.Optional[builtins.str] = None,
            pcr_period: typing.Optional[jsii.Number] = None,
            pcr_pid: typing.Optional[builtins.str] = None,
            pmt_interval: typing.Optional[jsii.Number] = None,
            pmt_pid: typing.Optional[builtins.str] = None,
            program_num: typing.Optional[jsii.Number] = None,
            scte35_behavior: typing.Optional[builtins.str] = None,
            scte35_pid: typing.Optional[builtins.str] = None,
            timed_metadata_behavior: typing.Optional[builtins.str] = None,
            timed_metadata_pid: typing.Optional[builtins.str] = None,
            transport_stream_id: typing.Optional[jsii.Number] = None,
            video_pid: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param audio_frames_per_pes: ``CfnChannel.M3u8SettingsProperty.AudioFramesPerPes``.
            :param audio_pids: ``CfnChannel.M3u8SettingsProperty.AudioPids``.
            :param ecm_pid: ``CfnChannel.M3u8SettingsProperty.EcmPid``.
            :param nielsen_id3_behavior: ``CfnChannel.M3u8SettingsProperty.NielsenId3Behavior``.
            :param pat_interval: ``CfnChannel.M3u8SettingsProperty.PatInterval``.
            :param pcr_control: ``CfnChannel.M3u8SettingsProperty.PcrControl``.
            :param pcr_period: ``CfnChannel.M3u8SettingsProperty.PcrPeriod``.
            :param pcr_pid: ``CfnChannel.M3u8SettingsProperty.PcrPid``.
            :param pmt_interval: ``CfnChannel.M3u8SettingsProperty.PmtInterval``.
            :param pmt_pid: ``CfnChannel.M3u8SettingsProperty.PmtPid``.
            :param program_num: ``CfnChannel.M3u8SettingsProperty.ProgramNum``.
            :param scte35_behavior: ``CfnChannel.M3u8SettingsProperty.Scte35Behavior``.
            :param scte35_pid: ``CfnChannel.M3u8SettingsProperty.Scte35Pid``.
            :param timed_metadata_behavior: ``CfnChannel.M3u8SettingsProperty.TimedMetadataBehavior``.
            :param timed_metadata_pid: ``CfnChannel.M3u8SettingsProperty.TimedMetadataPid``.
            :param transport_stream_id: ``CfnChannel.M3u8SettingsProperty.TransportStreamId``.
            :param video_pid: ``CfnChannel.M3u8SettingsProperty.VideoPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_frames_per_pes is not None:
                self._values["audio_frames_per_pes"] = audio_frames_per_pes
            if audio_pids is not None:
                self._values["audio_pids"] = audio_pids
            if ecm_pid is not None:
                self._values["ecm_pid"] = ecm_pid
            if nielsen_id3_behavior is not None:
                self._values["nielsen_id3_behavior"] = nielsen_id3_behavior
            if pat_interval is not None:
                self._values["pat_interval"] = pat_interval
            if pcr_control is not None:
                self._values["pcr_control"] = pcr_control
            if pcr_period is not None:
                self._values["pcr_period"] = pcr_period
            if pcr_pid is not None:
                self._values["pcr_pid"] = pcr_pid
            if pmt_interval is not None:
                self._values["pmt_interval"] = pmt_interval
            if pmt_pid is not None:
                self._values["pmt_pid"] = pmt_pid
            if program_num is not None:
                self._values["program_num"] = program_num
            if scte35_behavior is not None:
                self._values["scte35_behavior"] = scte35_behavior
            if scte35_pid is not None:
                self._values["scte35_pid"] = scte35_pid
            if timed_metadata_behavior is not None:
                self._values["timed_metadata_behavior"] = timed_metadata_behavior
            if timed_metadata_pid is not None:
                self._values["timed_metadata_pid"] = timed_metadata_pid
            if transport_stream_id is not None:
                self._values["transport_stream_id"] = transport_stream_id
            if video_pid is not None:
                self._values["video_pid"] = video_pid

        @builtins.property
        def audio_frames_per_pes(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M3u8SettingsProperty.AudioFramesPerPes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-audioframesperpes
            '''
            result = self._values.get("audio_frames_per_pes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def audio_pids(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.AudioPids``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-audiopids
            '''
            result = self._values.get("audio_pids")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ecm_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.EcmPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-ecmpid
            '''
            result = self._values.get("ecm_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def nielsen_id3_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.NielsenId3Behavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-nielsenid3behavior
            '''
            result = self._values.get("nielsen_id3_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pat_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M3u8SettingsProperty.PatInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-patinterval
            '''
            result = self._values.get("pat_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pcr_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.PcrControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pcrcontrol
            '''
            result = self._values.get("pcr_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pcr_period(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M3u8SettingsProperty.PcrPeriod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pcrperiod
            '''
            result = self._values.get("pcr_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pcr_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.PcrPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pcrpid
            '''
            result = self._values.get("pcr_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pmt_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M3u8SettingsProperty.PmtInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pmtinterval
            '''
            result = self._values.get("pmt_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pmt_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.PmtPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pmtpid
            '''
            result = self._values.get("pmt_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def program_num(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M3u8SettingsProperty.ProgramNum``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-programnum
            '''
            result = self._values.get("program_num")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scte35_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.Scte35Behavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-scte35behavior
            '''
            result = self._values.get("scte35_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scte35_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.Scte35Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-scte35pid
            '''
            result = self._values.get("scte35_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timed_metadata_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.TimedMetadataBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-timedmetadatabehavior
            '''
            result = self._values.get("timed_metadata_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timed_metadata_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.TimedMetadataPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-timedmetadatapid
            '''
            result = self._values.get("timed_metadata_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def transport_stream_id(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.M3u8SettingsProperty.TransportStreamId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-transportstreamid
            '''
            result = self._values.get("transport_stream_id")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def video_pid(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.M3u8SettingsProperty.VideoPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-videopid
            '''
            result = self._values.get("video_pid")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "M3u8SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MediaPackageGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination"},
    )
    class MediaPackageGroupSettingsProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]] = None,
        ) -> None:
            '''
            :param destination: ``CfnChannel.MediaPackageGroupSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]]:
            '''``CfnChannel.MediaPackageGroupSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html#cfn-medialive-channel-mediapackagegroupsettings-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaPackageGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MediaPackageOutputDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"channel_id": "channelId"},
    )
    class MediaPackageOutputDestinationSettingsProperty:
        def __init__(self, *, channel_id: typing.Optional[builtins.str] = None) -> None:
            '''
            :param channel_id: ``CfnChannel.MediaPackageOutputDestinationSettingsProperty.ChannelId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputdestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if channel_id is not None:
                self._values["channel_id"] = channel_id

        @builtins.property
        def channel_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MediaPackageOutputDestinationSettingsProperty.ChannelId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputdestinationsettings.html#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelid
            '''
            result = self._values.get("channel_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaPackageOutputDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MediaPackageOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class MediaPackageOutputSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaPackageOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MotionGraphicsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "motion_graphics_insertion": "motionGraphicsInsertion",
            "motion_graphics_settings": "motionGraphicsSettings",
        },
    )
    class MotionGraphicsConfigurationProperty:
        def __init__(
            self,
            *,
            motion_graphics_insertion: typing.Optional[builtins.str] = None,
            motion_graphics_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MotionGraphicsSettingsProperty"]] = None,
        ) -> None:
            '''
            :param motion_graphics_insertion: ``CfnChannel.MotionGraphicsConfigurationProperty.MotionGraphicsInsertion``.
            :param motion_graphics_settings: ``CfnChannel.MotionGraphicsConfigurationProperty.MotionGraphicsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicsconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if motion_graphics_insertion is not None:
                self._values["motion_graphics_insertion"] = motion_graphics_insertion
            if motion_graphics_settings is not None:
                self._values["motion_graphics_settings"] = motion_graphics_settings

        @builtins.property
        def motion_graphics_insertion(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MotionGraphicsConfigurationProperty.MotionGraphicsInsertion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicsconfiguration.html#cfn-medialive-channel-motiongraphicsconfiguration-motiongraphicsinsertion
            '''
            result = self._values.get("motion_graphics_insertion")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def motion_graphics_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MotionGraphicsSettingsProperty"]]:
            '''``CfnChannel.MotionGraphicsConfigurationProperty.MotionGraphicsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicsconfiguration.html#cfn-medialive-channel-motiongraphicsconfiguration-motiongraphicssettings
            '''
            result = self._values.get("motion_graphics_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MotionGraphicsSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MotionGraphicsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MotionGraphicsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"html_motion_graphics_settings": "htmlMotionGraphicsSettings"},
    )
    class MotionGraphicsSettingsProperty:
        def __init__(
            self,
            *,
            html_motion_graphics_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HtmlMotionGraphicsSettingsProperty"]] = None,
        ) -> None:
            '''
            :param html_motion_graphics_settings: ``CfnChannel.MotionGraphicsSettingsProperty.HtmlMotionGraphicsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicssettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if html_motion_graphics_settings is not None:
                self._values["html_motion_graphics_settings"] = html_motion_graphics_settings

        @builtins.property
        def html_motion_graphics_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HtmlMotionGraphicsSettingsProperty"]]:
            '''``CfnChannel.MotionGraphicsSettingsProperty.HtmlMotionGraphicsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicssettings.html#cfn-medialive-channel-motiongraphicssettings-htmlmotiongraphicssettings
            '''
            result = self._values.get("html_motion_graphics_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HtmlMotionGraphicsSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MotionGraphicsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Mp2SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bitrate": "bitrate",
            "coding_mode": "codingMode",
            "sample_rate": "sampleRate",
        },
    )
    class Mp2SettingsProperty:
        def __init__(
            self,
            *,
            bitrate: typing.Optional[jsii.Number] = None,
            coding_mode: typing.Optional[builtins.str] = None,
            sample_rate: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param bitrate: ``CfnChannel.Mp2SettingsProperty.Bitrate``.
            :param coding_mode: ``CfnChannel.Mp2SettingsProperty.CodingMode``.
            :param sample_rate: ``CfnChannel.Mp2SettingsProperty.SampleRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if coding_mode is not None:
                self._values["coding_mode"] = coding_mode
            if sample_rate is not None:
                self._values["sample_rate"] = sample_rate

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Mp2SettingsProperty.Bitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-bitrate
            '''
            result = self._values.get("bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def coding_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mp2SettingsProperty.CodingMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-codingmode
            '''
            result = self._values.get("coding_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sample_rate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Mp2SettingsProperty.SampleRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-samplerate
            '''
            result = self._values.get("sample_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Mp2SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Mpeg2FilterSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"temporal_filter_settings": "temporalFilterSettings"},
    )
    class Mpeg2FilterSettingsProperty:
        def __init__(
            self,
            *,
            temporal_filter_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TemporalFilterSettingsProperty"]] = None,
        ) -> None:
            '''
            :param temporal_filter_settings: ``CfnChannel.Mpeg2FilterSettingsProperty.TemporalFilterSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2filtersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if temporal_filter_settings is not None:
                self._values["temporal_filter_settings"] = temporal_filter_settings

        @builtins.property
        def temporal_filter_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TemporalFilterSettingsProperty"]]:
            '''``CfnChannel.Mpeg2FilterSettingsProperty.TemporalFilterSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2filtersettings.html#cfn-medialive-channel-mpeg2filtersettings-temporalfiltersettings
            '''
            result = self._values.get("temporal_filter_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.TemporalFilterSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Mpeg2FilterSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Mpeg2SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adaptive_quantization": "adaptiveQuantization",
            "afd_signaling": "afdSignaling",
            "color_metadata": "colorMetadata",
            "color_space": "colorSpace",
            "display_aspect_ratio": "displayAspectRatio",
            "filter_settings": "filterSettings",
            "fixed_afd": "fixedAfd",
            "framerate_denominator": "framerateDenominator",
            "framerate_numerator": "framerateNumerator",
            "gop_closed_cadence": "gopClosedCadence",
            "gop_num_b_frames": "gopNumBFrames",
            "gop_size": "gopSize",
            "gop_size_units": "gopSizeUnits",
            "scan_type": "scanType",
            "subgop_length": "subgopLength",
            "timecode_insertion": "timecodeInsertion",
        },
    )
    class Mpeg2SettingsProperty:
        def __init__(
            self,
            *,
            adaptive_quantization: typing.Optional[builtins.str] = None,
            afd_signaling: typing.Optional[builtins.str] = None,
            color_metadata: typing.Optional[builtins.str] = None,
            color_space: typing.Optional[builtins.str] = None,
            display_aspect_ratio: typing.Optional[builtins.str] = None,
            filter_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Mpeg2FilterSettingsProperty"]] = None,
            fixed_afd: typing.Optional[builtins.str] = None,
            framerate_denominator: typing.Optional[jsii.Number] = None,
            framerate_numerator: typing.Optional[jsii.Number] = None,
            gop_closed_cadence: typing.Optional[jsii.Number] = None,
            gop_num_b_frames: typing.Optional[jsii.Number] = None,
            gop_size: typing.Optional[jsii.Number] = None,
            gop_size_units: typing.Optional[builtins.str] = None,
            scan_type: typing.Optional[builtins.str] = None,
            subgop_length: typing.Optional[builtins.str] = None,
            timecode_insertion: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param adaptive_quantization: ``CfnChannel.Mpeg2SettingsProperty.AdaptiveQuantization``.
            :param afd_signaling: ``CfnChannel.Mpeg2SettingsProperty.AfdSignaling``.
            :param color_metadata: ``CfnChannel.Mpeg2SettingsProperty.ColorMetadata``.
            :param color_space: ``CfnChannel.Mpeg2SettingsProperty.ColorSpace``.
            :param display_aspect_ratio: ``CfnChannel.Mpeg2SettingsProperty.DisplayAspectRatio``.
            :param filter_settings: ``CfnChannel.Mpeg2SettingsProperty.FilterSettings``.
            :param fixed_afd: ``CfnChannel.Mpeg2SettingsProperty.FixedAfd``.
            :param framerate_denominator: ``CfnChannel.Mpeg2SettingsProperty.FramerateDenominator``.
            :param framerate_numerator: ``CfnChannel.Mpeg2SettingsProperty.FramerateNumerator``.
            :param gop_closed_cadence: ``CfnChannel.Mpeg2SettingsProperty.GopClosedCadence``.
            :param gop_num_b_frames: ``CfnChannel.Mpeg2SettingsProperty.GopNumBFrames``.
            :param gop_size: ``CfnChannel.Mpeg2SettingsProperty.GopSize``.
            :param gop_size_units: ``CfnChannel.Mpeg2SettingsProperty.GopSizeUnits``.
            :param scan_type: ``CfnChannel.Mpeg2SettingsProperty.ScanType``.
            :param subgop_length: ``CfnChannel.Mpeg2SettingsProperty.SubgopLength``.
            :param timecode_insertion: ``CfnChannel.Mpeg2SettingsProperty.TimecodeInsertion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if adaptive_quantization is not None:
                self._values["adaptive_quantization"] = adaptive_quantization
            if afd_signaling is not None:
                self._values["afd_signaling"] = afd_signaling
            if color_metadata is not None:
                self._values["color_metadata"] = color_metadata
            if color_space is not None:
                self._values["color_space"] = color_space
            if display_aspect_ratio is not None:
                self._values["display_aspect_ratio"] = display_aspect_ratio
            if filter_settings is not None:
                self._values["filter_settings"] = filter_settings
            if fixed_afd is not None:
                self._values["fixed_afd"] = fixed_afd
            if framerate_denominator is not None:
                self._values["framerate_denominator"] = framerate_denominator
            if framerate_numerator is not None:
                self._values["framerate_numerator"] = framerate_numerator
            if gop_closed_cadence is not None:
                self._values["gop_closed_cadence"] = gop_closed_cadence
            if gop_num_b_frames is not None:
                self._values["gop_num_b_frames"] = gop_num_b_frames
            if gop_size is not None:
                self._values["gop_size"] = gop_size
            if gop_size_units is not None:
                self._values["gop_size_units"] = gop_size_units
            if scan_type is not None:
                self._values["scan_type"] = scan_type
            if subgop_length is not None:
                self._values["subgop_length"] = subgop_length
            if timecode_insertion is not None:
                self._values["timecode_insertion"] = timecode_insertion

        @builtins.property
        def adaptive_quantization(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.AdaptiveQuantization``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-adaptivequantization
            '''
            result = self._values.get("adaptive_quantization")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def afd_signaling(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.AfdSignaling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-afdsignaling
            '''
            result = self._values.get("afd_signaling")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def color_metadata(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.ColorMetadata``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-colormetadata
            '''
            result = self._values.get("color_metadata")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def color_space(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.ColorSpace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-colorspace
            '''
            result = self._values.get("color_space")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def display_aspect_ratio(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.DisplayAspectRatio``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-displayaspectratio
            '''
            result = self._values.get("display_aspect_ratio")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def filter_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Mpeg2FilterSettingsProperty"]]:
            '''``CfnChannel.Mpeg2SettingsProperty.FilterSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-filtersettings
            '''
            result = self._values.get("filter_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Mpeg2FilterSettingsProperty"]], result)

        @builtins.property
        def fixed_afd(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.FixedAfd``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-fixedafd
            '''
            result = self._values.get("fixed_afd")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def framerate_denominator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Mpeg2SettingsProperty.FramerateDenominator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-frameratedenominator
            '''
            result = self._values.get("framerate_denominator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def framerate_numerator(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Mpeg2SettingsProperty.FramerateNumerator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-frameratenumerator
            '''
            result = self._values.get("framerate_numerator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_closed_cadence(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Mpeg2SettingsProperty.GopClosedCadence``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-gopclosedcadence
            '''
            result = self._values.get("gop_closed_cadence")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_num_b_frames(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Mpeg2SettingsProperty.GopNumBFrames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-gopnumbframes
            '''
            result = self._values.get("gop_num_b_frames")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Mpeg2SettingsProperty.GopSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-gopsize
            '''
            result = self._values.get("gop_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gop_size_units(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.GopSizeUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-gopsizeunits
            '''
            result = self._values.get("gop_size_units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scan_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.ScanType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-scantype
            '''
            result = self._values.get("scan_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subgop_length(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.SubgopLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-subgoplength
            '''
            result = self._values.get("subgop_length")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timecode_insertion(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Mpeg2SettingsProperty.TimecodeInsertion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-timecodeinsertion
            '''
            result = self._values.get("timecode_insertion")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Mpeg2SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MsSmoothGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "acquisition_point_id": "acquisitionPointId",
            "audio_only_timecode_control": "audioOnlyTimecodeControl",
            "certificate_mode": "certificateMode",
            "connection_retry_interval": "connectionRetryInterval",
            "destination": "destination",
            "event_id": "eventId",
            "event_id_mode": "eventIdMode",
            "event_stop_behavior": "eventStopBehavior",
            "filecache_duration": "filecacheDuration",
            "fragment_length": "fragmentLength",
            "input_loss_action": "inputLossAction",
            "num_retries": "numRetries",
            "restart_delay": "restartDelay",
            "segmentation_mode": "segmentationMode",
            "send_delay_ms": "sendDelayMs",
            "sparse_track_type": "sparseTrackType",
            "stream_manifest_behavior": "streamManifestBehavior",
            "timestamp_offset": "timestampOffset",
            "timestamp_offset_mode": "timestampOffsetMode",
        },
    )
    class MsSmoothGroupSettingsProperty:
        def __init__(
            self,
            *,
            acquisition_point_id: typing.Optional[builtins.str] = None,
            audio_only_timecode_control: typing.Optional[builtins.str] = None,
            certificate_mode: typing.Optional[builtins.str] = None,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]] = None,
            event_id: typing.Optional[builtins.str] = None,
            event_id_mode: typing.Optional[builtins.str] = None,
            event_stop_behavior: typing.Optional[builtins.str] = None,
            filecache_duration: typing.Optional[jsii.Number] = None,
            fragment_length: typing.Optional[jsii.Number] = None,
            input_loss_action: typing.Optional[builtins.str] = None,
            num_retries: typing.Optional[jsii.Number] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
            segmentation_mode: typing.Optional[builtins.str] = None,
            send_delay_ms: typing.Optional[jsii.Number] = None,
            sparse_track_type: typing.Optional[builtins.str] = None,
            stream_manifest_behavior: typing.Optional[builtins.str] = None,
            timestamp_offset: typing.Optional[builtins.str] = None,
            timestamp_offset_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param acquisition_point_id: ``CfnChannel.MsSmoothGroupSettingsProperty.AcquisitionPointId``.
            :param audio_only_timecode_control: ``CfnChannel.MsSmoothGroupSettingsProperty.AudioOnlyTimecodeControl``.
            :param certificate_mode: ``CfnChannel.MsSmoothGroupSettingsProperty.CertificateMode``.
            :param connection_retry_interval: ``CfnChannel.MsSmoothGroupSettingsProperty.ConnectionRetryInterval``.
            :param destination: ``CfnChannel.MsSmoothGroupSettingsProperty.Destination``.
            :param event_id: ``CfnChannel.MsSmoothGroupSettingsProperty.EventId``.
            :param event_id_mode: ``CfnChannel.MsSmoothGroupSettingsProperty.EventIdMode``.
            :param event_stop_behavior: ``CfnChannel.MsSmoothGroupSettingsProperty.EventStopBehavior``.
            :param filecache_duration: ``CfnChannel.MsSmoothGroupSettingsProperty.FilecacheDuration``.
            :param fragment_length: ``CfnChannel.MsSmoothGroupSettingsProperty.FragmentLength``.
            :param input_loss_action: ``CfnChannel.MsSmoothGroupSettingsProperty.InputLossAction``.
            :param num_retries: ``CfnChannel.MsSmoothGroupSettingsProperty.NumRetries``.
            :param restart_delay: ``CfnChannel.MsSmoothGroupSettingsProperty.RestartDelay``.
            :param segmentation_mode: ``CfnChannel.MsSmoothGroupSettingsProperty.SegmentationMode``.
            :param send_delay_ms: ``CfnChannel.MsSmoothGroupSettingsProperty.SendDelayMs``.
            :param sparse_track_type: ``CfnChannel.MsSmoothGroupSettingsProperty.SparseTrackType``.
            :param stream_manifest_behavior: ``CfnChannel.MsSmoothGroupSettingsProperty.StreamManifestBehavior``.
            :param timestamp_offset: ``CfnChannel.MsSmoothGroupSettingsProperty.TimestampOffset``.
            :param timestamp_offset_mode: ``CfnChannel.MsSmoothGroupSettingsProperty.TimestampOffsetMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if acquisition_point_id is not None:
                self._values["acquisition_point_id"] = acquisition_point_id
            if audio_only_timecode_control is not None:
                self._values["audio_only_timecode_control"] = audio_only_timecode_control
            if certificate_mode is not None:
                self._values["certificate_mode"] = certificate_mode
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if destination is not None:
                self._values["destination"] = destination
            if event_id is not None:
                self._values["event_id"] = event_id
            if event_id_mode is not None:
                self._values["event_id_mode"] = event_id_mode
            if event_stop_behavior is not None:
                self._values["event_stop_behavior"] = event_stop_behavior
            if filecache_duration is not None:
                self._values["filecache_duration"] = filecache_duration
            if fragment_length is not None:
                self._values["fragment_length"] = fragment_length
            if input_loss_action is not None:
                self._values["input_loss_action"] = input_loss_action
            if num_retries is not None:
                self._values["num_retries"] = num_retries
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay
            if segmentation_mode is not None:
                self._values["segmentation_mode"] = segmentation_mode
            if send_delay_ms is not None:
                self._values["send_delay_ms"] = send_delay_ms
            if sparse_track_type is not None:
                self._values["sparse_track_type"] = sparse_track_type
            if stream_manifest_behavior is not None:
                self._values["stream_manifest_behavior"] = stream_manifest_behavior
            if timestamp_offset is not None:
                self._values["timestamp_offset"] = timestamp_offset
            if timestamp_offset_mode is not None:
                self._values["timestamp_offset_mode"] = timestamp_offset_mode

        @builtins.property
        def acquisition_point_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.AcquisitionPointId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-acquisitionpointid
            '''
            result = self._values.get("acquisition_point_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def audio_only_timecode_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.AudioOnlyTimecodeControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-audioonlytimecodecontrol
            '''
            result = self._values.get("audio_only_timecode_control")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def certificate_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.CertificateMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-certificatemode
            '''
            result = self._values.get("certificate_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.ConnectionRetryInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-connectionretryinterval
            '''
            result = self._values.get("connection_retry_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]], result)

        @builtins.property
        def event_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.EventId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-eventid
            '''
            result = self._values.get("event_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_id_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.EventIdMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-eventidmode
            '''
            result = self._values.get("event_id_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_stop_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.EventStopBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-eventstopbehavior
            '''
            result = self._values.get("event_stop_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def filecache_duration(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.FilecacheDuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-filecacheduration
            '''
            result = self._values.get("filecache_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def fragment_length(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.FragmentLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-fragmentlength
            '''
            result = self._values.get("fragment_length")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def input_loss_action(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.InputLossAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-inputlossaction
            '''
            result = self._values.get("input_loss_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.NumRetries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-numretries
            '''
            result = self._values.get("num_retries")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-restartdelay
            '''
            result = self._values.get("restart_delay")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segmentation_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.SegmentationMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-segmentationmode
            '''
            result = self._values.get("segmentation_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def send_delay_ms(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.SendDelayMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-senddelayms
            '''
            result = self._values.get("send_delay_ms")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def sparse_track_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.SparseTrackType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-sparsetracktype
            '''
            result = self._values.get("sparse_track_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_manifest_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.StreamManifestBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-streammanifestbehavior
            '''
            result = self._values.get("stream_manifest_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timestamp_offset(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.TimestampOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-timestampoffset
            '''
            result = self._values.get("timestamp_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timestamp_offset_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothGroupSettingsProperty.TimestampOffsetMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-timestampoffsetmode
            '''
            result = self._values.get("timestamp_offset_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MsSmoothGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MsSmoothOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "h265_packaging_type": "h265PackagingType",
            "name_modifier": "nameModifier",
        },
    )
    class MsSmoothOutputSettingsProperty:
        def __init__(
            self,
            *,
            h265_packaging_type: typing.Optional[builtins.str] = None,
            name_modifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param h265_packaging_type: ``CfnChannel.MsSmoothOutputSettingsProperty.H265PackagingType``.
            :param name_modifier: ``CfnChannel.MsSmoothOutputSettingsProperty.NameModifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if h265_packaging_type is not None:
                self._values["h265_packaging_type"] = h265_packaging_type
            if name_modifier is not None:
                self._values["name_modifier"] = name_modifier

        @builtins.property
        def h265_packaging_type(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothOutputSettingsProperty.H265PackagingType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html#cfn-medialive-channel-mssmoothoutputsettings-h265packagingtype
            '''
            result = self._values.get("h265_packaging_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name_modifier(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MsSmoothOutputSettingsProperty.NameModifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html#cfn-medialive-channel-mssmoothoutputsettings-namemodifier
            '''
            result = self._values.get("name_modifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MsSmoothOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MultiplexGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class MultiplexGroupSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexgroupsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiplexGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MultiplexOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination"},
    )
    class MultiplexOutputSettingsProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]] = None,
        ) -> None:
            '''
            :param destination: ``CfnChannel.MultiplexOutputSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]]:
            '''``CfnChannel.MultiplexOutputSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html#cfn-medialive-channel-multiplexoutputsettings-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiplexOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.MultiplexProgramChannelDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"multiplex_id": "multiplexId", "program_name": "programName"},
    )
    class MultiplexProgramChannelDestinationSettingsProperty:
        def __init__(
            self,
            *,
            multiplex_id: typing.Optional[builtins.str] = None,
            program_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param multiplex_id: ``CfnChannel.MultiplexProgramChannelDestinationSettingsProperty.MultiplexId``.
            :param program_name: ``CfnChannel.MultiplexProgramChannelDestinationSettingsProperty.ProgramName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if multiplex_id is not None:
                self._values["multiplex_id"] = multiplex_id
            if program_name is not None:
                self._values["program_name"] = program_name

        @builtins.property
        def multiplex_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MultiplexProgramChannelDestinationSettingsProperty.MultiplexId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html#cfn-medialive-channel-multiplexprogramchanneldestinationsettings-multiplexid
            '''
            result = self._values.get("multiplex_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def program_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.MultiplexProgramChannelDestinationSettingsProperty.ProgramName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html#cfn-medialive-channel-multiplexprogramchanneldestinationsettings-programname
            '''
            result = self._values.get("program_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiplexProgramChannelDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.NetworkInputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hls_input_settings": "hlsInputSettings",
            "server_validation": "serverValidation",
        },
    )
    class NetworkInputSettingsProperty:
        def __init__(
            self,
            *,
            hls_input_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsInputSettingsProperty"]] = None,
            server_validation: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param hls_input_settings: ``CfnChannel.NetworkInputSettingsProperty.HlsInputSettings``.
            :param server_validation: ``CfnChannel.NetworkInputSettingsProperty.ServerValidation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if hls_input_settings is not None:
                self._values["hls_input_settings"] = hls_input_settings
            if server_validation is not None:
                self._values["server_validation"] = server_validation

        @builtins.property
        def hls_input_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsInputSettingsProperty"]]:
            '''``CfnChannel.NetworkInputSettingsProperty.HlsInputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html#cfn-medialive-channel-networkinputsettings-hlsinputsettings
            '''
            result = self._values.get("hls_input_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsInputSettingsProperty"]], result)

        @builtins.property
        def server_validation(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.NetworkInputSettingsProperty.ServerValidation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html#cfn-medialive-channel-networkinputsettings-servervalidation
            '''
            result = self._values.get("server_validation")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkInputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.NielsenConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "distributor_id": "distributorId",
            "nielsen_pcm_to_id3_tagging": "nielsenPcmToId3Tagging",
        },
    )
    class NielsenConfigurationProperty:
        def __init__(
            self,
            *,
            distributor_id: typing.Optional[builtins.str] = None,
            nielsen_pcm_to_id3_tagging: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param distributor_id: ``CfnChannel.NielsenConfigurationProperty.DistributorId``.
            :param nielsen_pcm_to_id3_tagging: ``CfnChannel.NielsenConfigurationProperty.NielsenPcmToId3Tagging``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if distributor_id is not None:
                self._values["distributor_id"] = distributor_id
            if nielsen_pcm_to_id3_tagging is not None:
                self._values["nielsen_pcm_to_id3_tagging"] = nielsen_pcm_to_id3_tagging

        @builtins.property
        def distributor_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.NielsenConfigurationProperty.DistributorId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html#cfn-medialive-channel-nielsenconfiguration-distributorid
            '''
            result = self._values.get("distributor_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def nielsen_pcm_to_id3_tagging(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.NielsenConfigurationProperty.NielsenPcmToId3Tagging``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html#cfn-medialive-channel-nielsenconfiguration-nielsenpcmtoid3tagging
            '''
            result = self._values.get("nielsen_pcm_to_id3_tagging")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NielsenConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.OutputDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "media_package_settings": "mediaPackageSettings",
            "multiplex_settings": "multiplexSettings",
            "settings": "settings",
        },
    )
    class OutputDestinationProperty:
        def __init__(
            self,
            *,
            id: typing.Optional[builtins.str] = None,
            media_package_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MediaPackageOutputDestinationSettingsProperty"]]]] = None,
            multiplex_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MultiplexProgramChannelDestinationSettingsProperty"]] = None,
            settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputDestinationSettingsProperty"]]]] = None,
        ) -> None:
            '''
            :param id: ``CfnChannel.OutputDestinationProperty.Id``.
            :param media_package_settings: ``CfnChannel.OutputDestinationProperty.MediaPackageSettings``.
            :param multiplex_settings: ``CfnChannel.OutputDestinationProperty.MultiplexSettings``.
            :param settings: ``CfnChannel.OutputDestinationProperty.Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id
            if media_package_settings is not None:
                self._values["media_package_settings"] = media_package_settings
            if multiplex_settings is not None:
                self._values["multiplex_settings"] = multiplex_settings
            if settings is not None:
                self._values["settings"] = settings

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.OutputDestinationProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def media_package_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MediaPackageOutputDestinationSettingsProperty"]]]]:
            '''``CfnChannel.OutputDestinationProperty.MediaPackageSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-mediapackagesettings
            '''
            result = self._values.get("media_package_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MediaPackageOutputDestinationSettingsProperty"]]]], result)

        @builtins.property
        def multiplex_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MultiplexProgramChannelDestinationSettingsProperty"]]:
            '''``CfnChannel.OutputDestinationProperty.MultiplexSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-multiplexsettings
            '''
            result = self._values.get("multiplex_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MultiplexProgramChannelDestinationSettingsProperty"]], result)

        @builtins.property
        def settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputDestinationSettingsProperty"]]]]:
            '''``CfnChannel.OutputDestinationProperty.Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-settings
            '''
            result = self._values.get("settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputDestinationSettingsProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.OutputDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password_param": "passwordParam",
            "stream_name": "streamName",
            "url": "url",
            "username": "username",
        },
    )
    class OutputDestinationSettingsProperty:
        def __init__(
            self,
            *,
            password_param: typing.Optional[builtins.str] = None,
            stream_name: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param password_param: ``CfnChannel.OutputDestinationSettingsProperty.PasswordParam``.
            :param stream_name: ``CfnChannel.OutputDestinationSettingsProperty.StreamName``.
            :param url: ``CfnChannel.OutputDestinationSettingsProperty.Url``.
            :param username: ``CfnChannel.OutputDestinationSettingsProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if password_param is not None:
                self._values["password_param"] = password_param
            if stream_name is not None:
                self._values["stream_name"] = stream_name
            if url is not None:
                self._values["url"] = url
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password_param(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.OutputDestinationSettingsProperty.PasswordParam``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-passwordparam
            '''
            result = self._values.get("password_param")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.OutputDestinationSettingsProperty.StreamName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-streamname
            '''
            result = self._values.get("stream_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.OutputDestinationSettingsProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.OutputDestinationSettingsProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.OutputGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "output_group_settings": "outputGroupSettings",
            "outputs": "outputs",
        },
    )
    class OutputGroupProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            output_group_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputGroupSettingsProperty"]] = None,
            outputs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputProperty"]]]] = None,
        ) -> None:
            '''
            :param name: ``CfnChannel.OutputGroupProperty.Name``.
            :param output_group_settings: ``CfnChannel.OutputGroupProperty.OutputGroupSettings``.
            :param outputs: ``CfnChannel.OutputGroupProperty.Outputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if output_group_settings is not None:
                self._values["output_group_settings"] = output_group_settings
            if outputs is not None:
                self._values["outputs"] = outputs

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.OutputGroupProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html#cfn-medialive-channel-outputgroup-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_group_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputGroupSettingsProperty"]]:
            '''``CfnChannel.OutputGroupProperty.OutputGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html#cfn-medialive-channel-outputgroup-outputgroupsettings
            '''
            result = self._values.get("output_group_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputGroupSettingsProperty"]], result)

        @builtins.property
        def outputs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputProperty"]]]]:
            '''``CfnChannel.OutputGroupProperty.Outputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html#cfn-medialive-channel-outputgroup-outputs
            '''
            result = self._values.get("outputs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.OutputGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "archive_group_settings": "archiveGroupSettings",
            "frame_capture_group_settings": "frameCaptureGroupSettings",
            "hls_group_settings": "hlsGroupSettings",
            "media_package_group_settings": "mediaPackageGroupSettings",
            "ms_smooth_group_settings": "msSmoothGroupSettings",
            "multiplex_group_settings": "multiplexGroupSettings",
            "rtmp_group_settings": "rtmpGroupSettings",
            "udp_group_settings": "udpGroupSettings",
        },
    )
    class OutputGroupSettingsProperty:
        def __init__(
            self,
            *,
            archive_group_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveGroupSettingsProperty"]] = None,
            frame_capture_group_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureGroupSettingsProperty"]] = None,
            hls_group_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsGroupSettingsProperty"]] = None,
            media_package_group_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MediaPackageGroupSettingsProperty"]] = None,
            ms_smooth_group_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MsSmoothGroupSettingsProperty"]] = None,
            multiplex_group_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MultiplexGroupSettingsProperty"]] = None,
            rtmp_group_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RtmpGroupSettingsProperty"]] = None,
            udp_group_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.UdpGroupSettingsProperty"]] = None,
        ) -> None:
            '''
            :param archive_group_settings: ``CfnChannel.OutputGroupSettingsProperty.ArchiveGroupSettings``.
            :param frame_capture_group_settings: ``CfnChannel.OutputGroupSettingsProperty.FrameCaptureGroupSettings``.
            :param hls_group_settings: ``CfnChannel.OutputGroupSettingsProperty.HlsGroupSettings``.
            :param media_package_group_settings: ``CfnChannel.OutputGroupSettingsProperty.MediaPackageGroupSettings``.
            :param ms_smooth_group_settings: ``CfnChannel.OutputGroupSettingsProperty.MsSmoothGroupSettings``.
            :param multiplex_group_settings: ``CfnChannel.OutputGroupSettingsProperty.MultiplexGroupSettings``.
            :param rtmp_group_settings: ``CfnChannel.OutputGroupSettingsProperty.RtmpGroupSettings``.
            :param udp_group_settings: ``CfnChannel.OutputGroupSettingsProperty.UdpGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if archive_group_settings is not None:
                self._values["archive_group_settings"] = archive_group_settings
            if frame_capture_group_settings is not None:
                self._values["frame_capture_group_settings"] = frame_capture_group_settings
            if hls_group_settings is not None:
                self._values["hls_group_settings"] = hls_group_settings
            if media_package_group_settings is not None:
                self._values["media_package_group_settings"] = media_package_group_settings
            if ms_smooth_group_settings is not None:
                self._values["ms_smooth_group_settings"] = ms_smooth_group_settings
            if multiplex_group_settings is not None:
                self._values["multiplex_group_settings"] = multiplex_group_settings
            if rtmp_group_settings is not None:
                self._values["rtmp_group_settings"] = rtmp_group_settings
            if udp_group_settings is not None:
                self._values["udp_group_settings"] = udp_group_settings

        @builtins.property
        def archive_group_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveGroupSettingsProperty"]]:
            '''``CfnChannel.OutputGroupSettingsProperty.ArchiveGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-archivegroupsettings
            '''
            result = self._values.get("archive_group_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveGroupSettingsProperty"]], result)

        @builtins.property
        def frame_capture_group_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureGroupSettingsProperty"]]:
            '''``CfnChannel.OutputGroupSettingsProperty.FrameCaptureGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-framecapturegroupsettings
            '''
            result = self._values.get("frame_capture_group_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureGroupSettingsProperty"]], result)

        @builtins.property
        def hls_group_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsGroupSettingsProperty"]]:
            '''``CfnChannel.OutputGroupSettingsProperty.HlsGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-hlsgroupsettings
            '''
            result = self._values.get("hls_group_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsGroupSettingsProperty"]], result)

        @builtins.property
        def media_package_group_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MediaPackageGroupSettingsProperty"]]:
            '''``CfnChannel.OutputGroupSettingsProperty.MediaPackageGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-mediapackagegroupsettings
            '''
            result = self._values.get("media_package_group_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MediaPackageGroupSettingsProperty"]], result)

        @builtins.property
        def ms_smooth_group_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MsSmoothGroupSettingsProperty"]]:
            '''``CfnChannel.OutputGroupSettingsProperty.MsSmoothGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-mssmoothgroupsettings
            '''
            result = self._values.get("ms_smooth_group_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MsSmoothGroupSettingsProperty"]], result)

        @builtins.property
        def multiplex_group_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MultiplexGroupSettingsProperty"]]:
            '''``CfnChannel.OutputGroupSettingsProperty.MultiplexGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-multiplexgroupsettings
            '''
            result = self._values.get("multiplex_group_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MultiplexGroupSettingsProperty"]], result)

        @builtins.property
        def rtmp_group_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RtmpGroupSettingsProperty"]]:
            '''``CfnChannel.OutputGroupSettingsProperty.RtmpGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-rtmpgroupsettings
            '''
            result = self._values.get("rtmp_group_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RtmpGroupSettingsProperty"]], result)

        @builtins.property
        def udp_group_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.UdpGroupSettingsProperty"]]:
            '''``CfnChannel.OutputGroupSettingsProperty.UdpGroupSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-udpgroupsettings
            '''
            result = self._values.get("udp_group_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.UdpGroupSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.OutputLocationRefProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_ref_id": "destinationRefId"},
    )
    class OutputLocationRefProperty:
        def __init__(
            self,
            *,
            destination_ref_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination_ref_id: ``CfnChannel.OutputLocationRefProperty.DestinationRefId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if destination_ref_id is not None:
                self._values["destination_ref_id"] = destination_ref_id

        @builtins.property
        def destination_ref_id(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.OutputLocationRefProperty.DestinationRefId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html#cfn-medialive-channel-outputlocationref-destinationrefid
            '''
            result = self._values.get("destination_ref_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputLocationRefProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_description_names": "audioDescriptionNames",
            "caption_description_names": "captionDescriptionNames",
            "output_name": "outputName",
            "output_settings": "outputSettings",
            "video_description_name": "videoDescriptionName",
        },
    )
    class OutputProperty:
        def __init__(
            self,
            *,
            audio_description_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            caption_description_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            output_name: typing.Optional[builtins.str] = None,
            output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputSettingsProperty"]] = None,
            video_description_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param audio_description_names: ``CfnChannel.OutputProperty.AudioDescriptionNames``.
            :param caption_description_names: ``CfnChannel.OutputProperty.CaptionDescriptionNames``.
            :param output_name: ``CfnChannel.OutputProperty.OutputName``.
            :param output_settings: ``CfnChannel.OutputProperty.OutputSettings``.
            :param video_description_name: ``CfnChannel.OutputProperty.VideoDescriptionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_description_names is not None:
                self._values["audio_description_names"] = audio_description_names
            if caption_description_names is not None:
                self._values["caption_description_names"] = caption_description_names
            if output_name is not None:
                self._values["output_name"] = output_name
            if output_settings is not None:
                self._values["output_settings"] = output_settings
            if video_description_name is not None:
                self._values["video_description_name"] = video_description_name

        @builtins.property
        def audio_description_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnChannel.OutputProperty.AudioDescriptionNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-audiodescriptionnames
            '''
            result = self._values.get("audio_description_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def caption_description_names(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnChannel.OutputProperty.CaptionDescriptionNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-captiondescriptionnames
            '''
            result = self._values.get("caption_description_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def output_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.OutputProperty.OutputName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-outputname
            '''
            result = self._values.get("output_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputSettingsProperty"]]:
            '''``CfnChannel.OutputProperty.OutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-outputsettings
            '''
            result = self._values.get("output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputSettingsProperty"]], result)

        @builtins.property
        def video_description_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.OutputProperty.VideoDescriptionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-videodescriptionname
            '''
            result = self._values.get("video_description_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.OutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "archive_output_settings": "archiveOutputSettings",
            "frame_capture_output_settings": "frameCaptureOutputSettings",
            "hls_output_settings": "hlsOutputSettings",
            "media_package_output_settings": "mediaPackageOutputSettings",
            "ms_smooth_output_settings": "msSmoothOutputSettings",
            "multiplex_output_settings": "multiplexOutputSettings",
            "rtmp_output_settings": "rtmpOutputSettings",
            "udp_output_settings": "udpOutputSettings",
        },
    )
    class OutputSettingsProperty:
        def __init__(
            self,
            *,
            archive_output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveOutputSettingsProperty"]] = None,
            frame_capture_output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureOutputSettingsProperty"]] = None,
            hls_output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsOutputSettingsProperty"]] = None,
            media_package_output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MediaPackageOutputSettingsProperty"]] = None,
            ms_smooth_output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MsSmoothOutputSettingsProperty"]] = None,
            multiplex_output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MultiplexOutputSettingsProperty"]] = None,
            rtmp_output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RtmpOutputSettingsProperty"]] = None,
            udp_output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.UdpOutputSettingsProperty"]] = None,
        ) -> None:
            '''
            :param archive_output_settings: ``CfnChannel.OutputSettingsProperty.ArchiveOutputSettings``.
            :param frame_capture_output_settings: ``CfnChannel.OutputSettingsProperty.FrameCaptureOutputSettings``.
            :param hls_output_settings: ``CfnChannel.OutputSettingsProperty.HlsOutputSettings``.
            :param media_package_output_settings: ``CfnChannel.OutputSettingsProperty.MediaPackageOutputSettings``.
            :param ms_smooth_output_settings: ``CfnChannel.OutputSettingsProperty.MsSmoothOutputSettings``.
            :param multiplex_output_settings: ``CfnChannel.OutputSettingsProperty.MultiplexOutputSettings``.
            :param rtmp_output_settings: ``CfnChannel.OutputSettingsProperty.RtmpOutputSettings``.
            :param udp_output_settings: ``CfnChannel.OutputSettingsProperty.UdpOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if archive_output_settings is not None:
                self._values["archive_output_settings"] = archive_output_settings
            if frame_capture_output_settings is not None:
                self._values["frame_capture_output_settings"] = frame_capture_output_settings
            if hls_output_settings is not None:
                self._values["hls_output_settings"] = hls_output_settings
            if media_package_output_settings is not None:
                self._values["media_package_output_settings"] = media_package_output_settings
            if ms_smooth_output_settings is not None:
                self._values["ms_smooth_output_settings"] = ms_smooth_output_settings
            if multiplex_output_settings is not None:
                self._values["multiplex_output_settings"] = multiplex_output_settings
            if rtmp_output_settings is not None:
                self._values["rtmp_output_settings"] = rtmp_output_settings
            if udp_output_settings is not None:
                self._values["udp_output_settings"] = udp_output_settings

        @builtins.property
        def archive_output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveOutputSettingsProperty"]]:
            '''``CfnChannel.OutputSettingsProperty.ArchiveOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-archiveoutputsettings
            '''
            result = self._values.get("archive_output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ArchiveOutputSettingsProperty"]], result)

        @builtins.property
        def frame_capture_output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureOutputSettingsProperty"]]:
            '''``CfnChannel.OutputSettingsProperty.FrameCaptureOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-framecaptureoutputsettings
            '''
            result = self._values.get("frame_capture_output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureOutputSettingsProperty"]], result)

        @builtins.property
        def hls_output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsOutputSettingsProperty"]]:
            '''``CfnChannel.OutputSettingsProperty.HlsOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-hlsoutputsettings
            '''
            result = self._values.get("hls_output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.HlsOutputSettingsProperty"]], result)

        @builtins.property
        def media_package_output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MediaPackageOutputSettingsProperty"]]:
            '''``CfnChannel.OutputSettingsProperty.MediaPackageOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-mediapackageoutputsettings
            '''
            result = self._values.get("media_package_output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MediaPackageOutputSettingsProperty"]], result)

        @builtins.property
        def ms_smooth_output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MsSmoothOutputSettingsProperty"]]:
            '''``CfnChannel.OutputSettingsProperty.MsSmoothOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-mssmoothoutputsettings
            '''
            result = self._values.get("ms_smooth_output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MsSmoothOutputSettingsProperty"]], result)

        @builtins.property
        def multiplex_output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MultiplexOutputSettingsProperty"]]:
            '''``CfnChannel.OutputSettingsProperty.MultiplexOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-multiplexoutputsettings
            '''
            result = self._values.get("multiplex_output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.MultiplexOutputSettingsProperty"]], result)

        @builtins.property
        def rtmp_output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RtmpOutputSettingsProperty"]]:
            '''``CfnChannel.OutputSettingsProperty.RtmpOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-rtmpoutputsettings
            '''
            result = self._values.get("rtmp_output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RtmpOutputSettingsProperty"]], result)

        @builtins.property
        def udp_output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.UdpOutputSettingsProperty"]]:
            '''``CfnChannel.OutputSettingsProperty.UdpOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-udpoutputsettings
            '''
            result = self._values.get("udp_output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.UdpOutputSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.PassThroughSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class PassThroughSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-passthroughsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PassThroughSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.RawSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class RawSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rawsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RawSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Rec601SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class Rec601SettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec601settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Rec601SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Rec709SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class Rec709SettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec709settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Rec709SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.RemixSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_mappings": "channelMappings",
            "channels_in": "channelsIn",
            "channels_out": "channelsOut",
        },
    )
    class RemixSettingsProperty:
        def __init__(
            self,
            *,
            channel_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioChannelMappingProperty"]]]] = None,
            channels_in: typing.Optional[jsii.Number] = None,
            channels_out: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param channel_mappings: ``CfnChannel.RemixSettingsProperty.ChannelMappings``.
            :param channels_in: ``CfnChannel.RemixSettingsProperty.ChannelsIn``.
            :param channels_out: ``CfnChannel.RemixSettingsProperty.ChannelsOut``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if channel_mappings is not None:
                self._values["channel_mappings"] = channel_mappings
            if channels_in is not None:
                self._values["channels_in"] = channels_in
            if channels_out is not None:
                self._values["channels_out"] = channels_out

        @builtins.property
        def channel_mappings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioChannelMappingProperty"]]]]:
            '''``CfnChannel.RemixSettingsProperty.ChannelMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html#cfn-medialive-channel-remixsettings-channelmappings
            '''
            result = self._values.get("channel_mappings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.AudioChannelMappingProperty"]]]], result)

        @builtins.property
        def channels_in(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.RemixSettingsProperty.ChannelsIn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html#cfn-medialive-channel-remixsettings-channelsin
            '''
            result = self._values.get("channels_in")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def channels_out(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.RemixSettingsProperty.ChannelsOut``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html#cfn-medialive-channel-remixsettings-channelsout
            '''
            result = self._values.get("channels_out")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RemixSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.RtmpCaptionInfoDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class RtmpCaptionInfoDestinationSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpcaptioninfodestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RtmpCaptionInfoDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.RtmpGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_markers": "adMarkers",
            "authentication_scheme": "authenticationScheme",
            "cache_full_behavior": "cacheFullBehavior",
            "cache_length": "cacheLength",
            "caption_data": "captionData",
            "input_loss_action": "inputLossAction",
            "restart_delay": "restartDelay",
        },
    )
    class RtmpGroupSettingsProperty:
        def __init__(
            self,
            *,
            ad_markers: typing.Optional[typing.Sequence[builtins.str]] = None,
            authentication_scheme: typing.Optional[builtins.str] = None,
            cache_full_behavior: typing.Optional[builtins.str] = None,
            cache_length: typing.Optional[jsii.Number] = None,
            caption_data: typing.Optional[builtins.str] = None,
            input_loss_action: typing.Optional[builtins.str] = None,
            restart_delay: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param ad_markers: ``CfnChannel.RtmpGroupSettingsProperty.AdMarkers``.
            :param authentication_scheme: ``CfnChannel.RtmpGroupSettingsProperty.AuthenticationScheme``.
            :param cache_full_behavior: ``CfnChannel.RtmpGroupSettingsProperty.CacheFullBehavior``.
            :param cache_length: ``CfnChannel.RtmpGroupSettingsProperty.CacheLength``.
            :param caption_data: ``CfnChannel.RtmpGroupSettingsProperty.CaptionData``.
            :param input_loss_action: ``CfnChannel.RtmpGroupSettingsProperty.InputLossAction``.
            :param restart_delay: ``CfnChannel.RtmpGroupSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_markers is not None:
                self._values["ad_markers"] = ad_markers
            if authentication_scheme is not None:
                self._values["authentication_scheme"] = authentication_scheme
            if cache_full_behavior is not None:
                self._values["cache_full_behavior"] = cache_full_behavior
            if cache_length is not None:
                self._values["cache_length"] = cache_length
            if caption_data is not None:
                self._values["caption_data"] = caption_data
            if input_loss_action is not None:
                self._values["input_loss_action"] = input_loss_action
            if restart_delay is not None:
                self._values["restart_delay"] = restart_delay

        @builtins.property
        def ad_markers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnChannel.RtmpGroupSettingsProperty.AdMarkers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-admarkers
            '''
            result = self._values.get("ad_markers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def authentication_scheme(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.RtmpGroupSettingsProperty.AuthenticationScheme``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-authenticationscheme
            '''
            result = self._values.get("authentication_scheme")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cache_full_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.RtmpGroupSettingsProperty.CacheFullBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-cachefullbehavior
            '''
            result = self._values.get("cache_full_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cache_length(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.RtmpGroupSettingsProperty.CacheLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-cachelength
            '''
            result = self._values.get("cache_length")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def caption_data(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.RtmpGroupSettingsProperty.CaptionData``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-captiondata
            '''
            result = self._values.get("caption_data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_loss_action(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.RtmpGroupSettingsProperty.InputLossAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-inputlossaction
            '''
            result = self._values.get("input_loss_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def restart_delay(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.RtmpGroupSettingsProperty.RestartDelay``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-restartdelay
            '''
            result = self._values.get("restart_delay")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RtmpGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.RtmpOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_mode": "certificateMode",
            "connection_retry_interval": "connectionRetryInterval",
            "destination": "destination",
            "num_retries": "numRetries",
        },
    )
    class RtmpOutputSettingsProperty:
        def __init__(
            self,
            *,
            certificate_mode: typing.Optional[builtins.str] = None,
            connection_retry_interval: typing.Optional[jsii.Number] = None,
            destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]] = None,
            num_retries: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param certificate_mode: ``CfnChannel.RtmpOutputSettingsProperty.CertificateMode``.
            :param connection_retry_interval: ``CfnChannel.RtmpOutputSettingsProperty.ConnectionRetryInterval``.
            :param destination: ``CfnChannel.RtmpOutputSettingsProperty.Destination``.
            :param num_retries: ``CfnChannel.RtmpOutputSettingsProperty.NumRetries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if certificate_mode is not None:
                self._values["certificate_mode"] = certificate_mode
            if connection_retry_interval is not None:
                self._values["connection_retry_interval"] = connection_retry_interval
            if destination is not None:
                self._values["destination"] = destination
            if num_retries is not None:
                self._values["num_retries"] = num_retries

        @builtins.property
        def certificate_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.RtmpOutputSettingsProperty.CertificateMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-certificatemode
            '''
            result = self._values.get("certificate_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connection_retry_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.RtmpOutputSettingsProperty.ConnectionRetryInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-connectionretryinterval
            '''
            result = self._values.get("connection_retry_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]]:
            '''``CfnChannel.RtmpOutputSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]], result)

        @builtins.property
        def num_retries(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.RtmpOutputSettingsProperty.NumRetries``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-numretries
            '''
            result = self._values.get("num_retries")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RtmpOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Scte20PlusEmbeddedDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class Scte20PlusEmbeddedDestinationSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20plusembeddeddestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte20PlusEmbeddedDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Scte20SourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "convert608_to708": "convert608To708",
            "source608_channel_number": "source608ChannelNumber",
        },
    )
    class Scte20SourceSettingsProperty:
        def __init__(
            self,
            *,
            convert608_to708: typing.Optional[builtins.str] = None,
            source608_channel_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param convert608_to708: ``CfnChannel.Scte20SourceSettingsProperty.Convert608To708``.
            :param source608_channel_number: ``CfnChannel.Scte20SourceSettingsProperty.Source608ChannelNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if convert608_to708 is not None:
                self._values["convert608_to708"] = convert608_to708
            if source608_channel_number is not None:
                self._values["source608_channel_number"] = source608_channel_number

        @builtins.property
        def convert608_to708(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Scte20SourceSettingsProperty.Convert608To708``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html#cfn-medialive-channel-scte20sourcesettings-convert608to708
            '''
            result = self._values.get("convert608_to708")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source608_channel_number(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Scte20SourceSettingsProperty.Source608ChannelNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html#cfn-medialive-channel-scte20sourcesettings-source608channelnumber
            '''
            result = self._values.get("source608_channel_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte20SourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Scte27DestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class Scte27DestinationSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27destinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte27DestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Scte27SourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"pid": "pid"},
    )
    class Scte27SourceSettingsProperty:
        def __init__(self, *, pid: typing.Optional[jsii.Number] = None) -> None:
            '''
            :param pid: ``CfnChannel.Scte27SourceSettingsProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27sourcesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if pid is not None:
                self._values["pid"] = pid

        @builtins.property
        def pid(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Scte27SourceSettingsProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27sourcesettings.html#cfn-medialive-channel-scte27sourcesettings-pid
            '''
            result = self._values.get("pid")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte27SourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Scte35SpliceInsertProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_avail_offset": "adAvailOffset",
            "no_regional_blackout_flag": "noRegionalBlackoutFlag",
            "web_delivery_allowed_flag": "webDeliveryAllowedFlag",
        },
    )
    class Scte35SpliceInsertProperty:
        def __init__(
            self,
            *,
            ad_avail_offset: typing.Optional[jsii.Number] = None,
            no_regional_blackout_flag: typing.Optional[builtins.str] = None,
            web_delivery_allowed_flag: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param ad_avail_offset: ``CfnChannel.Scte35SpliceInsertProperty.AdAvailOffset``.
            :param no_regional_blackout_flag: ``CfnChannel.Scte35SpliceInsertProperty.NoRegionalBlackoutFlag``.
            :param web_delivery_allowed_flag: ``CfnChannel.Scte35SpliceInsertProperty.WebDeliveryAllowedFlag``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_avail_offset is not None:
                self._values["ad_avail_offset"] = ad_avail_offset
            if no_regional_blackout_flag is not None:
                self._values["no_regional_blackout_flag"] = no_regional_blackout_flag
            if web_delivery_allowed_flag is not None:
                self._values["web_delivery_allowed_flag"] = web_delivery_allowed_flag

        @builtins.property
        def ad_avail_offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Scte35SpliceInsertProperty.AdAvailOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html#cfn-medialive-channel-scte35spliceinsert-adavailoffset
            '''
            result = self._values.get("ad_avail_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def no_regional_blackout_flag(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Scte35SpliceInsertProperty.NoRegionalBlackoutFlag``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html#cfn-medialive-channel-scte35spliceinsert-noregionalblackoutflag
            '''
            result = self._values.get("no_regional_blackout_flag")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def web_delivery_allowed_flag(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Scte35SpliceInsertProperty.WebDeliveryAllowedFlag``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html#cfn-medialive-channel-scte35spliceinsert-webdeliveryallowedflag
            '''
            result = self._values.get("web_delivery_allowed_flag")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte35SpliceInsertProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.Scte35TimeSignalAposProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_avail_offset": "adAvailOffset",
            "no_regional_blackout_flag": "noRegionalBlackoutFlag",
            "web_delivery_allowed_flag": "webDeliveryAllowedFlag",
        },
    )
    class Scte35TimeSignalAposProperty:
        def __init__(
            self,
            *,
            ad_avail_offset: typing.Optional[jsii.Number] = None,
            no_regional_blackout_flag: typing.Optional[builtins.str] = None,
            web_delivery_allowed_flag: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param ad_avail_offset: ``CfnChannel.Scte35TimeSignalAposProperty.AdAvailOffset``.
            :param no_regional_blackout_flag: ``CfnChannel.Scte35TimeSignalAposProperty.NoRegionalBlackoutFlag``.
            :param web_delivery_allowed_flag: ``CfnChannel.Scte35TimeSignalAposProperty.WebDeliveryAllowedFlag``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_avail_offset is not None:
                self._values["ad_avail_offset"] = ad_avail_offset
            if no_regional_blackout_flag is not None:
                self._values["no_regional_blackout_flag"] = no_regional_blackout_flag
            if web_delivery_allowed_flag is not None:
                self._values["web_delivery_allowed_flag"] = web_delivery_allowed_flag

        @builtins.property
        def ad_avail_offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.Scte35TimeSignalAposProperty.AdAvailOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html#cfn-medialive-channel-scte35timesignalapos-adavailoffset
            '''
            result = self._values.get("ad_avail_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def no_regional_blackout_flag(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Scte35TimeSignalAposProperty.NoRegionalBlackoutFlag``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html#cfn-medialive-channel-scte35timesignalapos-noregionalblackoutflag
            '''
            result = self._values.get("no_regional_blackout_flag")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def web_delivery_allowed_flag(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.Scte35TimeSignalAposProperty.WebDeliveryAllowedFlag``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html#cfn-medialive-channel-scte35timesignalapos-webdeliveryallowedflag
            '''
            result = self._values.get("web_delivery_allowed_flag")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Scte35TimeSignalAposProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.SmpteTtDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class SmpteTtDestinationSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-smptettdestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SmpteTtDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.StandardHlsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_rendition_sets": "audioRenditionSets",
            "m3_u8_settings": "m3U8Settings",
        },
    )
    class StandardHlsSettingsProperty:
        def __init__(
            self,
            *,
            audio_rendition_sets: typing.Optional[builtins.str] = None,
            m3_u8_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.M3u8SettingsProperty"]] = None,
        ) -> None:
            '''
            :param audio_rendition_sets: ``CfnChannel.StandardHlsSettingsProperty.AudioRenditionSets``.
            :param m3_u8_settings: ``CfnChannel.StandardHlsSettingsProperty.M3u8Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if audio_rendition_sets is not None:
                self._values["audio_rendition_sets"] = audio_rendition_sets
            if m3_u8_settings is not None:
                self._values["m3_u8_settings"] = m3_u8_settings

        @builtins.property
        def audio_rendition_sets(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.StandardHlsSettingsProperty.AudioRenditionSets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html#cfn-medialive-channel-standardhlssettings-audiorenditionsets
            '''
            result = self._values.get("audio_rendition_sets")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def m3_u8_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.M3u8SettingsProperty"]]:
            '''``CfnChannel.StandardHlsSettingsProperty.M3u8Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html#cfn-medialive-channel-standardhlssettings-m3u8settings
            '''
            result = self._values.get("m3_u8_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.M3u8SettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StandardHlsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.StaticKeySettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key_provider_server": "keyProviderServer",
            "static_key_value": "staticKeyValue",
        },
    )
    class StaticKeySettingsProperty:
        def __init__(
            self,
            *,
            key_provider_server: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]] = None,
            static_key_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key_provider_server: ``CfnChannel.StaticKeySettingsProperty.KeyProviderServer``.
            :param static_key_value: ``CfnChannel.StaticKeySettingsProperty.StaticKeyValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key_provider_server is not None:
                self._values["key_provider_server"] = key_provider_server
            if static_key_value is not None:
                self._values["static_key_value"] = static_key_value

        @builtins.property
        def key_provider_server(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]]:
            '''``CfnChannel.StaticKeySettingsProperty.KeyProviderServer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html#cfn-medialive-channel-statickeysettings-keyproviderserver
            '''
            result = self._values.get("key_provider_server")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.InputLocationProperty"]], result)

        @builtins.property
        def static_key_value(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.StaticKeySettingsProperty.StaticKeyValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html#cfn-medialive-channel-statickeysettings-statickeyvalue
            '''
            result = self._values.get("static_key_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StaticKeySettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.TeletextDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class TeletextDestinationSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextdestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TeletextDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.TeletextSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "output_rectangle": "outputRectangle",
            "page_number": "pageNumber",
        },
    )
    class TeletextSourceSettingsProperty:
        def __init__(
            self,
            *,
            output_rectangle: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionRectangleProperty"]] = None,
            page_number: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param output_rectangle: ``CfnChannel.TeletextSourceSettingsProperty.OutputRectangle``.
            :param page_number: ``CfnChannel.TeletextSourceSettingsProperty.PageNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if output_rectangle is not None:
                self._values["output_rectangle"] = output_rectangle
            if page_number is not None:
                self._values["page_number"] = page_number

        @builtins.property
        def output_rectangle(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionRectangleProperty"]]:
            '''``CfnChannel.TeletextSourceSettingsProperty.OutputRectangle``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html#cfn-medialive-channel-teletextsourcesettings-outputrectangle
            '''
            result = self._values.get("output_rectangle")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CaptionRectangleProperty"]], result)

        @builtins.property
        def page_number(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.TeletextSourceSettingsProperty.PageNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html#cfn-medialive-channel-teletextsourcesettings-pagenumber
            '''
            result = self._values.get("page_number")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TeletextSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.TemporalFilterSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "post_filter_sharpening": "postFilterSharpening",
            "strength": "strength",
        },
    )
    class TemporalFilterSettingsProperty:
        def __init__(
            self,
            *,
            post_filter_sharpening: typing.Optional[builtins.str] = None,
            strength: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param post_filter_sharpening: ``CfnChannel.TemporalFilterSettingsProperty.PostFilterSharpening``.
            :param strength: ``CfnChannel.TemporalFilterSettingsProperty.Strength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if post_filter_sharpening is not None:
                self._values["post_filter_sharpening"] = post_filter_sharpening
            if strength is not None:
                self._values["strength"] = strength

        @builtins.property
        def post_filter_sharpening(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.TemporalFilterSettingsProperty.PostFilterSharpening``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html#cfn-medialive-channel-temporalfiltersettings-postfiltersharpening
            '''
            result = self._values.get("post_filter_sharpening")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strength(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.TemporalFilterSettingsProperty.Strength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html#cfn-medialive-channel-temporalfiltersettings-strength
            '''
            result = self._values.get("strength")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemporalFilterSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.TimecodeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source", "sync_threshold": "syncThreshold"},
    )
    class TimecodeConfigProperty:
        def __init__(
            self,
            *,
            source: typing.Optional[builtins.str] = None,
            sync_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param source: ``CfnChannel.TimecodeConfigProperty.Source``.
            :param sync_threshold: ``CfnChannel.TimecodeConfigProperty.SyncThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source
            if sync_threshold is not None:
                self._values["sync_threshold"] = sync_threshold

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.TimecodeConfigProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html#cfn-medialive-channel-timecodeconfig-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sync_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.TimecodeConfigProperty.SyncThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html#cfn-medialive-channel-timecodeconfig-syncthreshold
            '''
            result = self._values.get("sync_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimecodeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.TtmlDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"style_control": "styleControl"},
    )
    class TtmlDestinationSettingsProperty:
        def __init__(
            self,
            *,
            style_control: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param style_control: ``CfnChannel.TtmlDestinationSettingsProperty.StyleControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if style_control is not None:
                self._values["style_control"] = style_control

        @builtins.property
        def style_control(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.TtmlDestinationSettingsProperty.StyleControl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html#cfn-medialive-channel-ttmldestinationsettings-stylecontrol
            '''
            result = self._values.get("style_control")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TtmlDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.UdpContainerSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"m2_ts_settings": "m2TsSettings"},
    )
    class UdpContainerSettingsProperty:
        def __init__(
            self,
            *,
            m2_ts_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.M2tsSettingsProperty"]] = None,
        ) -> None:
            '''
            :param m2_ts_settings: ``CfnChannel.UdpContainerSettingsProperty.M2tsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if m2_ts_settings is not None:
                self._values["m2_ts_settings"] = m2_ts_settings

        @builtins.property
        def m2_ts_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.M2tsSettingsProperty"]]:
            '''``CfnChannel.UdpContainerSettingsProperty.M2tsSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html#cfn-medialive-channel-udpcontainersettings-m2tssettings
            '''
            result = self._values.get("m2_ts_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.M2tsSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UdpContainerSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.UdpGroupSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_loss_action": "inputLossAction",
            "timed_metadata_id3_frame": "timedMetadataId3Frame",
            "timed_metadata_id3_period": "timedMetadataId3Period",
        },
    )
    class UdpGroupSettingsProperty:
        def __init__(
            self,
            *,
            input_loss_action: typing.Optional[builtins.str] = None,
            timed_metadata_id3_frame: typing.Optional[builtins.str] = None,
            timed_metadata_id3_period: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param input_loss_action: ``CfnChannel.UdpGroupSettingsProperty.InputLossAction``.
            :param timed_metadata_id3_frame: ``CfnChannel.UdpGroupSettingsProperty.TimedMetadataId3Frame``.
            :param timed_metadata_id3_period: ``CfnChannel.UdpGroupSettingsProperty.TimedMetadataId3Period``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if input_loss_action is not None:
                self._values["input_loss_action"] = input_loss_action
            if timed_metadata_id3_frame is not None:
                self._values["timed_metadata_id3_frame"] = timed_metadata_id3_frame
            if timed_metadata_id3_period is not None:
                self._values["timed_metadata_id3_period"] = timed_metadata_id3_period

        @builtins.property
        def input_loss_action(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.UdpGroupSettingsProperty.InputLossAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html#cfn-medialive-channel-udpgroupsettings-inputlossaction
            '''
            result = self._values.get("input_loss_action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timed_metadata_id3_frame(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.UdpGroupSettingsProperty.TimedMetadataId3Frame``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html#cfn-medialive-channel-udpgroupsettings-timedmetadataid3frame
            '''
            result = self._values.get("timed_metadata_id3_frame")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timed_metadata_id3_period(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.UdpGroupSettingsProperty.TimedMetadataId3Period``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html#cfn-medialive-channel-udpgroupsettings-timedmetadataid3period
            '''
            result = self._values.get("timed_metadata_id3_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UdpGroupSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.UdpOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "buffer_msec": "bufferMsec",
            "container_settings": "containerSettings",
            "destination": "destination",
            "fec_output_settings": "fecOutputSettings",
        },
    )
    class UdpOutputSettingsProperty:
        def __init__(
            self,
            *,
            buffer_msec: typing.Optional[jsii.Number] = None,
            container_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.UdpContainerSettingsProperty"]] = None,
            destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]] = None,
            fec_output_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FecOutputSettingsProperty"]] = None,
        ) -> None:
            '''
            :param buffer_msec: ``CfnChannel.UdpOutputSettingsProperty.BufferMsec``.
            :param container_settings: ``CfnChannel.UdpOutputSettingsProperty.ContainerSettings``.
            :param destination: ``CfnChannel.UdpOutputSettingsProperty.Destination``.
            :param fec_output_settings: ``CfnChannel.UdpOutputSettingsProperty.FecOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if buffer_msec is not None:
                self._values["buffer_msec"] = buffer_msec
            if container_settings is not None:
                self._values["container_settings"] = container_settings
            if destination is not None:
                self._values["destination"] = destination
            if fec_output_settings is not None:
                self._values["fec_output_settings"] = fec_output_settings

        @builtins.property
        def buffer_msec(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.UdpOutputSettingsProperty.BufferMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-buffermsec
            '''
            result = self._values.get("buffer_msec")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def container_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.UdpContainerSettingsProperty"]]:
            '''``CfnChannel.UdpOutputSettingsProperty.ContainerSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-containersettings
            '''
            result = self._values.get("container_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.UdpContainerSettingsProperty"]], result)

        @builtins.property
        def destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]]:
            '''``CfnChannel.UdpOutputSettingsProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.OutputLocationRefProperty"]], result)

        @builtins.property
        def fec_output_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FecOutputSettingsProperty"]]:
            '''``CfnChannel.UdpOutputSettingsProperty.FecOutputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-fecoutputsettings
            '''
            result = self._values.get("fec_output_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FecOutputSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UdpOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.VideoBlackFailoverSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "black_detect_threshold": "blackDetectThreshold",
            "video_black_threshold_msec": "videoBlackThresholdMsec",
        },
    )
    class VideoBlackFailoverSettingsProperty:
        def __init__(
            self,
            *,
            black_detect_threshold: typing.Optional[jsii.Number] = None,
            video_black_threshold_msec: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param black_detect_threshold: ``CfnChannel.VideoBlackFailoverSettingsProperty.BlackDetectThreshold``.
            :param video_black_threshold_msec: ``CfnChannel.VideoBlackFailoverSettingsProperty.VideoBlackThresholdMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoblackfailoversettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if black_detect_threshold is not None:
                self._values["black_detect_threshold"] = black_detect_threshold
            if video_black_threshold_msec is not None:
                self._values["video_black_threshold_msec"] = video_black_threshold_msec

        @builtins.property
        def black_detect_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.VideoBlackFailoverSettingsProperty.BlackDetectThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoblackfailoversettings.html#cfn-medialive-channel-videoblackfailoversettings-blackdetectthreshold
            '''
            result = self._values.get("black_detect_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def video_black_threshold_msec(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.VideoBlackFailoverSettingsProperty.VideoBlackThresholdMsec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoblackfailoversettings.html#cfn-medialive-channel-videoblackfailoversettings-videoblackthresholdmsec
            '''
            result = self._values.get("video_black_threshold_msec")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoBlackFailoverSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.VideoCodecSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "frame_capture_settings": "frameCaptureSettings",
            "h264_settings": "h264Settings",
            "h265_settings": "h265Settings",
            "mpeg2_settings": "mpeg2Settings",
        },
    )
    class VideoCodecSettingsProperty:
        def __init__(
            self,
            *,
            frame_capture_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureSettingsProperty"]] = None,
            h264_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H264SettingsProperty"]] = None,
            h265_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H265SettingsProperty"]] = None,
            mpeg2_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Mpeg2SettingsProperty"]] = None,
        ) -> None:
            '''
            :param frame_capture_settings: ``CfnChannel.VideoCodecSettingsProperty.FrameCaptureSettings``.
            :param h264_settings: ``CfnChannel.VideoCodecSettingsProperty.H264Settings``.
            :param h265_settings: ``CfnChannel.VideoCodecSettingsProperty.H265Settings``.
            :param mpeg2_settings: ``CfnChannel.VideoCodecSettingsProperty.Mpeg2Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if frame_capture_settings is not None:
                self._values["frame_capture_settings"] = frame_capture_settings
            if h264_settings is not None:
                self._values["h264_settings"] = h264_settings
            if h265_settings is not None:
                self._values["h265_settings"] = h265_settings
            if mpeg2_settings is not None:
                self._values["mpeg2_settings"] = mpeg2_settings

        @builtins.property
        def frame_capture_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureSettingsProperty"]]:
            '''``CfnChannel.VideoCodecSettingsProperty.FrameCaptureSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-framecapturesettings
            '''
            result = self._values.get("frame_capture_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.FrameCaptureSettingsProperty"]], result)

        @builtins.property
        def h264_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H264SettingsProperty"]]:
            '''``CfnChannel.VideoCodecSettingsProperty.H264Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-h264settings
            '''
            result = self._values.get("h264_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H264SettingsProperty"]], result)

        @builtins.property
        def h265_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H265SettingsProperty"]]:
            '''``CfnChannel.VideoCodecSettingsProperty.H265Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-h265settings
            '''
            result = self._values.get("h265_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.H265SettingsProperty"]], result)

        @builtins.property
        def mpeg2_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Mpeg2SettingsProperty"]]:
            '''``CfnChannel.VideoCodecSettingsProperty.Mpeg2Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-mpeg2settings
            '''
            result = self._values.get("mpeg2_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Mpeg2SettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoCodecSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.VideoDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "codec_settings": "codecSettings",
            "height": "height",
            "name": "name",
            "respond_to_afd": "respondToAfd",
            "scaling_behavior": "scalingBehavior",
            "sharpness": "sharpness",
            "width": "width",
        },
    )
    class VideoDescriptionProperty:
        def __init__(
            self,
            *,
            codec_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoCodecSettingsProperty"]] = None,
            height: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
            respond_to_afd: typing.Optional[builtins.str] = None,
            scaling_behavior: typing.Optional[builtins.str] = None,
            sharpness: typing.Optional[jsii.Number] = None,
            width: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param codec_settings: ``CfnChannel.VideoDescriptionProperty.CodecSettings``.
            :param height: ``CfnChannel.VideoDescriptionProperty.Height``.
            :param name: ``CfnChannel.VideoDescriptionProperty.Name``.
            :param respond_to_afd: ``CfnChannel.VideoDescriptionProperty.RespondToAfd``.
            :param scaling_behavior: ``CfnChannel.VideoDescriptionProperty.ScalingBehavior``.
            :param sharpness: ``CfnChannel.VideoDescriptionProperty.Sharpness``.
            :param width: ``CfnChannel.VideoDescriptionProperty.Width``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if codec_settings is not None:
                self._values["codec_settings"] = codec_settings
            if height is not None:
                self._values["height"] = height
            if name is not None:
                self._values["name"] = name
            if respond_to_afd is not None:
                self._values["respond_to_afd"] = respond_to_afd
            if scaling_behavior is not None:
                self._values["scaling_behavior"] = scaling_behavior
            if sharpness is not None:
                self._values["sharpness"] = sharpness
            if width is not None:
                self._values["width"] = width

        @builtins.property
        def codec_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoCodecSettingsProperty"]]:
            '''``CfnChannel.VideoDescriptionProperty.CodecSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-codecsettings
            '''
            result = self._values.get("codec_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoCodecSettingsProperty"]], result)

        @builtins.property
        def height(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.VideoDescriptionProperty.Height``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-height
            '''
            result = self._values.get("height")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.VideoDescriptionProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def respond_to_afd(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.VideoDescriptionProperty.RespondToAfd``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-respondtoafd
            '''
            result = self._values.get("respond_to_afd")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scaling_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.VideoDescriptionProperty.ScalingBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-scalingbehavior
            '''
            result = self._values.get("scaling_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sharpness(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.VideoDescriptionProperty.Sharpness``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-sharpness
            '''
            result = self._values.get("sharpness")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def width(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.VideoDescriptionProperty.Width``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-width
            '''
            result = self._values.get("width")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.VideoSelectorColorSpaceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"hdr10_settings": "hdr10Settings"},
    )
    class VideoSelectorColorSpaceSettingsProperty:
        def __init__(
            self,
            *,
            hdr10_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Hdr10SettingsProperty"]] = None,
        ) -> None:
            '''
            :param hdr10_settings: ``CfnChannel.VideoSelectorColorSpaceSettingsProperty.Hdr10Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorcolorspacesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if hdr10_settings is not None:
                self._values["hdr10_settings"] = hdr10_settings

        @builtins.property
        def hdr10_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Hdr10SettingsProperty"]]:
            '''``CfnChannel.VideoSelectorColorSpaceSettingsProperty.Hdr10Settings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorcolorspacesettings.html#cfn-medialive-channel-videoselectorcolorspacesettings-hdr10settings
            '''
            result = self._values.get("hdr10_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.Hdr10SettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoSelectorColorSpaceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.VideoSelectorPidProperty",
        jsii_struct_bases=[],
        name_mapping={"pid": "pid"},
    )
    class VideoSelectorPidProperty:
        def __init__(self, *, pid: typing.Optional[jsii.Number] = None) -> None:
            '''
            :param pid: ``CfnChannel.VideoSelectorPidProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorpid.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if pid is not None:
                self._values["pid"] = pid

        @builtins.property
        def pid(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.VideoSelectorPidProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorpid.html#cfn-medialive-channel-videoselectorpid-pid
            '''
            result = self._values.get("pid")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoSelectorPidProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.VideoSelectorProgramIdProperty",
        jsii_struct_bases=[],
        name_mapping={"program_id": "programId"},
    )
    class VideoSelectorProgramIdProperty:
        def __init__(self, *, program_id: typing.Optional[jsii.Number] = None) -> None:
            '''
            :param program_id: ``CfnChannel.VideoSelectorProgramIdProperty.ProgramId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorprogramid.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if program_id is not None:
                self._values["program_id"] = program_id

        @builtins.property
        def program_id(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.VideoSelectorProgramIdProperty.ProgramId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorprogramid.html#cfn-medialive-channel-videoselectorprogramid-programid
            '''
            result = self._values.get("program_id")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoSelectorProgramIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.VideoSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "color_space": "colorSpace",
            "color_space_settings": "colorSpaceSettings",
            "color_space_usage": "colorSpaceUsage",
            "selector_settings": "selectorSettings",
        },
    )
    class VideoSelectorProperty:
        def __init__(
            self,
            *,
            color_space: typing.Optional[builtins.str] = None,
            color_space_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorColorSpaceSettingsProperty"]] = None,
            color_space_usage: typing.Optional[builtins.str] = None,
            selector_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorSettingsProperty"]] = None,
        ) -> None:
            '''
            :param color_space: ``CfnChannel.VideoSelectorProperty.ColorSpace``.
            :param color_space_settings: ``CfnChannel.VideoSelectorProperty.ColorSpaceSettings``.
            :param color_space_usage: ``CfnChannel.VideoSelectorProperty.ColorSpaceUsage``.
            :param selector_settings: ``CfnChannel.VideoSelectorProperty.SelectorSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if color_space is not None:
                self._values["color_space"] = color_space
            if color_space_settings is not None:
                self._values["color_space_settings"] = color_space_settings
            if color_space_usage is not None:
                self._values["color_space_usage"] = color_space_usage
            if selector_settings is not None:
                self._values["selector_settings"] = selector_settings

        @builtins.property
        def color_space(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.VideoSelectorProperty.ColorSpace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-colorspace
            '''
            result = self._values.get("color_space")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def color_space_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorColorSpaceSettingsProperty"]]:
            '''``CfnChannel.VideoSelectorProperty.ColorSpaceSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-colorspacesettings
            '''
            result = self._values.get("color_space_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorColorSpaceSettingsProperty"]], result)

        @builtins.property
        def color_space_usage(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.VideoSelectorProperty.ColorSpaceUsage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-colorspaceusage
            '''
            result = self._values.get("color_space_usage")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def selector_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorSettingsProperty"]]:
            '''``CfnChannel.VideoSelectorProperty.SelectorSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-selectorsettings
            '''
            result = self._values.get("selector_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.VideoSelectorSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "video_selector_pid": "videoSelectorPid",
            "video_selector_program_id": "videoSelectorProgramId",
        },
    )
    class VideoSelectorSettingsProperty:
        def __init__(
            self,
            *,
            video_selector_pid: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorPidProperty"]] = None,
            video_selector_program_id: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorProgramIdProperty"]] = None,
        ) -> None:
            '''
            :param video_selector_pid: ``CfnChannel.VideoSelectorSettingsProperty.VideoSelectorPid``.
            :param video_selector_program_id: ``CfnChannel.VideoSelectorSettingsProperty.VideoSelectorProgramId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if video_selector_pid is not None:
                self._values["video_selector_pid"] = video_selector_pid
            if video_selector_program_id is not None:
                self._values["video_selector_program_id"] = video_selector_program_id

        @builtins.property
        def video_selector_pid(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorPidProperty"]]:
            '''``CfnChannel.VideoSelectorSettingsProperty.VideoSelectorPid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html#cfn-medialive-channel-videoselectorsettings-videoselectorpid
            '''
            result = self._values.get("video_selector_pid")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorPidProperty"]], result)

        @builtins.property
        def video_selector_program_id(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorProgramIdProperty"]]:
            '''``CfnChannel.VideoSelectorSettingsProperty.VideoSelectorProgramId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html#cfn-medialive-channel-videoselectorsettings-videoselectorprogramid
            '''
            result = self._values.get("video_selector_program_id")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.VideoSelectorProgramIdProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoSelectorSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.VpcOutputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "public_address_allocation_ids": "publicAddressAllocationIds",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcOutputSettingsProperty:
        def __init__(
            self,
            *,
            public_address_allocation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param public_address_allocation_ids: ``CfnChannel.VpcOutputSettingsProperty.PublicAddressAllocationIds``.
            :param security_group_ids: ``CfnChannel.VpcOutputSettingsProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnChannel.VpcOutputSettingsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-vpcoutputsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if public_address_allocation_ids is not None:
                self._values["public_address_allocation_ids"] = public_address_allocation_ids
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def public_address_allocation_ids(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnChannel.VpcOutputSettingsProperty.PublicAddressAllocationIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-vpcoutputsettings.html#cfn-medialive-channel-vpcoutputsettings-publicaddressallocationids
            '''
            result = self._values.get("public_address_allocation_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnChannel.VpcOutputSettingsProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-vpcoutputsettings.html#cfn-medialive-channel-vpcoutputsettings-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnChannel.VpcOutputSettingsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-vpcoutputsettings.html#cfn-medialive-channel-vpcoutputsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcOutputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.WavSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bit_depth": "bitDepth",
            "coding_mode": "codingMode",
            "sample_rate": "sampleRate",
        },
    )
    class WavSettingsProperty:
        def __init__(
            self,
            *,
            bit_depth: typing.Optional[jsii.Number] = None,
            coding_mode: typing.Optional[builtins.str] = None,
            sample_rate: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param bit_depth: ``CfnChannel.WavSettingsProperty.BitDepth``.
            :param coding_mode: ``CfnChannel.WavSettingsProperty.CodingMode``.
            :param sample_rate: ``CfnChannel.WavSettingsProperty.SampleRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-wavsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if bit_depth is not None:
                self._values["bit_depth"] = bit_depth
            if coding_mode is not None:
                self._values["coding_mode"] = coding_mode
            if sample_rate is not None:
                self._values["sample_rate"] = sample_rate

        @builtins.property
        def bit_depth(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.WavSettingsProperty.BitDepth``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-wavsettings.html#cfn-medialive-channel-wavsettings-bitdepth
            '''
            result = self._values.get("bit_depth")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def coding_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.WavSettingsProperty.CodingMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-wavsettings.html#cfn-medialive-channel-wavsettings-codingmode
            '''
            result = self._values.get("coding_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sample_rate(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.WavSettingsProperty.SampleRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-wavsettings.html#cfn-medialive-channel-wavsettings-samplerate
            '''
            result = self._values.get("sample_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WavSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnChannel.WebvttDestinationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class WebvttDestinationSettingsProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebvttDestinationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-medialive.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "cdi_input_specification": "cdiInputSpecification",
        "channel_class": "channelClass",
        "destinations": "destinations",
        "encoder_settings": "encoderSettings",
        "input_attachments": "inputAttachments",
        "input_specification": "inputSpecification",
        "log_level": "logLevel",
        "name": "name",
        "role_arn": "roleArn",
        "tags": "tags",
        "vpc": "vpc",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        cdi_input_specification: typing.Optional[typing.Union[CfnChannel.CdiInputSpecificationProperty, aws_cdk.core.IResolvable]] = None,
        channel_class: typing.Optional[builtins.str] = None,
        destinations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnChannel.OutputDestinationProperty]]]] = None,
        encoder_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.EncoderSettingsProperty]] = None,
        input_attachments: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnChannel.InputAttachmentProperty]]]] = None,
        input_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.InputSpecificationProperty]] = None,
        log_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        vpc: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.VpcOutputSettingsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaLive::Channel``.

        :param cdi_input_specification: ``AWS::MediaLive::Channel.CdiInputSpecification``.
        :param channel_class: ``AWS::MediaLive::Channel.ChannelClass``.
        :param destinations: ``AWS::MediaLive::Channel.Destinations``.
        :param encoder_settings: ``AWS::MediaLive::Channel.EncoderSettings``.
        :param input_attachments: ``AWS::MediaLive::Channel.InputAttachments``.
        :param input_specification: ``AWS::MediaLive::Channel.InputSpecification``.
        :param log_level: ``AWS::MediaLive::Channel.LogLevel``.
        :param name: ``AWS::MediaLive::Channel.Name``.
        :param role_arn: ``AWS::MediaLive::Channel.RoleArn``.
        :param tags: ``AWS::MediaLive::Channel.Tags``.
        :param vpc: ``AWS::MediaLive::Channel.Vpc``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if cdi_input_specification is not None:
            self._values["cdi_input_specification"] = cdi_input_specification
        if channel_class is not None:
            self._values["channel_class"] = channel_class
        if destinations is not None:
            self._values["destinations"] = destinations
        if encoder_settings is not None:
            self._values["encoder_settings"] = encoder_settings
        if input_attachments is not None:
            self._values["input_attachments"] = input_attachments
        if input_specification is not None:
            self._values["input_specification"] = input_specification
        if log_level is not None:
            self._values["log_level"] = log_level
        if name is not None:
            self._values["name"] = name
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def cdi_input_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnChannel.CdiInputSpecificationProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::MediaLive::Channel.CdiInputSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-cdiinputspecification
        '''
        result = self._values.get("cdi_input_specification")
        return typing.cast(typing.Optional[typing.Union[CfnChannel.CdiInputSpecificationProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def channel_class(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Channel.ChannelClass``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-channelclass
        '''
        result = self._values.get("channel_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnChannel.OutputDestinationProperty]]]]:
        '''``AWS::MediaLive::Channel.Destinations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-destinations
        '''
        result = self._values.get("destinations")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnChannel.OutputDestinationProperty]]]], result)

    @builtins.property
    def encoder_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.EncoderSettingsProperty]]:
        '''``AWS::MediaLive::Channel.EncoderSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-encodersettings
        '''
        result = self._values.get("encoder_settings")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.EncoderSettingsProperty]], result)

    @builtins.property
    def input_attachments(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnChannel.InputAttachmentProperty]]]]:
        '''``AWS::MediaLive::Channel.InputAttachments``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputattachments
        '''
        result = self._values.get("input_attachments")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnChannel.InputAttachmentProperty]]]], result)

    @builtins.property
    def input_specification(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.InputSpecificationProperty]]:
        '''``AWS::MediaLive::Channel.InputSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputspecification
        '''
        result = self._values.get("input_specification")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.InputSpecificationProperty]], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Channel.LogLevel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-loglevel
        '''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Channel.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Channel.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::MediaLive::Channel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def vpc(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.VpcOutputSettingsProperty]]:
        '''``AWS::MediaLive::Channel.Vpc``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-vpc
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.VpcOutputSettingsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInput(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-medialive.CfnInput",
):
    '''A CloudFormation ``AWS::MediaLive::Input``.

    :cloudformationResource: AWS::MediaLive::Input
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        destinations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDestinationRequestProperty"]]]] = None,
        input_devices: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDeviceSettingsProperty"]]]] = None,
        input_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        media_connect_flows: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInput.MediaConnectFlowRequestProperty"]]]] = None,
        name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputSourceRequestProperty"]]]] = None,
        tags: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputVpcRequestProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaLive::Input``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param destinations: ``AWS::MediaLive::Input.Destinations``.
        :param input_devices: ``AWS::MediaLive::Input.InputDevices``.
        :param input_security_groups: ``AWS::MediaLive::Input.InputSecurityGroups``.
        :param media_connect_flows: ``AWS::MediaLive::Input.MediaConnectFlows``.
        :param name: ``AWS::MediaLive::Input.Name``.
        :param role_arn: ``AWS::MediaLive::Input.RoleArn``.
        :param sources: ``AWS::MediaLive::Input.Sources``.
        :param tags: ``AWS::MediaLive::Input.Tags``.
        :param type: ``AWS::MediaLive::Input.Type``.
        :param vpc: ``AWS::MediaLive::Input.Vpc``.
        '''
        props = CfnInputProps(
            destinations=destinations,
            input_devices=input_devices,
            input_security_groups=input_security_groups,
            media_connect_flows=media_connect_flows,
            name=name,
            role_arn=role_arn,
            sources=sources,
            tags=tags,
            type=type,
            vpc=vpc,
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
    @jsii.member(jsii_name="attrDestinations")
    def attr_destinations(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: Destinations
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDestinations"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSources")
    def attr_sources(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: Sources
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrSources"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::MediaLive::Input.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="destinations")
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDestinationRequestProperty"]]]]:
        '''``AWS::MediaLive::Input.Destinations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-destinations
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDestinationRequestProperty"]]]], jsii.get(self, "destinations"))

    @destinations.setter
    def destinations(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDestinationRequestProperty"]]]],
    ) -> None:
        jsii.set(self, "destinations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inputDevices")
    def input_devices(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDeviceSettingsProperty"]]]]:
        '''``AWS::MediaLive::Input.InputDevices``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputdevices
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDeviceSettingsProperty"]]]], jsii.get(self, "inputDevices"))

    @input_devices.setter
    def input_devices(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDeviceSettingsProperty"]]]],
    ) -> None:
        jsii.set(self, "inputDevices", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inputSecurityGroups")
    def input_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::MediaLive::Input.InputSecurityGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputsecuritygroups
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inputSecurityGroups"))

    @input_security_groups.setter
    def input_security_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "inputSecurityGroups", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mediaConnectFlows")
    def media_connect_flows(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.MediaConnectFlowRequestProperty"]]]]:
        '''``AWS::MediaLive::Input.MediaConnectFlows``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-mediaconnectflows
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.MediaConnectFlowRequestProperty"]]]], jsii.get(self, "mediaConnectFlows"))

    @media_connect_flows.setter
    def media_connect_flows(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.MediaConnectFlowRequestProperty"]]]],
    ) -> None:
        jsii.set(self, "mediaConnectFlows", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Input.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Input.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputSourceRequestProperty"]]]]:
        '''``AWS::MediaLive::Input.Sources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-sources
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputSourceRequestProperty"]]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputSourceRequestProperty"]]]],
    ) -> None:
        jsii.set(self, "sources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Input.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpc")
    def vpc(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputVpcRequestProperty"]]:
        '''``AWS::MediaLive::Input.Vpc``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-vpc
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputVpcRequestProperty"]], jsii.get(self, "vpc"))

    @vpc.setter
    def vpc(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputVpcRequestProperty"]],
    ) -> None:
        jsii.set(self, "vpc", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnInput.InputDestinationRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"stream_name": "streamName"},
    )
    class InputDestinationRequestProperty:
        def __init__(
            self,
            *,
            stream_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param stream_name: ``CfnInput.InputDestinationRequestProperty.StreamName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdestinationrequest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if stream_name is not None:
                self._values["stream_name"] = stream_name

        @builtins.property
        def stream_name(self) -> typing.Optional[builtins.str]:
            '''``CfnInput.InputDestinationRequestProperty.StreamName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdestinationrequest.html#cfn-medialive-input-inputdestinationrequest-streamname
            '''
            result = self._values.get("stream_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputDestinationRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnInput.InputDeviceRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class InputDeviceRequestProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            '''
            :param id: ``CfnInput.InputDeviceRequestProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''``CfnInput.InputDeviceRequestProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html#cfn-medialive-input-inputdevicerequest-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputDeviceRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnInput.InputDeviceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class InputDeviceSettingsProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            '''
            :param id: ``CfnInput.InputDeviceSettingsProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''``CfnInput.InputDeviceSettingsProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html#cfn-medialive-input-inputdevicesettings-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputDeviceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnInput.InputSourceRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password_param": "passwordParam",
            "url": "url",
            "username": "username",
        },
    )
    class InputSourceRequestProperty:
        def __init__(
            self,
            *,
            password_param: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param password_param: ``CfnInput.InputSourceRequestProperty.PasswordParam``.
            :param url: ``CfnInput.InputSourceRequestProperty.Url``.
            :param username: ``CfnInput.InputSourceRequestProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if password_param is not None:
                self._values["password_param"] = password_param
            if url is not None:
                self._values["url"] = url
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password_param(self) -> typing.Optional[builtins.str]:
            '''``CfnInput.InputSourceRequestProperty.PasswordParam``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html#cfn-medialive-input-inputsourcerequest-passwordparam
            '''
            result = self._values.get("password_param")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnInput.InputSourceRequestProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html#cfn-medialive-input-inputsourcerequest-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''``CfnInput.InputSourceRequestProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html#cfn-medialive-input-inputsourcerequest-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSourceRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnInput.InputVpcRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class InputVpcRequestProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param security_group_ids: ``CfnInput.InputVpcRequestProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnInput.InputVpcRequestProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnInput.InputVpcRequestProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html#cfn-medialive-input-inputvpcrequest-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnInput.InputVpcRequestProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html#cfn-medialive-input-inputvpcrequest-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputVpcRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnInput.MediaConnectFlowRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"flow_arn": "flowArn"},
    )
    class MediaConnectFlowRequestProperty:
        def __init__(self, *, flow_arn: typing.Optional[builtins.str] = None) -> None:
            '''
            :param flow_arn: ``CfnInput.MediaConnectFlowRequestProperty.FlowArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-mediaconnectflowrequest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if flow_arn is not None:
                self._values["flow_arn"] = flow_arn

        @builtins.property
        def flow_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnInput.MediaConnectFlowRequestProperty.FlowArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-mediaconnectflowrequest.html#cfn-medialive-input-mediaconnectflowrequest-flowarn
            '''
            result = self._values.get("flow_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaConnectFlowRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-medialive.CfnInputProps",
    jsii_struct_bases=[],
    name_mapping={
        "destinations": "destinations",
        "input_devices": "inputDevices",
        "input_security_groups": "inputSecurityGroups",
        "media_connect_flows": "mediaConnectFlows",
        "name": "name",
        "role_arn": "roleArn",
        "sources": "sources",
        "tags": "tags",
        "type": "type",
        "vpc": "vpc",
    },
)
class CfnInputProps:
    def __init__(
        self,
        *,
        destinations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputDestinationRequestProperty]]]] = None,
        input_devices: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputDeviceSettingsProperty]]]] = None,
        input_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        media_connect_flows: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnInput.MediaConnectFlowRequestProperty]]]] = None,
        name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputSourceRequestProperty]]]] = None,
        tags: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputVpcRequestProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaLive::Input``.

        :param destinations: ``AWS::MediaLive::Input.Destinations``.
        :param input_devices: ``AWS::MediaLive::Input.InputDevices``.
        :param input_security_groups: ``AWS::MediaLive::Input.InputSecurityGroups``.
        :param media_connect_flows: ``AWS::MediaLive::Input.MediaConnectFlows``.
        :param name: ``AWS::MediaLive::Input.Name``.
        :param role_arn: ``AWS::MediaLive::Input.RoleArn``.
        :param sources: ``AWS::MediaLive::Input.Sources``.
        :param tags: ``AWS::MediaLive::Input.Tags``.
        :param type: ``AWS::MediaLive::Input.Type``.
        :param vpc: ``AWS::MediaLive::Input.Vpc``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if destinations is not None:
            self._values["destinations"] = destinations
        if input_devices is not None:
            self._values["input_devices"] = input_devices
        if input_security_groups is not None:
            self._values["input_security_groups"] = input_security_groups
        if media_connect_flows is not None:
            self._values["media_connect_flows"] = media_connect_flows
        if name is not None:
            self._values["name"] = name
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if sources is not None:
            self._values["sources"] = sources
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputDestinationRequestProperty]]]]:
        '''``AWS::MediaLive::Input.Destinations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-destinations
        '''
        result = self._values.get("destinations")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputDestinationRequestProperty]]]], result)

    @builtins.property
    def input_devices(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputDeviceSettingsProperty]]]]:
        '''``AWS::MediaLive::Input.InputDevices``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputdevices
        '''
        result = self._values.get("input_devices")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputDeviceSettingsProperty]]]], result)

    @builtins.property
    def input_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::MediaLive::Input.InputSecurityGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputsecuritygroups
        '''
        result = self._values.get("input_security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def media_connect_flows(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInput.MediaConnectFlowRequestProperty]]]]:
        '''``AWS::MediaLive::Input.MediaConnectFlows``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-mediaconnectflows
        '''
        result = self._values.get("media_connect_flows")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInput.MediaConnectFlowRequestProperty]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Input.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Input.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputSourceRequestProperty]]]]:
        '''``AWS::MediaLive::Input.Sources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-sources
        '''
        result = self._values.get("sources")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputSourceRequestProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::MediaLive::Input.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaLive::Input.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputVpcRequestProperty]]:
        '''``AWS::MediaLive::Input.Vpc``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-vpc
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInput.InputVpcRequestProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInputSecurityGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-medialive.CfnInputSecurityGroup",
):
    '''A CloudFormation ``AWS::MediaLive::InputSecurityGroup``.

    :cloudformationResource: AWS::MediaLive::InputSecurityGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        tags: typing.Any = None,
        whitelist_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInputSecurityGroup.InputWhitelistRuleCidrProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaLive::InputSecurityGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param tags: ``AWS::MediaLive::InputSecurityGroup.Tags``.
        :param whitelist_rules: ``AWS::MediaLive::InputSecurityGroup.WhitelistRules``.
        '''
        props = CfnInputSecurityGroupProps(tags=tags, whitelist_rules=whitelist_rules)

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
        '''``AWS::MediaLive::InputSecurityGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="whitelistRules")
    def whitelist_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInputSecurityGroup.InputWhitelistRuleCidrProperty"]]]]:
        '''``AWS::MediaLive::InputSecurityGroup.WhitelistRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-whitelistrules
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInputSecurityGroup.InputWhitelistRuleCidrProperty"]]]], jsii.get(self, "whitelistRules"))

    @whitelist_rules.setter
    def whitelist_rules(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInputSecurityGroup.InputWhitelistRuleCidrProperty"]]]],
    ) -> None:
        jsii.set(self, "whitelistRules", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-medialive.CfnInputSecurityGroup.InputWhitelistRuleCidrProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr": "cidr"},
    )
    class InputWhitelistRuleCidrProperty:
        def __init__(self, *, cidr: typing.Optional[builtins.str] = None) -> None:
            '''
            :param cidr: ``CfnInputSecurityGroup.InputWhitelistRuleCidrProperty.Cidr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cidr is not None:
                self._values["cidr"] = cidr

        @builtins.property
        def cidr(self) -> typing.Optional[builtins.str]:
            '''``CfnInputSecurityGroup.InputWhitelistRuleCidrProperty.Cidr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.html#cfn-medialive-inputsecuritygroup-inputwhitelistrulecidr-cidr
            '''
            result = self._values.get("cidr")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputWhitelistRuleCidrProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-medialive.CfnInputSecurityGroupProps",
    jsii_struct_bases=[],
    name_mapping={"tags": "tags", "whitelist_rules": "whitelistRules"},
)
class CfnInputSecurityGroupProps:
    def __init__(
        self,
        *,
        tags: typing.Any = None,
        whitelist_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnInputSecurityGroup.InputWhitelistRuleCidrProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaLive::InputSecurityGroup``.

        :param tags: ``AWS::MediaLive::InputSecurityGroup.Tags``.
        :param whitelist_rules: ``AWS::MediaLive::InputSecurityGroup.WhitelistRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if tags is not None:
            self._values["tags"] = tags
        if whitelist_rules is not None:
            self._values["whitelist_rules"] = whitelist_rules

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::MediaLive::InputSecurityGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def whitelist_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInputSecurityGroup.InputWhitelistRuleCidrProperty]]]]:
        '''``AWS::MediaLive::InputSecurityGroup.WhitelistRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-whitelistrules
        '''
        result = self._values.get("whitelist_rules")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInputSecurityGroup.InputWhitelistRuleCidrProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInputSecurityGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChannel",
    "CfnChannelProps",
    "CfnInput",
    "CfnInputProps",
    "CfnInputSecurityGroup",
    "CfnInputSecurityGroupProps",
]

publication.publish()
