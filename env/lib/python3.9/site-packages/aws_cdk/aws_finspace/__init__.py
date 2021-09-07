'''
# AWS::FinSpace Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_finspace as finspace
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
class CfnEnvironment(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-finspace.CfnEnvironment",
):
    '''A CloudFormation ``AWS::FinSpace::Environment``.

    :cloudformationResource: AWS::FinSpace::Environment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        federation_mode: typing.Optional[builtins.str] = None,
        federation_parameters: typing.Optional[typing.Union["CfnEnvironment.FederationParametersProperty", aws_cdk.core.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::FinSpace::Environment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::FinSpace::Environment.Name``.
        :param description: ``AWS::FinSpace::Environment.Description``.
        :param federation_mode: ``AWS::FinSpace::Environment.FederationMode``.
        :param federation_parameters: ``AWS::FinSpace::Environment.FederationParameters``.
        :param kms_key_id: ``AWS::FinSpace::Environment.KmsKeyId``.
        '''
        props = CfnEnvironmentProps(
            name=name,
            description=description,
            federation_mode=federation_mode,
            federation_parameters=federation_parameters,
            kms_key_id=kms_key_id,
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
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AwsAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDedicatedServiceAccountId")
    def attr_dedicated_service_account_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DedicatedServiceAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDedicatedServiceAccountId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEnvironmentArn")
    def attr_environment_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: EnvironmentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEnvironmentUrl")
    def attr_environment_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: EnvironmentUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSageMakerStudioDomainUrl")
    def attr_sage_maker_studio_domain_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: SageMakerStudioDomainUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSageMakerStudioDomainUrl"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::FinSpace::Environment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FinSpace::Environment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="federationMode")
    def federation_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::FinSpace::Environment.FederationMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "federationMode"))

    @federation_mode.setter
    def federation_mode(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "federationMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="federationParameters")
    def federation_parameters(
        self,
    ) -> typing.Optional[typing.Union["CfnEnvironment.FederationParametersProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::FinSpace::Environment.FederationParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationparameters
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEnvironment.FederationParametersProperty", aws_cdk.core.IResolvable]], jsii.get(self, "federationParameters"))

    @federation_parameters.setter
    def federation_parameters(
        self,
        value: typing.Optional[typing.Union["CfnEnvironment.FederationParametersProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "federationParameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::FinSpace::Environment.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-finspace.CfnEnvironment.FederationParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_call_back_url": "applicationCallBackUrl",
            "attribute_map": "attributeMap",
            "federation_provider_name": "federationProviderName",
            "federation_urn": "federationUrn",
            "saml_metadata_document": "samlMetadataDocument",
            "saml_metadata_url": "samlMetadataUrl",
        },
    )
    class FederationParametersProperty:
        def __init__(
            self,
            *,
            application_call_back_url: typing.Optional[builtins.str] = None,
            attribute_map: typing.Any = None,
            federation_provider_name: typing.Optional[builtins.str] = None,
            federation_urn: typing.Optional[builtins.str] = None,
            saml_metadata_document: typing.Optional[builtins.str] = None,
            saml_metadata_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param application_call_back_url: ``CfnEnvironment.FederationParametersProperty.ApplicationCallBackURL``.
            :param attribute_map: ``CfnEnvironment.FederationParametersProperty.AttributeMap``.
            :param federation_provider_name: ``CfnEnvironment.FederationParametersProperty.FederationProviderName``.
            :param federation_urn: ``CfnEnvironment.FederationParametersProperty.FederationURN``.
            :param saml_metadata_document: ``CfnEnvironment.FederationParametersProperty.SamlMetadataDocument``.
            :param saml_metadata_url: ``CfnEnvironment.FederationParametersProperty.SamlMetadataURL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if application_call_back_url is not None:
                self._values["application_call_back_url"] = application_call_back_url
            if attribute_map is not None:
                self._values["attribute_map"] = attribute_map
            if federation_provider_name is not None:
                self._values["federation_provider_name"] = federation_provider_name
            if federation_urn is not None:
                self._values["federation_urn"] = federation_urn
            if saml_metadata_document is not None:
                self._values["saml_metadata_document"] = saml_metadata_document
            if saml_metadata_url is not None:
                self._values["saml_metadata_url"] = saml_metadata_url

        @builtins.property
        def application_call_back_url(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.FederationParametersProperty.ApplicationCallBackURL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-applicationcallbackurl
            '''
            result = self._values.get("application_call_back_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def attribute_map(self) -> typing.Any:
            '''``CfnEnvironment.FederationParametersProperty.AttributeMap``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-attributemap
            '''
            result = self._values.get("attribute_map")
            return typing.cast(typing.Any, result)

        @builtins.property
        def federation_provider_name(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.FederationParametersProperty.FederationProviderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationprovidername
            '''
            result = self._values.get("federation_provider_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def federation_urn(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.FederationParametersProperty.FederationURN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationurn
            '''
            result = self._values.get("federation_urn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def saml_metadata_document(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.FederationParametersProperty.SamlMetadataDocument``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadatadocument
            '''
            result = self._values.get("saml_metadata_document")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def saml_metadata_url(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.FederationParametersProperty.SamlMetadataURL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadataurl
            '''
            result = self._values.get("saml_metadata_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FederationParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-finspace.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "federation_mode": "federationMode",
        "federation_parameters": "federationParameters",
        "kms_key_id": "kmsKeyId",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        federation_mode: typing.Optional[builtins.str] = None,
        federation_parameters: typing.Optional[typing.Union[CfnEnvironment.FederationParametersProperty, aws_cdk.core.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::FinSpace::Environment``.

        :param name: ``AWS::FinSpace::Environment.Name``.
        :param description: ``AWS::FinSpace::Environment.Description``.
        :param federation_mode: ``AWS::FinSpace::Environment.FederationMode``.
        :param federation_parameters: ``AWS::FinSpace::Environment.FederationParameters``.
        :param kms_key_id: ``AWS::FinSpace::Environment.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if federation_mode is not None:
            self._values["federation_mode"] = federation_mode
        if federation_parameters is not None:
            self._values["federation_parameters"] = federation_parameters
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::FinSpace::Environment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FinSpace::Environment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def federation_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::FinSpace::Environment.FederationMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationmode
        '''
        result = self._values.get("federation_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def federation_parameters(
        self,
    ) -> typing.Optional[typing.Union[CfnEnvironment.FederationParametersProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::FinSpace::Environment.FederationParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationparameters
        '''
        result = self._values.get("federation_parameters")
        return typing.cast(typing.Optional[typing.Union[CfnEnvironment.FederationParametersProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::FinSpace::Environment.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()
