'''
# AWS::CustomerProfiles Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_customerprofiles as customerprofiles
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
class CfnDomain(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-customerprofiles.CfnDomain",
):
    '''A CloudFormation ``AWS::CustomerProfiles::Domain``.

    :cloudformationResource: AWS::CustomerProfiles::Domain
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        dead_letter_queue_url: typing.Optional[builtins.str] = None,
        default_encryption_key: typing.Optional[builtins.str] = None,
        default_expiration_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::CustomerProfiles::Domain``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::CustomerProfiles::Domain.DomainName``.
        :param dead_letter_queue_url: ``AWS::CustomerProfiles::Domain.DeadLetterQueueUrl``.
        :param default_encryption_key: ``AWS::CustomerProfiles::Domain.DefaultEncryptionKey``.
        :param default_expiration_days: ``AWS::CustomerProfiles::Domain.DefaultExpirationDays``.
        :param tags: ``AWS::CustomerProfiles::Domain.Tags``.
        '''
        props = CfnDomainProps(
            domain_name=domain_name,
            dead_letter_queue_url=dead_letter_queue_url,
            default_encryption_key=default_encryption_key,
            default_expiration_days=default_expiration_days,
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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::CustomerProfiles::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Domain.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deadLetterQueueUrl")
    def dead_letter_queue_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Domain.DeadLetterQueueUrl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-deadletterqueueurl
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deadLetterQueueUrl"))

    @dead_letter_queue_url.setter
    def dead_letter_queue_url(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "deadLetterQueueUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultEncryptionKey")
    def default_encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Domain.DefaultEncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultencryptionkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultEncryptionKey"))

    @default_encryption_key.setter
    def default_encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultEncryptionKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultExpirationDays")
    def default_expiration_days(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CustomerProfiles::Domain.DefaultExpirationDays``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultexpirationdays
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultExpirationDays"))

    @default_expiration_days.setter
    def default_expiration_days(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "defaultExpirationDays", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-customerprofiles.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "dead_letter_queue_url": "deadLetterQueueUrl",
        "default_encryption_key": "defaultEncryptionKey",
        "default_expiration_days": "defaultExpirationDays",
        "tags": "tags",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        dead_letter_queue_url: typing.Optional[builtins.str] = None,
        default_encryption_key: typing.Optional[builtins.str] = None,
        default_expiration_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CustomerProfiles::Domain``.

        :param domain_name: ``AWS::CustomerProfiles::Domain.DomainName``.
        :param dead_letter_queue_url: ``AWS::CustomerProfiles::Domain.DeadLetterQueueUrl``.
        :param default_encryption_key: ``AWS::CustomerProfiles::Domain.DefaultEncryptionKey``.
        :param default_expiration_days: ``AWS::CustomerProfiles::Domain.DefaultExpirationDays``.
        :param tags: ``AWS::CustomerProfiles::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if dead_letter_queue_url is not None:
            self._values["dead_letter_queue_url"] = dead_letter_queue_url
        if default_encryption_key is not None:
            self._values["default_encryption_key"] = default_encryption_key
        if default_expiration_days is not None:
            self._values["default_expiration_days"] = default_expiration_days
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Domain.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dead_letter_queue_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Domain.DeadLetterQueueUrl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-deadletterqueueurl
        '''
        result = self._values.get("dead_letter_queue_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Domain.DefaultEncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultencryptionkey
        '''
        result = self._values.get("default_encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_expiration_days(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CustomerProfiles::Domain.DefaultExpirationDays``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultexpirationdays
        '''
        result = self._values.get("default_expiration_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::CustomerProfiles::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnIntegration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration",
):
    '''A CloudFormation ``AWS::CustomerProfiles::Integration``.

    :cloudformationResource: AWS::CustomerProfiles::Integration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        object_type_name: builtins.str,
        flow_definition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.FlowDefinitionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CustomerProfiles::Integration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::CustomerProfiles::Integration.DomainName``.
        :param object_type_name: ``AWS::CustomerProfiles::Integration.ObjectTypeName``.
        :param flow_definition: ``AWS::CustomerProfiles::Integration.FlowDefinition``.
        :param tags: ``AWS::CustomerProfiles::Integration.Tags``.
        :param uri: ``AWS::CustomerProfiles::Integration.Uri``.
        '''
        props = CfnIntegrationProps(
            domain_name=domain_name,
            object_type_name=object_type_name,
            flow_definition=flow_definition,
            tags=tags,
            uri=uri,
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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::CustomerProfiles::Integration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Integration.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Integration.ObjectTypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypename
        '''
        return typing.cast(builtins.str, jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: builtins.str) -> None:
        jsii.set(self, "objectTypeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="flowDefinition")
    def flow_definition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.FlowDefinitionProperty"]]:
        '''``AWS::CustomerProfiles::Integration.FlowDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-flowdefinition
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.FlowDefinitionProperty"]], jsii.get(self, "flowDefinition"))

    @flow_definition.setter
    def flow_definition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.FlowDefinitionProperty"]],
    ) -> None:
        jsii.set(self, "flowDefinition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="uri")
    def uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Integration.Uri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-uri
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "uri", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.ConnectorOperatorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "marketo": "marketo",
            "s3": "s3",
            "salesforce": "salesforce",
            "service_now": "serviceNow",
            "zendesk": "zendesk",
        },
    )
    class ConnectorOperatorProperty:
        def __init__(
            self,
            *,
            marketo: typing.Optional[builtins.str] = None,
            s3: typing.Optional[builtins.str] = None,
            salesforce: typing.Optional[builtins.str] = None,
            service_now: typing.Optional[builtins.str] = None,
            zendesk: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param marketo: ``CfnIntegration.ConnectorOperatorProperty.Marketo``.
            :param s3: ``CfnIntegration.ConnectorOperatorProperty.S3``.
            :param salesforce: ``CfnIntegration.ConnectorOperatorProperty.Salesforce``.
            :param service_now: ``CfnIntegration.ConnectorOperatorProperty.ServiceNow``.
            :param zendesk: ``CfnIntegration.ConnectorOperatorProperty.Zendesk``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if marketo is not None:
                self._values["marketo"] = marketo
            if s3 is not None:
                self._values["s3"] = s3
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if service_now is not None:
                self._values["service_now"] = service_now
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def marketo(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.ConnectorOperatorProperty.Marketo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.ConnectorOperatorProperty.S3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def salesforce(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.ConnectorOperatorProperty.Salesforce``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_now(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.ConnectorOperatorProperty.ServiceNow``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def zendesk(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.ConnectorOperatorProperty.Zendesk``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorOperatorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.FlowDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "flow_name": "flowName",
            "kms_arn": "kmsArn",
            "source_flow_config": "sourceFlowConfig",
            "tasks": "tasks",
            "trigger_config": "triggerConfig",
            "description": "description",
        },
    )
    class FlowDefinitionProperty:
        def __init__(
            self,
            *,
            flow_name: builtins.str,
            kms_arn: builtins.str,
            source_flow_config: typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.SourceFlowConfigProperty"],
            tasks: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TaskProperty"]]],
            trigger_config: typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TriggerConfigProperty"],
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param flow_name: ``CfnIntegration.FlowDefinitionProperty.FlowName``.
            :param kms_arn: ``CfnIntegration.FlowDefinitionProperty.KmsArn``.
            :param source_flow_config: ``CfnIntegration.FlowDefinitionProperty.SourceFlowConfig``.
            :param tasks: ``CfnIntegration.FlowDefinitionProperty.Tasks``.
            :param trigger_config: ``CfnIntegration.FlowDefinitionProperty.TriggerConfig``.
            :param description: ``CfnIntegration.FlowDefinitionProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "flow_name": flow_name,
                "kms_arn": kms_arn,
                "source_flow_config": source_flow_config,
                "tasks": tasks,
                "trigger_config": trigger_config,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def flow_name(self) -> builtins.str:
            '''``CfnIntegration.FlowDefinitionProperty.FlowName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-flowname
            '''
            result = self._values.get("flow_name")
            assert result is not None, "Required property 'flow_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_arn(self) -> builtins.str:
            '''``CfnIntegration.FlowDefinitionProperty.KmsArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-kmsarn
            '''
            result = self._values.get("kms_arn")
            assert result is not None, "Required property 'kms_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_flow_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.SourceFlowConfigProperty"]:
            '''``CfnIntegration.FlowDefinitionProperty.SourceFlowConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-sourceflowconfig
            '''
            result = self._values.get("source_flow_config")
            assert result is not None, "Required property 'source_flow_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.SourceFlowConfigProperty"], result)

        @builtins.property
        def tasks(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TaskProperty"]]]:
            '''``CfnIntegration.FlowDefinitionProperty.Tasks``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-tasks
            '''
            result = self._values.get("tasks")
            assert result is not None, "Required property 'tasks' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TaskProperty"]]], result)

        @builtins.property
        def trigger_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TriggerConfigProperty"]:
            '''``CfnIntegration.FlowDefinitionProperty.TriggerConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-triggerconfig
            '''
            result = self._values.get("trigger_config")
            assert result is not None, "Required property 'trigger_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TriggerConfigProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.FlowDefinitionProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.IncrementalPullConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"datetime_type_field_name": "datetimeTypeFieldName"},
    )
    class IncrementalPullConfigProperty:
        def __init__(
            self,
            *,
            datetime_type_field_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param datetime_type_field_name: ``CfnIntegration.IncrementalPullConfigProperty.DatetimeTypeFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if datetime_type_field_name is not None:
                self._values["datetime_type_field_name"] = datetime_type_field_name

        @builtins.property
        def datetime_type_field_name(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.IncrementalPullConfigProperty.DatetimeTypeFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html#cfn-customerprofiles-integration-incrementalpullconfig-datetimetypefieldname
            '''
            result = self._values.get("datetime_type_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IncrementalPullConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class MarketoSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''
            :param object: ``CfnIntegration.MarketoSourcePropertiesProperty.Object``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''``CfnIntegration.MarketoSourcePropertiesProperty.Object``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html#cfn-customerprofiles-integration-marketosourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MarketoSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.S3SourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "bucket_prefix": "bucketPrefix"},
    )
    class S3SourcePropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket_name: ``CfnIntegration.S3SourcePropertiesProperty.BucketName``.
            :param bucket_prefix: ``CfnIntegration.S3SourcePropertiesProperty.BucketPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''``CfnIntegration.S3SourcePropertiesProperty.BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.S3SourcePropertiesProperty.BucketPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object": "object",
            "enable_dynamic_field_update": "enableDynamicFieldUpdate",
            "include_deleted_records": "includeDeletedRecords",
        },
    )
    class SalesforceSourcePropertiesProperty:
        def __init__(
            self,
            *,
            object: builtins.str,
            enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            include_deleted_records: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param object: ``CfnIntegration.SalesforceSourcePropertiesProperty.Object``.
            :param enable_dynamic_field_update: ``CfnIntegration.SalesforceSourcePropertiesProperty.EnableDynamicFieldUpdate``.
            :param include_deleted_records: ``CfnIntegration.SalesforceSourcePropertiesProperty.IncludeDeletedRecords``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "object": object,
            }
            if enable_dynamic_field_update is not None:
                self._values["enable_dynamic_field_update"] = enable_dynamic_field_update
            if include_deleted_records is not None:
                self._values["include_deleted_records"] = include_deleted_records

        @builtins.property
        def object(self) -> builtins.str:
            '''``CfnIntegration.SalesforceSourcePropertiesProperty.Object``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def enable_dynamic_field_update(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnIntegration.SalesforceSourcePropertiesProperty.EnableDynamicFieldUpdate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-enabledynamicfieldupdate
            '''
            result = self._values.get("enable_dynamic_field_update")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def include_deleted_records(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnIntegration.SalesforceSourcePropertiesProperty.IncludeDeletedRecords``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-includedeletedrecords
            '''
            result = self._values.get("include_deleted_records")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule_expression": "scheduleExpression",
            "data_pull_mode": "dataPullMode",
            "first_execution_from": "firstExecutionFrom",
            "schedule_end_time": "scheduleEndTime",
            "schedule_offset": "scheduleOffset",
            "schedule_start_time": "scheduleStartTime",
            "timezone": "timezone",
        },
    )
    class ScheduledTriggerPropertiesProperty:
        def __init__(
            self,
            *,
            schedule_expression: builtins.str,
            data_pull_mode: typing.Optional[builtins.str] = None,
            first_execution_from: typing.Optional[jsii.Number] = None,
            schedule_end_time: typing.Optional[jsii.Number] = None,
            schedule_offset: typing.Optional[jsii.Number] = None,
            schedule_start_time: typing.Optional[jsii.Number] = None,
            timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param schedule_expression: ``CfnIntegration.ScheduledTriggerPropertiesProperty.ScheduleExpression``.
            :param data_pull_mode: ``CfnIntegration.ScheduledTriggerPropertiesProperty.DataPullMode``.
            :param first_execution_from: ``CfnIntegration.ScheduledTriggerPropertiesProperty.FirstExecutionFrom``.
            :param schedule_end_time: ``CfnIntegration.ScheduledTriggerPropertiesProperty.ScheduleEndTime``.
            :param schedule_offset: ``CfnIntegration.ScheduledTriggerPropertiesProperty.ScheduleOffset``.
            :param schedule_start_time: ``CfnIntegration.ScheduledTriggerPropertiesProperty.ScheduleStartTime``.
            :param timezone: ``CfnIntegration.ScheduledTriggerPropertiesProperty.Timezone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }
            if data_pull_mode is not None:
                self._values["data_pull_mode"] = data_pull_mode
            if first_execution_from is not None:
                self._values["first_execution_from"] = first_execution_from
            if schedule_end_time is not None:
                self._values["schedule_end_time"] = schedule_end_time
            if schedule_offset is not None:
                self._values["schedule_offset"] = schedule_offset
            if schedule_start_time is not None:
                self._values["schedule_start_time"] = schedule_start_time
            if timezone is not None:
                self._values["timezone"] = timezone

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''``CfnIntegration.ScheduledTriggerPropertiesProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_pull_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.ScheduledTriggerPropertiesProperty.DataPullMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-datapullmode
            '''
            result = self._values.get("data_pull_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def first_execution_from(self) -> typing.Optional[jsii.Number]:
            '''``CfnIntegration.ScheduledTriggerPropertiesProperty.FirstExecutionFrom``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-firstexecutionfrom
            '''
            result = self._values.get("first_execution_from")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_end_time(self) -> typing.Optional[jsii.Number]:
            '''``CfnIntegration.ScheduledTriggerPropertiesProperty.ScheduleEndTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleendtime
            '''
            result = self._values.get("schedule_end_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnIntegration.ScheduledTriggerPropertiesProperty.ScheduleOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleoffset
            '''
            result = self._values.get("schedule_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_start_time(self) -> typing.Optional[jsii.Number]:
            '''``CfnIntegration.ScheduledTriggerPropertiesProperty.ScheduleStartTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-schedulestarttime
            '''
            result = self._values.get("schedule_start_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timezone(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.ScheduledTriggerPropertiesProperty.Timezone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-timezone
            '''
            result = self._values.get("timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduledTriggerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class ServiceNowSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''
            :param object: ``CfnIntegration.ServiceNowSourcePropertiesProperty.Object``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''``CfnIntegration.ServiceNowSourcePropertiesProperty.Object``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html#cfn-customerprofiles-integration-servicenowsourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "marketo": "marketo",
            "s3": "s3",
            "salesforce": "salesforce",
            "service_now": "serviceNow",
            "zendesk": "zendesk",
        },
    )
    class SourceConnectorPropertiesProperty:
        def __init__(
            self,
            *,
            marketo: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.MarketoSourcePropertiesProperty"]] = None,
            s3: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.S3SourcePropertiesProperty"]] = None,
            salesforce: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.SalesforceSourcePropertiesProperty"]] = None,
            service_now: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ServiceNowSourcePropertiesProperty"]] = None,
            zendesk: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ZendeskSourcePropertiesProperty"]] = None,
        ) -> None:
            '''
            :param marketo: ``CfnIntegration.SourceConnectorPropertiesProperty.Marketo``.
            :param s3: ``CfnIntegration.SourceConnectorPropertiesProperty.S3``.
            :param salesforce: ``CfnIntegration.SourceConnectorPropertiesProperty.Salesforce``.
            :param service_now: ``CfnIntegration.SourceConnectorPropertiesProperty.ServiceNow``.
            :param zendesk: ``CfnIntegration.SourceConnectorPropertiesProperty.Zendesk``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if marketo is not None:
                self._values["marketo"] = marketo
            if s3 is not None:
                self._values["s3"] = s3
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if service_now is not None:
                self._values["service_now"] = service_now
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def marketo(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.MarketoSourcePropertiesProperty"]]:
            '''``CfnIntegration.SourceConnectorPropertiesProperty.Marketo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.MarketoSourcePropertiesProperty"]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.S3SourcePropertiesProperty"]]:
            '''``CfnIntegration.SourceConnectorPropertiesProperty.S3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.S3SourcePropertiesProperty"]], result)

        @builtins.property
        def salesforce(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.SalesforceSourcePropertiesProperty"]]:
            '''``CfnIntegration.SourceConnectorPropertiesProperty.Salesforce``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.SalesforceSourcePropertiesProperty"]], result)

        @builtins.property
        def service_now(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ServiceNowSourcePropertiesProperty"]]:
            '''``CfnIntegration.SourceConnectorPropertiesProperty.ServiceNow``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ServiceNowSourcePropertiesProperty"]], result)

        @builtins.property
        def zendesk(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ZendeskSourcePropertiesProperty"]]:
            '''``CfnIntegration.SourceConnectorPropertiesProperty.Zendesk``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ZendeskSourcePropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConnectorPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.SourceFlowConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_type": "connectorType",
            "source_connector_properties": "sourceConnectorProperties",
            "connector_profile_name": "connectorProfileName",
            "incremental_pull_config": "incrementalPullConfig",
        },
    )
    class SourceFlowConfigProperty:
        def __init__(
            self,
            *,
            connector_type: builtins.str,
            source_connector_properties: typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.SourceConnectorPropertiesProperty"],
            connector_profile_name: typing.Optional[builtins.str] = None,
            incremental_pull_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.IncrementalPullConfigProperty"]] = None,
        ) -> None:
            '''
            :param connector_type: ``CfnIntegration.SourceFlowConfigProperty.ConnectorType``.
            :param source_connector_properties: ``CfnIntegration.SourceFlowConfigProperty.SourceConnectorProperties``.
            :param connector_profile_name: ``CfnIntegration.SourceFlowConfigProperty.ConnectorProfileName``.
            :param incremental_pull_config: ``CfnIntegration.SourceFlowConfigProperty.IncrementalPullConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "connector_type": connector_type,
                "source_connector_properties": source_connector_properties,
            }
            if connector_profile_name is not None:
                self._values["connector_profile_name"] = connector_profile_name
            if incremental_pull_config is not None:
                self._values["incremental_pull_config"] = incremental_pull_config

        @builtins.property
        def connector_type(self) -> builtins.str:
            '''``CfnIntegration.SourceFlowConfigProperty.ConnectorType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectortype
            '''
            result = self._values.get("connector_type")
            assert result is not None, "Required property 'connector_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_connector_properties(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.SourceConnectorPropertiesProperty"]:
            '''``CfnIntegration.SourceFlowConfigProperty.SourceConnectorProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-sourceconnectorproperties
            '''
            result = self._values.get("source_connector_properties")
            assert result is not None, "Required property 'source_connector_properties' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.SourceConnectorPropertiesProperty"], result)

        @builtins.property
        def connector_profile_name(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.SourceFlowConfigProperty.ConnectorProfileName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectorprofilename
            '''
            result = self._values.get("connector_profile_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def incremental_pull_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.IncrementalPullConfigProperty"]]:
            '''``CfnIntegration.SourceFlowConfigProperty.IncrementalPullConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-incrementalpullconfig
            '''
            result = self._values.get("incremental_pull_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.IncrementalPullConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceFlowConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.TaskPropertiesMapProperty",
        jsii_struct_bases=[],
        name_mapping={
            "operator_property_key": "operatorPropertyKey",
            "property": "property",
        },
    )
    class TaskPropertiesMapProperty:
        def __init__(
            self,
            *,
            operator_property_key: builtins.str,
            property: builtins.str,
        ) -> None:
            '''
            :param operator_property_key: ``CfnIntegration.TaskPropertiesMapProperty.OperatorPropertyKey``.
            :param property: ``CfnIntegration.TaskPropertiesMapProperty.Property``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "operator_property_key": operator_property_key,
                "property": property,
            }

        @builtins.property
        def operator_property_key(self) -> builtins.str:
            '''``CfnIntegration.TaskPropertiesMapProperty.OperatorPropertyKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-operatorpropertykey
            '''
            result = self._values.get("operator_property_key")
            assert result is not None, "Required property 'operator_property_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def property(self) -> builtins.str:
            '''``CfnIntegration.TaskPropertiesMapProperty.Property``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-property
            '''
            result = self._values.get("property")
            assert result is not None, "Required property 'property' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskPropertiesMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.TaskProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_fields": "sourceFields",
            "task_type": "taskType",
            "connector_operator": "connectorOperator",
            "destination_field": "destinationField",
            "task_properties": "taskProperties",
        },
    )
    class TaskProperty:
        def __init__(
            self,
            *,
            source_fields: typing.Sequence[builtins.str],
            task_type: builtins.str,
            connector_operator: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ConnectorOperatorProperty"]] = None,
            destination_field: typing.Optional[builtins.str] = None,
            task_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TaskPropertiesMapProperty"]]]] = None,
        ) -> None:
            '''
            :param source_fields: ``CfnIntegration.TaskProperty.SourceFields``.
            :param task_type: ``CfnIntegration.TaskProperty.TaskType``.
            :param connector_operator: ``CfnIntegration.TaskProperty.ConnectorOperator``.
            :param destination_field: ``CfnIntegration.TaskProperty.DestinationField``.
            :param task_properties: ``CfnIntegration.TaskProperty.TaskProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "source_fields": source_fields,
                "task_type": task_type,
            }
            if connector_operator is not None:
                self._values["connector_operator"] = connector_operator
            if destination_field is not None:
                self._values["destination_field"] = destination_field
            if task_properties is not None:
                self._values["task_properties"] = task_properties

        @builtins.property
        def source_fields(self) -> typing.List[builtins.str]:
            '''``CfnIntegration.TaskProperty.SourceFields``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-sourcefields
            '''
            result = self._values.get("source_fields")
            assert result is not None, "Required property 'source_fields' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def task_type(self) -> builtins.str:
            '''``CfnIntegration.TaskProperty.TaskType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-tasktype
            '''
            result = self._values.get("task_type")
            assert result is not None, "Required property 'task_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def connector_operator(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ConnectorOperatorProperty"]]:
            '''``CfnIntegration.TaskProperty.ConnectorOperator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-connectoroperator
            '''
            result = self._values.get("connector_operator")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ConnectorOperatorProperty"]], result)

        @builtins.property
        def destination_field(self) -> typing.Optional[builtins.str]:
            '''``CfnIntegration.TaskProperty.DestinationField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-destinationfield
            '''
            result = self._values.get("destination_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def task_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TaskPropertiesMapProperty"]]]]:
            '''``CfnIntegration.TaskProperty.TaskProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-taskproperties
            '''
            result = self._values.get("task_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TaskPropertiesMapProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.TriggerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trigger_type": "triggerType",
            "trigger_properties": "triggerProperties",
        },
    )
    class TriggerConfigProperty:
        def __init__(
            self,
            *,
            trigger_type: builtins.str,
            trigger_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TriggerPropertiesProperty"]] = None,
        ) -> None:
            '''
            :param trigger_type: ``CfnIntegration.TriggerConfigProperty.TriggerType``.
            :param trigger_properties: ``CfnIntegration.TriggerConfigProperty.TriggerProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "trigger_type": trigger_type,
            }
            if trigger_properties is not None:
                self._values["trigger_properties"] = trigger_properties

        @builtins.property
        def trigger_type(self) -> builtins.str:
            '''``CfnIntegration.TriggerConfigProperty.TriggerType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggertype
            '''
            result = self._values.get("trigger_type")
            assert result is not None, "Required property 'trigger_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def trigger_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TriggerPropertiesProperty"]]:
            '''``CfnIntegration.TriggerConfigProperty.TriggerProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggerproperties
            '''
            result = self._values.get("trigger_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.TriggerPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.TriggerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"scheduled": "scheduled"},
    )
    class TriggerPropertiesProperty:
        def __init__(
            self,
            *,
            scheduled: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ScheduledTriggerPropertiesProperty"]] = None,
        ) -> None:
            '''
            :param scheduled: ``CfnIntegration.TriggerPropertiesProperty.Scheduled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if scheduled is not None:
                self._values["scheduled"] = scheduled

        @builtins.property
        def scheduled(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ScheduledTriggerPropertiesProperty"]]:
            '''``CfnIntegration.TriggerPropertiesProperty.Scheduled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html#cfn-customerprofiles-integration-triggerproperties-scheduled
            '''
            result = self._values.get("scheduled")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIntegration.ScheduledTriggerPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class ZendeskSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''
            :param object: ``CfnIntegration.ZendeskSourcePropertiesProperty.Object``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''``CfnIntegration.ZendeskSourcePropertiesProperty.Object``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html#cfn-customerprofiles-integration-zendesksourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZendeskSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-customerprofiles.CfnIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "object_type_name": "objectTypeName",
        "flow_definition": "flowDefinition",
        "tags": "tags",
        "uri": "uri",
    },
)
class CfnIntegrationProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        object_type_name: builtins.str,
        flow_definition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnIntegration.FlowDefinitionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CustomerProfiles::Integration``.

        :param domain_name: ``AWS::CustomerProfiles::Integration.DomainName``.
        :param object_type_name: ``AWS::CustomerProfiles::Integration.ObjectTypeName``.
        :param flow_definition: ``AWS::CustomerProfiles::Integration.FlowDefinition``.
        :param tags: ``AWS::CustomerProfiles::Integration.Tags``.
        :param uri: ``AWS::CustomerProfiles::Integration.Uri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
        }
        if flow_definition is not None:
            self._values["flow_definition"] = flow_definition
        if tags is not None:
            self._values["tags"] = tags
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Integration.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Integration.ObjectTypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypename
        '''
        result = self._values.get("object_type_name")
        assert result is not None, "Required property 'object_type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_definition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnIntegration.FlowDefinitionProperty]]:
        '''``AWS::CustomerProfiles::Integration.FlowDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-flowdefinition
        '''
        result = self._values.get("flow_definition")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnIntegration.FlowDefinitionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::CustomerProfiles::Integration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Integration.Uri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnObjectType(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-customerprofiles.CfnObjectType",
):
    '''A CloudFormation ``AWS::CustomerProfiles::ObjectType``.

    :cloudformationResource: AWS::CustomerProfiles::ObjectType
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        allow_profile_creation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        expiration_days: typing.Optional[jsii.Number] = None,
        fields: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.FieldMapProperty"]]]] = None,
        keys: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.KeyMapProperty"]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CustomerProfiles::ObjectType``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::CustomerProfiles::ObjectType.DomainName``.
        :param allow_profile_creation: ``AWS::CustomerProfiles::ObjectType.AllowProfileCreation``.
        :param description: ``AWS::CustomerProfiles::ObjectType.Description``.
        :param encryption_key: ``AWS::CustomerProfiles::ObjectType.EncryptionKey``.
        :param expiration_days: ``AWS::CustomerProfiles::ObjectType.ExpirationDays``.
        :param fields: ``AWS::CustomerProfiles::ObjectType.Fields``.
        :param keys: ``AWS::CustomerProfiles::ObjectType.Keys``.
        :param object_type_name: ``AWS::CustomerProfiles::ObjectType.ObjectTypeName``.
        :param tags: ``AWS::CustomerProfiles::ObjectType.Tags``.
        :param template_id: ``AWS::CustomerProfiles::ObjectType.TemplateId``.
        '''
        props = CfnObjectTypeProps(
            domain_name=domain_name,
            allow_profile_creation=allow_profile_creation,
            description=description,
            encryption_key=encryption_key,
            expiration_days=expiration_days,
            fields=fields,
            keys=keys,
            object_type_name=object_type_name,
            tags=tags,
            template_id=template_id,
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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::CustomerProfiles::ObjectType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::ObjectType.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowProfileCreation")
    def allow_profile_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CustomerProfiles::ObjectType.AllowProfileCreation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-allowprofilecreation
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "allowProfileCreation"))

    @allow_profile_creation.setter
    def allow_profile_creation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "allowProfileCreation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.EncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-encryptionkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "encryptionKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="expirationDays")
    def expiration_days(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CustomerProfiles::ObjectType.ExpirationDays``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-expirationdays
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationDays"))

    @expiration_days.setter
    def expiration_days(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "expirationDays", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fields")
    def fields(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.FieldMapProperty"]]]]:
        '''``AWS::CustomerProfiles::ObjectType.Fields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-fields
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.FieldMapProperty"]]]], jsii.get(self, "fields"))

    @fields.setter
    def fields(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.FieldMapProperty"]]]],
    ) -> None:
        jsii.set(self, "fields", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keys")
    def keys(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.KeyMapProperty"]]]]:
        '''``AWS::CustomerProfiles::ObjectType.Keys``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-keys
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.KeyMapProperty"]]]], jsii.get(self, "keys"))

    @keys.setter
    def keys(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.KeyMapProperty"]]]],
    ) -> None:
        jsii.set(self, "keys", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.ObjectTypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-objecttypename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "objectTypeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateId")
    def template_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.TemplateId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-templateid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateId"))

    @template_id.setter
    def template_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnObjectType.FieldMapProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "object_type_field": "objectTypeField"},
    )
    class FieldMapProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            object_type_field: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.ObjectTypeFieldProperty"]] = None,
        ) -> None:
            '''
            :param name: ``CfnObjectType.FieldMapProperty.Name``.
            :param object_type_field: ``CfnObjectType.FieldMapProperty.ObjectTypeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if object_type_field is not None:
                self._values["object_type_field"] = object_type_field

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.FieldMapProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_type_field(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.ObjectTypeFieldProperty"]]:
            '''``CfnObjectType.FieldMapProperty.ObjectTypeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-objecttypefield
            '''
            result = self._values.get("object_type_field")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.ObjectTypeFieldProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnObjectType.KeyMapProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "object_type_key_list": "objectTypeKeyList"},
    )
    class KeyMapProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            object_type_key_list: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.ObjectTypeKeyProperty"]]]] = None,
        ) -> None:
            '''
            :param name: ``CfnObjectType.KeyMapProperty.Name``.
            :param object_type_key_list: ``CfnObjectType.KeyMapProperty.ObjectTypeKeyList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if object_type_key_list is not None:
                self._values["object_type_key_list"] = object_type_key_list

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.KeyMapProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_type_key_list(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.ObjectTypeKeyProperty"]]]]:
            '''``CfnObjectType.KeyMapProperty.ObjectTypeKeyList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-objecttypekeylist
            '''
            result = self._values.get("object_type_key_list")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnObjectType.ObjectTypeKeyProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnObjectType.ObjectTypeFieldProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content_type": "contentType",
            "source": "source",
            "target": "target",
        },
    )
    class ObjectTypeFieldProperty:
        def __init__(
            self,
            *,
            content_type: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
            target: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param content_type: ``CfnObjectType.ObjectTypeFieldProperty.ContentType``.
            :param source: ``CfnObjectType.ObjectTypeFieldProperty.Source``.
            :param target: ``CfnObjectType.ObjectTypeFieldProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if content_type is not None:
                self._values["content_type"] = content_type
            if source is not None:
                self._values["source"] = source
            if target is not None:
                self._values["target"] = target

        @builtins.property
        def content_type(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.ObjectTypeFieldProperty.ContentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-contenttype
            '''
            result = self._values.get("content_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.ObjectTypeFieldProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.ObjectTypeFieldProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-customerprofiles.CfnObjectType.ObjectTypeKeyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_names": "fieldNames",
            "standard_identifiers": "standardIdentifiers",
        },
    )
    class ObjectTypeKeyProperty:
        def __init__(
            self,
            *,
            field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            standard_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param field_names: ``CfnObjectType.ObjectTypeKeyProperty.FieldNames``.
            :param standard_identifiers: ``CfnObjectType.ObjectTypeKeyProperty.StandardIdentifiers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if field_names is not None:
                self._values["field_names"] = field_names
            if standard_identifiers is not None:
                self._values["standard_identifiers"] = standard_identifiers

        @builtins.property
        def field_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnObjectType.ObjectTypeKeyProperty.FieldNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-fieldnames
            '''
            result = self._values.get("field_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def standard_identifiers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnObjectType.ObjectTypeKeyProperty.StandardIdentifiers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers
            '''
            result = self._values.get("standard_identifiers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeKeyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-customerprofiles.CfnObjectTypeProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "allow_profile_creation": "allowProfileCreation",
        "description": "description",
        "encryption_key": "encryptionKey",
        "expiration_days": "expirationDays",
        "fields": "fields",
        "keys": "keys",
        "object_type_name": "objectTypeName",
        "tags": "tags",
        "template_id": "templateId",
    },
)
class CfnObjectTypeProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        allow_profile_creation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        expiration_days: typing.Optional[jsii.Number] = None,
        fields: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnObjectType.FieldMapProperty]]]] = None,
        keys: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnObjectType.KeyMapProperty]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CustomerProfiles::ObjectType``.

        :param domain_name: ``AWS::CustomerProfiles::ObjectType.DomainName``.
        :param allow_profile_creation: ``AWS::CustomerProfiles::ObjectType.AllowProfileCreation``.
        :param description: ``AWS::CustomerProfiles::ObjectType.Description``.
        :param encryption_key: ``AWS::CustomerProfiles::ObjectType.EncryptionKey``.
        :param expiration_days: ``AWS::CustomerProfiles::ObjectType.ExpirationDays``.
        :param fields: ``AWS::CustomerProfiles::ObjectType.Fields``.
        :param keys: ``AWS::CustomerProfiles::ObjectType.Keys``.
        :param object_type_name: ``AWS::CustomerProfiles::ObjectType.ObjectTypeName``.
        :param tags: ``AWS::CustomerProfiles::ObjectType.Tags``.
        :param template_id: ``AWS::CustomerProfiles::ObjectType.TemplateId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if allow_profile_creation is not None:
            self._values["allow_profile_creation"] = allow_profile_creation
        if description is not None:
            self._values["description"] = description
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if expiration_days is not None:
            self._values["expiration_days"] = expiration_days
        if fields is not None:
            self._values["fields"] = fields
        if keys is not None:
            self._values["keys"] = keys
        if object_type_name is not None:
            self._values["object_type_name"] = object_type_name
        if tags is not None:
            self._values["tags"] = tags
        if template_id is not None:
            self._values["template_id"] = template_id

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::ObjectType.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_profile_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CustomerProfiles::ObjectType.AllowProfileCreation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-allowprofilecreation
        '''
        result = self._values.get("allow_profile_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.EncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-encryptionkey
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_days(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CustomerProfiles::ObjectType.ExpirationDays``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-expirationdays
        '''
        result = self._values.get("expiration_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fields(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnObjectType.FieldMapProperty]]]]:
        '''``AWS::CustomerProfiles::ObjectType.Fields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-fields
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnObjectType.FieldMapProperty]]]], result)

    @builtins.property
    def keys(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnObjectType.KeyMapProperty]]]]:
        '''``AWS::CustomerProfiles::ObjectType.Keys``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-keys
        '''
        result = self._values.get("keys")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnObjectType.KeyMapProperty]]]], result)

    @builtins.property
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.ObjectTypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-objecttypename
        '''
        result = self._values.get("object_type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::CustomerProfiles::ObjectType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.TemplateId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-templateid
        '''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnObjectTypeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDomain",
    "CfnDomainProps",
    "CfnIntegration",
    "CfnIntegrationProps",
    "CfnObjectType",
    "CfnObjectTypeProps",
]

publication.publish()
