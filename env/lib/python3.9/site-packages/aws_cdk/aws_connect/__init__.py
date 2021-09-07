'''
# AWS::Connect Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_connect as connect
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
class CfnQuickConnect(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-connect.CfnQuickConnect",
):
    '''A CloudFormation ``AWS::Connect::QuickConnect``.

    :cloudformationResource: AWS::Connect::QuickConnect
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        quick_connect_config: typing.Union["CfnQuickConnect.QuickConnectConfigProperty", aws_cdk.core.IResolvable],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::QuickConnect``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: ``AWS::Connect::QuickConnect.InstanceArn``.
        :param name: ``AWS::Connect::QuickConnect.Name``.
        :param quick_connect_config: ``AWS::Connect::QuickConnect.QuickConnectConfig``.
        :param description: ``AWS::Connect::QuickConnect.Description``.
        :param tags: ``AWS::Connect::QuickConnect.Tags``.
        '''
        props = CfnQuickConnectProps(
            instance_arn=instance_arn,
            name=name,
            quick_connect_config=quick_connect_config,
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
    @jsii.member(jsii_name="attrQuickConnectArn")
    def attr_quick_connect_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: QuickConnectArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQuickConnectArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Connect::QuickConnect.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::QuickConnect.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Connect::QuickConnect.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectConfig")
    def quick_connect_config(
        self,
    ) -> typing.Union["CfnQuickConnect.QuickConnectConfigProperty", aws_cdk.core.IResolvable]:
        '''``AWS::Connect::QuickConnect.QuickConnectConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-quickconnectconfig
        '''
        return typing.cast(typing.Union["CfnQuickConnect.QuickConnectConfigProperty", aws_cdk.core.IResolvable], jsii.get(self, "quickConnectConfig"))

    @quick_connect_config.setter
    def quick_connect_config(
        self,
        value: typing.Union["CfnQuickConnect.QuickConnectConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "quickConnectConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::QuickConnect.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"phone_number": "phoneNumber"},
    )
    class PhoneNumberQuickConnectConfigProperty:
        def __init__(self, *, phone_number: builtins.str) -> None:
            '''
            :param phone_number: ``CfnQuickConnect.PhoneNumberQuickConnectConfigProperty.PhoneNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "phone_number": phone_number,
            }

        @builtins.property
        def phone_number(self) -> builtins.str:
            '''``CfnQuickConnect.PhoneNumberQuickConnectConfigProperty.PhoneNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html#cfn-connect-quickconnect-phonenumberquickconnectconfig-phonenumber
            '''
            result = self._values.get("phone_number")
            assert result is not None, "Required property 'phone_number' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhoneNumberQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-connect.CfnQuickConnect.QueueQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_flow_arn": "contactFlowArn", "queue_arn": "queueArn"},
    )
    class QueueQuickConnectConfigProperty:
        def __init__(
            self,
            *,
            contact_flow_arn: builtins.str,
            queue_arn: builtins.str,
        ) -> None:
            '''
            :param contact_flow_arn: ``CfnQuickConnect.QueueQuickConnectConfigProperty.ContactFlowArn``.
            :param queue_arn: ``CfnQuickConnect.QueueQuickConnectConfigProperty.QueueArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "contact_flow_arn": contact_flow_arn,
                "queue_arn": queue_arn,
            }

        @builtins.property
        def contact_flow_arn(self) -> builtins.str:
            '''``CfnQuickConnect.QueueQuickConnectConfigProperty.ContactFlowArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-contactflowarn
            '''
            result = self._values.get("contact_flow_arn")
            assert result is not None, "Required property 'contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def queue_arn(self) -> builtins.str:
            '''``CfnQuickConnect.QueueQuickConnectConfigProperty.QueueArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-queuearn
            '''
            result = self._values.get("queue_arn")
            assert result is not None, "Required property 'queue_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueueQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-connect.CfnQuickConnect.QuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "quick_connect_type": "quickConnectType",
            "phone_config": "phoneConfig",
            "queue_config": "queueConfig",
            "user_config": "userConfig",
        },
    )
    class QuickConnectConfigProperty:
        def __init__(
            self,
            *,
            quick_connect_type: builtins.str,
            phone_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnQuickConnect.PhoneNumberQuickConnectConfigProperty"]] = None,
            queue_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnQuickConnect.QueueQuickConnectConfigProperty"]] = None,
            user_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnQuickConnect.UserQuickConnectConfigProperty"]] = None,
        ) -> None:
            '''
            :param quick_connect_type: ``CfnQuickConnect.QuickConnectConfigProperty.QuickConnectType``.
            :param phone_config: ``CfnQuickConnect.QuickConnectConfigProperty.PhoneConfig``.
            :param queue_config: ``CfnQuickConnect.QuickConnectConfigProperty.QueueConfig``.
            :param user_config: ``CfnQuickConnect.QuickConnectConfigProperty.UserConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "quick_connect_type": quick_connect_type,
            }
            if phone_config is not None:
                self._values["phone_config"] = phone_config
            if queue_config is not None:
                self._values["queue_config"] = queue_config
            if user_config is not None:
                self._values["user_config"] = user_config

        @builtins.property
        def quick_connect_type(self) -> builtins.str:
            '''``CfnQuickConnect.QuickConnectConfigProperty.QuickConnectType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-quickconnecttype
            '''
            result = self._values.get("quick_connect_type")
            assert result is not None, "Required property 'quick_connect_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def phone_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnQuickConnect.PhoneNumberQuickConnectConfigProperty"]]:
            '''``CfnQuickConnect.QuickConnectConfigProperty.PhoneConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-phoneconfig
            '''
            result = self._values.get("phone_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnQuickConnect.PhoneNumberQuickConnectConfigProperty"]], result)

        @builtins.property
        def queue_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnQuickConnect.QueueQuickConnectConfigProperty"]]:
            '''``CfnQuickConnect.QuickConnectConfigProperty.QueueConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-queueconfig
            '''
            result = self._values.get("queue_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnQuickConnect.QueueQuickConnectConfigProperty"]], result)

        @builtins.property
        def user_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnQuickConnect.UserQuickConnectConfigProperty"]]:
            '''``CfnQuickConnect.QuickConnectConfigProperty.UserConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-userconfig
            '''
            result = self._values.get("user_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnQuickConnect.UserQuickConnectConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-connect.CfnQuickConnect.UserQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_flow_arn": "contactFlowArn", "user_arn": "userArn"},
    )
    class UserQuickConnectConfigProperty:
        def __init__(
            self,
            *,
            contact_flow_arn: builtins.str,
            user_arn: builtins.str,
        ) -> None:
            '''
            :param contact_flow_arn: ``CfnQuickConnect.UserQuickConnectConfigProperty.ContactFlowArn``.
            :param user_arn: ``CfnQuickConnect.UserQuickConnectConfigProperty.UserArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "contact_flow_arn": contact_flow_arn,
                "user_arn": user_arn,
            }

        @builtins.property
        def contact_flow_arn(self) -> builtins.str:
            '''``CfnQuickConnect.UserQuickConnectConfigProperty.ContactFlowArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-contactflowarn
            '''
            result = self._values.get("contact_flow_arn")
            assert result is not None, "Required property 'contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_arn(self) -> builtins.str:
            '''``CfnQuickConnect.UserQuickConnectConfigProperty.UserArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-userarn
            '''
            result = self._values.get("user_arn")
            assert result is not None, "Required property 'user_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-connect.CfnQuickConnectProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "quick_connect_config": "quickConnectConfig",
        "description": "description",
        "tags": "tags",
    },
)
class CfnQuickConnectProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        quick_connect_config: typing.Union[CfnQuickConnect.QuickConnectConfigProperty, aws_cdk.core.IResolvable],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Connect::QuickConnect``.

        :param instance_arn: ``AWS::Connect::QuickConnect.InstanceArn``.
        :param name: ``AWS::Connect::QuickConnect.Name``.
        :param quick_connect_config: ``AWS::Connect::QuickConnect.QuickConnectConfig``.
        :param description: ``AWS::Connect::QuickConnect.Description``.
        :param tags: ``AWS::Connect::QuickConnect.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
            "quick_connect_config": quick_connect_config,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::QuickConnect.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Connect::QuickConnect.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def quick_connect_config(
        self,
    ) -> typing.Union[CfnQuickConnect.QuickConnectConfigProperty, aws_cdk.core.IResolvable]:
        '''``AWS::Connect::QuickConnect.QuickConnectConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-quickconnectconfig
        '''
        result = self._values.get("quick_connect_config")
        assert result is not None, "Required property 'quick_connect_config' is missing"
        return typing.cast(typing.Union[CfnQuickConnect.QuickConnectConfigProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::QuickConnect.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Connect::QuickConnect.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickConnectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnQuickConnect",
    "CfnQuickConnectProps",
]

publication.publish()
