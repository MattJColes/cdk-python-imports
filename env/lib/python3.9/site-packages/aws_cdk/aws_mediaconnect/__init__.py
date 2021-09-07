'''
# AWS::MediaConnect Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_mediaconnect as mediaconnect
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
class CfnFlow(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlow",
):
    '''A CloudFormation ``AWS::MediaConnect::Flow``.

    :cloudformationResource: AWS::MediaConnect::Flow
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        source: typing.Union["CfnFlow.SourceProperty", aws_cdk.core.IResolvable],
        availability_zone: typing.Optional[builtins.str] = None,
        source_failover_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlow.FailoverConfigProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::Flow``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::MediaConnect::Flow.Name``.
        :param source: ``AWS::MediaConnect::Flow.Source``.
        :param availability_zone: ``AWS::MediaConnect::Flow.AvailabilityZone``.
        :param source_failover_config: ``AWS::MediaConnect::Flow.SourceFailoverConfig``.
        '''
        props = CfnFlowProps(
            name=name,
            source=source,
            availability_zone=availability_zone,
            source_failover_config=source_failover_config,
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
    @jsii.member(jsii_name="attrFlowArn")
    def attr_flow_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: FlowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFlowArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrFlowAvailabilityZone")
    def attr_flow_availability_zone(self) -> builtins.str:
        '''
        :cloudformationAttribute: FlowAvailabilityZone
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFlowAvailabilityZone"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSourceIngestIp")
    def attr_source_ingest_ip(self) -> builtins.str:
        '''
        :cloudformationAttribute: Source.IngestIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceIngestIp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSourceSourceArn")
    def attr_source_source_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Source.SourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceSourceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::MediaConnect::Flow.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Union["CfnFlow.SourceProperty", aws_cdk.core.IResolvable]:
        '''``AWS::MediaConnect::Flow.Source``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-source
        '''
        return typing.cast(typing.Union["CfnFlow.SourceProperty", aws_cdk.core.IResolvable], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union["CfnFlow.SourceProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "source", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::Flow.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "availabilityZone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceFailoverConfig")
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlow.FailoverConfigProperty"]]:
        '''``AWS::MediaConnect::Flow.SourceFailoverConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-sourcefailoverconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlow.FailoverConfigProperty"]], jsii.get(self, "sourceFailoverConfig"))

    @source_failover_config.setter
    def source_failover_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlow.FailoverConfigProperty"]],
    ) -> None:
        jsii.set(self, "sourceFailoverConfig", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediaconnect.CfnFlow.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "role_arn": "roleArn",
            "constant_initialization_vector": "constantInitializationVector",
            "device_id": "deviceId",
            "key_type": "keyType",
            "region": "region",
            "resource_id": "resourceId",
            "secret_arn": "secretArn",
            "url": "url",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            algorithm: builtins.str,
            role_arn: builtins.str,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            device_id: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param algorithm: ``CfnFlow.EncryptionProperty.Algorithm``.
            :param role_arn: ``CfnFlow.EncryptionProperty.RoleArn``.
            :param constant_initialization_vector: ``CfnFlow.EncryptionProperty.ConstantInitializationVector``.
            :param device_id: ``CfnFlow.EncryptionProperty.DeviceId``.
            :param key_type: ``CfnFlow.EncryptionProperty.KeyType``.
            :param region: ``CfnFlow.EncryptionProperty.Region``.
            :param resource_id: ``CfnFlow.EncryptionProperty.ResourceId``.
            :param secret_arn: ``CfnFlow.EncryptionProperty.SecretArn``.
            :param url: ``CfnFlow.EncryptionProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "algorithm": algorithm,
                "role_arn": role_arn,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if device_id is not None:
                self._values["device_id"] = device_id
            if key_type is not None:
                self._values["key_type"] = key_type
            if region is not None:
                self._values["region"] = region
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def algorithm(self) -> builtins.str:
            '''``CfnFlow.EncryptionProperty.Algorithm``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            assert result is not None, "Required property 'algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnFlow.EncryptionProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.EncryptionProperty.ConstantInitializationVector``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_id(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.EncryptionProperty.DeviceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-deviceid
            '''
            result = self._values.get("device_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.EncryptionProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.EncryptionProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.EncryptionProperty.ResourceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.EncryptionProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.EncryptionProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediaconnect.CfnFlow.FailoverConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"recovery_window": "recoveryWindow", "state": "state"},
    )
    class FailoverConfigProperty:
        def __init__(
            self,
            *,
            recovery_window: typing.Optional[jsii.Number] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param recovery_window: ``CfnFlow.FailoverConfigProperty.RecoveryWindow``.
            :param state: ``CfnFlow.FailoverConfigProperty.State``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if recovery_window is not None:
                self._values["recovery_window"] = recovery_window
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def recovery_window(self) -> typing.Optional[jsii.Number]:
            '''``CfnFlow.FailoverConfigProperty.RecoveryWindow``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-recoverywindow
            '''
            result = self._values.get("recovery_window")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.FailoverConfigProperty.State``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailoverConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediaconnect.CfnFlow.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "decryption": "decryption",
            "description": "description",
            "entitlement_arn": "entitlementArn",
            "ingest_ip": "ingestIp",
            "ingest_port": "ingestPort",
            "max_bitrate": "maxBitrate",
            "max_latency": "maxLatency",
            "name": "name",
            "protocol": "protocol",
            "source_arn": "sourceArn",
            "stream_id": "streamId",
            "vpc_interface_name": "vpcInterfaceName",
            "whitelist_cidr": "whitelistCidr",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            decryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlow.EncryptionProperty"]] = None,
            description: typing.Optional[builtins.str] = None,
            entitlement_arn: typing.Optional[builtins.str] = None,
            ingest_ip: typing.Optional[builtins.str] = None,
            ingest_port: typing.Optional[jsii.Number] = None,
            max_bitrate: typing.Optional[jsii.Number] = None,
            max_latency: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
            protocol: typing.Optional[builtins.str] = None,
            source_arn: typing.Optional[builtins.str] = None,
            stream_id: typing.Optional[builtins.str] = None,
            vpc_interface_name: typing.Optional[builtins.str] = None,
            whitelist_cidr: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param decryption: ``CfnFlow.SourceProperty.Decryption``.
            :param description: ``CfnFlow.SourceProperty.Description``.
            :param entitlement_arn: ``CfnFlow.SourceProperty.EntitlementArn``.
            :param ingest_ip: ``CfnFlow.SourceProperty.IngestIp``.
            :param ingest_port: ``CfnFlow.SourceProperty.IngestPort``.
            :param max_bitrate: ``CfnFlow.SourceProperty.MaxBitrate``.
            :param max_latency: ``CfnFlow.SourceProperty.MaxLatency``.
            :param name: ``CfnFlow.SourceProperty.Name``.
            :param protocol: ``CfnFlow.SourceProperty.Protocol``.
            :param source_arn: ``CfnFlow.SourceProperty.SourceArn``.
            :param stream_id: ``CfnFlow.SourceProperty.StreamId``.
            :param vpc_interface_name: ``CfnFlow.SourceProperty.VpcInterfaceName``.
            :param whitelist_cidr: ``CfnFlow.SourceProperty.WhitelistCidr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if decryption is not None:
                self._values["decryption"] = decryption
            if description is not None:
                self._values["description"] = description
            if entitlement_arn is not None:
                self._values["entitlement_arn"] = entitlement_arn
            if ingest_ip is not None:
                self._values["ingest_ip"] = ingest_ip
            if ingest_port is not None:
                self._values["ingest_port"] = ingest_port
            if max_bitrate is not None:
                self._values["max_bitrate"] = max_bitrate
            if max_latency is not None:
                self._values["max_latency"] = max_latency
            if name is not None:
                self._values["name"] = name
            if protocol is not None:
                self._values["protocol"] = protocol
            if source_arn is not None:
                self._values["source_arn"] = source_arn
            if stream_id is not None:
                self._values["stream_id"] = stream_id
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name
            if whitelist_cidr is not None:
                self._values["whitelist_cidr"] = whitelist_cidr

        @builtins.property
        def decryption(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlow.EncryptionProperty"]]:
            '''``CfnFlow.SourceProperty.Decryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-decryption
            '''
            result = self._values.get("decryption")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlow.EncryptionProperty"]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.SourceProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entitlement_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.SourceProperty.EntitlementArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-entitlementarn
            '''
            result = self._values.get("entitlement_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ingest_ip(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.SourceProperty.IngestIp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-ingestip
            '''
            result = self._values.get("ingest_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ingest_port(self) -> typing.Optional[jsii.Number]:
            '''``CfnFlow.SourceProperty.IngestPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-ingestport
            '''
            result = self._values.get("ingest_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_bitrate(self) -> typing.Optional[jsii.Number]:
            '''``CfnFlow.SourceProperty.MaxBitrate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-maxbitrate
            '''
            result = self._values.get("max_bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_latency(self) -> typing.Optional[jsii.Number]:
            '''``CfnFlow.SourceProperty.MaxLatency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-maxlatency
            '''
            result = self._values.get("max_latency")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.SourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.SourceProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.SourceProperty.SourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcearn
            '''
            result = self._values.get("source_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_id(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.SourceProperty.StreamId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-streamid
            '''
            result = self._values.get("stream_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.SourceProperty.VpcInterfaceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def whitelist_cidr(self) -> typing.Optional[builtins.str]:
            '''``CfnFlow.SourceProperty.WhitelistCidr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-whitelistcidr
            '''
            result = self._values.get("whitelist_cidr")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFlowEntitlement(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowEntitlement",
):
    '''A CloudFormation ``AWS::MediaConnect::FlowEntitlement``.

    :cloudformationResource: AWS::MediaConnect::FlowEntitlement
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        flow_arn: builtins.str,
        name: builtins.str,
        subscribers: typing.Sequence[builtins.str],
        data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
        encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowEntitlement.EncryptionProperty"]] = None,
        entitlement_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::FlowEntitlement``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::MediaConnect::FlowEntitlement.Description``.
        :param flow_arn: ``AWS::MediaConnect::FlowEntitlement.FlowArn``.
        :param name: ``AWS::MediaConnect::FlowEntitlement.Name``.
        :param subscribers: ``AWS::MediaConnect::FlowEntitlement.Subscribers``.
        :param data_transfer_subscriber_fee_percent: ``AWS::MediaConnect::FlowEntitlement.DataTransferSubscriberFeePercent``.
        :param encryption: ``AWS::MediaConnect::FlowEntitlement.Encryption``.
        :param entitlement_status: ``AWS::MediaConnect::FlowEntitlement.EntitlementStatus``.
        '''
        props = CfnFlowEntitlementProps(
            description=description,
            flow_arn=flow_arn,
            name=name,
            subscribers=subscribers,
            data_transfer_subscriber_fee_percent=data_transfer_subscriber_fee_percent,
            encryption=encryption,
            entitlement_status=entitlement_status,
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
    @jsii.member(jsii_name="attrEntitlementArn")
    def attr_entitlement_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: EntitlementArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEntitlementArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowEntitlement.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowEntitlement.FlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-flowarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: builtins.str) -> None:
        jsii.set(self, "flowArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowEntitlement.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subscribers")
    def subscribers(self) -> typing.List[builtins.str]:
        '''``AWS::MediaConnect::FlowEntitlement.Subscribers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-subscribers
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subscribers"))

    @subscribers.setter
    def subscribers(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "subscribers", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataTransferSubscriberFeePercent")
    def data_transfer_subscriber_fee_percent(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowEntitlement.DataTransferSubscriberFeePercent``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-datatransfersubscriberfeepercent
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataTransferSubscriberFeePercent"))

    @data_transfer_subscriber_fee_percent.setter
    def data_transfer_subscriber_fee_percent(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "dataTransferSubscriberFeePercent", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryption")
    def encryption(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowEntitlement.EncryptionProperty"]]:
        '''``AWS::MediaConnect::FlowEntitlement.Encryption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-encryption
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowEntitlement.EncryptionProperty"]], jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowEntitlement.EncryptionProperty"]],
    ) -> None:
        jsii.set(self, "encryption", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="entitlementStatus")
    def entitlement_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowEntitlement.EntitlementStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-entitlementstatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entitlementStatus"))

    @entitlement_status.setter
    def entitlement_status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "entitlementStatus", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowEntitlement.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "role_arn": "roleArn",
            "constant_initialization_vector": "constantInitializationVector",
            "device_id": "deviceId",
            "key_type": "keyType",
            "region": "region",
            "resource_id": "resourceId",
            "secret_arn": "secretArn",
            "url": "url",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            algorithm: builtins.str,
            role_arn: builtins.str,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            device_id: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param algorithm: ``CfnFlowEntitlement.EncryptionProperty.Algorithm``.
            :param role_arn: ``CfnFlowEntitlement.EncryptionProperty.RoleArn``.
            :param constant_initialization_vector: ``CfnFlowEntitlement.EncryptionProperty.ConstantInitializationVector``.
            :param device_id: ``CfnFlowEntitlement.EncryptionProperty.DeviceId``.
            :param key_type: ``CfnFlowEntitlement.EncryptionProperty.KeyType``.
            :param region: ``CfnFlowEntitlement.EncryptionProperty.Region``.
            :param resource_id: ``CfnFlowEntitlement.EncryptionProperty.ResourceId``.
            :param secret_arn: ``CfnFlowEntitlement.EncryptionProperty.SecretArn``.
            :param url: ``CfnFlowEntitlement.EncryptionProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "algorithm": algorithm,
                "role_arn": role_arn,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if device_id is not None:
                self._values["device_id"] = device_id
            if key_type is not None:
                self._values["key_type"] = key_type
            if region is not None:
                self._values["region"] = region
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def algorithm(self) -> builtins.str:
            '''``CfnFlowEntitlement.EncryptionProperty.Algorithm``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            assert result is not None, "Required property 'algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnFlowEntitlement.EncryptionProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowEntitlement.EncryptionProperty.ConstantInitializationVector``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_id(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowEntitlement.EncryptionProperty.DeviceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-deviceid
            '''
            result = self._values.get("device_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowEntitlement.EncryptionProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowEntitlement.EncryptionProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowEntitlement.EncryptionProperty.ResourceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowEntitlement.EncryptionProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowEntitlement.EncryptionProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowEntitlementProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "flow_arn": "flowArn",
        "name": "name",
        "subscribers": "subscribers",
        "data_transfer_subscriber_fee_percent": "dataTransferSubscriberFeePercent",
        "encryption": "encryption",
        "entitlement_status": "entitlementStatus",
    },
)
class CfnFlowEntitlementProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        flow_arn: builtins.str,
        name: builtins.str,
        subscribers: typing.Sequence[builtins.str],
        data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
        encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowEntitlement.EncryptionProperty]] = None,
        entitlement_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaConnect::FlowEntitlement``.

        :param description: ``AWS::MediaConnect::FlowEntitlement.Description``.
        :param flow_arn: ``AWS::MediaConnect::FlowEntitlement.FlowArn``.
        :param name: ``AWS::MediaConnect::FlowEntitlement.Name``.
        :param subscribers: ``AWS::MediaConnect::FlowEntitlement.Subscribers``.
        :param data_transfer_subscriber_fee_percent: ``AWS::MediaConnect::FlowEntitlement.DataTransferSubscriberFeePercent``.
        :param encryption: ``AWS::MediaConnect::FlowEntitlement.Encryption``.
        :param entitlement_status: ``AWS::MediaConnect::FlowEntitlement.EntitlementStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "flow_arn": flow_arn,
            "name": name,
            "subscribers": subscribers,
        }
        if data_transfer_subscriber_fee_percent is not None:
            self._values["data_transfer_subscriber_fee_percent"] = data_transfer_subscriber_fee_percent
        if encryption is not None:
            self._values["encryption"] = encryption
        if entitlement_status is not None:
            self._values["entitlement_status"] = entitlement_status

    @builtins.property
    def description(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowEntitlement.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowEntitlement.FlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-flowarn
        '''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowEntitlement.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscribers(self) -> typing.List[builtins.str]:
        '''``AWS::MediaConnect::FlowEntitlement.Subscribers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-subscribers
        '''
        result = self._values.get("subscribers")
        assert result is not None, "Required property 'subscribers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def data_transfer_subscriber_fee_percent(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowEntitlement.DataTransferSubscriberFeePercent``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-datatransfersubscriberfeepercent
        '''
        result = self._values.get("data_transfer_subscriber_fee_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowEntitlement.EncryptionProperty]]:
        '''``AWS::MediaConnect::FlowEntitlement.Encryption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-encryption
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowEntitlement.EncryptionProperty]], result)

    @builtins.property
    def entitlement_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowEntitlement.EntitlementStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-entitlementstatus
        '''
        result = self._values.get("entitlement_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowEntitlementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFlowOutput(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowOutput",
):
    '''A CloudFormation ``AWS::MediaConnect::FlowOutput``.

    :cloudformationResource: AWS::MediaConnect::FlowOutput
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        flow_arn: builtins.str,
        protocol: builtins.str,
        cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        destination: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowOutput.EncryptionProperty"]] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        remote_id: typing.Optional[builtins.str] = None,
        smoothing_latency: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_attachment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowOutput.VpcInterfaceAttachmentProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::FlowOutput``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param flow_arn: ``AWS::MediaConnect::FlowOutput.FlowArn``.
        :param protocol: ``AWS::MediaConnect::FlowOutput.Protocol``.
        :param cidr_allow_list: ``AWS::MediaConnect::FlowOutput.CidrAllowList``.
        :param description: ``AWS::MediaConnect::FlowOutput.Description``.
        :param destination: ``AWS::MediaConnect::FlowOutput.Destination``.
        :param encryption: ``AWS::MediaConnect::FlowOutput.Encryption``.
        :param max_latency: ``AWS::MediaConnect::FlowOutput.MaxLatency``.
        :param name: ``AWS::MediaConnect::FlowOutput.Name``.
        :param port: ``AWS::MediaConnect::FlowOutput.Port``.
        :param remote_id: ``AWS::MediaConnect::FlowOutput.RemoteId``.
        :param smoothing_latency: ``AWS::MediaConnect::FlowOutput.SmoothingLatency``.
        :param stream_id: ``AWS::MediaConnect::FlowOutput.StreamId``.
        :param vpc_interface_attachment: ``AWS::MediaConnect::FlowOutput.VpcInterfaceAttachment``.
        '''
        props = CfnFlowOutputProps(
            flow_arn=flow_arn,
            protocol=protocol,
            cidr_allow_list=cidr_allow_list,
            description=description,
            destination=destination,
            encryption=encryption,
            max_latency=max_latency,
            name=name,
            port=port,
            remote_id=remote_id,
            smoothing_latency=smoothing_latency,
            stream_id=stream_id,
            vpc_interface_attachment=vpc_interface_attachment,
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
    @jsii.member(jsii_name="attrOutputArn")
    def attr_output_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: OutputArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOutputArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowOutput.FlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-flowarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: builtins.str) -> None:
        jsii.set(self, "flowArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowOutput.Protocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-protocol
        '''
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        jsii.set(self, "protocol", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cidrAllowList")
    def cidr_allow_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::MediaConnect::FlowOutput.CidrAllowList``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-cidrallowlist
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cidrAllowList"))

    @cidr_allow_list.setter
    def cidr_allow_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "cidrAllowList", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="destination")
    def destination(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.Destination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-destination
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "destination", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryption")
    def encryption(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowOutput.EncryptionProperty"]]:
        '''``AWS::MediaConnect::FlowOutput.Encryption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-encryption
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowOutput.EncryptionProperty"]], jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowOutput.EncryptionProperty"]],
    ) -> None:
        jsii.set(self, "encryption", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxLatency")
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowOutput.MaxLatency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-maxlatency
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLatency"))

    @max_latency.setter
    def max_latency(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maxLatency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowOutput.Port``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-port
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "port", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="remoteId")
    def remote_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.RemoteId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-remoteid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteId"))

    @remote_id.setter
    def remote_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "remoteId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="smoothingLatency")
    def smoothing_latency(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowOutput.SmoothingLatency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-smoothinglatency
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "smoothingLatency"))

    @smoothing_latency.setter
    def smoothing_latency(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "smoothingLatency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.StreamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-streamid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "streamId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcInterfaceAttachment")
    def vpc_interface_attachment(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowOutput.VpcInterfaceAttachmentProperty"]]:
        '''``AWS::MediaConnect::FlowOutput.VpcInterfaceAttachment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-vpcinterfaceattachment
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowOutput.VpcInterfaceAttachmentProperty"]], jsii.get(self, "vpcInterfaceAttachment"))

    @vpc_interface_attachment.setter
    def vpc_interface_attachment(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowOutput.VpcInterfaceAttachmentProperty"]],
    ) -> None:
        jsii.set(self, "vpcInterfaceAttachment", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowOutput.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "role_arn": "roleArn",
            "secret_arn": "secretArn",
            "key_type": "keyType",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            algorithm: builtins.str,
            role_arn: builtins.str,
            secret_arn: builtins.str,
            key_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param algorithm: ``CfnFlowOutput.EncryptionProperty.Algorithm``.
            :param role_arn: ``CfnFlowOutput.EncryptionProperty.RoleArn``.
            :param secret_arn: ``CfnFlowOutput.EncryptionProperty.SecretArn``.
            :param key_type: ``CfnFlowOutput.EncryptionProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "algorithm": algorithm,
                "role_arn": role_arn,
                "secret_arn": secret_arn,
            }
            if key_type is not None:
                self._values["key_type"] = key_type

        @builtins.property
        def algorithm(self) -> builtins.str:
            '''``CfnFlowOutput.EncryptionProperty.Algorithm``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            assert result is not None, "Required property 'algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnFlowOutput.EncryptionProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''``CfnFlowOutput.EncryptionProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowOutput.EncryptionProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowOutput.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param vpc_interface_name: ``CfnFlowOutput.VpcInterfaceAttachmentProperty.VpcInterfaceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-vpcinterfaceattachment.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowOutput.VpcInterfaceAttachmentProperty.VpcInterfaceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-vpcinterfaceattachment.html#cfn-mediaconnect-flowoutput-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowOutputProps",
    jsii_struct_bases=[],
    name_mapping={
        "flow_arn": "flowArn",
        "protocol": "protocol",
        "cidr_allow_list": "cidrAllowList",
        "description": "description",
        "destination": "destination",
        "encryption": "encryption",
        "max_latency": "maxLatency",
        "name": "name",
        "port": "port",
        "remote_id": "remoteId",
        "smoothing_latency": "smoothingLatency",
        "stream_id": "streamId",
        "vpc_interface_attachment": "vpcInterfaceAttachment",
    },
)
class CfnFlowOutputProps:
    def __init__(
        self,
        *,
        flow_arn: builtins.str,
        protocol: builtins.str,
        cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        destination: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowOutput.EncryptionProperty]] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        remote_id: typing.Optional[builtins.str] = None,
        smoothing_latency: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_attachment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowOutput.VpcInterfaceAttachmentProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaConnect::FlowOutput``.

        :param flow_arn: ``AWS::MediaConnect::FlowOutput.FlowArn``.
        :param protocol: ``AWS::MediaConnect::FlowOutput.Protocol``.
        :param cidr_allow_list: ``AWS::MediaConnect::FlowOutput.CidrAllowList``.
        :param description: ``AWS::MediaConnect::FlowOutput.Description``.
        :param destination: ``AWS::MediaConnect::FlowOutput.Destination``.
        :param encryption: ``AWS::MediaConnect::FlowOutput.Encryption``.
        :param max_latency: ``AWS::MediaConnect::FlowOutput.MaxLatency``.
        :param name: ``AWS::MediaConnect::FlowOutput.Name``.
        :param port: ``AWS::MediaConnect::FlowOutput.Port``.
        :param remote_id: ``AWS::MediaConnect::FlowOutput.RemoteId``.
        :param smoothing_latency: ``AWS::MediaConnect::FlowOutput.SmoothingLatency``.
        :param stream_id: ``AWS::MediaConnect::FlowOutput.StreamId``.
        :param vpc_interface_attachment: ``AWS::MediaConnect::FlowOutput.VpcInterfaceAttachment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "flow_arn": flow_arn,
            "protocol": protocol,
        }
        if cidr_allow_list is not None:
            self._values["cidr_allow_list"] = cidr_allow_list
        if description is not None:
            self._values["description"] = description
        if destination is not None:
            self._values["destination"] = destination
        if encryption is not None:
            self._values["encryption"] = encryption
        if max_latency is not None:
            self._values["max_latency"] = max_latency
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if remote_id is not None:
            self._values["remote_id"] = remote_id
        if smoothing_latency is not None:
            self._values["smoothing_latency"] = smoothing_latency
        if stream_id is not None:
            self._values["stream_id"] = stream_id
        if vpc_interface_attachment is not None:
            self._values["vpc_interface_attachment"] = vpc_interface_attachment

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowOutput.FlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-flowarn
        '''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowOutput.Protocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr_allow_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::MediaConnect::FlowOutput.CidrAllowList``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-cidrallowlist
        '''
        result = self._values.get("cidr_allow_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.Destination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-destination
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowOutput.EncryptionProperty]]:
        '''``AWS::MediaConnect::FlowOutput.Encryption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-encryption
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowOutput.EncryptionProperty]], result)

    @builtins.property
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowOutput.MaxLatency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-maxlatency
        '''
        result = self._values.get("max_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowOutput.Port``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def remote_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.RemoteId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-remoteid
        '''
        result = self._values.get("remote_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smoothing_latency(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowOutput.SmoothingLatency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-smoothinglatency
        '''
        result = self._values.get("smoothing_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowOutput.StreamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-streamid
        '''
        result = self._values.get("stream_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_interface_attachment(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowOutput.VpcInterfaceAttachmentProperty]]:
        '''``AWS::MediaConnect::FlowOutput.VpcInterfaceAttachment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-vpcinterfaceattachment
        '''
        result = self._values.get("vpc_interface_attachment")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowOutput.VpcInterfaceAttachmentProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowOutputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source": "source",
        "availability_zone": "availabilityZone",
        "source_failover_config": "sourceFailoverConfig",
    },
)
class CfnFlowProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        source: typing.Union[CfnFlow.SourceProperty, aws_cdk.core.IResolvable],
        availability_zone: typing.Optional[builtins.str] = None,
        source_failover_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlow.FailoverConfigProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaConnect::Flow``.

        :param name: ``AWS::MediaConnect::Flow.Name``.
        :param source: ``AWS::MediaConnect::Flow.Source``.
        :param availability_zone: ``AWS::MediaConnect::Flow.AvailabilityZone``.
        :param source_failover_config: ``AWS::MediaConnect::Flow.SourceFailoverConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "source": source,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if source_failover_config is not None:
            self._values["source_failover_config"] = source_failover_config

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::MediaConnect::Flow.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> typing.Union[CfnFlow.SourceProperty, aws_cdk.core.IResolvable]:
        '''``AWS::MediaConnect::Flow.Source``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[CfnFlow.SourceProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::Flow.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlow.FailoverConfigProperty]]:
        '''``AWS::MediaConnect::Flow.SourceFailoverConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-sourcefailoverconfig
        '''
        result = self._values.get("source_failover_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlow.FailoverConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFlowSource(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowSource",
):
    '''A CloudFormation ``AWS::MediaConnect::FlowSource``.

    :cloudformationResource: AWS::MediaConnect::FlowSource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        name: builtins.str,
        decryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowSource.EncryptionProperty"]] = None,
        entitlement_arn: typing.Optional[builtins.str] = None,
        flow_arn: typing.Optional[builtins.str] = None,
        ingest_port: typing.Optional[jsii.Number] = None,
        max_bitrate: typing.Optional[jsii.Number] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_name: typing.Optional[builtins.str] = None,
        whitelist_cidr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::FlowSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::MediaConnect::FlowSource.Description``.
        :param name: ``AWS::MediaConnect::FlowSource.Name``.
        :param decryption: ``AWS::MediaConnect::FlowSource.Decryption``.
        :param entitlement_arn: ``AWS::MediaConnect::FlowSource.EntitlementArn``.
        :param flow_arn: ``AWS::MediaConnect::FlowSource.FlowArn``.
        :param ingest_port: ``AWS::MediaConnect::FlowSource.IngestPort``.
        :param max_bitrate: ``AWS::MediaConnect::FlowSource.MaxBitrate``.
        :param max_latency: ``AWS::MediaConnect::FlowSource.MaxLatency``.
        :param protocol: ``AWS::MediaConnect::FlowSource.Protocol``.
        :param stream_id: ``AWS::MediaConnect::FlowSource.StreamId``.
        :param vpc_interface_name: ``AWS::MediaConnect::FlowSource.VpcInterfaceName``.
        :param whitelist_cidr: ``AWS::MediaConnect::FlowSource.WhitelistCidr``.
        '''
        props = CfnFlowSourceProps(
            description=description,
            name=name,
            decryption=decryption,
            entitlement_arn=entitlement_arn,
            flow_arn=flow_arn,
            ingest_port=ingest_port,
            max_bitrate=max_bitrate,
            max_latency=max_latency,
            protocol=protocol,
            stream_id=stream_id,
            vpc_interface_name=vpc_interface_name,
            whitelist_cidr=whitelist_cidr,
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
    @jsii.member(jsii_name="attrIngestIp")
    def attr_ingest_ip(self) -> builtins.str:
        '''
        :cloudformationAttribute: IngestIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIngestIp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSourceArn")
    def attr_source_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowSource.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowSource.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="decryption")
    def decryption(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowSource.EncryptionProperty"]]:
        '''``AWS::MediaConnect::FlowSource.Decryption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-decryption
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowSource.EncryptionProperty"]], jsii.get(self, "decryption"))

    @decryption.setter
    def decryption(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFlowSource.EncryptionProperty"]],
    ) -> None:
        jsii.set(self, "decryption", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="entitlementArn")
    def entitlement_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.EntitlementArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-entitlementarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entitlementArn"))

    @entitlement_arn.setter
    def entitlement_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "entitlementArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.FlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-flowarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "flowArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ingestPort")
    def ingest_port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowSource.IngestPort``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-ingestport
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ingestPort"))

    @ingest_port.setter
    def ingest_port(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "ingestPort", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxBitrate")
    def max_bitrate(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowSource.MaxBitrate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxbitrate
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBitrate"))

    @max_bitrate.setter
    def max_bitrate(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maxBitrate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxLatency")
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowSource.MaxLatency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxlatency
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLatency"))

    @max_latency.setter
    def max_latency(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maxLatency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.Protocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-protocol
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "protocol", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.StreamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-streamid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "streamId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcInterfaceName")
    def vpc_interface_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.VpcInterfaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-vpcinterfacename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcInterfaceName"))

    @vpc_interface_name.setter
    def vpc_interface_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "vpcInterfaceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="whitelistCidr")
    def whitelist_cidr(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.WhitelistCidr``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-whitelistcidr
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whitelistCidr"))

    @whitelist_cidr.setter
    def whitelist_cidr(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "whitelistCidr", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowSource.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "role_arn": "roleArn",
            "constant_initialization_vector": "constantInitializationVector",
            "device_id": "deviceId",
            "key_type": "keyType",
            "region": "region",
            "resource_id": "resourceId",
            "secret_arn": "secretArn",
            "url": "url",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            algorithm: builtins.str,
            role_arn: builtins.str,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            device_id: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param algorithm: ``CfnFlowSource.EncryptionProperty.Algorithm``.
            :param role_arn: ``CfnFlowSource.EncryptionProperty.RoleArn``.
            :param constant_initialization_vector: ``CfnFlowSource.EncryptionProperty.ConstantInitializationVector``.
            :param device_id: ``CfnFlowSource.EncryptionProperty.DeviceId``.
            :param key_type: ``CfnFlowSource.EncryptionProperty.KeyType``.
            :param region: ``CfnFlowSource.EncryptionProperty.Region``.
            :param resource_id: ``CfnFlowSource.EncryptionProperty.ResourceId``.
            :param secret_arn: ``CfnFlowSource.EncryptionProperty.SecretArn``.
            :param url: ``CfnFlowSource.EncryptionProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "algorithm": algorithm,
                "role_arn": role_arn,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if device_id is not None:
                self._values["device_id"] = device_id
            if key_type is not None:
                self._values["key_type"] = key_type
            if region is not None:
                self._values["region"] = region
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def algorithm(self) -> builtins.str:
            '''``CfnFlowSource.EncryptionProperty.Algorithm``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            assert result is not None, "Required property 'algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnFlowSource.EncryptionProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowSource.EncryptionProperty.ConstantInitializationVector``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_id(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowSource.EncryptionProperty.DeviceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-deviceid
            '''
            result = self._values.get("device_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowSource.EncryptionProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowSource.EncryptionProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowSource.EncryptionProperty.ResourceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowSource.EncryptionProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnFlowSource.EncryptionProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "decryption": "decryption",
        "entitlement_arn": "entitlementArn",
        "flow_arn": "flowArn",
        "ingest_port": "ingestPort",
        "max_bitrate": "maxBitrate",
        "max_latency": "maxLatency",
        "protocol": "protocol",
        "stream_id": "streamId",
        "vpc_interface_name": "vpcInterfaceName",
        "whitelist_cidr": "whitelistCidr",
    },
)
class CfnFlowSourceProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        name: builtins.str,
        decryption: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowSource.EncryptionProperty]] = None,
        entitlement_arn: typing.Optional[builtins.str] = None,
        flow_arn: typing.Optional[builtins.str] = None,
        ingest_port: typing.Optional[jsii.Number] = None,
        max_bitrate: typing.Optional[jsii.Number] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_name: typing.Optional[builtins.str] = None,
        whitelist_cidr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MediaConnect::FlowSource``.

        :param description: ``AWS::MediaConnect::FlowSource.Description``.
        :param name: ``AWS::MediaConnect::FlowSource.Name``.
        :param decryption: ``AWS::MediaConnect::FlowSource.Decryption``.
        :param entitlement_arn: ``AWS::MediaConnect::FlowSource.EntitlementArn``.
        :param flow_arn: ``AWS::MediaConnect::FlowSource.FlowArn``.
        :param ingest_port: ``AWS::MediaConnect::FlowSource.IngestPort``.
        :param max_bitrate: ``AWS::MediaConnect::FlowSource.MaxBitrate``.
        :param max_latency: ``AWS::MediaConnect::FlowSource.MaxLatency``.
        :param protocol: ``AWS::MediaConnect::FlowSource.Protocol``.
        :param stream_id: ``AWS::MediaConnect::FlowSource.StreamId``.
        :param vpc_interface_name: ``AWS::MediaConnect::FlowSource.VpcInterfaceName``.
        :param whitelist_cidr: ``AWS::MediaConnect::FlowSource.WhitelistCidr``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "name": name,
        }
        if decryption is not None:
            self._values["decryption"] = decryption
        if entitlement_arn is not None:
            self._values["entitlement_arn"] = entitlement_arn
        if flow_arn is not None:
            self._values["flow_arn"] = flow_arn
        if ingest_port is not None:
            self._values["ingest_port"] = ingest_port
        if max_bitrate is not None:
            self._values["max_bitrate"] = max_bitrate
        if max_latency is not None:
            self._values["max_latency"] = max_latency
        if protocol is not None:
            self._values["protocol"] = protocol
        if stream_id is not None:
            self._values["stream_id"] = stream_id
        if vpc_interface_name is not None:
            self._values["vpc_interface_name"] = vpc_interface_name
        if whitelist_cidr is not None:
            self._values["whitelist_cidr"] = whitelist_cidr

    @builtins.property
    def description(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowSource.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowSource.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def decryption(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowSource.EncryptionProperty]]:
        '''``AWS::MediaConnect::FlowSource.Decryption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-decryption
        '''
        result = self._values.get("decryption")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnFlowSource.EncryptionProperty]], result)

    @builtins.property
    def entitlement_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.EntitlementArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-entitlementarn
        '''
        result = self._values.get("entitlement_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.FlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-flowarn
        '''
        result = self._values.get("flow_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingest_port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowSource.IngestPort``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-ingestport
        '''
        result = self._values.get("ingest_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_bitrate(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowSource.MaxBitrate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxbitrate
        '''
        result = self._values.get("max_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MediaConnect::FlowSource.MaxLatency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxlatency
        '''
        result = self._values.get("max_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.Protocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.StreamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-streamid
        '''
        result = self._values.get("stream_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_interface_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.VpcInterfaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-vpcinterfacename
        '''
        result = self._values.get("vpc_interface_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def whitelist_cidr(self) -> typing.Optional[builtins.str]:
        '''``AWS::MediaConnect::FlowSource.WhitelistCidr``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-whitelistcidr
        '''
        result = self._values.get("whitelist_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFlowVpcInterface(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowVpcInterface",
):
    '''A CloudFormation ``AWS::MediaConnect::FlowVpcInterface``.

    :cloudformationResource: AWS::MediaConnect::FlowVpcInterface
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        flow_arn: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_id: builtins.str,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::FlowVpcInterface``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param flow_arn: ``AWS::MediaConnect::FlowVpcInterface.FlowArn``.
        :param name: ``AWS::MediaConnect::FlowVpcInterface.Name``.
        :param role_arn: ``AWS::MediaConnect::FlowVpcInterface.RoleArn``.
        :param security_group_ids: ``AWS::MediaConnect::FlowVpcInterface.SecurityGroupIds``.
        :param subnet_id: ``AWS::MediaConnect::FlowVpcInterface.SubnetId``.
        '''
        props = CfnFlowVpcInterfaceProps(
            flow_arn=flow_arn,
            name=name,
            role_arn=role_arn,
            security_group_ids=security_group_ids,
            subnet_id=subnet_id,
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
    @jsii.member(jsii_name="attrNetworkInterfaceIds")
    def attr_network_interface_ids(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: NetworkInterfaceIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNetworkInterfaceIds"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowVpcInterface.FlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-flowarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: builtins.str) -> None:
        jsii.set(self, "flowArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowVpcInterface.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowVpcInterface.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''``AWS::MediaConnect::FlowVpcInterface.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-securitygroupids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowVpcInterface.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-subnetid
        '''
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        jsii.set(self, "subnetId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mediaconnect.CfnFlowVpcInterfaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "flow_arn": "flowArn",
        "name": "name",
        "role_arn": "roleArn",
        "security_group_ids": "securityGroupIds",
        "subnet_id": "subnetId",
    },
)
class CfnFlowVpcInterfaceProps:
    def __init__(
        self,
        *,
        flow_arn: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::MediaConnect::FlowVpcInterface``.

        :param flow_arn: ``AWS::MediaConnect::FlowVpcInterface.FlowArn``.
        :param name: ``AWS::MediaConnect::FlowVpcInterface.Name``.
        :param role_arn: ``AWS::MediaConnect::FlowVpcInterface.RoleArn``.
        :param security_group_ids: ``AWS::MediaConnect::FlowVpcInterface.SecurityGroupIds``.
        :param subnet_id: ``AWS::MediaConnect::FlowVpcInterface.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "flow_arn": flow_arn,
            "name": name,
            "role_arn": role_arn,
            "security_group_ids": security_group_ids,
            "subnet_id": subnet_id,
        }

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowVpcInterface.FlowArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-flowarn
        '''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowVpcInterface.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowVpcInterface.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''``AWS::MediaConnect::FlowVpcInterface.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''``AWS::MediaConnect::FlowVpcInterface.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-subnetid
        '''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowVpcInterfaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFlow",
    "CfnFlowEntitlement",
    "CfnFlowEntitlementProps",
    "CfnFlowOutput",
    "CfnFlowOutputProps",
    "CfnFlowProps",
    "CfnFlowSource",
    "CfnFlowSourceProps",
    "CfnFlowVpcInterface",
    "CfnFlowVpcInterfaceProps",
]

publication.publish()
