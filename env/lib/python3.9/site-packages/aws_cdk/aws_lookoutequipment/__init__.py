'''
# AWS::LookoutEquipment Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_lookoutequipment as lookoutequipment
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
class CfnInferenceScheduler(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lookoutequipment.CfnInferenceScheduler",
):
    '''A CloudFormation ``AWS::LookoutEquipment::InferenceScheduler``.

    :cloudformationResource: AWS::LookoutEquipment::InferenceScheduler
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        data_input_configuration: typing.Any,
        data_output_configuration: typing.Any,
        data_upload_frequency: builtins.str,
        model_name: builtins.str,
        role_arn: builtins.str,
        data_delay_offset_in_minutes: typing.Optional[jsii.Number] = None,
        inference_scheduler_name: typing.Optional[builtins.str] = None,
        server_side_kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::LookoutEquipment::InferenceScheduler``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_input_configuration: ``AWS::LookoutEquipment::InferenceScheduler.DataInputConfiguration``.
        :param data_output_configuration: ``AWS::LookoutEquipment::InferenceScheduler.DataOutputConfiguration``.
        :param data_upload_frequency: ``AWS::LookoutEquipment::InferenceScheduler.DataUploadFrequency``.
        :param model_name: ``AWS::LookoutEquipment::InferenceScheduler.ModelName``.
        :param role_arn: ``AWS::LookoutEquipment::InferenceScheduler.RoleArn``.
        :param data_delay_offset_in_minutes: ``AWS::LookoutEquipment::InferenceScheduler.DataDelayOffsetInMinutes``.
        :param inference_scheduler_name: ``AWS::LookoutEquipment::InferenceScheduler.InferenceSchedulerName``.
        :param server_side_kms_key_id: ``AWS::LookoutEquipment::InferenceScheduler.ServerSideKmsKeyId``.
        :param tags: ``AWS::LookoutEquipment::InferenceScheduler.Tags``.
        '''
        props = CfnInferenceSchedulerProps(
            data_input_configuration=data_input_configuration,
            data_output_configuration=data_output_configuration,
            data_upload_frequency=data_upload_frequency,
            model_name=model_name,
            role_arn=role_arn,
            data_delay_offset_in_minutes=data_delay_offset_in_minutes,
            inference_scheduler_name=inference_scheduler_name,
            server_side_kms_key_id=server_side_kms_key_id,
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
    @jsii.member(jsii_name="attrInferenceSchedulerArn")
    def attr_inference_scheduler_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: InferenceSchedulerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInferenceSchedulerArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::LookoutEquipment::InferenceScheduler.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataInputConfiguration")
    def data_input_configuration(self) -> typing.Any:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataInputConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration
        '''
        return typing.cast(typing.Any, jsii.get(self, "dataInputConfiguration"))

    @data_input_configuration.setter
    def data_input_configuration(self, value: typing.Any) -> None:
        jsii.set(self, "dataInputConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataOutputConfiguration")
    def data_output_configuration(self) -> typing.Any:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataOutputConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration
        '''
        return typing.cast(typing.Any, jsii.get(self, "dataOutputConfiguration"))

    @data_output_configuration.setter
    def data_output_configuration(self, value: typing.Any) -> None:
        jsii.set(self, "dataOutputConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataUploadFrequency")
    def data_upload_frequency(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataUploadFrequency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datauploadfrequency
        '''
        return typing.cast(builtins.str, jsii.get(self, "dataUploadFrequency"))

    @data_upload_frequency.setter
    def data_upload_frequency(self, value: builtins.str) -> None:
        jsii.set(self, "dataUploadFrequency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.ModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-modelname
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelName"))

    @model_name.setter
    def model_name(self, value: builtins.str) -> None:
        jsii.set(self, "modelName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataDelayOffsetInMinutes")
    def data_delay_offset_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataDelayOffsetInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataDelayOffsetInMinutes"))

    @data_delay_offset_in_minutes.setter
    def data_delay_offset_in_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "dataDelayOffsetInMinutes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inferenceSchedulerName")
    def inference_scheduler_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutEquipment::InferenceScheduler.InferenceSchedulerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-inferenceschedulername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inferenceSchedulerName"))

    @inference_scheduler_name.setter
    def inference_scheduler_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "inferenceSchedulerName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverSideKmsKeyId")
    def server_side_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutEquipment::InferenceScheduler.ServerSideKmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-serversidekmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverSideKmsKeyId"))

    @server_side_kms_key_id.setter
    def server_side_kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serverSideKmsKeyId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lookoutequipment.CfnInferenceSchedulerProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_input_configuration": "dataInputConfiguration",
        "data_output_configuration": "dataOutputConfiguration",
        "data_upload_frequency": "dataUploadFrequency",
        "model_name": "modelName",
        "role_arn": "roleArn",
        "data_delay_offset_in_minutes": "dataDelayOffsetInMinutes",
        "inference_scheduler_name": "inferenceSchedulerName",
        "server_side_kms_key_id": "serverSideKmsKeyId",
        "tags": "tags",
    },
)
class CfnInferenceSchedulerProps:
    def __init__(
        self,
        *,
        data_input_configuration: typing.Any,
        data_output_configuration: typing.Any,
        data_upload_frequency: builtins.str,
        model_name: builtins.str,
        role_arn: builtins.str,
        data_delay_offset_in_minutes: typing.Optional[jsii.Number] = None,
        inference_scheduler_name: typing.Optional[builtins.str] = None,
        server_side_kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::LookoutEquipment::InferenceScheduler``.

        :param data_input_configuration: ``AWS::LookoutEquipment::InferenceScheduler.DataInputConfiguration``.
        :param data_output_configuration: ``AWS::LookoutEquipment::InferenceScheduler.DataOutputConfiguration``.
        :param data_upload_frequency: ``AWS::LookoutEquipment::InferenceScheduler.DataUploadFrequency``.
        :param model_name: ``AWS::LookoutEquipment::InferenceScheduler.ModelName``.
        :param role_arn: ``AWS::LookoutEquipment::InferenceScheduler.RoleArn``.
        :param data_delay_offset_in_minutes: ``AWS::LookoutEquipment::InferenceScheduler.DataDelayOffsetInMinutes``.
        :param inference_scheduler_name: ``AWS::LookoutEquipment::InferenceScheduler.InferenceSchedulerName``.
        :param server_side_kms_key_id: ``AWS::LookoutEquipment::InferenceScheduler.ServerSideKmsKeyId``.
        :param tags: ``AWS::LookoutEquipment::InferenceScheduler.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_input_configuration": data_input_configuration,
            "data_output_configuration": data_output_configuration,
            "data_upload_frequency": data_upload_frequency,
            "model_name": model_name,
            "role_arn": role_arn,
        }
        if data_delay_offset_in_minutes is not None:
            self._values["data_delay_offset_in_minutes"] = data_delay_offset_in_minutes
        if inference_scheduler_name is not None:
            self._values["inference_scheduler_name"] = inference_scheduler_name
        if server_side_kms_key_id is not None:
            self._values["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_input_configuration(self) -> typing.Any:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataInputConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration
        '''
        result = self._values.get("data_input_configuration")
        assert result is not None, "Required property 'data_input_configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def data_output_configuration(self) -> typing.Any:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataOutputConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration
        '''
        result = self._values.get("data_output_configuration")
        assert result is not None, "Required property 'data_output_configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def data_upload_frequency(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataUploadFrequency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datauploadfrequency
        '''
        result = self._values.get("data_upload_frequency")
        assert result is not None, "Required property 'data_upload_frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_name(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.ModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-modelname
        '''
        result = self._values.get("model_name")
        assert result is not None, "Required property 'model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_delay_offset_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataDelayOffsetInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes
        '''
        result = self._values.get("data_delay_offset_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def inference_scheduler_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutEquipment::InferenceScheduler.InferenceSchedulerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-inferenceschedulername
        '''
        result = self._values.get("inference_scheduler_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutEquipment::InferenceScheduler.ServerSideKmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-serversidekmskeyid
        '''
        result = self._values.get("server_side_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::LookoutEquipment::InferenceScheduler.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInferenceSchedulerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnInferenceScheduler",
    "CfnInferenceSchedulerProps",
]

publication.publish()
