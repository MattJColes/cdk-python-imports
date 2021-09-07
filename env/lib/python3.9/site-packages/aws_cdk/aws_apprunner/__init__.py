'''
# AWS::AppRunner Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_apprunner as apprunner
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
class CfnService(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-apprunner.CfnService",
):
    '''A CloudFormation ``AWS::AppRunner::Service``.

    :cloudformationResource: AWS::AppRunner::Service
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        source_configuration: typing.Union["CfnService.SourceConfigurationProperty", aws_cdk.core.IResolvable],
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.EncryptionConfigurationProperty"]] = None,
        health_check_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigurationProperty"]] = None,
        instance_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.InstanceConfigurationProperty"]] = None,
        service_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::AppRunner::Service``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param source_configuration: ``AWS::AppRunner::Service.SourceConfiguration``.
        :param auto_scaling_configuration_arn: ``AWS::AppRunner::Service.AutoScalingConfigurationArn``.
        :param encryption_configuration: ``AWS::AppRunner::Service.EncryptionConfiguration``.
        :param health_check_configuration: ``AWS::AppRunner::Service.HealthCheckConfiguration``.
        :param instance_configuration: ``AWS::AppRunner::Service.InstanceConfiguration``.
        :param service_name: ``AWS::AppRunner::Service.ServiceName``.
        :param tags: ``AWS::AppRunner::Service.Tags``.
        '''
        props = CfnServiceProps(
            source_configuration=source_configuration,
            auto_scaling_configuration_arn=auto_scaling_configuration_arn,
            encryption_configuration=encryption_configuration,
            health_check_configuration=health_check_configuration,
            instance_configuration=instance_configuration,
            service_name=service_name,
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
    @jsii.member(jsii_name="attrServiceArn")
    def attr_service_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServiceId")
    def attr_service_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServiceUrl")
    def attr_service_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceUrl"))

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppRunner::Service.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> typing.Union["CfnService.SourceConfigurationProperty", aws_cdk.core.IResolvable]:
        '''``AWS::AppRunner::Service.SourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
        '''
        return typing.cast(typing.Union["CfnService.SourceConfigurationProperty", aws_cdk.core.IResolvable], jsii.get(self, "sourceConfiguration"))

    @source_configuration.setter
    def source_configuration(
        self,
        value: typing.Union["CfnService.SourceConfigurationProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "sourceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppRunner::Service.AutoScalingConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingConfigurationArn"))

    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "autoScalingConfigurationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.EncryptionConfigurationProperty"]]:
        '''``AWS::AppRunner::Service.EncryptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.EncryptionConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "encryptionConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckConfiguration")
    def health_check_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigurationProperty"]]:
        '''``AWS::AppRunner::Service.HealthCheckConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigurationProperty"]], jsii.get(self, "healthCheckConfiguration"))

    @health_check_configuration.setter
    def health_check_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "healthCheckConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.InstanceConfigurationProperty"]]:
        '''``AWS::AppRunner::Service.InstanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.InstanceConfigurationProperty"]], jsii.get(self, "instanceConfiguration"))

    @instance_configuration.setter
    def instance_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.InstanceConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "instanceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppRunner::Service.ServiceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serviceName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_role_arn": "accessRoleArn",
            "connection_arn": "connectionArn",
        },
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            access_role_arn: typing.Optional[builtins.str] = None,
            connection_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param access_role_arn: ``CfnService.AuthenticationConfigurationProperty.AccessRoleArn``.
            :param connection_arn: ``CfnService.AuthenticationConfigurationProperty.ConnectionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if access_role_arn is not None:
                self._values["access_role_arn"] = access_role_arn
            if connection_arn is not None:
                self._values["connection_arn"] = connection_arn

        @builtins.property
        def access_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnService.AuthenticationConfigurationProperty.AccessRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-accessrolearn
            '''
            result = self._values.get("access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connection_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnService.AuthenticationConfigurationProperty.ConnectionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-connectionarn
            '''
            result = self._values.get("connection_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.CodeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_source": "configurationSource",
            "code_configuration_values": "codeConfigurationValues",
        },
    )
    class CodeConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_source: builtins.str,
            code_configuration_values: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationValuesProperty"]] = None,
        ) -> None:
            '''
            :param configuration_source: ``CfnService.CodeConfigurationProperty.ConfigurationSource``.
            :param code_configuration_values: ``CfnService.CodeConfigurationProperty.CodeConfigurationValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "configuration_source": configuration_source,
            }
            if code_configuration_values is not None:
                self._values["code_configuration_values"] = code_configuration_values

        @builtins.property
        def configuration_source(self) -> builtins.str:
            '''``CfnService.CodeConfigurationProperty.ConfigurationSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-configurationsource
            '''
            result = self._values.get("configuration_source")
            assert result is not None, "Required property 'configuration_source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def code_configuration_values(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationValuesProperty"]]:
            '''``CfnService.CodeConfigurationProperty.CodeConfigurationValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-codeconfigurationvalues
            '''
            result = self._values.get("code_configuration_values")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationValuesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.CodeConfigurationValuesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "runtime": "runtime",
            "build_command": "buildCommand",
            "port": "port",
            "runtime_environment_variables": "runtimeEnvironmentVariables",
            "start_command": "startCommand",
        },
    )
    class CodeConfigurationValuesProperty:
        def __init__(
            self,
            *,
            runtime: builtins.str,
            build_command: typing.Optional[builtins.str] = None,
            port: typing.Optional[builtins.str] = None,
            runtime_environment_variables: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]] = None,
            start_command: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param runtime: ``CfnService.CodeConfigurationValuesProperty.Runtime``.
            :param build_command: ``CfnService.CodeConfigurationValuesProperty.BuildCommand``.
            :param port: ``CfnService.CodeConfigurationValuesProperty.Port``.
            :param runtime_environment_variables: ``CfnService.CodeConfigurationValuesProperty.RuntimeEnvironmentVariables``.
            :param start_command: ``CfnService.CodeConfigurationValuesProperty.StartCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "runtime": runtime,
            }
            if build_command is not None:
                self._values["build_command"] = build_command
            if port is not None:
                self._values["port"] = port
            if runtime_environment_variables is not None:
                self._values["runtime_environment_variables"] = runtime_environment_variables
            if start_command is not None:
                self._values["start_command"] = start_command

        @builtins.property
        def runtime(self) -> builtins.str:
            '''``CfnService.CodeConfigurationValuesProperty.Runtime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def build_command(self) -> typing.Optional[builtins.str]:
            '''``CfnService.CodeConfigurationValuesProperty.BuildCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-buildcommand
            '''
            result = self._values.get("build_command")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''``CfnService.CodeConfigurationValuesProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime_environment_variables(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]]:
            '''``CfnService.CodeConfigurationValuesProperty.RuntimeEnvironmentVariables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtimeenvironmentvariables
            '''
            result = self._values.get("runtime_environment_variables")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]], result)

        @builtins.property
        def start_command(self) -> typing.Optional[builtins.str]:
            '''``CfnService.CodeConfigurationValuesProperty.StartCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-startcommand
            '''
            result = self._values.get("start_command")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeConfigurationValuesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.CodeRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "repository_url": "repositoryUrl",
            "source_code_version": "sourceCodeVersion",
            "code_configuration": "codeConfiguration",
        },
    )
    class CodeRepositoryProperty:
        def __init__(
            self,
            *,
            repository_url: builtins.str,
            source_code_version: typing.Union[aws_cdk.core.IResolvable, "CfnService.SourceCodeVersionProperty"],
            code_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param repository_url: ``CfnService.CodeRepositoryProperty.RepositoryUrl``.
            :param source_code_version: ``CfnService.CodeRepositoryProperty.SourceCodeVersion``.
            :param code_configuration: ``CfnService.CodeRepositoryProperty.CodeConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "repository_url": repository_url,
                "source_code_version": source_code_version,
            }
            if code_configuration is not None:
                self._values["code_configuration"] = code_configuration

        @builtins.property
        def repository_url(self) -> builtins.str:
            '''``CfnService.CodeRepositoryProperty.RepositoryUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-repositoryurl
            '''
            result = self._values.get("repository_url")
            assert result is not None, "Required property 'repository_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_code_version(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnService.SourceCodeVersionProperty"]:
            '''``CfnService.CodeRepositoryProperty.SourceCodeVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-sourcecodeversion
            '''
            result = self._values.get("source_code_version")
            assert result is not None, "Required property 'source_code_version' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnService.SourceCodeVersionProperty"], result)

        @builtins.property
        def code_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationProperty"]]:
            '''``CfnService.CodeRepositoryProperty.CodeConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-codeconfiguration
            '''
            result = self._values.get("code_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key": "kmsKey"},
    )
    class EncryptionConfigurationProperty:
        def __init__(self, *, kms_key: builtins.str) -> None:
            '''
            :param kms_key: ``CfnService.EncryptionConfigurationProperty.KmsKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "kms_key": kms_key,
            }

        @builtins.property
        def kms_key(self) -> builtins.str:
            '''``CfnService.EncryptionConfigurationProperty.KmsKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html#cfn-apprunner-service-encryptionconfiguration-kmskey
            '''
            result = self._values.get("kms_key")
            assert result is not None, "Required property 'kms_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.HealthCheckConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "healthy_threshold": "healthyThreshold",
            "interval": "interval",
            "path": "path",
            "protocol": "protocol",
            "timeout": "timeout",
            "unhealthy_threshold": "unhealthyThreshold",
        },
    )
    class HealthCheckConfigurationProperty:
        def __init__(
            self,
            *,
            healthy_threshold: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            path: typing.Optional[builtins.str] = None,
            protocol: typing.Optional[builtins.str] = None,
            timeout: typing.Optional[jsii.Number] = None,
            unhealthy_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param healthy_threshold: ``CfnService.HealthCheckConfigurationProperty.HealthyThreshold``.
            :param interval: ``CfnService.HealthCheckConfigurationProperty.Interval``.
            :param path: ``CfnService.HealthCheckConfigurationProperty.Path``.
            :param protocol: ``CfnService.HealthCheckConfigurationProperty.Protocol``.
            :param timeout: ``CfnService.HealthCheckConfigurationProperty.Timeout``.
            :param unhealthy_threshold: ``CfnService.HealthCheckConfigurationProperty.UnhealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if healthy_threshold is not None:
                self._values["healthy_threshold"] = healthy_threshold
            if interval is not None:
                self._values["interval"] = interval
            if path is not None:
                self._values["path"] = path
            if protocol is not None:
                self._values["protocol"] = protocol
            if timeout is not None:
                self._values["timeout"] = timeout
            if unhealthy_threshold is not None:
                self._values["unhealthy_threshold"] = unhealthy_threshold

        @builtins.property
        def healthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckConfigurationProperty.HealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-healthythreshold
            '''
            result = self._values.get("healthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckConfigurationProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''``CfnService.HealthCheckConfigurationProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''``CfnService.HealthCheckConfigurationProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckConfigurationProperty.Timeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckConfigurationProperty.UnhealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-unhealthythreshold
            '''
            result = self._values.get("unhealthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.ImageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "port": "port",
            "runtime_environment_variables": "runtimeEnvironmentVariables",
            "start_command": "startCommand",
        },
    )
    class ImageConfigurationProperty:
        def __init__(
            self,
            *,
            port: typing.Optional[builtins.str] = None,
            runtime_environment_variables: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]] = None,
            start_command: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param port: ``CfnService.ImageConfigurationProperty.Port``.
            :param runtime_environment_variables: ``CfnService.ImageConfigurationProperty.RuntimeEnvironmentVariables``.
            :param start_command: ``CfnService.ImageConfigurationProperty.StartCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if port is not None:
                self._values["port"] = port
            if runtime_environment_variables is not None:
                self._values["runtime_environment_variables"] = runtime_environment_variables
            if start_command is not None:
                self._values["start_command"] = start_command

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''``CfnService.ImageConfigurationProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime_environment_variables(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]]:
            '''``CfnService.ImageConfigurationProperty.RuntimeEnvironmentVariables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables
            '''
            result = self._values.get("runtime_environment_variables")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]], result)

        @builtins.property
        def start_command(self) -> typing.Optional[builtins.str]:
            '''``CfnService.ImageConfigurationProperty.StartCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-startcommand
            '''
            result = self._values.get("start_command")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.ImageRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_identifier": "imageIdentifier",
            "image_repository_type": "imageRepositoryType",
            "image_configuration": "imageConfiguration",
        },
    )
    class ImageRepositoryProperty:
        def __init__(
            self,
            *,
            image_identifier: builtins.str,
            image_repository_type: builtins.str,
            image_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param image_identifier: ``CfnService.ImageRepositoryProperty.ImageIdentifier``.
            :param image_repository_type: ``CfnService.ImageRepositoryProperty.ImageRepositoryType``.
            :param image_configuration: ``CfnService.ImageRepositoryProperty.ImageConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "image_identifier": image_identifier,
                "image_repository_type": image_repository_type,
            }
            if image_configuration is not None:
                self._values["image_configuration"] = image_configuration

        @builtins.property
        def image_identifier(self) -> builtins.str:
            '''``CfnService.ImageRepositoryProperty.ImageIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageidentifier
            '''
            result = self._values.get("image_identifier")
            assert result is not None, "Required property 'image_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_repository_type(self) -> builtins.str:
            '''``CfnService.ImageRepositoryProperty.ImageRepositoryType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imagerepositorytype
            '''
            result = self._values.get("image_repository_type")
            assert result is not None, "Required property 'image_repository_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageConfigurationProperty"]]:
            '''``CfnService.ImageRepositoryProperty.ImageConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageconfiguration
            '''
            result = self._values.get("image_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.InstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu": "cpu",
            "instance_role_arn": "instanceRoleArn",
            "memory": "memory",
        },
    )
    class InstanceConfigurationProperty:
        def __init__(
            self,
            *,
            cpu: typing.Optional[builtins.str] = None,
            instance_role_arn: typing.Optional[builtins.str] = None,
            memory: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param cpu: ``CfnService.InstanceConfigurationProperty.Cpu``.
            :param instance_role_arn: ``CfnService.InstanceConfigurationProperty.InstanceRoleArn``.
            :param memory: ``CfnService.InstanceConfigurationProperty.Memory``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cpu is not None:
                self._values["cpu"] = cpu
            if instance_role_arn is not None:
                self._values["instance_role_arn"] = instance_role_arn
            if memory is not None:
                self._values["memory"] = memory

        @builtins.property
        def cpu(self) -> typing.Optional[builtins.str]:
            '''``CfnService.InstanceConfigurationProperty.Cpu``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-cpu
            '''
            result = self._values.get("cpu")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnService.InstanceConfigurationProperty.InstanceRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-instancerolearn
            '''
            result = self._values.get("instance_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def memory(self) -> typing.Optional[builtins.str]:
            '''``CfnService.InstanceConfigurationProperty.Memory``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-memory
            '''
            result = self._values.get("memory")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.KeyValuePairProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class KeyValuePairProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnService.KeyValuePairProperty.Name``.
            :param value: ``CfnService.KeyValuePairProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnService.KeyValuePairProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnService.KeyValuePairProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValuePairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.SourceCodeVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class SourceCodeVersionProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''
            :param type: ``CfnService.SourceCodeVersionProperty.Type``.
            :param value: ``CfnService.SourceCodeVersionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnService.SourceCodeVersionProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnService.SourceCodeVersionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceCodeVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_configuration": "authenticationConfiguration",
            "auto_deployments_enabled": "autoDeploymentsEnabled",
            "code_repository": "codeRepository",
            "image_repository": "imageRepository",
        },
    )
    class SourceConfigurationProperty:
        def __init__(
            self,
            *,
            authentication_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.AuthenticationConfigurationProperty"]] = None,
            auto_deployments_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            code_repository: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeRepositoryProperty"]] = None,
            image_repository: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageRepositoryProperty"]] = None,
        ) -> None:
            '''
            :param authentication_configuration: ``CfnService.SourceConfigurationProperty.AuthenticationConfiguration``.
            :param auto_deployments_enabled: ``CfnService.SourceConfigurationProperty.AutoDeploymentsEnabled``.
            :param code_repository: ``CfnService.SourceConfigurationProperty.CodeRepository``.
            :param image_repository: ``CfnService.SourceConfigurationProperty.ImageRepository``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if auto_deployments_enabled is not None:
                self._values["auto_deployments_enabled"] = auto_deployments_enabled
            if code_repository is not None:
                self._values["code_repository"] = code_repository
            if image_repository is not None:
                self._values["image_repository"] = image_repository

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.AuthenticationConfigurationProperty"]]:
            '''``CfnService.SourceConfigurationProperty.AuthenticationConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.AuthenticationConfigurationProperty"]], result)

        @builtins.property
        def auto_deployments_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnService.SourceConfigurationProperty.AutoDeploymentsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-autodeploymentsenabled
            '''
            result = self._values.get("auto_deployments_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def code_repository(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeRepositoryProperty"]]:
            '''``CfnService.SourceConfigurationProperty.CodeRepository``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-coderepository
            '''
            result = self._values.get("code_repository")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeRepositoryProperty"]], result)

        @builtins.property
        def image_repository(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageRepositoryProperty"]]:
            '''``CfnService.SourceConfigurationProperty.ImageRepository``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-imagerepository
            '''
            result = self._values.get("image_repository")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageRepositoryProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "source_configuration": "sourceConfiguration",
        "auto_scaling_configuration_arn": "autoScalingConfigurationArn",
        "encryption_configuration": "encryptionConfiguration",
        "health_check_configuration": "healthCheckConfiguration",
        "instance_configuration": "instanceConfiguration",
        "service_name": "serviceName",
        "tags": "tags",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        source_configuration: typing.Union[CfnService.SourceConfigurationProperty, aws_cdk.core.IResolvable],
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.EncryptionConfigurationProperty]] = None,
        health_check_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckConfigurationProperty]] = None,
        instance_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.InstanceConfigurationProperty]] = None,
        service_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppRunner::Service``.

        :param source_configuration: ``AWS::AppRunner::Service.SourceConfiguration``.
        :param auto_scaling_configuration_arn: ``AWS::AppRunner::Service.AutoScalingConfigurationArn``.
        :param encryption_configuration: ``AWS::AppRunner::Service.EncryptionConfiguration``.
        :param health_check_configuration: ``AWS::AppRunner::Service.HealthCheckConfiguration``.
        :param instance_configuration: ``AWS::AppRunner::Service.InstanceConfiguration``.
        :param service_name: ``AWS::AppRunner::Service.ServiceName``.
        :param tags: ``AWS::AppRunner::Service.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source_configuration": source_configuration,
        }
        if auto_scaling_configuration_arn is not None:
            self._values["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if health_check_configuration is not None:
            self._values["health_check_configuration"] = health_check_configuration
        if instance_configuration is not None:
            self._values["instance_configuration"] = instance_configuration
        if service_name is not None:
            self._values["service_name"] = service_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def source_configuration(
        self,
    ) -> typing.Union[CfnService.SourceConfigurationProperty, aws_cdk.core.IResolvable]:
        '''``AWS::AppRunner::Service.SourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
        '''
        result = self._values.get("source_configuration")
        assert result is not None, "Required property 'source_configuration' is missing"
        return typing.cast(typing.Union[CfnService.SourceConfigurationProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def auto_scaling_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppRunner::Service.AutoScalingConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
        '''
        result = self._values.get("auto_scaling_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.EncryptionConfigurationProperty]]:
        '''``AWS::AppRunner::Service.EncryptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.EncryptionConfigurationProperty]], result)

    @builtins.property
    def health_check_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckConfigurationProperty]]:
        '''``AWS::AppRunner::Service.HealthCheckConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
        '''
        result = self._values.get("health_check_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckConfigurationProperty]], result)

    @builtins.property
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.InstanceConfigurationProperty]]:
        '''``AWS::AppRunner::Service.InstanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
        '''
        result = self._values.get("instance_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.InstanceConfigurationProperty]], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppRunner::Service.ServiceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppRunner::Service.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnService",
    "CfnServiceProps",
]

publication.publish()
