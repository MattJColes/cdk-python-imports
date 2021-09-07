'''
# AWS::NimbleStudio Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_nimblestudio as nimblestudio
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
class CfnLaunchProfile(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-nimblestudio.CfnLaunchProfile",
):
    '''A CloudFormation ``AWS::NimbleStudio::LaunchProfile``.

    :cloudformationResource: AWS::NimbleStudio::LaunchProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        ec2_subnet_ids: typing.Sequence[builtins.str],
        launch_profile_protocol_versions: typing.Sequence[builtins.str],
        name: builtins.str,
        stream_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnLaunchProfile.StreamConfigurationProperty"],
        studio_component_ids: typing.Sequence[builtins.str],
        studio_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::NimbleStudio::LaunchProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param ec2_subnet_ids: ``AWS::NimbleStudio::LaunchProfile.Ec2SubnetIds``.
        :param launch_profile_protocol_versions: ``AWS::NimbleStudio::LaunchProfile.LaunchProfileProtocolVersions``.
        :param name: ``AWS::NimbleStudio::LaunchProfile.Name``.
        :param stream_configuration: ``AWS::NimbleStudio::LaunchProfile.StreamConfiguration``.
        :param studio_component_ids: ``AWS::NimbleStudio::LaunchProfile.StudioComponentIds``.
        :param studio_id: ``AWS::NimbleStudio::LaunchProfile.StudioId``.
        :param description: ``AWS::NimbleStudio::LaunchProfile.Description``.
        :param tags: ``AWS::NimbleStudio::LaunchProfile.Tags``.
        '''
        props = CfnLaunchProfileProps(
            ec2_subnet_ids=ec2_subnet_ids,
            launch_profile_protocol_versions=launch_profile_protocol_versions,
            name=name,
            stream_configuration=stream_configuration,
            studio_component_ids=studio_component_ids,
            studio_id=studio_id,
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
    @jsii.member(jsii_name="attrLaunchProfileId")
    def attr_launch_profile_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: LaunchProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLaunchProfileId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NimbleStudio::LaunchProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2SubnetIds")
    def ec2_subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::NimbleStudio::LaunchProfile.Ec2SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-ec2subnetids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ec2SubnetIds"))

    @ec2_subnet_ids.setter
    def ec2_subnet_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "ec2SubnetIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="launchProfileProtocolVersions")
    def launch_profile_protocol_versions(self) -> typing.List[builtins.str]:
        '''``AWS::NimbleStudio::LaunchProfile.LaunchProfileProtocolVersions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-launchprofileprotocolversions
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "launchProfileProtocolVersions"))

    @launch_profile_protocol_versions.setter
    def launch_profile_protocol_versions(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        jsii.set(self, "launchProfileProtocolVersions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::NimbleStudio::LaunchProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="streamConfiguration")
    def stream_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnLaunchProfile.StreamConfigurationProperty"]:
        '''``AWS::NimbleStudio::LaunchProfile.StreamConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-streamconfiguration
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnLaunchProfile.StreamConfigurationProperty"], jsii.get(self, "streamConfiguration"))

    @stream_configuration.setter
    def stream_configuration(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnLaunchProfile.StreamConfigurationProperty"],
    ) -> None:
        jsii.set(self, "streamConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="studioComponentIds")
    def studio_component_ids(self) -> typing.List[builtins.str]:
        '''``AWS::NimbleStudio::LaunchProfile.StudioComponentIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-studiocomponentids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "studioComponentIds"))

    @studio_component_ids.setter
    def studio_component_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "studioComponentIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="studioId")
    def studio_id(self) -> builtins.str:
        '''``AWS::NimbleStudio::LaunchProfile.StudioId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-studioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "studioId"))

    @studio_id.setter
    def studio_id(self, value: builtins.str) -> None:
        jsii.set(self, "studioId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NimbleStudio::LaunchProfile.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnLaunchProfile.StreamConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "clipboard_mode": "clipboardMode",
            "ec2_instance_types": "ec2InstanceTypes",
            "streaming_image_ids": "streamingImageIds",
            "max_session_length_in_minutes": "maxSessionLengthInMinutes",
        },
    )
    class StreamConfigurationProperty:
        def __init__(
            self,
            *,
            clipboard_mode: builtins.str,
            ec2_instance_types: typing.Sequence[builtins.str],
            streaming_image_ids: typing.Sequence[builtins.str],
            max_session_length_in_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param clipboard_mode: ``CfnLaunchProfile.StreamConfigurationProperty.ClipboardMode``.
            :param ec2_instance_types: ``CfnLaunchProfile.StreamConfigurationProperty.Ec2InstanceTypes``.
            :param streaming_image_ids: ``CfnLaunchProfile.StreamConfigurationProperty.StreamingImageIds``.
            :param max_session_length_in_minutes: ``CfnLaunchProfile.StreamConfigurationProperty.MaxSessionLengthInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "clipboard_mode": clipboard_mode,
                "ec2_instance_types": ec2_instance_types,
                "streaming_image_ids": streaming_image_ids,
            }
            if max_session_length_in_minutes is not None:
                self._values["max_session_length_in_minutes"] = max_session_length_in_minutes

        @builtins.property
        def clipboard_mode(self) -> builtins.str:
            '''``CfnLaunchProfile.StreamConfigurationProperty.ClipboardMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-clipboardmode
            '''
            result = self._values.get("clipboard_mode")
            assert result is not None, "Required property 'clipboard_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ec2_instance_types(self) -> typing.List[builtins.str]:
            '''``CfnLaunchProfile.StreamConfigurationProperty.Ec2InstanceTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-ec2instancetypes
            '''
            result = self._values.get("ec2_instance_types")
            assert result is not None, "Required property 'ec2_instance_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def streaming_image_ids(self) -> typing.List[builtins.str]:
            '''``CfnLaunchProfile.StreamConfigurationProperty.StreamingImageIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-streamingimageids
            '''
            result = self._values.get("streaming_image_ids")
            assert result is not None, "Required property 'streaming_image_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def max_session_length_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''``CfnLaunchProfile.StreamConfigurationProperty.MaxSessionLengthInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-maxsessionlengthinminutes
            '''
            result = self._values.get("max_session_length_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-nimblestudio.CfnLaunchProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "ec2_subnet_ids": "ec2SubnetIds",
        "launch_profile_protocol_versions": "launchProfileProtocolVersions",
        "name": "name",
        "stream_configuration": "streamConfiguration",
        "studio_component_ids": "studioComponentIds",
        "studio_id": "studioId",
        "description": "description",
        "tags": "tags",
    },
)
class CfnLaunchProfileProps:
    def __init__(
        self,
        *,
        ec2_subnet_ids: typing.Sequence[builtins.str],
        launch_profile_protocol_versions: typing.Sequence[builtins.str],
        name: builtins.str,
        stream_configuration: typing.Union[aws_cdk.core.IResolvable, CfnLaunchProfile.StreamConfigurationProperty],
        studio_component_ids: typing.Sequence[builtins.str],
        studio_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NimbleStudio::LaunchProfile``.

        :param ec2_subnet_ids: ``AWS::NimbleStudio::LaunchProfile.Ec2SubnetIds``.
        :param launch_profile_protocol_versions: ``AWS::NimbleStudio::LaunchProfile.LaunchProfileProtocolVersions``.
        :param name: ``AWS::NimbleStudio::LaunchProfile.Name``.
        :param stream_configuration: ``AWS::NimbleStudio::LaunchProfile.StreamConfiguration``.
        :param studio_component_ids: ``AWS::NimbleStudio::LaunchProfile.StudioComponentIds``.
        :param studio_id: ``AWS::NimbleStudio::LaunchProfile.StudioId``.
        :param description: ``AWS::NimbleStudio::LaunchProfile.Description``.
        :param tags: ``AWS::NimbleStudio::LaunchProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "ec2_subnet_ids": ec2_subnet_ids,
            "launch_profile_protocol_versions": launch_profile_protocol_versions,
            "name": name,
            "stream_configuration": stream_configuration,
            "studio_component_ids": studio_component_ids,
            "studio_id": studio_id,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def ec2_subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::NimbleStudio::LaunchProfile.Ec2SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-ec2subnetids
        '''
        result = self._values.get("ec2_subnet_ids")
        assert result is not None, "Required property 'ec2_subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def launch_profile_protocol_versions(self) -> typing.List[builtins.str]:
        '''``AWS::NimbleStudio::LaunchProfile.LaunchProfileProtocolVersions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-launchprofileprotocolversions
        '''
        result = self._values.get("launch_profile_protocol_versions")
        assert result is not None, "Required property 'launch_profile_protocol_versions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::NimbleStudio::LaunchProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnLaunchProfile.StreamConfigurationProperty]:
        '''``AWS::NimbleStudio::LaunchProfile.StreamConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-streamconfiguration
        '''
        result = self._values.get("stream_configuration")
        assert result is not None, "Required property 'stream_configuration' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnLaunchProfile.StreamConfigurationProperty], result)

    @builtins.property
    def studio_component_ids(self) -> typing.List[builtins.str]:
        '''``AWS::NimbleStudio::LaunchProfile.StudioComponentIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-studiocomponentids
        '''
        result = self._values.get("studio_component_ids")
        assert result is not None, "Required property 'studio_component_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''``AWS::NimbleStudio::LaunchProfile.StudioId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-studioid
        '''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NimbleStudio::LaunchProfile.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::NimbleStudio::LaunchProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStreamingImage(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-nimblestudio.CfnStreamingImage",
):
    '''A CloudFormation ``AWS::NimbleStudio::StreamingImage``.

    :cloudformationResource: AWS::NimbleStudio::StreamingImage
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        ec2_image_id: builtins.str,
        name: builtins.str,
        studio_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::NimbleStudio::StreamingImage``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param ec2_image_id: ``AWS::NimbleStudio::StreamingImage.Ec2ImageId``.
        :param name: ``AWS::NimbleStudio::StreamingImage.Name``.
        :param studio_id: ``AWS::NimbleStudio::StreamingImage.StudioId``.
        :param description: ``AWS::NimbleStudio::StreamingImage.Description``.
        :param tags: ``AWS::NimbleStudio::StreamingImage.Tags``.
        '''
        props = CfnStreamingImageProps(
            ec2_image_id=ec2_image_id,
            name=name,
            studio_id=studio_id,
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
    @jsii.member(jsii_name="attrEulaIds")
    def attr_eula_ids(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: EulaIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrEulaIds"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOwner")
    def attr_owner(self) -> builtins.str:
        '''
        :cloudformationAttribute: Owner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwner"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPlatform")
    def attr_platform(self) -> builtins.str:
        '''
        :cloudformationAttribute: Platform
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlatform"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStreamingImageId")
    def attr_streaming_image_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: StreamingImageId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStreamingImageId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NimbleStudio::StreamingImage.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2ImageId")
    def ec2_image_id(self) -> builtins.str:
        '''``AWS::NimbleStudio::StreamingImage.Ec2ImageId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-ec2imageid
        '''
        return typing.cast(builtins.str, jsii.get(self, "ec2ImageId"))

    @ec2_image_id.setter
    def ec2_image_id(self, value: builtins.str) -> None:
        jsii.set(self, "ec2ImageId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::NimbleStudio::StreamingImage.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="studioId")
    def studio_id(self) -> builtins.str:
        '''``AWS::NimbleStudio::StreamingImage.StudioId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-studioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "studioId"))

    @studio_id.setter
    def studio_id(self, value: builtins.str) -> None:
        jsii.set(self, "studioId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NimbleStudio::StreamingImage.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-nimblestudio.CfnStreamingImageProps",
    jsii_struct_bases=[],
    name_mapping={
        "ec2_image_id": "ec2ImageId",
        "name": "name",
        "studio_id": "studioId",
        "description": "description",
        "tags": "tags",
    },
)
class CfnStreamingImageProps:
    def __init__(
        self,
        *,
        ec2_image_id: builtins.str,
        name: builtins.str,
        studio_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NimbleStudio::StreamingImage``.

        :param ec2_image_id: ``AWS::NimbleStudio::StreamingImage.Ec2ImageId``.
        :param name: ``AWS::NimbleStudio::StreamingImage.Name``.
        :param studio_id: ``AWS::NimbleStudio::StreamingImage.StudioId``.
        :param description: ``AWS::NimbleStudio::StreamingImage.Description``.
        :param tags: ``AWS::NimbleStudio::StreamingImage.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "ec2_image_id": ec2_image_id,
            "name": name,
            "studio_id": studio_id,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def ec2_image_id(self) -> builtins.str:
        '''``AWS::NimbleStudio::StreamingImage.Ec2ImageId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-ec2imageid
        '''
        result = self._values.get("ec2_image_id")
        assert result is not None, "Required property 'ec2_image_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::NimbleStudio::StreamingImage.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''``AWS::NimbleStudio::StreamingImage.StudioId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-studioid
        '''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NimbleStudio::StreamingImage.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::NimbleStudio::StreamingImage.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamingImageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStudio(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-nimblestudio.CfnStudio",
):
    '''A CloudFormation ``AWS::NimbleStudio::Studio``.

    :cloudformationResource: AWS::NimbleStudio::Studio
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        admin_role_arn: builtins.str,
        display_name: builtins.str,
        studio_name: builtins.str,
        user_role_arn: builtins.str,
        studio_encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudio.StudioEncryptionConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::NimbleStudio::Studio``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param admin_role_arn: ``AWS::NimbleStudio::Studio.AdminRoleArn``.
        :param display_name: ``AWS::NimbleStudio::Studio.DisplayName``.
        :param studio_name: ``AWS::NimbleStudio::Studio.StudioName``.
        :param user_role_arn: ``AWS::NimbleStudio::Studio.UserRoleArn``.
        :param studio_encryption_configuration: ``AWS::NimbleStudio::Studio.StudioEncryptionConfiguration``.
        :param tags: ``AWS::NimbleStudio::Studio.Tags``.
        '''
        props = CfnStudioProps(
            admin_role_arn=admin_role_arn,
            display_name=display_name,
            studio_name=studio_name,
            user_role_arn=user_role_arn,
            studio_encryption_configuration=studio_encryption_configuration,
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
    @jsii.member(jsii_name="attrHomeRegion")
    def attr_home_region(self) -> builtins.str:
        '''
        :cloudformationAttribute: HomeRegion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHomeRegion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSsoClientId")
    def attr_sso_client_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SsoClientId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSsoClientId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStudioId")
    def attr_studio_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: StudioId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStudioId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStudioUrl")
    def attr_studio_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: StudioUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStudioUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NimbleStudio::Studio.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="adminRoleArn")
    def admin_role_arn(self) -> builtins.str:
        '''``AWS::NimbleStudio::Studio.AdminRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-adminrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "adminRoleArn"))

    @admin_role_arn.setter
    def admin_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "adminRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''``AWS::NimbleStudio::Studio.DisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-displayname
        '''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        jsii.set(self, "displayName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="studioName")
    def studio_name(self) -> builtins.str:
        '''``AWS::NimbleStudio::Studio.StudioName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-studioname
        '''
        return typing.cast(builtins.str, jsii.get(self, "studioName"))

    @studio_name.setter
    def studio_name(self, value: builtins.str) -> None:
        jsii.set(self, "studioName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userRoleArn")
    def user_role_arn(self) -> builtins.str:
        '''``AWS::NimbleStudio::Studio.UserRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-userrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "userRoleArn"))

    @user_role_arn.setter
    def user_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "userRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="studioEncryptionConfiguration")
    def studio_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudio.StudioEncryptionConfigurationProperty"]]:
        '''``AWS::NimbleStudio::Studio.StudioEncryptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-studioencryptionconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudio.StudioEncryptionConfigurationProperty"]], jsii.get(self, "studioEncryptionConfiguration"))

    @studio_encryption_configuration.setter
    def studio_encryption_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudio.StudioEncryptionConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "studioEncryptionConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnStudio.StudioEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"key_type": "keyType", "key_arn": "keyArn"},
    )
    class StudioEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            key_type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key_type: ``CfnStudio.StudioEncryptionConfigurationProperty.KeyType``.
            :param key_arn: ``CfnStudio.StudioEncryptionConfigurationProperty.KeyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key_type": key_type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def key_type(self) -> builtins.str:
            '''``CfnStudio.StudioEncryptionConfigurationProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html#cfn-nimblestudio-studio-studioencryptionconfiguration-keytype
            '''
            result = self._values.get("key_type")
            assert result is not None, "Required property 'key_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnStudio.StudioEncryptionConfigurationProperty.KeyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html#cfn-nimblestudio-studio-studioencryptionconfiguration-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StudioEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStudioComponent(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponent",
):
    '''A CloudFormation ``AWS::NimbleStudio::StudioComponent``.

    :cloudformationResource: AWS::NimbleStudio::StudioComponent
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        studio_id: builtins.str,
        type: builtins.str,
        configuration: typing.Optional[typing.Union["CfnStudioComponent.StudioComponentConfigurationProperty", aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        ec2_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        initialization_scripts: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.StudioComponentInitializationScriptProperty"]]]] = None,
        script_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ScriptParameterKeyValueProperty"]]]] = None,
        subtype: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::NimbleStudio::StudioComponent``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::NimbleStudio::StudioComponent.Name``.
        :param studio_id: ``AWS::NimbleStudio::StudioComponent.StudioId``.
        :param type: ``AWS::NimbleStudio::StudioComponent.Type``.
        :param configuration: ``AWS::NimbleStudio::StudioComponent.Configuration``.
        :param description: ``AWS::NimbleStudio::StudioComponent.Description``.
        :param ec2_security_group_ids: ``AWS::NimbleStudio::StudioComponent.Ec2SecurityGroupIds``.
        :param initialization_scripts: ``AWS::NimbleStudio::StudioComponent.InitializationScripts``.
        :param script_parameters: ``AWS::NimbleStudio::StudioComponent.ScriptParameters``.
        :param subtype: ``AWS::NimbleStudio::StudioComponent.Subtype``.
        :param tags: ``AWS::NimbleStudio::StudioComponent.Tags``.
        '''
        props = CfnStudioComponentProps(
            name=name,
            studio_id=studio_id,
            type=type,
            configuration=configuration,
            description=description,
            ec2_security_group_ids=ec2_security_group_ids,
            initialization_scripts=initialization_scripts,
            script_parameters=script_parameters,
            subtype=subtype,
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
    @jsii.member(jsii_name="attrStudioComponentId")
    def attr_studio_component_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: StudioComponentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStudioComponentId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NimbleStudio::StudioComponent.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::NimbleStudio::StudioComponent.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="studioId")
    def studio_id(self) -> builtins.str:
        '''``AWS::NimbleStudio::StudioComponent.StudioId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-studioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "studioId"))

    @studio_id.setter
    def studio_id(self, value: builtins.str) -> None:
        jsii.set(self, "studioId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::NimbleStudio::StudioComponent.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnStudioComponent.StudioComponentConfigurationProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::NimbleStudio::StudioComponent.Configuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-configuration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnStudioComponent.StudioComponentConfigurationProperty", aws_cdk.core.IResolvable]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union["CfnStudioComponent.StudioComponentConfigurationProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "configuration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NimbleStudio::StudioComponent.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2SecurityGroupIds")
    def ec2_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::NimbleStudio::StudioComponent.Ec2SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-ec2securitygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ec2SecurityGroupIds"))

    @ec2_security_group_ids.setter
    def ec2_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "ec2SecurityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initializationScripts")
    def initialization_scripts(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.StudioComponentInitializationScriptProperty"]]]]:
        '''``AWS::NimbleStudio::StudioComponent.InitializationScripts``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-initializationscripts
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.StudioComponentInitializationScriptProperty"]]]], jsii.get(self, "initializationScripts"))

    @initialization_scripts.setter
    def initialization_scripts(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.StudioComponentInitializationScriptProperty"]]]],
    ) -> None:
        jsii.set(self, "initializationScripts", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scriptParameters")
    def script_parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ScriptParameterKeyValueProperty"]]]]:
        '''``AWS::NimbleStudio::StudioComponent.ScriptParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-scriptparameters
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ScriptParameterKeyValueProperty"]]]], jsii.get(self, "scriptParameters"))

    @script_parameters.setter
    def script_parameters(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ScriptParameterKeyValueProperty"]]]],
    ) -> None:
        jsii.set(self, "scriptParameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subtype")
    def subtype(self) -> typing.Optional[builtins.str]:
        '''``AWS::NimbleStudio::StudioComponent.Subtype``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-subtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subtype"))

    @subtype.setter
    def subtype(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subtype", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponent.ActiveDirectoryComputerAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ActiveDirectoryComputerAttributeProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnStudioComponent.ActiveDirectoryComputerAttributeProperty.Name``.
            :param value: ``CfnStudioComponent.ActiveDirectoryComputerAttributeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.ActiveDirectoryComputerAttributeProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html#cfn-nimblestudio-studiocomponent-activedirectorycomputerattribute-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.ActiveDirectoryComputerAttributeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html#cfn-nimblestudio-studiocomponent-activedirectorycomputerattribute-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActiveDirectoryComputerAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponent.ActiveDirectoryConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "computer_attributes": "computerAttributes",
            "directory_id": "directoryId",
            "organizational_unit_distinguished_name": "organizationalUnitDistinguishedName",
        },
    )
    class ActiveDirectoryConfigurationProperty:
        def __init__(
            self,
            *,
            computer_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ActiveDirectoryComputerAttributeProperty"]]]] = None,
            directory_id: typing.Optional[builtins.str] = None,
            organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param computer_attributes: ``CfnStudioComponent.ActiveDirectoryConfigurationProperty.ComputerAttributes``.
            :param directory_id: ``CfnStudioComponent.ActiveDirectoryConfigurationProperty.DirectoryId``.
            :param organizational_unit_distinguished_name: ``CfnStudioComponent.ActiveDirectoryConfigurationProperty.OrganizationalUnitDistinguishedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if computer_attributes is not None:
                self._values["computer_attributes"] = computer_attributes
            if directory_id is not None:
                self._values["directory_id"] = directory_id
            if organizational_unit_distinguished_name is not None:
                self._values["organizational_unit_distinguished_name"] = organizational_unit_distinguished_name

        @builtins.property
        def computer_attributes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ActiveDirectoryComputerAttributeProperty"]]]]:
            '''``CfnStudioComponent.ActiveDirectoryConfigurationProperty.ComputerAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html#cfn-nimblestudio-studiocomponent-activedirectoryconfiguration-computerattributes
            '''
            result = self._values.get("computer_attributes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ActiveDirectoryComputerAttributeProperty"]]]], result)

        @builtins.property
        def directory_id(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.ActiveDirectoryConfigurationProperty.DirectoryId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html#cfn-nimblestudio-studiocomponent-activedirectoryconfiguration-directoryid
            '''
            result = self._values.get("directory_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit_distinguished_name(
            self,
        ) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.ActiveDirectoryConfigurationProperty.OrganizationalUnitDistinguishedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html#cfn-nimblestudio-studiocomponent-activedirectoryconfiguration-organizationalunitdistinguishedname
            '''
            result = self._values.get("organizational_unit_distinguished_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActiveDirectoryConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponent.ComputeFarmConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "active_directory_user": "activeDirectoryUser",
            "endpoint": "endpoint",
        },
    )
    class ComputeFarmConfigurationProperty:
        def __init__(
            self,
            *,
            active_directory_user: typing.Optional[builtins.str] = None,
            endpoint: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param active_directory_user: ``CfnStudioComponent.ComputeFarmConfigurationProperty.ActiveDirectoryUser``.
            :param endpoint: ``CfnStudioComponent.ComputeFarmConfigurationProperty.Endpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if active_directory_user is not None:
                self._values["active_directory_user"] = active_directory_user
            if endpoint is not None:
                self._values["endpoint"] = endpoint

        @builtins.property
        def active_directory_user(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.ComputeFarmConfigurationProperty.ActiveDirectoryUser``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html#cfn-nimblestudio-studiocomponent-computefarmconfiguration-activedirectoryuser
            '''
            result = self._values.get("active_directory_user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def endpoint(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.ComputeFarmConfigurationProperty.Endpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html#cfn-nimblestudio-studiocomponent-computefarmconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeFarmConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponent.LicenseServiceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint": "endpoint"},
    )
    class LicenseServiceConfigurationProperty:
        def __init__(self, *, endpoint: typing.Optional[builtins.str] = None) -> None:
            '''
            :param endpoint: ``CfnStudioComponent.LicenseServiceConfigurationProperty.Endpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-licenseserviceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if endpoint is not None:
                self._values["endpoint"] = endpoint

        @builtins.property
        def endpoint(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.LicenseServiceConfigurationProperty.Endpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-licenseserviceconfiguration.html#cfn-nimblestudio-studiocomponent-licenseserviceconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LicenseServiceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponent.ScriptParameterKeyValueProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ScriptParameterKeyValueProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: ``CfnStudioComponent.ScriptParameterKeyValueProperty.Key``.
            :param value: ``CfnStudioComponent.ScriptParameterKeyValueProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.ScriptParameterKeyValueProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html#cfn-nimblestudio-studiocomponent-scriptparameterkeyvalue-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.ScriptParameterKeyValueProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html#cfn-nimblestudio-studiocomponent-scriptparameterkeyvalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScriptParameterKeyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponent.SharedFileSystemConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "file_system_id": "fileSystemId",
            "linux_mount_point": "linuxMountPoint",
            "share_name": "shareName",
            "windows_mount_drive": "windowsMountDrive",
        },
    )
    class SharedFileSystemConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint: typing.Optional[builtins.str] = None,
            file_system_id: typing.Optional[builtins.str] = None,
            linux_mount_point: typing.Optional[builtins.str] = None,
            share_name: typing.Optional[builtins.str] = None,
            windows_mount_drive: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint: ``CfnStudioComponent.SharedFileSystemConfigurationProperty.Endpoint``.
            :param file_system_id: ``CfnStudioComponent.SharedFileSystemConfigurationProperty.FileSystemId``.
            :param linux_mount_point: ``CfnStudioComponent.SharedFileSystemConfigurationProperty.LinuxMountPoint``.
            :param share_name: ``CfnStudioComponent.SharedFileSystemConfigurationProperty.ShareName``.
            :param windows_mount_drive: ``CfnStudioComponent.SharedFileSystemConfigurationProperty.WindowsMountDrive``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if endpoint is not None:
                self._values["endpoint"] = endpoint
            if file_system_id is not None:
                self._values["file_system_id"] = file_system_id
            if linux_mount_point is not None:
                self._values["linux_mount_point"] = linux_mount_point
            if share_name is not None:
                self._values["share_name"] = share_name
            if windows_mount_drive is not None:
                self._values["windows_mount_drive"] = windows_mount_drive

        @builtins.property
        def endpoint(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.SharedFileSystemConfigurationProperty.Endpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_system_id(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.SharedFileSystemConfigurationProperty.FileSystemId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-filesystemid
            '''
            result = self._values.get("file_system_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def linux_mount_point(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.SharedFileSystemConfigurationProperty.LinuxMountPoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-linuxmountpoint
            '''
            result = self._values.get("linux_mount_point")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def share_name(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.SharedFileSystemConfigurationProperty.ShareName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-sharename
            '''
            result = self._values.get("share_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def windows_mount_drive(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.SharedFileSystemConfigurationProperty.WindowsMountDrive``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-windowsmountdrive
            '''
            result = self._values.get("windows_mount_drive")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SharedFileSystemConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponent.StudioComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "active_directory_configuration": "activeDirectoryConfiguration",
            "compute_farm_configuration": "computeFarmConfiguration",
            "license_service_configuration": "licenseServiceConfiguration",
            "shared_file_system_configuration": "sharedFileSystemConfiguration",
        },
    )
    class StudioComponentConfigurationProperty:
        def __init__(
            self,
            *,
            active_directory_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ActiveDirectoryConfigurationProperty"]] = None,
            compute_farm_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ComputeFarmConfigurationProperty"]] = None,
            license_service_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.LicenseServiceConfigurationProperty"]] = None,
            shared_file_system_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.SharedFileSystemConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param active_directory_configuration: ``CfnStudioComponent.StudioComponentConfigurationProperty.ActiveDirectoryConfiguration``.
            :param compute_farm_configuration: ``CfnStudioComponent.StudioComponentConfigurationProperty.ComputeFarmConfiguration``.
            :param license_service_configuration: ``CfnStudioComponent.StudioComponentConfigurationProperty.LicenseServiceConfiguration``.
            :param shared_file_system_configuration: ``CfnStudioComponent.StudioComponentConfigurationProperty.SharedFileSystemConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if active_directory_configuration is not None:
                self._values["active_directory_configuration"] = active_directory_configuration
            if compute_farm_configuration is not None:
                self._values["compute_farm_configuration"] = compute_farm_configuration
            if license_service_configuration is not None:
                self._values["license_service_configuration"] = license_service_configuration
            if shared_file_system_configuration is not None:
                self._values["shared_file_system_configuration"] = shared_file_system_configuration

        @builtins.property
        def active_directory_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ActiveDirectoryConfigurationProperty"]]:
            '''``CfnStudioComponent.StudioComponentConfigurationProperty.ActiveDirectoryConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-activedirectoryconfiguration
            '''
            result = self._values.get("active_directory_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ActiveDirectoryConfigurationProperty"]], result)

        @builtins.property
        def compute_farm_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ComputeFarmConfigurationProperty"]]:
            '''``CfnStudioComponent.StudioComponentConfigurationProperty.ComputeFarmConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-computefarmconfiguration
            '''
            result = self._values.get("compute_farm_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.ComputeFarmConfigurationProperty"]], result)

        @builtins.property
        def license_service_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.LicenseServiceConfigurationProperty"]]:
            '''``CfnStudioComponent.StudioComponentConfigurationProperty.LicenseServiceConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-licenseserviceconfiguration
            '''
            result = self._values.get("license_service_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.LicenseServiceConfigurationProperty"]], result)

        @builtins.property
        def shared_file_system_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.SharedFileSystemConfigurationProperty"]]:
            '''``CfnStudioComponent.StudioComponentConfigurationProperty.SharedFileSystemConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-sharedfilesystemconfiguration
            '''
            result = self._values.get("shared_file_system_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStudioComponent.SharedFileSystemConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StudioComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponent.StudioComponentInitializationScriptProperty",
        jsii_struct_bases=[],
        name_mapping={
            "launch_profile_protocol_version": "launchProfileProtocolVersion",
            "platform": "platform",
            "run_context": "runContext",
            "script": "script",
        },
    )
    class StudioComponentInitializationScriptProperty:
        def __init__(
            self,
            *,
            launch_profile_protocol_version: typing.Optional[builtins.str] = None,
            platform: typing.Optional[builtins.str] = None,
            run_context: typing.Optional[builtins.str] = None,
            script: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param launch_profile_protocol_version: ``CfnStudioComponent.StudioComponentInitializationScriptProperty.LaunchProfileProtocolVersion``.
            :param platform: ``CfnStudioComponent.StudioComponentInitializationScriptProperty.Platform``.
            :param run_context: ``CfnStudioComponent.StudioComponentInitializationScriptProperty.RunContext``.
            :param script: ``CfnStudioComponent.StudioComponentInitializationScriptProperty.Script``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if launch_profile_protocol_version is not None:
                self._values["launch_profile_protocol_version"] = launch_profile_protocol_version
            if platform is not None:
                self._values["platform"] = platform
            if run_context is not None:
                self._values["run_context"] = run_context
            if script is not None:
                self._values["script"] = script

        @builtins.property
        def launch_profile_protocol_version(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.StudioComponentInitializationScriptProperty.LaunchProfileProtocolVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-launchprofileprotocolversion
            '''
            result = self._values.get("launch_profile_protocol_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def platform(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.StudioComponentInitializationScriptProperty.Platform``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-platform
            '''
            result = self._values.get("platform")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def run_context(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.StudioComponentInitializationScriptProperty.RunContext``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-runcontext
            '''
            result = self._values.get("run_context")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def script(self) -> typing.Optional[builtins.str]:
            '''``CfnStudioComponent.StudioComponentInitializationScriptProperty.Script``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-script
            '''
            result = self._values.get("script")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StudioComponentInitializationScriptProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioComponentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "studio_id": "studioId",
        "type": "type",
        "configuration": "configuration",
        "description": "description",
        "ec2_security_group_ids": "ec2SecurityGroupIds",
        "initialization_scripts": "initializationScripts",
        "script_parameters": "scriptParameters",
        "subtype": "subtype",
        "tags": "tags",
    },
)
class CfnStudioComponentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        studio_id: builtins.str,
        type: builtins.str,
        configuration: typing.Optional[typing.Union[CfnStudioComponent.StudioComponentConfigurationProperty, aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        ec2_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        initialization_scripts: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnStudioComponent.StudioComponentInitializationScriptProperty]]]] = None,
        script_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnStudioComponent.ScriptParameterKeyValueProperty]]]] = None,
        subtype: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NimbleStudio::StudioComponent``.

        :param name: ``AWS::NimbleStudio::StudioComponent.Name``.
        :param studio_id: ``AWS::NimbleStudio::StudioComponent.StudioId``.
        :param type: ``AWS::NimbleStudio::StudioComponent.Type``.
        :param configuration: ``AWS::NimbleStudio::StudioComponent.Configuration``.
        :param description: ``AWS::NimbleStudio::StudioComponent.Description``.
        :param ec2_security_group_ids: ``AWS::NimbleStudio::StudioComponent.Ec2SecurityGroupIds``.
        :param initialization_scripts: ``AWS::NimbleStudio::StudioComponent.InitializationScripts``.
        :param script_parameters: ``AWS::NimbleStudio::StudioComponent.ScriptParameters``.
        :param subtype: ``AWS::NimbleStudio::StudioComponent.Subtype``.
        :param tags: ``AWS::NimbleStudio::StudioComponent.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "studio_id": studio_id,
            "type": type,
        }
        if configuration is not None:
            self._values["configuration"] = configuration
        if description is not None:
            self._values["description"] = description
        if ec2_security_group_ids is not None:
            self._values["ec2_security_group_ids"] = ec2_security_group_ids
        if initialization_scripts is not None:
            self._values["initialization_scripts"] = initialization_scripts
        if script_parameters is not None:
            self._values["script_parameters"] = script_parameters
        if subtype is not None:
            self._values["subtype"] = subtype
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::NimbleStudio::StudioComponent.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''``AWS::NimbleStudio::StudioComponent.StudioId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-studioid
        '''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::NimbleStudio::StudioComponent.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnStudioComponent.StudioComponentConfigurationProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::NimbleStudio::StudioComponent.Configuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[CfnStudioComponent.StudioComponentConfigurationProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NimbleStudio::StudioComponent.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::NimbleStudio::StudioComponent.Ec2SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-ec2securitygroupids
        '''
        result = self._values.get("ec2_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def initialization_scripts(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnStudioComponent.StudioComponentInitializationScriptProperty]]]]:
        '''``AWS::NimbleStudio::StudioComponent.InitializationScripts``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-initializationscripts
        '''
        result = self._values.get("initialization_scripts")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnStudioComponent.StudioComponentInitializationScriptProperty]]]], result)

    @builtins.property
    def script_parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnStudioComponent.ScriptParameterKeyValueProperty]]]]:
        '''``AWS::NimbleStudio::StudioComponent.ScriptParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-scriptparameters
        '''
        result = self._values.get("script_parameters")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnStudioComponent.ScriptParameterKeyValueProperty]]]], result)

    @builtins.property
    def subtype(self) -> typing.Optional[builtins.str]:
        '''``AWS::NimbleStudio::StudioComponent.Subtype``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-subtype
        '''
        result = self._values.get("subtype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::NimbleStudio::StudioComponent.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStudioComponentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-nimblestudio.CfnStudioProps",
    jsii_struct_bases=[],
    name_mapping={
        "admin_role_arn": "adminRoleArn",
        "display_name": "displayName",
        "studio_name": "studioName",
        "user_role_arn": "userRoleArn",
        "studio_encryption_configuration": "studioEncryptionConfiguration",
        "tags": "tags",
    },
)
class CfnStudioProps:
    def __init__(
        self,
        *,
        admin_role_arn: builtins.str,
        display_name: builtins.str,
        studio_name: builtins.str,
        user_role_arn: builtins.str,
        studio_encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStudio.StudioEncryptionConfigurationProperty]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NimbleStudio::Studio``.

        :param admin_role_arn: ``AWS::NimbleStudio::Studio.AdminRoleArn``.
        :param display_name: ``AWS::NimbleStudio::Studio.DisplayName``.
        :param studio_name: ``AWS::NimbleStudio::Studio.StudioName``.
        :param user_role_arn: ``AWS::NimbleStudio::Studio.UserRoleArn``.
        :param studio_encryption_configuration: ``AWS::NimbleStudio::Studio.StudioEncryptionConfiguration``.
        :param tags: ``AWS::NimbleStudio::Studio.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "admin_role_arn": admin_role_arn,
            "display_name": display_name,
            "studio_name": studio_name,
            "user_role_arn": user_role_arn,
        }
        if studio_encryption_configuration is not None:
            self._values["studio_encryption_configuration"] = studio_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def admin_role_arn(self) -> builtins.str:
        '''``AWS::NimbleStudio::Studio.AdminRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-adminrolearn
        '''
        result = self._values.get("admin_role_arn")
        assert result is not None, "Required property 'admin_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''``AWS::NimbleStudio::Studio.DisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_name(self) -> builtins.str:
        '''``AWS::NimbleStudio::Studio.StudioName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-studioname
        '''
        result = self._values.get("studio_name")
        assert result is not None, "Required property 'studio_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_role_arn(self) -> builtins.str:
        '''``AWS::NimbleStudio::Studio.UserRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-userrolearn
        '''
        result = self._values.get("user_role_arn")
        assert result is not None, "Required property 'user_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStudio.StudioEncryptionConfigurationProperty]]:
        '''``AWS::NimbleStudio::Studio.StudioEncryptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-studioencryptionconfiguration
        '''
        result = self._values.get("studio_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStudio.StudioEncryptionConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::NimbleStudio::Studio.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStudioProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLaunchProfile",
    "CfnLaunchProfileProps",
    "CfnStreamingImage",
    "CfnStreamingImageProps",
    "CfnStudio",
    "CfnStudioComponent",
    "CfnStudioComponentProps",
    "CfnStudioProps",
]

publication.publish()
