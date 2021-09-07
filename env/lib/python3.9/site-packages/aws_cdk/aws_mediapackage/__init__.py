'''
# AWS::MediaPackage Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_mediapackage as mediapackage
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
class CfnAsset(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediapackage.CfnAsset",
):
    '''A CloudFormation ``AWS::MediaPackage::Asset``.

    :cloudformationResource: AWS::MediaPackage::Asset
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id_: builtins.str,
        *,
        id: builtins.str,
        packaging_group_id: builtins.str,
        source_arn: builtins.str,
        source_role_arn: builtins.str,
        resource_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaPackage::Asset``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param id: ``AWS::MediaPackage::Asset.Id``.
        :param packaging_group_id: ``AWS::MediaPackage::Asset.PackagingGroupId``.
        :param source_arn: ``AWS::MediaPackage::Asset.SourceArn``.
        :param source_role_arn: ``AWS::MediaPackage::Asset.SourceRoleArn``.
        :param resource_id: ``AWS::MediaPackage::Asset.ResourceId``.
        :param tags: ``AWS::MediaPackage::Asset.Tags``.
        '''
        props = CfnAssetProps(
            id=id,
            packaging_group_id=packaging_group_id,
            source_arn=source_arn,
            source_role_arn=source_role_arn,
            resource_id=resource_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEgressEndpoints")
    def attr_egress_endpoints(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: EgressEndpoints
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrEgressEndpoints"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::MediaPackage::Asset.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::Asset.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-id
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="packagingGroupId")
    def packaging_group_id(self) -> builtins.str:
        '''``AWS::MediaPackage::Asset.PackagingGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-packaginggroupid
        '''
        return typing.cast(builtins.str, jsii.get(self, "packagingGroupId"))

    @packaging_group_id.setter
    def packaging_group_id(self, value: builtins.str) -> None:
        jsii.set(self, "packagingGroupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> builtins.str:
        '''``AWS::MediaPackage::Asset.SourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "sourceArn"))

    @source_arn.setter
    def source_arn(self, value: builtins.str) -> None:
        jsii.set(self, "sourceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceRoleArn")
    def source_role_arn(self) -> builtins.str:
        '''``AWS::MediaPackage::Asset.SourceRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcerolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "sourceRoleArn"))

    @source_role_arn.setter
    def source_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "sourceRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::Asset.ResourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-resourceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "resourceId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnAsset.EgressEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "packaging_configuration_id": "packagingConfigurationId",
            "url": "url",
        },
    )
    class EgressEndpointProperty:
        def __init__(
            self,
            *,
            packaging_configuration_id: builtins.str,
            url: builtins.str,
        ) -> None:
            '''
            :param packaging_configuration_id: ``CfnAsset.EgressEndpointProperty.PackagingConfigurationId``.
            :param url: ``CfnAsset.EgressEndpointProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "packaging_configuration_id": packaging_configuration_id,
                "url": url,
            }

        @builtins.property
        def packaging_configuration_id(self) -> builtins.str:
            '''``CfnAsset.EgressEndpointProperty.PackagingConfigurationId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-packagingconfigurationid
            '''
            result = self._values.get("packaging_configuration_id")
            assert result is not None, "Required property 'packaging_configuration_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def url(self) -> builtins.str:
            '''``CfnAsset.EgressEndpointProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EgressEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediapackage.CfnAssetProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "packaging_group_id": "packagingGroupId",
        "source_arn": "sourceArn",
        "source_role_arn": "sourceRoleArn",
        "resource_id": "resourceId",
        "tags": "tags",
    },
)
class CfnAssetProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        packaging_group_id: builtins.str,
        source_arn: builtins.str,
        source_role_arn: builtins.str,
        resource_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaPackage::Asset``.

        :param id: ``AWS::MediaPackage::Asset.Id``.
        :param packaging_group_id: ``AWS::MediaPackage::Asset.PackagingGroupId``.
        :param source_arn: ``AWS::MediaPackage::Asset.SourceArn``.
        :param source_role_arn: ``AWS::MediaPackage::Asset.SourceRoleArn``.
        :param resource_id: ``AWS::MediaPackage::Asset.ResourceId``.
        :param tags: ``AWS::MediaPackage::Asset.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "packaging_group_id": packaging_group_id,
            "source_arn": source_arn,
            "source_role_arn": source_role_arn,
        }
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::Asset.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def packaging_group_id(self) -> builtins.str:
        '''``AWS::MediaPackage::Asset.PackagingGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-packaginggroupid
        '''
        result = self._values.get("packaging_group_id")
        assert result is not None, "Required property 'packaging_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_arn(self) -> builtins.str:
        '''``AWS::MediaPackage::Asset.SourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcearn
        '''
        result = self._values.get("source_arn")
        assert result is not None, "Required property 'source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_role_arn(self) -> builtins.str:
        '''``AWS::MediaPackage::Asset.SourceRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcerolearn
        '''
        result = self._values.get("source_role_arn")
        assert result is not None, "Required property 'source_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::Asset.ResourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-resourceid
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::MediaPackage::Asset.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediapackage.CfnChannel",
):
    '''A CloudFormation ``AWS::MediaPackage::Channel``.

    :cloudformationResource: AWS::MediaPackage::Channel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id_: builtins.str,
        *,
        id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        egress_access_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.LogConfigurationProperty"]] = None,
        ingress_access_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.LogConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaPackage::Channel``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param id: ``AWS::MediaPackage::Channel.Id``.
        :param description: ``AWS::MediaPackage::Channel.Description``.
        :param egress_access_logs: ``AWS::MediaPackage::Channel.EgressAccessLogs``.
        :param ingress_access_logs: ``AWS::MediaPackage::Channel.IngressAccessLogs``.
        :param tags: ``AWS::MediaPackage::Channel.Tags``.
        '''
        props = CfnChannelProps(
            id=id,
            description=description,
            egress_access_logs=egress_access_logs,
            ingress_access_logs=ingress_access_logs,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

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
        '''``AWS::MediaPackage::Channel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::Channel.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-id
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::Channel.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="egressAccessLogs")
    def egress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.LogConfigurationProperty"]]:
        '''``AWS::MediaPackage::Channel.EgressAccessLogs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-egressaccesslogs
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.LogConfigurationProperty"]], jsii.get(self, "egressAccessLogs"))

    @egress_access_logs.setter
    def egress_access_logs(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.LogConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "egressAccessLogs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ingressAccessLogs")
    def ingress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.LogConfigurationProperty"]]:
        '''``AWS::MediaPackage::Channel.IngressAccessLogs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-ingressaccesslogs
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.LogConfigurationProperty"]], jsii.get(self, "ingressAccessLogs"))

    @ingress_access_logs.setter
    def ingress_access_logs(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.LogConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "ingressAccessLogs", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnChannel.LogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName"},
    )
    class LogConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_group_name: ``CfnChannel.LogConfigurationProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.LogConfigurationProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html#cfn-mediapackage-channel-logconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediapackage.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "description": "description",
        "egress_access_logs": "egressAccessLogs",
        "ingress_access_logs": "ingressAccessLogs",
        "tags": "tags",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        egress_access_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.LogConfigurationProperty]] = None,
        ingress_access_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.LogConfigurationProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaPackage::Channel``.

        :param id: ``AWS::MediaPackage::Channel.Id``.
        :param description: ``AWS::MediaPackage::Channel.Description``.
        :param egress_access_logs: ``AWS::MediaPackage::Channel.EgressAccessLogs``.
        :param ingress_access_logs: ``AWS::MediaPackage::Channel.IngressAccessLogs``.
        :param tags: ``AWS::MediaPackage::Channel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if description is not None:
            self._values["description"] = description
        if egress_access_logs is not None:
            self._values["egress_access_logs"] = egress_access_logs
        if ingress_access_logs is not None:
            self._values["ingress_access_logs"] = ingress_access_logs
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::Channel.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::Channel.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def egress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.LogConfigurationProperty]]:
        '''``AWS::MediaPackage::Channel.EgressAccessLogs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-egressaccesslogs
        '''
        result = self._values.get("egress_access_logs")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.LogConfigurationProperty]], result)

    @builtins.property
    def ingress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.LogConfigurationProperty]]:
        '''``AWS::MediaPackage::Channel.IngressAccessLogs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-ingressaccesslogs
        '''
        result = self._values.get("ingress_access_logs")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.LogConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::MediaPackage::Channel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnOriginEndpoint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint",
):
    '''A CloudFormation ``AWS::MediaPackage::OriginEndpoint``.

    :cloudformationResource: AWS::MediaPackage::OriginEndpoint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id_: builtins.str,
        *,
        channel_id: builtins.str,
        id: builtins.str,
        authorization: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.AuthorizationProperty"]] = None,
        cmaf_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.CmafPackageProperty"]] = None,
        dash_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.DashPackageProperty"]] = None,
        description: typing.Optional[builtins.str] = None,
        hls_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsPackageProperty"]] = None,
        manifest_name: typing.Optional[builtins.str] = None,
        mss_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.MssPackageProperty"]] = None,
        origination: typing.Optional[builtins.str] = None,
        startover_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        time_delay_seconds: typing.Optional[jsii.Number] = None,
        whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaPackage::OriginEndpoint``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param channel_id: ``AWS::MediaPackage::OriginEndpoint.ChannelId``.
        :param id: ``AWS::MediaPackage::OriginEndpoint.Id``.
        :param authorization: ``AWS::MediaPackage::OriginEndpoint.Authorization``.
        :param cmaf_package: ``AWS::MediaPackage::OriginEndpoint.CmafPackage``.
        :param dash_package: ``AWS::MediaPackage::OriginEndpoint.DashPackage``.
        :param description: ``AWS::MediaPackage::OriginEndpoint.Description``.
        :param hls_package: ``AWS::MediaPackage::OriginEndpoint.HlsPackage``.
        :param manifest_name: ``AWS::MediaPackage::OriginEndpoint.ManifestName``.
        :param mss_package: ``AWS::MediaPackage::OriginEndpoint.MssPackage``.
        :param origination: ``AWS::MediaPackage::OriginEndpoint.Origination``.
        :param startover_window_seconds: ``AWS::MediaPackage::OriginEndpoint.StartoverWindowSeconds``.
        :param tags: ``AWS::MediaPackage::OriginEndpoint.Tags``.
        :param time_delay_seconds: ``AWS::MediaPackage::OriginEndpoint.TimeDelaySeconds``.
        :param whitelist: ``AWS::MediaPackage::OriginEndpoint.Whitelist``.
        '''
        props = CfnOriginEndpointProps(
            channel_id=channel_id,
            id=id,
            authorization=authorization,
            cmaf_package=cmaf_package,
            dash_package=dash_package,
            description=description,
            hls_package=hls_package,
            manifest_name=manifest_name,
            mss_package=mss_package,
            origination=origination,
            startover_window_seconds=startover_window_seconds,
            tags=tags,
            time_delay_seconds=time_delay_seconds,
            whitelist=whitelist,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

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
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: Url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::MediaPackage::OriginEndpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="channelId")
    def channel_id(self) -> builtins.str:
        '''``AWS::MediaPackage::OriginEndpoint.ChannelId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-channelid
        '''
        return typing.cast(builtins.str, jsii.get(self, "channelId"))

    @channel_id.setter
    def channel_id(self, value: builtins.str) -> None:
        jsii.set(self, "channelId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::OriginEndpoint.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-id
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="authorization")
    def authorization(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.AuthorizationProperty"]]:
        '''``AWS::MediaPackage::OriginEndpoint.Authorization``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-authorization
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.AuthorizationProperty"]], jsii.get(self, "authorization"))

    @authorization.setter
    def authorization(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.AuthorizationProperty"]],
    ) -> None:
        jsii.set(self, "authorization", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cmafPackage")
    def cmaf_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.CmafPackageProperty"]]:
        '''``AWS::MediaPackage::OriginEndpoint.CmafPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-cmafpackage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.CmafPackageProperty"]], jsii.get(self, "cmafPackage"))

    @cmaf_package.setter
    def cmaf_package(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.CmafPackageProperty"]],
    ) -> None:
        jsii.set(self, "cmafPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dashPackage")
    def dash_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.DashPackageProperty"]]:
        '''``AWS::MediaPackage::OriginEndpoint.DashPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-dashpackage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.DashPackageProperty"]], jsii.get(self, "dashPackage"))

    @dash_package.setter
    def dash_package(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.DashPackageProperty"]],
    ) -> None:
        jsii.set(self, "dashPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::OriginEndpoint.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hlsPackage")
    def hls_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsPackageProperty"]]:
        '''``AWS::MediaPackage::OriginEndpoint.HlsPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-hlspackage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsPackageProperty"]], jsii.get(self, "hlsPackage"))

    @hls_package.setter
    def hls_package(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsPackageProperty"]],
    ) -> None:
        jsii.set(self, "hlsPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="manifestName")
    def manifest_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::OriginEndpoint.ManifestName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-manifestname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "manifestName"))

    @manifest_name.setter
    def manifest_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "manifestName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mssPackage")
    def mss_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.MssPackageProperty"]]:
        '''``AWS::MediaPackage::OriginEndpoint.MssPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-msspackage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.MssPackageProperty"]], jsii.get(self, "mssPackage"))

    @mss_package.setter
    def mss_package(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.MssPackageProperty"]],
    ) -> None:
        jsii.set(self, "mssPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="origination")
    def origination(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::OriginEndpoint.Origination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-origination
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "origination"))

    @origination.setter
    def origination(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "origination", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startoverWindowSeconds")
    def startover_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaPackage::OriginEndpoint.StartoverWindowSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-startoverwindowseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startoverWindowSeconds"))

    @startover_window_seconds.setter
    def startover_window_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "startoverWindowSeconds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeDelaySeconds")
    def time_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaPackage::OriginEndpoint.TimeDelaySeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-timedelayseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeDelaySeconds"))

    @time_delay_seconds.setter
    def time_delay_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "timeDelaySeconds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="whitelist")
    def whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::MediaPackage::OriginEndpoint.Whitelist``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-whitelist
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "whitelist"))

    @whitelist.setter
    def whitelist(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "whitelist", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.AuthorizationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cdn_identifier_secret": "cdnIdentifierSecret",
            "secrets_role_arn": "secretsRoleArn",
        },
    )
    class AuthorizationProperty:
        def __init__(
            self,
            *,
            cdn_identifier_secret: builtins.str,
            secrets_role_arn: builtins.str,
        ) -> None:
            '''
            :param cdn_identifier_secret: ``CfnOriginEndpoint.AuthorizationProperty.CdnIdentifierSecret``.
            :param secrets_role_arn: ``CfnOriginEndpoint.AuthorizationProperty.SecretsRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cdn_identifier_secret": cdn_identifier_secret,
                "secrets_role_arn": secrets_role_arn,
            }

        @builtins.property
        def cdn_identifier_secret(self) -> builtins.str:
            '''``CfnOriginEndpoint.AuthorizationProperty.CdnIdentifierSecret``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-cdnidentifiersecret
            '''
            result = self._values.get("cdn_identifier_secret")
            assert result is not None, "Required property 'cdn_identifier_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secrets_role_arn(self) -> builtins.str:
            '''``CfnOriginEndpoint.AuthorizationProperty.SecretsRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-secretsrolearn
            '''
            result = self._values.get("secrets_role_arn")
            assert result is not None, "Required property 'secrets_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.CmafEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "speke_key_provider": "spekeKeyProvider",
            "constant_initialization_vector": "constantInitializationVector",
            "key_rotation_interval_seconds": "keyRotationIntervalSeconds",
        },
    )
    class CmafEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"],
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param speke_key_provider: ``CfnOriginEndpoint.CmafEncryptionProperty.SpekeKeyProvider``.
            :param constant_initialization_vector: ``CfnOriginEndpoint.CmafEncryptionProperty.ConstantInitializationVector``.
            :param key_rotation_interval_seconds: ``CfnOriginEndpoint.CmafEncryptionProperty.KeyRotationIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if key_rotation_interval_seconds is not None:
                self._values["key_rotation_interval_seconds"] = key_rotation_interval_seconds

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"]:
            '''``CfnOriginEndpoint.CmafEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.CmafEncryptionProperty.ConstantInitializationVector``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_rotation_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.CmafEncryptionProperty.KeyRotationIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-keyrotationintervalseconds
            '''
            result = self._values.get("key_rotation_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CmafEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.CmafPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption": "encryption",
            "hls_manifests": "hlsManifests",
            "segment_duration_seconds": "segmentDurationSeconds",
            "segment_prefix": "segmentPrefix",
            "stream_selection": "streamSelection",
        },
    )
    class CmafPackageProperty:
        def __init__(
            self,
            *,
            encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.CmafEncryptionProperty"]] = None,
            hls_manifests: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsManifestProperty"]]]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            segment_prefix: typing.Optional[builtins.str] = None,
            stream_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]] = None,
        ) -> None:
            '''
            :param encryption: ``CfnOriginEndpoint.CmafPackageProperty.Encryption``.
            :param hls_manifests: ``CfnOriginEndpoint.CmafPackageProperty.HlsManifests``.
            :param segment_duration_seconds: ``CfnOriginEndpoint.CmafPackageProperty.SegmentDurationSeconds``.
            :param segment_prefix: ``CfnOriginEndpoint.CmafPackageProperty.SegmentPrefix``.
            :param stream_selection: ``CfnOriginEndpoint.CmafPackageProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if encryption is not None:
                self._values["encryption"] = encryption
            if hls_manifests is not None:
                self._values["hls_manifests"] = hls_manifests
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if segment_prefix is not None:
                self._values["segment_prefix"] = segment_prefix
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.CmafEncryptionProperty"]]:
            '''``CfnOriginEndpoint.CmafPackageProperty.Encryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.CmafEncryptionProperty"]], result)

        @builtins.property
        def hls_manifests(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsManifestProperty"]]]]:
            '''``CfnOriginEndpoint.CmafPackageProperty.HlsManifests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-hlsmanifests
            '''
            result = self._values.get("hls_manifests")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsManifestProperty"]]]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.CmafPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.CmafPackageProperty.SegmentPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentprefix
            '''
            result = self._values.get("segment_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]]:
            '''``CfnOriginEndpoint.CmafPackageProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CmafPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.DashEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "speke_key_provider": "spekeKeyProvider",
            "key_rotation_interval_seconds": "keyRotationIntervalSeconds",
        },
    )
    class DashEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"],
            key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param speke_key_provider: ``CfnOriginEndpoint.DashEncryptionProperty.SpekeKeyProvider``.
            :param key_rotation_interval_seconds: ``CfnOriginEndpoint.DashEncryptionProperty.KeyRotationIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }
            if key_rotation_interval_seconds is not None:
                self._values["key_rotation_interval_seconds"] = key_rotation_interval_seconds

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"]:
            '''``CfnOriginEndpoint.DashEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"], result)

        @builtins.property
        def key_rotation_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.DashEncryptionProperty.KeyRotationIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-keyrotationintervalseconds
            '''
            result = self._values.get("key_rotation_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.DashPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ads_on_delivery_restrictions": "adsOnDeliveryRestrictions",
            "ad_triggers": "adTriggers",
            "encryption": "encryption",
            "manifest_layout": "manifestLayout",
            "manifest_window_seconds": "manifestWindowSeconds",
            "min_buffer_time_seconds": "minBufferTimeSeconds",
            "min_update_period_seconds": "minUpdatePeriodSeconds",
            "period_triggers": "periodTriggers",
            "profile": "profile",
            "segment_duration_seconds": "segmentDurationSeconds",
            "segment_template_format": "segmentTemplateFormat",
            "stream_selection": "streamSelection",
            "suggested_presentation_delay_seconds": "suggestedPresentationDelaySeconds",
            "utc_timing": "utcTiming",
            "utc_timing_uri": "utcTimingUri",
        },
    )
    class DashPackageProperty:
        def __init__(
            self,
            *,
            ads_on_delivery_restrictions: typing.Optional[builtins.str] = None,
            ad_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.DashEncryptionProperty"]] = None,
            manifest_layout: typing.Optional[builtins.str] = None,
            manifest_window_seconds: typing.Optional[jsii.Number] = None,
            min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
            min_update_period_seconds: typing.Optional[jsii.Number] = None,
            period_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            profile: typing.Optional[builtins.str] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            segment_template_format: typing.Optional[builtins.str] = None,
            stream_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]] = None,
            suggested_presentation_delay_seconds: typing.Optional[jsii.Number] = None,
            utc_timing: typing.Optional[builtins.str] = None,
            utc_timing_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param ads_on_delivery_restrictions: ``CfnOriginEndpoint.DashPackageProperty.AdsOnDeliveryRestrictions``.
            :param ad_triggers: ``CfnOriginEndpoint.DashPackageProperty.AdTriggers``.
            :param encryption: ``CfnOriginEndpoint.DashPackageProperty.Encryption``.
            :param manifest_layout: ``CfnOriginEndpoint.DashPackageProperty.ManifestLayout``.
            :param manifest_window_seconds: ``CfnOriginEndpoint.DashPackageProperty.ManifestWindowSeconds``.
            :param min_buffer_time_seconds: ``CfnOriginEndpoint.DashPackageProperty.MinBufferTimeSeconds``.
            :param min_update_period_seconds: ``CfnOriginEndpoint.DashPackageProperty.MinUpdatePeriodSeconds``.
            :param period_triggers: ``CfnOriginEndpoint.DashPackageProperty.PeriodTriggers``.
            :param profile: ``CfnOriginEndpoint.DashPackageProperty.Profile``.
            :param segment_duration_seconds: ``CfnOriginEndpoint.DashPackageProperty.SegmentDurationSeconds``.
            :param segment_template_format: ``CfnOriginEndpoint.DashPackageProperty.SegmentTemplateFormat``.
            :param stream_selection: ``CfnOriginEndpoint.DashPackageProperty.StreamSelection``.
            :param suggested_presentation_delay_seconds: ``CfnOriginEndpoint.DashPackageProperty.SuggestedPresentationDelaySeconds``.
            :param utc_timing: ``CfnOriginEndpoint.DashPackageProperty.UtcTiming``.
            :param utc_timing_uri: ``CfnOriginEndpoint.DashPackageProperty.UtcTimingUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ads_on_delivery_restrictions is not None:
                self._values["ads_on_delivery_restrictions"] = ads_on_delivery_restrictions
            if ad_triggers is not None:
                self._values["ad_triggers"] = ad_triggers
            if encryption is not None:
                self._values["encryption"] = encryption
            if manifest_layout is not None:
                self._values["manifest_layout"] = manifest_layout
            if manifest_window_seconds is not None:
                self._values["manifest_window_seconds"] = manifest_window_seconds
            if min_buffer_time_seconds is not None:
                self._values["min_buffer_time_seconds"] = min_buffer_time_seconds
            if min_update_period_seconds is not None:
                self._values["min_update_period_seconds"] = min_update_period_seconds
            if period_triggers is not None:
                self._values["period_triggers"] = period_triggers
            if profile is not None:
                self._values["profile"] = profile
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if segment_template_format is not None:
                self._values["segment_template_format"] = segment_template_format
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection
            if suggested_presentation_delay_seconds is not None:
                self._values["suggested_presentation_delay_seconds"] = suggested_presentation_delay_seconds
            if utc_timing is not None:
                self._values["utc_timing"] = utc_timing
            if utc_timing_uri is not None:
                self._values["utc_timing_uri"] = utc_timing_uri

        @builtins.property
        def ads_on_delivery_restrictions(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.DashPackageProperty.AdsOnDeliveryRestrictions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adsondeliveryrestrictions
            '''
            result = self._values.get("ads_on_delivery_restrictions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ad_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnOriginEndpoint.DashPackageProperty.AdTriggers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adtriggers
            '''
            result = self._values.get("ad_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.DashEncryptionProperty"]]:
            '''``CfnOriginEndpoint.DashPackageProperty.Encryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.DashEncryptionProperty"]], result)

        @builtins.property
        def manifest_layout(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.DashPackageProperty.ManifestLayout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestlayout
            '''
            result = self._values.get("manifest_layout")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manifest_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.DashPackageProperty.ManifestWindowSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestwindowseconds
            '''
            result = self._values.get("manifest_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_buffer_time_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.DashPackageProperty.MinBufferTimeSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minbuffertimeseconds
            '''
            result = self._values.get("min_buffer_time_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_update_period_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.DashPackageProperty.MinUpdatePeriodSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minupdateperiodseconds
            '''
            result = self._values.get("min_update_period_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def period_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnOriginEndpoint.DashPackageProperty.PeriodTriggers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-periodtriggers
            '''
            result = self._values.get("period_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.DashPackageProperty.Profile``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-profile
            '''
            result = self._values.get("profile")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.DashPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_template_format(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.DashPackageProperty.SegmentTemplateFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmenttemplateformat
            '''
            result = self._values.get("segment_template_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]]:
            '''``CfnOriginEndpoint.DashPackageProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]], result)

        @builtins.property
        def suggested_presentation_delay_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.DashPackageProperty.SuggestedPresentationDelaySeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-suggestedpresentationdelayseconds
            '''
            result = self._values.get("suggested_presentation_delay_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def utc_timing(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.DashPackageProperty.UtcTiming``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiming
            '''
            result = self._values.get("utc_timing")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def utc_timing_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.DashPackageProperty.UtcTimingUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiminguri
            '''
            result = self._values.get("utc_timing_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.HlsEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "speke_key_provider": "spekeKeyProvider",
            "constant_initialization_vector": "constantInitializationVector",
            "encryption_method": "encryptionMethod",
            "key_rotation_interval_seconds": "keyRotationIntervalSeconds",
            "repeat_ext_x_key": "repeatExtXKey",
        },
    )
    class HlsEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"],
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            encryption_method: typing.Optional[builtins.str] = None,
            key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
            repeat_ext_x_key: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param speke_key_provider: ``CfnOriginEndpoint.HlsEncryptionProperty.SpekeKeyProvider``.
            :param constant_initialization_vector: ``CfnOriginEndpoint.HlsEncryptionProperty.ConstantInitializationVector``.
            :param encryption_method: ``CfnOriginEndpoint.HlsEncryptionProperty.EncryptionMethod``.
            :param key_rotation_interval_seconds: ``CfnOriginEndpoint.HlsEncryptionProperty.KeyRotationIntervalSeconds``.
            :param repeat_ext_x_key: ``CfnOriginEndpoint.HlsEncryptionProperty.RepeatExtXKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if encryption_method is not None:
                self._values["encryption_method"] = encryption_method
            if key_rotation_interval_seconds is not None:
                self._values["key_rotation_interval_seconds"] = key_rotation_interval_seconds
            if repeat_ext_x_key is not None:
                self._values["repeat_ext_x_key"] = repeat_ext_x_key

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"]:
            '''``CfnOriginEndpoint.HlsEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsEncryptionProperty.ConstantInitializationVector``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_method(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsEncryptionProperty.EncryptionMethod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-encryptionmethod
            '''
            result = self._values.get("encryption_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_rotation_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.HlsEncryptionProperty.KeyRotationIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-keyrotationintervalseconds
            '''
            result = self._values.get("key_rotation_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def repeat_ext_x_key(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnOriginEndpoint.HlsEncryptionProperty.RepeatExtXKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-repeatextxkey
            '''
            result = self._values.get("repeat_ext_x_key")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.HlsManifestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "ad_markers": "adMarkers",
            "ads_on_delivery_restrictions": "adsOnDeliveryRestrictions",
            "ad_triggers": "adTriggers",
            "include_iframe_only_stream": "includeIframeOnlyStream",
            "manifest_name": "manifestName",
            "playlist_type": "playlistType",
            "playlist_window_seconds": "playlistWindowSeconds",
            "program_date_time_interval_seconds": "programDateTimeIntervalSeconds",
            "url": "url",
        },
    )
    class HlsManifestProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            ad_markers: typing.Optional[builtins.str] = None,
            ads_on_delivery_restrictions: typing.Optional[builtins.str] = None,
            ad_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            manifest_name: typing.Optional[builtins.str] = None,
            playlist_type: typing.Optional[builtins.str] = None,
            playlist_window_seconds: typing.Optional[jsii.Number] = None,
            program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param id: ``CfnOriginEndpoint.HlsManifestProperty.Id``.
            :param ad_markers: ``CfnOriginEndpoint.HlsManifestProperty.AdMarkers``.
            :param ads_on_delivery_restrictions: ``CfnOriginEndpoint.HlsManifestProperty.AdsOnDeliveryRestrictions``.
            :param ad_triggers: ``CfnOriginEndpoint.HlsManifestProperty.AdTriggers``.
            :param include_iframe_only_stream: ``CfnOriginEndpoint.HlsManifestProperty.IncludeIframeOnlyStream``.
            :param manifest_name: ``CfnOriginEndpoint.HlsManifestProperty.ManifestName``.
            :param playlist_type: ``CfnOriginEndpoint.HlsManifestProperty.PlaylistType``.
            :param playlist_window_seconds: ``CfnOriginEndpoint.HlsManifestProperty.PlaylistWindowSeconds``.
            :param program_date_time_interval_seconds: ``CfnOriginEndpoint.HlsManifestProperty.ProgramDateTimeIntervalSeconds``.
            :param url: ``CfnOriginEndpoint.HlsManifestProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "id": id,
            }
            if ad_markers is not None:
                self._values["ad_markers"] = ad_markers
            if ads_on_delivery_restrictions is not None:
                self._values["ads_on_delivery_restrictions"] = ads_on_delivery_restrictions
            if ad_triggers is not None:
                self._values["ad_triggers"] = ad_triggers
            if include_iframe_only_stream is not None:
                self._values["include_iframe_only_stream"] = include_iframe_only_stream
            if manifest_name is not None:
                self._values["manifest_name"] = manifest_name
            if playlist_type is not None:
                self._values["playlist_type"] = playlist_type
            if playlist_window_seconds is not None:
                self._values["playlist_window_seconds"] = playlist_window_seconds
            if program_date_time_interval_seconds is not None:
                self._values["program_date_time_interval_seconds"] = program_date_time_interval_seconds
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def id(self) -> builtins.str:
            '''``CfnOriginEndpoint.HlsManifestProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ad_markers(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsManifestProperty.AdMarkers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-admarkers
            '''
            result = self._values.get("ad_markers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ads_on_delivery_restrictions(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsManifestProperty.AdsOnDeliveryRestrictions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adsondeliveryrestrictions
            '''
            result = self._values.get("ads_on_delivery_restrictions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ad_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnOriginEndpoint.HlsManifestProperty.AdTriggers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adtriggers
            '''
            result = self._values.get("ad_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include_iframe_only_stream(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnOriginEndpoint.HlsManifestProperty.IncludeIframeOnlyStream``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-includeiframeonlystream
            '''
            result = self._values.get("include_iframe_only_stream")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def manifest_name(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsManifestProperty.ManifestName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-manifestname
            '''
            result = self._values.get("manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def playlist_type(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsManifestProperty.PlaylistType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlisttype
            '''
            result = self._values.get("playlist_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def playlist_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.HlsManifestProperty.PlaylistWindowSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlistwindowseconds
            '''
            result = self._values.get("playlist_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def program_date_time_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.HlsManifestProperty.ProgramDateTimeIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-programdatetimeintervalseconds
            '''
            result = self._values.get("program_date_time_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsManifestProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsManifestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.HlsPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_markers": "adMarkers",
            "ads_on_delivery_restrictions": "adsOnDeliveryRestrictions",
            "ad_triggers": "adTriggers",
            "encryption": "encryption",
            "include_iframe_only_stream": "includeIframeOnlyStream",
            "playlist_type": "playlistType",
            "playlist_window_seconds": "playlistWindowSeconds",
            "program_date_time_interval_seconds": "programDateTimeIntervalSeconds",
            "segment_duration_seconds": "segmentDurationSeconds",
            "stream_selection": "streamSelection",
            "use_audio_rendition_group": "useAudioRenditionGroup",
        },
    )
    class HlsPackageProperty:
        def __init__(
            self,
            *,
            ad_markers: typing.Optional[builtins.str] = None,
            ads_on_delivery_restrictions: typing.Optional[builtins.str] = None,
            ad_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsEncryptionProperty"]] = None,
            include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            playlist_type: typing.Optional[builtins.str] = None,
            playlist_window_seconds: typing.Optional[jsii.Number] = None,
            program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            stream_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]] = None,
            use_audio_rendition_group: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param ad_markers: ``CfnOriginEndpoint.HlsPackageProperty.AdMarkers``.
            :param ads_on_delivery_restrictions: ``CfnOriginEndpoint.HlsPackageProperty.AdsOnDeliveryRestrictions``.
            :param ad_triggers: ``CfnOriginEndpoint.HlsPackageProperty.AdTriggers``.
            :param encryption: ``CfnOriginEndpoint.HlsPackageProperty.Encryption``.
            :param include_iframe_only_stream: ``CfnOriginEndpoint.HlsPackageProperty.IncludeIframeOnlyStream``.
            :param playlist_type: ``CfnOriginEndpoint.HlsPackageProperty.PlaylistType``.
            :param playlist_window_seconds: ``CfnOriginEndpoint.HlsPackageProperty.PlaylistWindowSeconds``.
            :param program_date_time_interval_seconds: ``CfnOriginEndpoint.HlsPackageProperty.ProgramDateTimeIntervalSeconds``.
            :param segment_duration_seconds: ``CfnOriginEndpoint.HlsPackageProperty.SegmentDurationSeconds``.
            :param stream_selection: ``CfnOriginEndpoint.HlsPackageProperty.StreamSelection``.
            :param use_audio_rendition_group: ``CfnOriginEndpoint.HlsPackageProperty.UseAudioRenditionGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_markers is not None:
                self._values["ad_markers"] = ad_markers
            if ads_on_delivery_restrictions is not None:
                self._values["ads_on_delivery_restrictions"] = ads_on_delivery_restrictions
            if ad_triggers is not None:
                self._values["ad_triggers"] = ad_triggers
            if encryption is not None:
                self._values["encryption"] = encryption
            if include_iframe_only_stream is not None:
                self._values["include_iframe_only_stream"] = include_iframe_only_stream
            if playlist_type is not None:
                self._values["playlist_type"] = playlist_type
            if playlist_window_seconds is not None:
                self._values["playlist_window_seconds"] = playlist_window_seconds
            if program_date_time_interval_seconds is not None:
                self._values["program_date_time_interval_seconds"] = program_date_time_interval_seconds
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection
            if use_audio_rendition_group is not None:
                self._values["use_audio_rendition_group"] = use_audio_rendition_group

        @builtins.property
        def ad_markers(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsPackageProperty.AdMarkers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-admarkers
            '''
            result = self._values.get("ad_markers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ads_on_delivery_restrictions(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsPackageProperty.AdsOnDeliveryRestrictions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adsondeliveryrestrictions
            '''
            result = self._values.get("ads_on_delivery_restrictions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ad_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnOriginEndpoint.HlsPackageProperty.AdTriggers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adtriggers
            '''
            result = self._values.get("ad_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsEncryptionProperty"]]:
            '''``CfnOriginEndpoint.HlsPackageProperty.Encryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.HlsEncryptionProperty"]], result)

        @builtins.property
        def include_iframe_only_stream(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnOriginEndpoint.HlsPackageProperty.IncludeIframeOnlyStream``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-includeiframeonlystream
            '''
            result = self._values.get("include_iframe_only_stream")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def playlist_type(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.HlsPackageProperty.PlaylistType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlisttype
            '''
            result = self._values.get("playlist_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def playlist_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.HlsPackageProperty.PlaylistWindowSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlistwindowseconds
            '''
            result = self._values.get("playlist_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def program_date_time_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.HlsPackageProperty.ProgramDateTimeIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-programdatetimeintervalseconds
            '''
            result = self._values.get("program_date_time_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.HlsPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]]:
            '''``CfnOriginEndpoint.HlsPackageProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]], result)

        @builtins.property
        def use_audio_rendition_group(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnOriginEndpoint.HlsPackageProperty.UseAudioRenditionGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-useaudiorenditiongroup
            '''
            result = self._values.get("use_audio_rendition_group")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.MssEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"speke_key_provider": "spekeKeyProvider"},
    )
    class MssEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"],
        ) -> None:
            '''
            :param speke_key_provider: ``CfnOriginEndpoint.MssEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-mssencryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"]:
            '''``CfnOriginEndpoint.MssEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-mssencryption.html#cfn-mediapackage-originendpoint-mssencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.SpekeKeyProviderProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.MssPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption": "encryption",
            "manifest_window_seconds": "manifestWindowSeconds",
            "segment_duration_seconds": "segmentDurationSeconds",
            "stream_selection": "streamSelection",
        },
    )
    class MssPackageProperty:
        def __init__(
            self,
            *,
            encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.MssEncryptionProperty"]] = None,
            manifest_window_seconds: typing.Optional[jsii.Number] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            stream_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]] = None,
        ) -> None:
            '''
            :param encryption: ``CfnOriginEndpoint.MssPackageProperty.Encryption``.
            :param manifest_window_seconds: ``CfnOriginEndpoint.MssPackageProperty.ManifestWindowSeconds``.
            :param segment_duration_seconds: ``CfnOriginEndpoint.MssPackageProperty.SegmentDurationSeconds``.
            :param stream_selection: ``CfnOriginEndpoint.MssPackageProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if encryption is not None:
                self._values["encryption"] = encryption
            if manifest_window_seconds is not None:
                self._values["manifest_window_seconds"] = manifest_window_seconds
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.MssEncryptionProperty"]]:
            '''``CfnOriginEndpoint.MssPackageProperty.Encryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.MssEncryptionProperty"]], result)

        @builtins.property
        def manifest_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.MssPackageProperty.ManifestWindowSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-manifestwindowseconds
            '''
            result = self._values.get("manifest_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.MssPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]]:
            '''``CfnOriginEndpoint.MssPackageProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnOriginEndpoint.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_id": "resourceId",
            "role_arn": "roleArn",
            "system_ids": "systemIds",
            "url": "url",
            "certificate_arn": "certificateArn",
        },
    )
    class SpekeKeyProviderProperty:
        def __init__(
            self,
            *,
            resource_id: builtins.str,
            role_arn: builtins.str,
            system_ids: typing.Sequence[builtins.str],
            url: builtins.str,
            certificate_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param resource_id: ``CfnOriginEndpoint.SpekeKeyProviderProperty.ResourceId``.
            :param role_arn: ``CfnOriginEndpoint.SpekeKeyProviderProperty.RoleArn``.
            :param system_ids: ``CfnOriginEndpoint.SpekeKeyProviderProperty.SystemIds``.
            :param url: ``CfnOriginEndpoint.SpekeKeyProviderProperty.Url``.
            :param certificate_arn: ``CfnOriginEndpoint.SpekeKeyProviderProperty.CertificateArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "resource_id": resource_id,
                "role_arn": role_arn,
                "system_ids": system_ids,
                "url": url,
            }
            if certificate_arn is not None:
                self._values["certificate_arn"] = certificate_arn

        @builtins.property
        def resource_id(self) -> builtins.str:
            '''``CfnOriginEndpoint.SpekeKeyProviderProperty.ResourceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-resourceid
            '''
            result = self._values.get("resource_id")
            assert result is not None, "Required property 'resource_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnOriginEndpoint.SpekeKeyProviderProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def system_ids(self) -> typing.List[builtins.str]:
            '''``CfnOriginEndpoint.SpekeKeyProviderProperty.SystemIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-systemids
            '''
            result = self._values.get("system_ids")
            assert result is not None, "Required property 'system_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def url(self) -> builtins.str:
            '''``CfnOriginEndpoint.SpekeKeyProviderProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def certificate_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.SpekeKeyProviderProperty.CertificateArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-certificatearn
            '''
            result = self._values.get("certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpekeKeyProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpoint.StreamSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_video_bits_per_second": "maxVideoBitsPerSecond",
            "min_video_bits_per_second": "minVideoBitsPerSecond",
            "stream_order": "streamOrder",
        },
    )
    class StreamSelectionProperty:
        def __init__(
            self,
            *,
            max_video_bits_per_second: typing.Optional[jsii.Number] = None,
            min_video_bits_per_second: typing.Optional[jsii.Number] = None,
            stream_order: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param max_video_bits_per_second: ``CfnOriginEndpoint.StreamSelectionProperty.MaxVideoBitsPerSecond``.
            :param min_video_bits_per_second: ``CfnOriginEndpoint.StreamSelectionProperty.MinVideoBitsPerSecond``.
            :param stream_order: ``CfnOriginEndpoint.StreamSelectionProperty.StreamOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if max_video_bits_per_second is not None:
                self._values["max_video_bits_per_second"] = max_video_bits_per_second
            if min_video_bits_per_second is not None:
                self._values["min_video_bits_per_second"] = min_video_bits_per_second
            if stream_order is not None:
                self._values["stream_order"] = stream_order

        @builtins.property
        def max_video_bits_per_second(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.StreamSelectionProperty.MaxVideoBitsPerSecond``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-maxvideobitspersecond
            '''
            result = self._values.get("max_video_bits_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_video_bits_per_second(self) -> typing.Optional[jsii.Number]:
            '''``CfnOriginEndpoint.StreamSelectionProperty.MinVideoBitsPerSecond``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-minvideobitspersecond
            '''
            result = self._values.get("min_video_bits_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_order(self) -> typing.Optional[builtins.str]:
            '''``CfnOriginEndpoint.StreamSelectionProperty.StreamOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-streamorder
            '''
            result = self._values.get("stream_order")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediapackage.CfnOriginEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_id": "channelId",
        "id": "id",
        "authorization": "authorization",
        "cmaf_package": "cmafPackage",
        "dash_package": "dashPackage",
        "description": "description",
        "hls_package": "hlsPackage",
        "manifest_name": "manifestName",
        "mss_package": "mssPackage",
        "origination": "origination",
        "startover_window_seconds": "startoverWindowSeconds",
        "tags": "tags",
        "time_delay_seconds": "timeDelaySeconds",
        "whitelist": "whitelist",
    },
)
class CfnOriginEndpointProps:
    def __init__(
        self,
        *,
        channel_id: builtins.str,
        id: builtins.str,
        authorization: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.AuthorizationProperty]] = None,
        cmaf_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.CmafPackageProperty]] = None,
        dash_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.DashPackageProperty]] = None,
        description: typing.Optional[builtins.str] = None,
        hls_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.HlsPackageProperty]] = None,
        manifest_name: typing.Optional[builtins.str] = None,
        mss_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.MssPackageProperty]] = None,
        origination: typing.Optional[builtins.str] = None,
        startover_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        time_delay_seconds: typing.Optional[jsii.Number] = None,
        whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaPackage::OriginEndpoint``.

        :param channel_id: ``AWS::MediaPackage::OriginEndpoint.ChannelId``.
        :param id: ``AWS::MediaPackage::OriginEndpoint.Id``.
        :param authorization: ``AWS::MediaPackage::OriginEndpoint.Authorization``.
        :param cmaf_package: ``AWS::MediaPackage::OriginEndpoint.CmafPackage``.
        :param dash_package: ``AWS::MediaPackage::OriginEndpoint.DashPackage``.
        :param description: ``AWS::MediaPackage::OriginEndpoint.Description``.
        :param hls_package: ``AWS::MediaPackage::OriginEndpoint.HlsPackage``.
        :param manifest_name: ``AWS::MediaPackage::OriginEndpoint.ManifestName``.
        :param mss_package: ``AWS::MediaPackage::OriginEndpoint.MssPackage``.
        :param origination: ``AWS::MediaPackage::OriginEndpoint.Origination``.
        :param startover_window_seconds: ``AWS::MediaPackage::OriginEndpoint.StartoverWindowSeconds``.
        :param tags: ``AWS::MediaPackage::OriginEndpoint.Tags``.
        :param time_delay_seconds: ``AWS::MediaPackage::OriginEndpoint.TimeDelaySeconds``.
        :param whitelist: ``AWS::MediaPackage::OriginEndpoint.Whitelist``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "channel_id": channel_id,
            "id": id,
        }
        if authorization is not None:
            self._values["authorization"] = authorization
        if cmaf_package is not None:
            self._values["cmaf_package"] = cmaf_package
        if dash_package is not None:
            self._values["dash_package"] = dash_package
        if description is not None:
            self._values["description"] = description
        if hls_package is not None:
            self._values["hls_package"] = hls_package
        if manifest_name is not None:
            self._values["manifest_name"] = manifest_name
        if mss_package is not None:
            self._values["mss_package"] = mss_package
        if origination is not None:
            self._values["origination"] = origination
        if startover_window_seconds is not None:
            self._values["startover_window_seconds"] = startover_window_seconds
        if tags is not None:
            self._values["tags"] = tags
        if time_delay_seconds is not None:
            self._values["time_delay_seconds"] = time_delay_seconds
        if whitelist is not None:
            self._values["whitelist"] = whitelist

    @builtins.property
    def channel_id(self) -> builtins.str:
        '''``AWS::MediaPackage::OriginEndpoint.ChannelId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-channelid
        '''
        result = self._values.get("channel_id")
        assert result is not None, "Required property 'channel_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::OriginEndpoint.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.AuthorizationProperty]]:
        '''``AWS::MediaPackage::OriginEndpoint.Authorization``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-authorization
        '''
        result = self._values.get("authorization")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.AuthorizationProperty]], result)

    @builtins.property
    def cmaf_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.CmafPackageProperty]]:
        '''``AWS::MediaPackage::OriginEndpoint.CmafPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-cmafpackage
        '''
        result = self._values.get("cmaf_package")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.CmafPackageProperty]], result)

    @builtins.property
    def dash_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.DashPackageProperty]]:
        '''``AWS::MediaPackage::OriginEndpoint.DashPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-dashpackage
        '''
        result = self._values.get("dash_package")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.DashPackageProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::OriginEndpoint.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hls_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.HlsPackageProperty]]:
        '''``AWS::MediaPackage::OriginEndpoint.HlsPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-hlspackage
        '''
        result = self._values.get("hls_package")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.HlsPackageProperty]], result)

    @builtins.property
    def manifest_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::OriginEndpoint.ManifestName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-manifestname
        '''
        result = self._values.get("manifest_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mss_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.MssPackageProperty]]:
        '''``AWS::MediaPackage::OriginEndpoint.MssPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-msspackage
        '''
        result = self._values.get("mss_package")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnOriginEndpoint.MssPackageProperty]], result)

    @builtins.property
    def origination(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaPackage::OriginEndpoint.Origination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-origination
        '''
        result = self._values.get("origination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def startover_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaPackage::OriginEndpoint.StartoverWindowSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-startoverwindowseconds
        '''
        result = self._values.get("startover_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::MediaPackage::OriginEndpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def time_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaPackage::OriginEndpoint.TimeDelaySeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-timedelayseconds
        '''
        result = self._values.get("time_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::MediaPackage::OriginEndpoint.Whitelist``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-whitelist
        '''
        result = self._values.get("whitelist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOriginEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPackagingConfiguration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration",
):
    '''A CloudFormation ``AWS::MediaPackage::PackagingConfiguration``.

    :cloudformationResource: AWS::MediaPackage::PackagingConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id_: builtins.str,
        *,
        id: builtins.str,
        packaging_group_id: builtins.str,
        cmaf_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.CmafPackageProperty"]] = None,
        dash_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashPackageProperty"]] = None,
        hls_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsPackageProperty"]] = None,
        mss_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssPackageProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaPackage::PackagingConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param id: ``AWS::MediaPackage::PackagingConfiguration.Id``.
        :param packaging_group_id: ``AWS::MediaPackage::PackagingConfiguration.PackagingGroupId``.
        :param cmaf_package: ``AWS::MediaPackage::PackagingConfiguration.CmafPackage``.
        :param dash_package: ``AWS::MediaPackage::PackagingConfiguration.DashPackage``.
        :param hls_package: ``AWS::MediaPackage::PackagingConfiguration.HlsPackage``.
        :param mss_package: ``AWS::MediaPackage::PackagingConfiguration.MssPackage``.
        :param tags: ``AWS::MediaPackage::PackagingConfiguration.Tags``.
        '''
        props = CfnPackagingConfigurationProps(
            id=id,
            packaging_group_id=packaging_group_id,
            cmaf_package=cmaf_package,
            dash_package=dash_package,
            hls_package=hls_package,
            mss_package=mss_package,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

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
        '''``AWS::MediaPackage::PackagingConfiguration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::PackagingConfiguration.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-id
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="packagingGroupId")
    def packaging_group_id(self) -> builtins.str:
        '''``AWS::MediaPackage::PackagingConfiguration.PackagingGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-packaginggroupid
        '''
        return typing.cast(builtins.str, jsii.get(self, "packagingGroupId"))

    @packaging_group_id.setter
    def packaging_group_id(self, value: builtins.str) -> None:
        jsii.set(self, "packagingGroupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cmafPackage")
    def cmaf_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.CmafPackageProperty"]]:
        '''``AWS::MediaPackage::PackagingConfiguration.CmafPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-cmafpackage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.CmafPackageProperty"]], jsii.get(self, "cmafPackage"))

    @cmaf_package.setter
    def cmaf_package(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.CmafPackageProperty"]],
    ) -> None:
        jsii.set(self, "cmafPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dashPackage")
    def dash_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashPackageProperty"]]:
        '''``AWS::MediaPackage::PackagingConfiguration.DashPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-dashpackage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashPackageProperty"]], jsii.get(self, "dashPackage"))

    @dash_package.setter
    def dash_package(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashPackageProperty"]],
    ) -> None:
        jsii.set(self, "dashPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hlsPackage")
    def hls_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsPackageProperty"]]:
        '''``AWS::MediaPackage::PackagingConfiguration.HlsPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-hlspackage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsPackageProperty"]], jsii.get(self, "hlsPackage"))

    @hls_package.setter
    def hls_package(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsPackageProperty"]],
    ) -> None:
        jsii.set(self, "hlsPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mssPackage")
    def mss_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssPackageProperty"]]:
        '''``AWS::MediaPackage::PackagingConfiguration.MssPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-msspackage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssPackageProperty"]], jsii.get(self, "mssPackage"))

    @mss_package.setter
    def mss_package(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssPackageProperty"]],
    ) -> None:
        jsii.set(self, "mssPackage", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.CmafEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"speke_key_provider": "spekeKeyProvider"},
    )
    class CmafEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"],
        ) -> None:
            '''
            :param speke_key_provider: ``CfnPackagingConfiguration.CmafEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"]:
            '''``CfnPackagingConfiguration.CmafEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html#cfn-mediapackage-packagingconfiguration-cmafencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CmafEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.CmafPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hls_manifests": "hlsManifests",
            "encryption": "encryption",
            "include_encoder_configuration_in_segments": "includeEncoderConfigurationInSegments",
            "segment_duration_seconds": "segmentDurationSeconds",
        },
    )
    class CmafPackageProperty:
        def __init__(
            self,
            *,
            hls_manifests: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsManifestProperty"]]],
            encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.CmafEncryptionProperty"]] = None,
            include_encoder_configuration_in_segments: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param hls_manifests: ``CfnPackagingConfiguration.CmafPackageProperty.HlsManifests``.
            :param encryption: ``CfnPackagingConfiguration.CmafPackageProperty.Encryption``.
            :param include_encoder_configuration_in_segments: ``CfnPackagingConfiguration.CmafPackageProperty.IncludeEncoderConfigurationInSegments``.
            :param segment_duration_seconds: ``CfnPackagingConfiguration.CmafPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "hls_manifests": hls_manifests,
            }
            if encryption is not None:
                self._values["encryption"] = encryption
            if include_encoder_configuration_in_segments is not None:
                self._values["include_encoder_configuration_in_segments"] = include_encoder_configuration_in_segments
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds

        @builtins.property
        def hls_manifests(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsManifestProperty"]]]:
            '''``CfnPackagingConfiguration.CmafPackageProperty.HlsManifests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-hlsmanifests
            '''
            result = self._values.get("hls_manifests")
            assert result is not None, "Required property 'hls_manifests' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsManifestProperty"]]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.CmafEncryptionProperty"]]:
            '''``CfnPackagingConfiguration.CmafPackageProperty.Encryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.CmafEncryptionProperty"]], result)

        @builtins.property
        def include_encoder_configuration_in_segments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnPackagingConfiguration.CmafPackageProperty.IncludeEncoderConfigurationInSegments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-includeencoderconfigurationinsegments
            '''
            result = self._values.get("include_encoder_configuration_in_segments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnPackagingConfiguration.CmafPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CmafPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.DashEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"speke_key_provider": "spekeKeyProvider"},
    )
    class DashEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"],
        ) -> None:
            '''
            :param speke_key_provider: ``CfnPackagingConfiguration.DashEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"]:
            '''``CfnPackagingConfiguration.DashEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html#cfn-mediapackage-packagingconfiguration-dashencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.DashManifestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_layout": "manifestLayout",
            "manifest_name": "manifestName",
            "min_buffer_time_seconds": "minBufferTimeSeconds",
            "profile": "profile",
            "stream_selection": "streamSelection",
        },
    )
    class DashManifestProperty:
        def __init__(
            self,
            *,
            manifest_layout: typing.Optional[builtins.str] = None,
            manifest_name: typing.Optional[builtins.str] = None,
            min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
            profile: typing.Optional[builtins.str] = None,
            stream_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.StreamSelectionProperty"]] = None,
        ) -> None:
            '''
            :param manifest_layout: ``CfnPackagingConfiguration.DashManifestProperty.ManifestLayout``.
            :param manifest_name: ``CfnPackagingConfiguration.DashManifestProperty.ManifestName``.
            :param min_buffer_time_seconds: ``CfnPackagingConfiguration.DashManifestProperty.MinBufferTimeSeconds``.
            :param profile: ``CfnPackagingConfiguration.DashManifestProperty.Profile``.
            :param stream_selection: ``CfnPackagingConfiguration.DashManifestProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if manifest_layout is not None:
                self._values["manifest_layout"] = manifest_layout
            if manifest_name is not None:
                self._values["manifest_name"] = manifest_name
            if min_buffer_time_seconds is not None:
                self._values["min_buffer_time_seconds"] = min_buffer_time_seconds
            if profile is not None:
                self._values["profile"] = profile
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def manifest_layout(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.DashManifestProperty.ManifestLayout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestlayout
            '''
            result = self._values.get("manifest_layout")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manifest_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.DashManifestProperty.ManifestName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestname
            '''
            result = self._values.get("manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def min_buffer_time_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnPackagingConfiguration.DashManifestProperty.MinBufferTimeSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-minbuffertimeseconds
            '''
            result = self._values.get("min_buffer_time_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.DashManifestProperty.Profile``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-profile
            '''
            result = self._values.get("profile")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.StreamSelectionProperty"]]:
            '''``CfnPackagingConfiguration.DashManifestProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashManifestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.DashPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dash_manifests": "dashManifests",
            "encryption": "encryption",
            "include_encoder_configuration_in_segments": "includeEncoderConfigurationInSegments",
            "period_triggers": "periodTriggers",
            "segment_duration_seconds": "segmentDurationSeconds",
            "segment_template_format": "segmentTemplateFormat",
        },
    )
    class DashPackageProperty:
        def __init__(
            self,
            *,
            dash_manifests: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashManifestProperty"]]],
            encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashEncryptionProperty"]] = None,
            include_encoder_configuration_in_segments: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            period_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            segment_template_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param dash_manifests: ``CfnPackagingConfiguration.DashPackageProperty.DashManifests``.
            :param encryption: ``CfnPackagingConfiguration.DashPackageProperty.Encryption``.
            :param include_encoder_configuration_in_segments: ``CfnPackagingConfiguration.DashPackageProperty.IncludeEncoderConfigurationInSegments``.
            :param period_triggers: ``CfnPackagingConfiguration.DashPackageProperty.PeriodTriggers``.
            :param segment_duration_seconds: ``CfnPackagingConfiguration.DashPackageProperty.SegmentDurationSeconds``.
            :param segment_template_format: ``CfnPackagingConfiguration.DashPackageProperty.SegmentTemplateFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "dash_manifests": dash_manifests,
            }
            if encryption is not None:
                self._values["encryption"] = encryption
            if include_encoder_configuration_in_segments is not None:
                self._values["include_encoder_configuration_in_segments"] = include_encoder_configuration_in_segments
            if period_triggers is not None:
                self._values["period_triggers"] = period_triggers
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if segment_template_format is not None:
                self._values["segment_template_format"] = segment_template_format

        @builtins.property
        def dash_manifests(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashManifestProperty"]]]:
            '''``CfnPackagingConfiguration.DashPackageProperty.DashManifests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-dashmanifests
            '''
            result = self._values.get("dash_manifests")
            assert result is not None, "Required property 'dash_manifests' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashManifestProperty"]]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashEncryptionProperty"]]:
            '''``CfnPackagingConfiguration.DashPackageProperty.Encryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.DashEncryptionProperty"]], result)

        @builtins.property
        def include_encoder_configuration_in_segments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnPackagingConfiguration.DashPackageProperty.IncludeEncoderConfigurationInSegments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-includeencoderconfigurationinsegments
            '''
            result = self._values.get("include_encoder_configuration_in_segments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def period_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPackagingConfiguration.DashPackageProperty.PeriodTriggers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-periodtriggers
            '''
            result = self._values.get("period_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnPackagingConfiguration.DashPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_template_format(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.DashPackageProperty.SegmentTemplateFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmenttemplateformat
            '''
            result = self._values.get("segment_template_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.HlsEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "speke_key_provider": "spekeKeyProvider",
            "constant_initialization_vector": "constantInitializationVector",
            "encryption_method": "encryptionMethod",
        },
    )
    class HlsEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"],
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            encryption_method: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param speke_key_provider: ``CfnPackagingConfiguration.HlsEncryptionProperty.SpekeKeyProvider``.
            :param constant_initialization_vector: ``CfnPackagingConfiguration.HlsEncryptionProperty.ConstantInitializationVector``.
            :param encryption_method: ``CfnPackagingConfiguration.HlsEncryptionProperty.EncryptionMethod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if encryption_method is not None:
                self._values["encryption_method"] = encryption_method

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"]:
            '''``CfnPackagingConfiguration.HlsEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.HlsEncryptionProperty.ConstantInitializationVector``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_method(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.HlsEncryptionProperty.EncryptionMethod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-encryptionmethod
            '''
            result = self._values.get("encryption_method")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.HlsManifestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_markers": "adMarkers",
            "include_iframe_only_stream": "includeIframeOnlyStream",
            "manifest_name": "manifestName",
            "program_date_time_interval_seconds": "programDateTimeIntervalSeconds",
            "repeat_ext_x_key": "repeatExtXKey",
            "stream_selection": "streamSelection",
        },
    )
    class HlsManifestProperty:
        def __init__(
            self,
            *,
            ad_markers: typing.Optional[builtins.str] = None,
            include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            manifest_name: typing.Optional[builtins.str] = None,
            program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
            repeat_ext_x_key: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            stream_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.StreamSelectionProperty"]] = None,
        ) -> None:
            '''
            :param ad_markers: ``CfnPackagingConfiguration.HlsManifestProperty.AdMarkers``.
            :param include_iframe_only_stream: ``CfnPackagingConfiguration.HlsManifestProperty.IncludeIframeOnlyStream``.
            :param manifest_name: ``CfnPackagingConfiguration.HlsManifestProperty.ManifestName``.
            :param program_date_time_interval_seconds: ``CfnPackagingConfiguration.HlsManifestProperty.ProgramDateTimeIntervalSeconds``.
            :param repeat_ext_x_key: ``CfnPackagingConfiguration.HlsManifestProperty.RepeatExtXKey``.
            :param stream_selection: ``CfnPackagingConfiguration.HlsManifestProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_markers is not None:
                self._values["ad_markers"] = ad_markers
            if include_iframe_only_stream is not None:
                self._values["include_iframe_only_stream"] = include_iframe_only_stream
            if manifest_name is not None:
                self._values["manifest_name"] = manifest_name
            if program_date_time_interval_seconds is not None:
                self._values["program_date_time_interval_seconds"] = program_date_time_interval_seconds
            if repeat_ext_x_key is not None:
                self._values["repeat_ext_x_key"] = repeat_ext_x_key
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def ad_markers(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.HlsManifestProperty.AdMarkers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-admarkers
            '''
            result = self._values.get("ad_markers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def include_iframe_only_stream(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnPackagingConfiguration.HlsManifestProperty.IncludeIframeOnlyStream``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-includeiframeonlystream
            '''
            result = self._values.get("include_iframe_only_stream")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def manifest_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.HlsManifestProperty.ManifestName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-manifestname
            '''
            result = self._values.get("manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def program_date_time_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnPackagingConfiguration.HlsManifestProperty.ProgramDateTimeIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-programdatetimeintervalseconds
            '''
            result = self._values.get("program_date_time_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def repeat_ext_x_key(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnPackagingConfiguration.HlsManifestProperty.RepeatExtXKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-repeatextxkey
            '''
            result = self._values.get("repeat_ext_x_key")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.StreamSelectionProperty"]]:
            '''``CfnPackagingConfiguration.HlsManifestProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsManifestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.HlsPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hls_manifests": "hlsManifests",
            "encryption": "encryption",
            "segment_duration_seconds": "segmentDurationSeconds",
            "use_audio_rendition_group": "useAudioRenditionGroup",
        },
    )
    class HlsPackageProperty:
        def __init__(
            self,
            *,
            hls_manifests: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsManifestProperty"]]],
            encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsEncryptionProperty"]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            use_audio_rendition_group: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param hls_manifests: ``CfnPackagingConfiguration.HlsPackageProperty.HlsManifests``.
            :param encryption: ``CfnPackagingConfiguration.HlsPackageProperty.Encryption``.
            :param segment_duration_seconds: ``CfnPackagingConfiguration.HlsPackageProperty.SegmentDurationSeconds``.
            :param use_audio_rendition_group: ``CfnPackagingConfiguration.HlsPackageProperty.UseAudioRenditionGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "hls_manifests": hls_manifests,
            }
            if encryption is not None:
                self._values["encryption"] = encryption
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if use_audio_rendition_group is not None:
                self._values["use_audio_rendition_group"] = use_audio_rendition_group

        @builtins.property
        def hls_manifests(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsManifestProperty"]]]:
            '''``CfnPackagingConfiguration.HlsPackageProperty.HlsManifests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-hlsmanifests
            '''
            result = self._values.get("hls_manifests")
            assert result is not None, "Required property 'hls_manifests' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsManifestProperty"]]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsEncryptionProperty"]]:
            '''``CfnPackagingConfiguration.HlsPackageProperty.Encryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.HlsEncryptionProperty"]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnPackagingConfiguration.HlsPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def use_audio_rendition_group(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnPackagingConfiguration.HlsPackageProperty.UseAudioRenditionGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-useaudiorenditiongroup
            '''
            result = self._values.get("use_audio_rendition_group")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.MssEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"speke_key_provider": "spekeKeyProvider"},
    )
    class MssEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"],
        ) -> None:
            '''
            :param speke_key_provider: ``CfnPackagingConfiguration.MssEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"]:
            '''``CfnPackagingConfiguration.MssEncryptionProperty.SpekeKeyProvider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html#cfn-mediapackage-packagingconfiguration-mssencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.SpekeKeyProviderProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.MssManifestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_name": "manifestName",
            "stream_selection": "streamSelection",
        },
    )
    class MssManifestProperty:
        def __init__(
            self,
            *,
            manifest_name: typing.Optional[builtins.str] = None,
            stream_selection: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.StreamSelectionProperty"]] = None,
        ) -> None:
            '''
            :param manifest_name: ``CfnPackagingConfiguration.MssManifestProperty.ManifestName``.
            :param stream_selection: ``CfnPackagingConfiguration.MssManifestProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if manifest_name is not None:
                self._values["manifest_name"] = manifest_name
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def manifest_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.MssManifestProperty.ManifestName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-manifestname
            '''
            result = self._values.get("manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.StreamSelectionProperty"]]:
            '''``CfnPackagingConfiguration.MssManifestProperty.StreamSelection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssManifestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.MssPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mss_manifests": "mssManifests",
            "encryption": "encryption",
            "segment_duration_seconds": "segmentDurationSeconds",
        },
    )
    class MssPackageProperty:
        def __init__(
            self,
            *,
            mss_manifests: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssManifestProperty"]]],
            encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssEncryptionProperty"]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param mss_manifests: ``CfnPackagingConfiguration.MssPackageProperty.MssManifests``.
            :param encryption: ``CfnPackagingConfiguration.MssPackageProperty.Encryption``.
            :param segment_duration_seconds: ``CfnPackagingConfiguration.MssPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "mss_manifests": mss_manifests,
            }
            if encryption is not None:
                self._values["encryption"] = encryption
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds

        @builtins.property
        def mss_manifests(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssManifestProperty"]]]:
            '''``CfnPackagingConfiguration.MssPackageProperty.MssManifests``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-mssmanifests
            '''
            result = self._values.get("mss_manifests")
            assert result is not None, "Required property 'mss_manifests' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssManifestProperty"]]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssEncryptionProperty"]]:
            '''``CfnPackagingConfiguration.MssPackageProperty.Encryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingConfiguration.MssEncryptionProperty"]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnPackagingConfiguration.MssPackageProperty.SegmentDurationSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "system_ids": "systemIds", "url": "url"},
    )
    class SpekeKeyProviderProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            system_ids: typing.Sequence[builtins.str],
            url: builtins.str,
        ) -> None:
            '''
            :param role_arn: ``CfnPackagingConfiguration.SpekeKeyProviderProperty.RoleArn``.
            :param system_ids: ``CfnPackagingConfiguration.SpekeKeyProviderProperty.SystemIds``.
            :param url: ``CfnPackagingConfiguration.SpekeKeyProviderProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "role_arn": role_arn,
                "system_ids": system_ids,
                "url": url,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnPackagingConfiguration.SpekeKeyProviderProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def system_ids(self) -> typing.List[builtins.str]:
            '''``CfnPackagingConfiguration.SpekeKeyProviderProperty.SystemIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-systemids
            '''
            result = self._values.get("system_ids")
            assert result is not None, "Required property 'system_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def url(self) -> builtins.str:
            '''``CfnPackagingConfiguration.SpekeKeyProviderProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpekeKeyProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfiguration.StreamSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_video_bits_per_second": "maxVideoBitsPerSecond",
            "min_video_bits_per_second": "minVideoBitsPerSecond",
            "stream_order": "streamOrder",
        },
    )
    class StreamSelectionProperty:
        def __init__(
            self,
            *,
            max_video_bits_per_second: typing.Optional[jsii.Number] = None,
            min_video_bits_per_second: typing.Optional[jsii.Number] = None,
            stream_order: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param max_video_bits_per_second: ``CfnPackagingConfiguration.StreamSelectionProperty.MaxVideoBitsPerSecond``.
            :param min_video_bits_per_second: ``CfnPackagingConfiguration.StreamSelectionProperty.MinVideoBitsPerSecond``.
            :param stream_order: ``CfnPackagingConfiguration.StreamSelectionProperty.StreamOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if max_video_bits_per_second is not None:
                self._values["max_video_bits_per_second"] = max_video_bits_per_second
            if min_video_bits_per_second is not None:
                self._values["min_video_bits_per_second"] = min_video_bits_per_second
            if stream_order is not None:
                self._values["stream_order"] = stream_order

        @builtins.property
        def max_video_bits_per_second(self) -> typing.Optional[jsii.Number]:
            '''``CfnPackagingConfiguration.StreamSelectionProperty.MaxVideoBitsPerSecond``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-maxvideobitspersecond
            '''
            result = self._values.get("max_video_bits_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_video_bits_per_second(self) -> typing.Optional[jsii.Number]:
            '''``CfnPackagingConfiguration.StreamSelectionProperty.MinVideoBitsPerSecond``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-minvideobitspersecond
            '''
            result = self._values.get("min_video_bits_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_order(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingConfiguration.StreamSelectionProperty.StreamOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-streamorder
            '''
            result = self._values.get("stream_order")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "packaging_group_id": "packagingGroupId",
        "cmaf_package": "cmafPackage",
        "dash_package": "dashPackage",
        "hls_package": "hlsPackage",
        "mss_package": "mssPackage",
        "tags": "tags",
    },
)
class CfnPackagingConfigurationProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        packaging_group_id: builtins.str,
        cmaf_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.CmafPackageProperty]] = None,
        dash_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.DashPackageProperty]] = None,
        hls_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.HlsPackageProperty]] = None,
        mss_package: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.MssPackageProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaPackage::PackagingConfiguration``.

        :param id: ``AWS::MediaPackage::PackagingConfiguration.Id``.
        :param packaging_group_id: ``AWS::MediaPackage::PackagingConfiguration.PackagingGroupId``.
        :param cmaf_package: ``AWS::MediaPackage::PackagingConfiguration.CmafPackage``.
        :param dash_package: ``AWS::MediaPackage::PackagingConfiguration.DashPackage``.
        :param hls_package: ``AWS::MediaPackage::PackagingConfiguration.HlsPackage``.
        :param mss_package: ``AWS::MediaPackage::PackagingConfiguration.MssPackage``.
        :param tags: ``AWS::MediaPackage::PackagingConfiguration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "packaging_group_id": packaging_group_id,
        }
        if cmaf_package is not None:
            self._values["cmaf_package"] = cmaf_package
        if dash_package is not None:
            self._values["dash_package"] = dash_package
        if hls_package is not None:
            self._values["hls_package"] = hls_package
        if mss_package is not None:
            self._values["mss_package"] = mss_package
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::PackagingConfiguration.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def packaging_group_id(self) -> builtins.str:
        '''``AWS::MediaPackage::PackagingConfiguration.PackagingGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-packaginggroupid
        '''
        result = self._values.get("packaging_group_id")
        assert result is not None, "Required property 'packaging_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cmaf_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.CmafPackageProperty]]:
        '''``AWS::MediaPackage::PackagingConfiguration.CmafPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-cmafpackage
        '''
        result = self._values.get("cmaf_package")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.CmafPackageProperty]], result)

    @builtins.property
    def dash_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.DashPackageProperty]]:
        '''``AWS::MediaPackage::PackagingConfiguration.DashPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-dashpackage
        '''
        result = self._values.get("dash_package")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.DashPackageProperty]], result)

    @builtins.property
    def hls_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.HlsPackageProperty]]:
        '''``AWS::MediaPackage::PackagingConfiguration.HlsPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-hlspackage
        '''
        result = self._values.get("hls_package")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.HlsPackageProperty]], result)

    @builtins.property
    def mss_package(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.MssPackageProperty]]:
        '''``AWS::MediaPackage::PackagingConfiguration.MssPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-msspackage
        '''
        result = self._values.get("mss_package")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingConfiguration.MssPackageProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::MediaPackage::PackagingConfiguration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPackagingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPackagingGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingGroup",
):
    '''A CloudFormation ``AWS::MediaPackage::PackagingGroup``.

    :cloudformationResource: AWS::MediaPackage::PackagingGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id_: builtins.str,
        *,
        id: builtins.str,
        authorization: typing.Optional[typing.Union["CfnPackagingGroup.AuthorizationProperty", aws_cdk.core.IResolvable]] = None,
        egress_access_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingGroup.LogConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaPackage::PackagingGroup``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param id: ``AWS::MediaPackage::PackagingGroup.Id``.
        :param authorization: ``AWS::MediaPackage::PackagingGroup.Authorization``.
        :param egress_access_logs: ``AWS::MediaPackage::PackagingGroup.EgressAccessLogs``.
        :param tags: ``AWS::MediaPackage::PackagingGroup.Tags``.
        '''
        props = CfnPackagingGroupProps(
            id=id,
            authorization=authorization,
            egress_access_logs=egress_access_logs,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

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
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::MediaPackage::PackagingGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::PackagingGroup.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-id
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        jsii.set(self, "id", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="authorization")
    def authorization(
        self,
    ) -> typing.Optional[typing.Union["CfnPackagingGroup.AuthorizationProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::MediaPackage::PackagingGroup.Authorization``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-authorization
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPackagingGroup.AuthorizationProperty", aws_cdk.core.IResolvable]], jsii.get(self, "authorization"))

    @authorization.setter
    def authorization(
        self,
        value: typing.Optional[typing.Union["CfnPackagingGroup.AuthorizationProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "authorization", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="egressAccessLogs")
    def egress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingGroup.LogConfigurationProperty"]]:
        '''``AWS::MediaPackage::PackagingGroup.EgressAccessLogs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-egressaccesslogs
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingGroup.LogConfigurationProperty"]], jsii.get(self, "egressAccessLogs"))

    @egress_access_logs.setter
    def egress_access_logs(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPackagingGroup.LogConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "egressAccessLogs", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingGroup.AuthorizationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cdn_identifier_secret": "cdnIdentifierSecret",
            "secrets_role_arn": "secretsRoleArn",
        },
    )
    class AuthorizationProperty:
        def __init__(
            self,
            *,
            cdn_identifier_secret: builtins.str,
            secrets_role_arn: builtins.str,
        ) -> None:
            '''
            :param cdn_identifier_secret: ``CfnPackagingGroup.AuthorizationProperty.CdnIdentifierSecret``.
            :param secrets_role_arn: ``CfnPackagingGroup.AuthorizationProperty.SecretsRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cdn_identifier_secret": cdn_identifier_secret,
                "secrets_role_arn": secrets_role_arn,
            }

        @builtins.property
        def cdn_identifier_secret(self) -> builtins.str:
            '''``CfnPackagingGroup.AuthorizationProperty.CdnIdentifierSecret``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-cdnidentifiersecret
            '''
            result = self._values.get("cdn_identifier_secret")
            assert result is not None, "Required property 'cdn_identifier_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secrets_role_arn(self) -> builtins.str:
            '''``CfnPackagingGroup.AuthorizationProperty.SecretsRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-secretsrolearn
            '''
            result = self._values.get("secrets_role_arn")
            assert result is not None, "Required property 'secrets_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingGroup.LogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName"},
    )
    class LogConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_group_name: ``CfnPackagingGroup.LogConfigurationProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPackagingGroup.LogConfigurationProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html#cfn-mediapackage-packaginggroup-logconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediapackage.CfnPackagingGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "authorization": "authorization",
        "egress_access_logs": "egressAccessLogs",
        "tags": "tags",
    },
)
class CfnPackagingGroupProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        authorization: typing.Optional[typing.Union[CfnPackagingGroup.AuthorizationProperty, aws_cdk.core.IResolvable]] = None,
        egress_access_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingGroup.LogConfigurationProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaPackage::PackagingGroup``.

        :param id: ``AWS::MediaPackage::PackagingGroup.Id``.
        :param authorization: ``AWS::MediaPackage::PackagingGroup.Authorization``.
        :param egress_access_logs: ``AWS::MediaPackage::PackagingGroup.EgressAccessLogs``.
        :param tags: ``AWS::MediaPackage::PackagingGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if authorization is not None:
            self._values["authorization"] = authorization
        if egress_access_logs is not None:
            self._values["egress_access_logs"] = egress_access_logs
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''``AWS::MediaPackage::PackagingGroup.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization(
        self,
    ) -> typing.Optional[typing.Union[CfnPackagingGroup.AuthorizationProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::MediaPackage::PackagingGroup.Authorization``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-authorization
        '''
        result = self._values.get("authorization")
        return typing.cast(typing.Optional[typing.Union[CfnPackagingGroup.AuthorizationProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def egress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingGroup.LogConfigurationProperty]]:
        '''``AWS::MediaPackage::PackagingGroup.EgressAccessLogs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-egressaccesslogs
        '''
        result = self._values.get("egress_access_logs")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPackagingGroup.LogConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::MediaPackage::PackagingGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPackagingGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAsset",
    "CfnAssetProps",
    "CfnChannel",
    "CfnChannelProps",
    "CfnOriginEndpoint",
    "CfnOriginEndpointProps",
    "CfnPackagingConfiguration",
    "CfnPackagingConfigurationProps",
    "CfnPackagingGroup",
    "CfnPackagingGroupProps",
]

publication.publish()
