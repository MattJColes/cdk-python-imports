'''
# AWS IoT GreengrassV2 Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_greengrassv2 as greengrass
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
class CfnComponentVersion(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion",
):
    '''A CloudFormation ``AWS::GreengrassV2::ComponentVersion``.

    :cloudformationResource: AWS::GreengrassV2::ComponentVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        inline_recipe: typing.Optional[builtins.str] = None,
        lambda_function: typing.Optional[typing.Union["CfnComponentVersion.LambdaFunctionRecipeSourceProperty", aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::GreengrassV2::ComponentVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param inline_recipe: ``AWS::GreengrassV2::ComponentVersion.InlineRecipe``.
        :param lambda_function: ``AWS::GreengrassV2::ComponentVersion.LambdaFunction``.
        :param tags: ``AWS::GreengrassV2::ComponentVersion.Tags``.
        '''
        props = CfnComponentVersionProps(
            inline_recipe=inline_recipe, lambda_function=lambda_function, tags=tags
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
    @jsii.member(jsii_name="attrComponentName")
    def attr_component_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ComponentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComponentName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrComponentVersion")
    def attr_component_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: ComponentVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComponentVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::GreengrassV2::ComponentVersion.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inlineRecipe")
    def inline_recipe(self) -> typing.Optional[builtins.str]:
        '''``AWS::GreengrassV2::ComponentVersion.InlineRecipe``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-inlinerecipe
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inlineRecipe"))

    @inline_recipe.setter
    def inline_recipe(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "inlineRecipe", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lambdaFunction")
    def lambda_function(
        self,
    ) -> typing.Optional[typing.Union["CfnComponentVersion.LambdaFunctionRecipeSourceProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::GreengrassV2::ComponentVersion.LambdaFunction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-lambdafunction
        '''
        return typing.cast(typing.Optional[typing.Union["CfnComponentVersion.LambdaFunctionRecipeSourceProperty", aws_cdk.core.IResolvable]], jsii.get(self, "lambdaFunction"))

    @lambda_function.setter
    def lambda_function(
        self,
        value: typing.Optional[typing.Union["CfnComponentVersion.LambdaFunctionRecipeSourceProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "lambdaFunction", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion.ComponentDependencyRequirementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dependency_type": "dependencyType",
            "version_requirement": "versionRequirement",
        },
    )
    class ComponentDependencyRequirementProperty:
        def __init__(
            self,
            *,
            dependency_type: typing.Optional[builtins.str] = None,
            version_requirement: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param dependency_type: ``CfnComponentVersion.ComponentDependencyRequirementProperty.DependencyType``.
            :param version_requirement: ``CfnComponentVersion.ComponentDependencyRequirementProperty.VersionRequirement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dependency_type is not None:
                self._values["dependency_type"] = dependency_type
            if version_requirement is not None:
                self._values["version_requirement"] = version_requirement

        @builtins.property
        def dependency_type(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.ComponentDependencyRequirementProperty.DependencyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html#cfn-greengrassv2-componentversion-componentdependencyrequirement-dependencytype
            '''
            result = self._values.get("dependency_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version_requirement(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.ComponentDependencyRequirementProperty.VersionRequirement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html#cfn-greengrassv2-componentversion-componentdependencyrequirement-versionrequirement
            '''
            result = self._values.get("version_requirement")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentDependencyRequirementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion.ComponentPlatformProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "name": "name"},
    )
    class ComponentPlatformProperty:
        def __init__(
            self,
            *,
            attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attributes: ``CfnComponentVersion.ComponentPlatformProperty.Attributes``.
            :param name: ``CfnComponentVersion.ComponentPlatformProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnComponentVersion.ComponentPlatformProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html#cfn-greengrassv2-componentversion-componentplatform-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.ComponentPlatformProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html#cfn-greengrassv2-componentversion-componentplatform-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentPlatformProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion.LambdaContainerParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "devices": "devices",
            "memory_size_in_kb": "memorySizeInKb",
            "mount_ro_sysfs": "mountRoSysfs",
            "volumes": "volumes",
        },
    )
    class LambdaContainerParamsProperty:
        def __init__(
            self,
            *,
            devices: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaDeviceMountProperty"]]]] = None,
            memory_size_in_kb: typing.Optional[jsii.Number] = None,
            mount_ro_sysfs: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            volumes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaVolumeMountProperty"]]]] = None,
        ) -> None:
            '''
            :param devices: ``CfnComponentVersion.LambdaContainerParamsProperty.Devices``.
            :param memory_size_in_kb: ``CfnComponentVersion.LambdaContainerParamsProperty.MemorySizeInKB``.
            :param mount_ro_sysfs: ``CfnComponentVersion.LambdaContainerParamsProperty.MountROSysfs``.
            :param volumes: ``CfnComponentVersion.LambdaContainerParamsProperty.Volumes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if devices is not None:
                self._values["devices"] = devices
            if memory_size_in_kb is not None:
                self._values["memory_size_in_kb"] = memory_size_in_kb
            if mount_ro_sysfs is not None:
                self._values["mount_ro_sysfs"] = mount_ro_sysfs
            if volumes is not None:
                self._values["volumes"] = volumes

        @builtins.property
        def devices(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaDeviceMountProperty"]]]]:
            '''``CfnComponentVersion.LambdaContainerParamsProperty.Devices``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-devices
            '''
            result = self._values.get("devices")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaDeviceMountProperty"]]]], result)

        @builtins.property
        def memory_size_in_kb(self) -> typing.Optional[jsii.Number]:
            '''``CfnComponentVersion.LambdaContainerParamsProperty.MemorySizeInKB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-memorysizeinkb
            '''
            result = self._values.get("memory_size_in_kb")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mount_ro_sysfs(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnComponentVersion.LambdaContainerParamsProperty.MountROSysfs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-mountrosysfs
            '''
            result = self._values.get("mount_ro_sysfs")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def volumes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaVolumeMountProperty"]]]]:
            '''``CfnComponentVersion.LambdaContainerParamsProperty.Volumes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-volumes
            '''
            result = self._values.get("volumes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaVolumeMountProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaContainerParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion.LambdaDeviceMountProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_group_owner": "addGroupOwner",
            "path": "path",
            "permission": "permission",
        },
    )
    class LambdaDeviceMountProperty:
        def __init__(
            self,
            *,
            add_group_owner: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            path: typing.Optional[builtins.str] = None,
            permission: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param add_group_owner: ``CfnComponentVersion.LambdaDeviceMountProperty.AddGroupOwner``.
            :param path: ``CfnComponentVersion.LambdaDeviceMountProperty.Path``.
            :param permission: ``CfnComponentVersion.LambdaDeviceMountProperty.Permission``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if add_group_owner is not None:
                self._values["add_group_owner"] = add_group_owner
            if path is not None:
                self._values["path"] = path
            if permission is not None:
                self._values["permission"] = permission

        @builtins.property
        def add_group_owner(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnComponentVersion.LambdaDeviceMountProperty.AddGroupOwner``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html#cfn-greengrassv2-componentversion-lambdadevicemount-addgroupowner
            '''
            result = self._values.get("add_group_owner")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaDeviceMountProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html#cfn-greengrassv2-componentversion-lambdadevicemount-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def permission(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaDeviceMountProperty.Permission``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html#cfn-greengrassv2-componentversion-lambdadevicemount-permission
            '''
            result = self._values.get("permission")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaDeviceMountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion.LambdaEventSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"topic": "topic", "type": "type"},
    )
    class LambdaEventSourceProperty:
        def __init__(
            self,
            *,
            topic: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param topic: ``CfnComponentVersion.LambdaEventSourceProperty.Topic``.
            :param type: ``CfnComponentVersion.LambdaEventSourceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if topic is not None:
                self._values["topic"] = topic
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def topic(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaEventSourceProperty.Topic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html#cfn-greengrassv2-componentversion-lambdaeventsource-topic
            '''
            result = self._values.get("topic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaEventSourceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html#cfn-greengrassv2-componentversion-lambdaeventsource-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaEventSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion.LambdaExecutionParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "environment_variables": "environmentVariables",
            "event_sources": "eventSources",
            "exec_args": "execArgs",
            "input_payload_encoding_type": "inputPayloadEncodingType",
            "linux_process_params": "linuxProcessParams",
            "max_idle_time_in_seconds": "maxIdleTimeInSeconds",
            "max_instances_count": "maxInstancesCount",
            "max_queue_size": "maxQueueSize",
            "pinned": "pinned",
            "status_timeout_in_seconds": "statusTimeoutInSeconds",
            "timeout_in_seconds": "timeoutInSeconds",
        },
    )
    class LambdaExecutionParametersProperty:
        def __init__(
            self,
            *,
            environment_variables: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            event_sources: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaEventSourceProperty"]]]] = None,
            exec_args: typing.Optional[typing.Sequence[builtins.str]] = None,
            input_payload_encoding_type: typing.Optional[builtins.str] = None,
            linux_process_params: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaLinuxProcessParamsProperty"]] = None,
            max_idle_time_in_seconds: typing.Optional[jsii.Number] = None,
            max_instances_count: typing.Optional[jsii.Number] = None,
            max_queue_size: typing.Optional[jsii.Number] = None,
            pinned: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            status_timeout_in_seconds: typing.Optional[jsii.Number] = None,
            timeout_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param environment_variables: ``CfnComponentVersion.LambdaExecutionParametersProperty.EnvironmentVariables``.
            :param event_sources: ``CfnComponentVersion.LambdaExecutionParametersProperty.EventSources``.
            :param exec_args: ``CfnComponentVersion.LambdaExecutionParametersProperty.ExecArgs``.
            :param input_payload_encoding_type: ``CfnComponentVersion.LambdaExecutionParametersProperty.InputPayloadEncodingType``.
            :param linux_process_params: ``CfnComponentVersion.LambdaExecutionParametersProperty.LinuxProcessParams``.
            :param max_idle_time_in_seconds: ``CfnComponentVersion.LambdaExecutionParametersProperty.MaxIdleTimeInSeconds``.
            :param max_instances_count: ``CfnComponentVersion.LambdaExecutionParametersProperty.MaxInstancesCount``.
            :param max_queue_size: ``CfnComponentVersion.LambdaExecutionParametersProperty.MaxQueueSize``.
            :param pinned: ``CfnComponentVersion.LambdaExecutionParametersProperty.Pinned``.
            :param status_timeout_in_seconds: ``CfnComponentVersion.LambdaExecutionParametersProperty.StatusTimeoutInSeconds``.
            :param timeout_in_seconds: ``CfnComponentVersion.LambdaExecutionParametersProperty.TimeoutInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if environment_variables is not None:
                self._values["environment_variables"] = environment_variables
            if event_sources is not None:
                self._values["event_sources"] = event_sources
            if exec_args is not None:
                self._values["exec_args"] = exec_args
            if input_payload_encoding_type is not None:
                self._values["input_payload_encoding_type"] = input_payload_encoding_type
            if linux_process_params is not None:
                self._values["linux_process_params"] = linux_process_params
            if max_idle_time_in_seconds is not None:
                self._values["max_idle_time_in_seconds"] = max_idle_time_in_seconds
            if max_instances_count is not None:
                self._values["max_instances_count"] = max_instances_count
            if max_queue_size is not None:
                self._values["max_queue_size"] = max_queue_size
            if pinned is not None:
                self._values["pinned"] = pinned
            if status_timeout_in_seconds is not None:
                self._values["status_timeout_in_seconds"] = status_timeout_in_seconds
            if timeout_in_seconds is not None:
                self._values["timeout_in_seconds"] = timeout_in_seconds

        @builtins.property
        def environment_variables(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.EnvironmentVariables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-environmentvariables
            '''
            result = self._values.get("environment_variables")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def event_sources(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaEventSourceProperty"]]]]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.EventSources``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-eventsources
            '''
            result = self._values.get("event_sources")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaEventSourceProperty"]]]], result)

        @builtins.property
        def exec_args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.ExecArgs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-execargs
            '''
            result = self._values.get("exec_args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def input_payload_encoding_type(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.InputPayloadEncodingType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-inputpayloadencodingtype
            '''
            result = self._values.get("input_payload_encoding_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def linux_process_params(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaLinuxProcessParamsProperty"]]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.LinuxProcessParams``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-linuxprocessparams
            '''
            result = self._values.get("linux_process_params")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaLinuxProcessParamsProperty"]], result)

        @builtins.property
        def max_idle_time_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.MaxIdleTimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-maxidletimeinseconds
            '''
            result = self._values.get("max_idle_time_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_instances_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.MaxInstancesCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-maxinstancescount
            '''
            result = self._values.get("max_instances_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_queue_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.MaxQueueSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-maxqueuesize
            '''
            result = self._values.get("max_queue_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def pinned(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.Pinned``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-pinned
            '''
            result = self._values.get("pinned")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def status_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.StatusTimeoutInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-statustimeoutinseconds
            '''
            result = self._values.get("status_timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnComponentVersion.LambdaExecutionParametersProperty.TimeoutInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-timeoutinseconds
            '''
            result = self._values.get("timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaExecutionParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion.LambdaFunctionRecipeSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_dependencies": "componentDependencies",
            "component_lambda_parameters": "componentLambdaParameters",
            "component_name": "componentName",
            "component_platforms": "componentPlatforms",
            "component_version": "componentVersion",
            "lambda_arn": "lambdaArn",
        },
    )
    class LambdaFunctionRecipeSourceProperty:
        def __init__(
            self,
            *,
            component_dependencies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.ComponentDependencyRequirementProperty"]]]] = None,
            component_lambda_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaExecutionParametersProperty"]] = None,
            component_name: typing.Optional[builtins.str] = None,
            component_platforms: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.ComponentPlatformProperty"]]]] = None,
            component_version: typing.Optional[builtins.str] = None,
            lambda_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param component_dependencies: ``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentDependencies``.
            :param component_lambda_parameters: ``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentLambdaParameters``.
            :param component_name: ``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentName``.
            :param component_platforms: ``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentPlatforms``.
            :param component_version: ``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentVersion``.
            :param lambda_arn: ``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.LambdaArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if component_dependencies is not None:
                self._values["component_dependencies"] = component_dependencies
            if component_lambda_parameters is not None:
                self._values["component_lambda_parameters"] = component_lambda_parameters
            if component_name is not None:
                self._values["component_name"] = component_name
            if component_platforms is not None:
                self._values["component_platforms"] = component_platforms
            if component_version is not None:
                self._values["component_version"] = component_version
            if lambda_arn is not None:
                self._values["lambda_arn"] = lambda_arn

        @builtins.property
        def component_dependencies(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.ComponentDependencyRequirementProperty"]]]]:
            '''``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentDependencies``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentdependencies
            '''
            result = self._values.get("component_dependencies")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.ComponentDependencyRequirementProperty"]]]], result)

        @builtins.property
        def component_lambda_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaExecutionParametersProperty"]]:
            '''``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentLambdaParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentlambdaparameters
            '''
            result = self._values.get("component_lambda_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaExecutionParametersProperty"]], result)

        @builtins.property
        def component_name(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentname
            '''
            result = self._values.get("component_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def component_platforms(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.ComponentPlatformProperty"]]]]:
            '''``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentPlatforms``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentplatforms
            '''
            result = self._values.get("component_platforms")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.ComponentPlatformProperty"]]]], result)

        @builtins.property
        def component_version(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.ComponentVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentversion
            '''
            result = self._values.get("component_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lambda_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaFunctionRecipeSourceProperty.LambdaArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaFunctionRecipeSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion.LambdaLinuxProcessParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_params": "containerParams",
            "isolation_mode": "isolationMode",
        },
    )
    class LambdaLinuxProcessParamsProperty:
        def __init__(
            self,
            *,
            container_params: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaContainerParamsProperty"]] = None,
            isolation_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param container_params: ``CfnComponentVersion.LambdaLinuxProcessParamsProperty.ContainerParams``.
            :param isolation_mode: ``CfnComponentVersion.LambdaLinuxProcessParamsProperty.IsolationMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if container_params is not None:
                self._values["container_params"] = container_params
            if isolation_mode is not None:
                self._values["isolation_mode"] = isolation_mode

        @builtins.property
        def container_params(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaContainerParamsProperty"]]:
            '''``CfnComponentVersion.LambdaLinuxProcessParamsProperty.ContainerParams``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html#cfn-greengrassv2-componentversion-lambdalinuxprocessparams-containerparams
            '''
            result = self._values.get("container_params")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnComponentVersion.LambdaContainerParamsProperty"]], result)

        @builtins.property
        def isolation_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaLinuxProcessParamsProperty.IsolationMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html#cfn-greengrassv2-componentversion-lambdalinuxprocessparams-isolationmode
            '''
            result = self._values.get("isolation_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaLinuxProcessParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersion.LambdaVolumeMountProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_group_owner": "addGroupOwner",
            "destination_path": "destinationPath",
            "permission": "permission",
            "source_path": "sourcePath",
        },
    )
    class LambdaVolumeMountProperty:
        def __init__(
            self,
            *,
            add_group_owner: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            destination_path: typing.Optional[builtins.str] = None,
            permission: typing.Optional[builtins.str] = None,
            source_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param add_group_owner: ``CfnComponentVersion.LambdaVolumeMountProperty.AddGroupOwner``.
            :param destination_path: ``CfnComponentVersion.LambdaVolumeMountProperty.DestinationPath``.
            :param permission: ``CfnComponentVersion.LambdaVolumeMountProperty.Permission``.
            :param source_path: ``CfnComponentVersion.LambdaVolumeMountProperty.SourcePath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if add_group_owner is not None:
                self._values["add_group_owner"] = add_group_owner
            if destination_path is not None:
                self._values["destination_path"] = destination_path
            if permission is not None:
                self._values["permission"] = permission
            if source_path is not None:
                self._values["source_path"] = source_path

        @builtins.property
        def add_group_owner(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnComponentVersion.LambdaVolumeMountProperty.AddGroupOwner``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-addgroupowner
            '''
            result = self._values.get("add_group_owner")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def destination_path(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaVolumeMountProperty.DestinationPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-destinationpath
            '''
            result = self._values.get("destination_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def permission(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaVolumeMountProperty.Permission``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-permission
            '''
            result = self._values.get("permission")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_path(self) -> typing.Optional[builtins.str]:
            '''``CfnComponentVersion.LambdaVolumeMountProperty.SourcePath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-sourcepath
            '''
            result = self._values.get("source_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaVolumeMountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-greengrassv2.CfnComponentVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "inline_recipe": "inlineRecipe",
        "lambda_function": "lambdaFunction",
        "tags": "tags",
    },
)
class CfnComponentVersionProps:
    def __init__(
        self,
        *,
        inline_recipe: typing.Optional[builtins.str] = None,
        lambda_function: typing.Optional[typing.Union[CfnComponentVersion.LambdaFunctionRecipeSourceProperty, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GreengrassV2::ComponentVersion``.

        :param inline_recipe: ``AWS::GreengrassV2::ComponentVersion.InlineRecipe``.
        :param lambda_function: ``AWS::GreengrassV2::ComponentVersion.LambdaFunction``.
        :param tags: ``AWS::GreengrassV2::ComponentVersion.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if inline_recipe is not None:
            self._values["inline_recipe"] = inline_recipe
        if lambda_function is not None:
            self._values["lambda_function"] = lambda_function
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def inline_recipe(self) -> typing.Optional[builtins.str]:
        '''``AWS::GreengrassV2::ComponentVersion.InlineRecipe``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-inlinerecipe
        '''
        result = self._values.get("inline_recipe")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_function(
        self,
    ) -> typing.Optional[typing.Union[CfnComponentVersion.LambdaFunctionRecipeSourceProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::GreengrassV2::ComponentVersion.LambdaFunction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-lambdafunction
        '''
        result = self._values.get("lambda_function")
        return typing.cast(typing.Optional[typing.Union[CfnComponentVersion.LambdaFunctionRecipeSourceProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::GreengrassV2::ComponentVersion.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComponentVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnComponentVersion",
    "CfnComponentVersionProps",
]

publication.publish()
