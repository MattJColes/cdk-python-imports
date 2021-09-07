'''
# AWS::DevOpsGuru Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_devopsguru as devopsguru
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
class CfnNotificationChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-devopsguru.CfnNotificationChannel",
):
    '''A CloudFormation ``AWS::DevOpsGuru::NotificationChannel``.

    :cloudformationResource: AWS::DevOpsGuru::NotificationChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        config: typing.Union["CfnNotificationChannel.NotificationChannelConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        '''Create a new ``AWS::DevOpsGuru::NotificationChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param config: ``AWS::DevOpsGuru::NotificationChannel.Config``.
        '''
        props = CfnNotificationChannelProps(config=config)

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
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> typing.Union["CfnNotificationChannel.NotificationChannelConfigProperty", aws_cdk.core.IResolvable]:
        '''``AWS::DevOpsGuru::NotificationChannel.Config``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html#cfn-devopsguru-notificationchannel-config
        '''
        return typing.cast(typing.Union["CfnNotificationChannel.NotificationChannelConfigProperty", aws_cdk.core.IResolvable], jsii.get(self, "config"))

    @config.setter
    def config(
        self,
        value: typing.Union["CfnNotificationChannel.NotificationChannelConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "config", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-devopsguru.CfnNotificationChannel.NotificationChannelConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"sns": "sns"},
    )
    class NotificationChannelConfigProperty:
        def __init__(
            self,
            *,
            sns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNotificationChannel.SnsChannelConfigProperty"]] = None,
        ) -> None:
            '''
            :param sns: ``CfnNotificationChannel.NotificationChannelConfigProperty.Sns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if sns is not None:
                self._values["sns"] = sns

        @builtins.property
        def sns(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNotificationChannel.SnsChannelConfigProperty"]]:
            '''``CfnNotificationChannel.NotificationChannelConfigProperty.Sns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html#cfn-devopsguru-notificationchannel-notificationchannelconfig-sns
            '''
            result = self._values.get("sns")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNotificationChannel.SnsChannelConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationChannelConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-devopsguru.CfnNotificationChannel.SnsChannelConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class SnsChannelConfigProperty:
        def __init__(self, *, topic_arn: typing.Optional[builtins.str] = None) -> None:
            '''
            :param topic_arn: ``CfnNotificationChannel.SnsChannelConfigProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnNotificationChannel.SnsChannelConfigProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html#cfn-devopsguru-notificationchannel-snschannelconfig-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsChannelConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-devopsguru.CfnNotificationChannelProps",
    jsii_struct_bases=[],
    name_mapping={"config": "config"},
)
class CfnNotificationChannelProps:
    def __init__(
        self,
        *,
        config: typing.Union[CfnNotificationChannel.NotificationChannelConfigProperty, aws_cdk.core.IResolvable],
    ) -> None:
        '''Properties for defining a ``AWS::DevOpsGuru::NotificationChannel``.

        :param config: ``AWS::DevOpsGuru::NotificationChannel.Config``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "config": config,
        }

    @builtins.property
    def config(
        self,
    ) -> typing.Union[CfnNotificationChannel.NotificationChannelConfigProperty, aws_cdk.core.IResolvable]:
        '''``AWS::DevOpsGuru::NotificationChannel.Config``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html#cfn-devopsguru-notificationchannel-config
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast(typing.Union[CfnNotificationChannel.NotificationChannelConfigProperty, aws_cdk.core.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotificationChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResourceCollection(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-devopsguru.CfnResourceCollection",
):
    '''A CloudFormation ``AWS::DevOpsGuru::ResourceCollection``.

    :cloudformationResource: AWS::DevOpsGuru::ResourceCollection
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resource_collection_filter: typing.Union[aws_cdk.core.IResolvable, "CfnResourceCollection.ResourceCollectionFilterProperty"],
    ) -> None:
        '''Create a new ``AWS::DevOpsGuru::ResourceCollection``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_collection_filter: ``AWS::DevOpsGuru::ResourceCollection.ResourceCollectionFilter``.
        '''
        props = CfnResourceCollectionProps(
            resource_collection_filter=resource_collection_filter
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
    @jsii.member(jsii_name="attrResourceCollectionType")
    def attr_resource_collection_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceCollectionType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceCollectionType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceCollectionFilter")
    def resource_collection_filter(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnResourceCollection.ResourceCollectionFilterProperty"]:
        '''``AWS::DevOpsGuru::ResourceCollection.ResourceCollectionFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnResourceCollection.ResourceCollectionFilterProperty"], jsii.get(self, "resourceCollectionFilter"))

    @resource_collection_filter.setter
    def resource_collection_filter(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnResourceCollection.ResourceCollectionFilterProperty"],
    ) -> None:
        jsii.set(self, "resourceCollectionFilter", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-devopsguru.CfnResourceCollection.CloudFormationCollectionFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"stack_names": "stackNames"},
    )
    class CloudFormationCollectionFilterProperty:
        def __init__(
            self,
            *,
            stack_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param stack_names: ``CfnResourceCollection.CloudFormationCollectionFilterProperty.StackNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if stack_names is not None:
                self._values["stack_names"] = stack_names

        @builtins.property
        def stack_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnResourceCollection.CloudFormationCollectionFilterProperty.StackNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html#cfn-devopsguru-resourcecollection-cloudformationcollectionfilter-stacknames
            '''
            result = self._values.get("stack_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudFormationCollectionFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-devopsguru.CfnResourceCollection.ResourceCollectionFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_formation": "cloudFormation"},
    )
    class ResourceCollectionFilterProperty:
        def __init__(
            self,
            *,
            cloud_formation: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceCollection.CloudFormationCollectionFilterProperty"]] = None,
        ) -> None:
            '''
            :param cloud_formation: ``CfnResourceCollection.ResourceCollectionFilterProperty.CloudFormation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_formation is not None:
                self._values["cloud_formation"] = cloud_formation

        @builtins.property
        def cloud_formation(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceCollection.CloudFormationCollectionFilterProperty"]]:
            '''``CfnResourceCollection.ResourceCollectionFilterProperty.CloudFormation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter-cloudformation
            '''
            result = self._values.get("cloud_formation")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceCollection.CloudFormationCollectionFilterProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceCollectionFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-devopsguru.CfnResourceCollectionProps",
    jsii_struct_bases=[],
    name_mapping={"resource_collection_filter": "resourceCollectionFilter"},
)
class CfnResourceCollectionProps:
    def __init__(
        self,
        *,
        resource_collection_filter: typing.Union[aws_cdk.core.IResolvable, CfnResourceCollection.ResourceCollectionFilterProperty],
    ) -> None:
        '''Properties for defining a ``AWS::DevOpsGuru::ResourceCollection``.

        :param resource_collection_filter: ``AWS::DevOpsGuru::ResourceCollection.ResourceCollectionFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_collection_filter": resource_collection_filter,
        }

    @builtins.property
    def resource_collection_filter(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnResourceCollection.ResourceCollectionFilterProperty]:
        '''``AWS::DevOpsGuru::ResourceCollection.ResourceCollectionFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter
        '''
        result = self._values.get("resource_collection_filter")
        assert result is not None, "Required property 'resource_collection_filter' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnResourceCollection.ResourceCollectionFilterProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceCollectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNotificationChannel",
    "CfnNotificationChannelProps",
    "CfnResourceCollection",
    "CfnResourceCollectionProps",
]

publication.publish()
