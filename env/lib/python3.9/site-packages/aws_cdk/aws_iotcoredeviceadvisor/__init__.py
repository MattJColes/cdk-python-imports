'''
# AWS::IoTCoreDeviceAdvisor Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iotcoredeviceadvisor as iotcoredeviceadvisor
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
class CfnSuiteDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotcoredeviceadvisor.CfnSuiteDefinition",
):
    '''A CloudFormation ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition``.

    :cloudformationResource: AWS::IoTCoreDeviceAdvisor::SuiteDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        suite_definition_configuration: typing.Any,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param suite_definition_configuration: ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.SuiteDefinitionConfiguration``.
        :param tags: ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.Tags``.
        '''
        props = CfnSuiteDefinitionProps(
            suite_definition_configuration=suite_definition_configuration, tags=tags
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
    @jsii.member(jsii_name="attrSuiteDefinitionArn")
    def attr_suite_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SuiteDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSuiteDefinitionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSuiteDefinitionId")
    def attr_suite_definition_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SuiteDefinitionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSuiteDefinitionId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSuiteDefinitionVersion")
    def attr_suite_definition_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: SuiteDefinitionVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSuiteDefinitionVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="suiteDefinitionConfiguration")
    def suite_definition_configuration(self) -> typing.Any:
        '''``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.SuiteDefinitionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
        '''
        return typing.cast(typing.Any, jsii.get(self, "suiteDefinitionConfiguration"))

    @suite_definition_configuration.setter
    def suite_definition_configuration(self, value: typing.Any) -> None:
        jsii.set(self, "suiteDefinitionConfiguration", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotcoredeviceadvisor.CfnSuiteDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "suite_definition_configuration": "suiteDefinitionConfiguration",
        "tags": "tags",
    },
)
class CfnSuiteDefinitionProps:
    def __init__(
        self,
        *,
        suite_definition_configuration: typing.Any,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition``.

        :param suite_definition_configuration: ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.SuiteDefinitionConfiguration``.
        :param tags: ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "suite_definition_configuration": suite_definition_configuration,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def suite_definition_configuration(self) -> typing.Any:
        '''``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.SuiteDefinitionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
        '''
        result = self._values.get("suite_definition_configuration")
        assert result is not None, "Required property 'suite_definition_configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSuiteDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSuiteDefinition",
    "CfnSuiteDefinitionProps",
]

publication.publish()
