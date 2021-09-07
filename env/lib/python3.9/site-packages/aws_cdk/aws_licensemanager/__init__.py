'''
# AWS::LicenseManager Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_licensemanager as licensemanager
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
class CfnGrant(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-licensemanager.CfnGrant",
):
    '''A CloudFormation ``AWS::LicenseManager::Grant``.

    :cloudformationResource: AWS::LicenseManager::Grant
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
        grant_name: typing.Optional[builtins.str] = None,
        home_region: typing.Optional[builtins.str] = None,
        license_arn: typing.Optional[builtins.str] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::LicenseManager::Grant``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param allowed_operations: ``AWS::LicenseManager::Grant.AllowedOperations``.
        :param grant_name: ``AWS::LicenseManager::Grant.GrantName``.
        :param home_region: ``AWS::LicenseManager::Grant.HomeRegion``.
        :param license_arn: ``AWS::LicenseManager::Grant.LicenseArn``.
        :param principals: ``AWS::LicenseManager::Grant.Principals``.
        :param status: ``AWS::LicenseManager::Grant.Status``.
        '''
        props = CfnGrantProps(
            allowed_operations=allowed_operations,
            grant_name=grant_name,
            home_region=home_region,
            license_arn=license_arn,
            principals=principals,
            status=status,
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
    @jsii.member(jsii_name="attrGrantArn")
    def attr_grant_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: GrantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGrantArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: Version
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowedOperations")
    def allowed_operations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LicenseManager::Grant.AllowedOperations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-allowedoperations
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOperations"))

    @allowed_operations.setter
    def allowed_operations(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "allowedOperations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="grantName")
    def grant_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::Grant.GrantName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-grantname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grantName"))

    @grant_name.setter
    def grant_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "grantName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="homeRegion")
    def home_region(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::Grant.HomeRegion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-homeregion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeRegion"))

    @home_region.setter
    def home_region(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "homeRegion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="licenseArn")
    def license_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::Grant.LicenseArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-licensearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseArn"))

    @license_arn.setter
    def license_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "licenseArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="principals")
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LicenseManager::Grant.Principals``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-principals
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "principals"))

    @principals.setter
    def principals(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "principals", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::Grant.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-licensemanager.CfnGrantProps",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_operations": "allowedOperations",
        "grant_name": "grantName",
        "home_region": "homeRegion",
        "license_arn": "licenseArn",
        "principals": "principals",
        "status": "status",
    },
)
class CfnGrantProps:
    def __init__(
        self,
        *,
        allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
        grant_name: typing.Optional[builtins.str] = None,
        home_region: typing.Optional[builtins.str] = None,
        license_arn: typing.Optional[builtins.str] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::LicenseManager::Grant``.

        :param allowed_operations: ``AWS::LicenseManager::Grant.AllowedOperations``.
        :param grant_name: ``AWS::LicenseManager::Grant.GrantName``.
        :param home_region: ``AWS::LicenseManager::Grant.HomeRegion``.
        :param license_arn: ``AWS::LicenseManager::Grant.LicenseArn``.
        :param principals: ``AWS::LicenseManager::Grant.Principals``.
        :param status: ``AWS::LicenseManager::Grant.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_operations is not None:
            self._values["allowed_operations"] = allowed_operations
        if grant_name is not None:
            self._values["grant_name"] = grant_name
        if home_region is not None:
            self._values["home_region"] = home_region
        if license_arn is not None:
            self._values["license_arn"] = license_arn
        if principals is not None:
            self._values["principals"] = principals
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def allowed_operations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LicenseManager::Grant.AllowedOperations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-allowedoperations
        '''
        result = self._values.get("allowed_operations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def grant_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::Grant.GrantName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-grantname
        '''
        result = self._values.get("grant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_region(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::Grant.HomeRegion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-homeregion
        '''
        result = self._values.get("home_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::Grant.LicenseArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-licensearn
        '''
        result = self._values.get("license_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LicenseManager::Grant.Principals``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-principals
        '''
        result = self._values.get("principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::Grant.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGrantProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLicense(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-licensemanager.CfnLicense",
):
    '''A CloudFormation ``AWS::LicenseManager::License``.

    :cloudformationResource: AWS::LicenseManager::License
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        consumption_configuration: typing.Union["CfnLicense.ConsumptionConfigurationProperty", aws_cdk.core.IResolvable],
        entitlements: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.EntitlementProperty"]]],
        home_region: builtins.str,
        issuer: typing.Union[aws_cdk.core.IResolvable, "CfnLicense.IssuerDataProperty"],
        license_name: builtins.str,
        product_name: builtins.str,
        validity: typing.Union[aws_cdk.core.IResolvable, "CfnLicense.ValidityDateFormatProperty"],
        beneficiary: typing.Optional[builtins.str] = None,
        license_metadata: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.MetadataProperty"]]]] = None,
        product_sku: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::LicenseManager::License``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param consumption_configuration: ``AWS::LicenseManager::License.ConsumptionConfiguration``.
        :param entitlements: ``AWS::LicenseManager::License.Entitlements``.
        :param home_region: ``AWS::LicenseManager::License.HomeRegion``.
        :param issuer: ``AWS::LicenseManager::License.Issuer``.
        :param license_name: ``AWS::LicenseManager::License.LicenseName``.
        :param product_name: ``AWS::LicenseManager::License.ProductName``.
        :param validity: ``AWS::LicenseManager::License.Validity``.
        :param beneficiary: ``AWS::LicenseManager::License.Beneficiary``.
        :param license_metadata: ``AWS::LicenseManager::License.LicenseMetadata``.
        :param product_sku: ``AWS::LicenseManager::License.ProductSKU``.
        :param status: ``AWS::LicenseManager::License.Status``.
        '''
        props = CfnLicenseProps(
            consumption_configuration=consumption_configuration,
            entitlements=entitlements,
            home_region=home_region,
            issuer=issuer,
            license_name=license_name,
            product_name=product_name,
            validity=validity,
            beneficiary=beneficiary,
            license_metadata=license_metadata,
            product_sku=product_sku,
            status=status,
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
    @jsii.member(jsii_name="attrLicenseArn")
    def attr_license_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: LicenseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLicenseArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: Version
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="consumptionConfiguration")
    def consumption_configuration(
        self,
    ) -> typing.Union["CfnLicense.ConsumptionConfigurationProperty", aws_cdk.core.IResolvable]:
        '''``AWS::LicenseManager::License.ConsumptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-consumptionconfiguration
        '''
        return typing.cast(typing.Union["CfnLicense.ConsumptionConfigurationProperty", aws_cdk.core.IResolvable], jsii.get(self, "consumptionConfiguration"))

    @consumption_configuration.setter
    def consumption_configuration(
        self,
        value: typing.Union["CfnLicense.ConsumptionConfigurationProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "consumptionConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="entitlements")
    def entitlements(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.EntitlementProperty"]]]:
        '''``AWS::LicenseManager::License.Entitlements``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-entitlements
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.EntitlementProperty"]]], jsii.get(self, "entitlements"))

    @entitlements.setter
    def entitlements(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.EntitlementProperty"]]],
    ) -> None:
        jsii.set(self, "entitlements", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="homeRegion")
    def home_region(self) -> builtins.str:
        '''``AWS::LicenseManager::License.HomeRegion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-homeregion
        '''
        return typing.cast(builtins.str, jsii.get(self, "homeRegion"))

    @home_region.setter
    def home_region(self, value: builtins.str) -> None:
        jsii.set(self, "homeRegion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="issuer")
    def issuer(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnLicense.IssuerDataProperty"]:
        '''``AWS::LicenseManager::License.Issuer``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-issuer
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnLicense.IssuerDataProperty"], jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnLicense.IssuerDataProperty"],
    ) -> None:
        jsii.set(self, "issuer", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="licenseName")
    def license_name(self) -> builtins.str:
        '''``AWS::LicenseManager::License.LicenseName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensename
        '''
        return typing.cast(builtins.str, jsii.get(self, "licenseName"))

    @license_name.setter
    def license_name(self, value: builtins.str) -> None:
        jsii.set(self, "licenseName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="productName")
    def product_name(self) -> builtins.str:
        '''``AWS::LicenseManager::License.ProductName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productname
        '''
        return typing.cast(builtins.str, jsii.get(self, "productName"))

    @product_name.setter
    def product_name(self, value: builtins.str) -> None:
        jsii.set(self, "productName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="validity")
    def validity(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnLicense.ValidityDateFormatProperty"]:
        '''``AWS::LicenseManager::License.Validity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-validity
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnLicense.ValidityDateFormatProperty"], jsii.get(self, "validity"))

    @validity.setter
    def validity(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnLicense.ValidityDateFormatProperty"],
    ) -> None:
        jsii.set(self, "validity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="beneficiary")
    def beneficiary(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::License.Beneficiary``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-beneficiary
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "beneficiary"))

    @beneficiary.setter
    def beneficiary(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "beneficiary", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="licenseMetadata")
    def license_metadata(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.MetadataProperty"]]]]:
        '''``AWS::LicenseManager::License.LicenseMetadata``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensemetadata
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.MetadataProperty"]]]], jsii.get(self, "licenseMetadata"))

    @license_metadata.setter
    def license_metadata(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.MetadataProperty"]]]],
    ) -> None:
        jsii.set(self, "licenseMetadata", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="productSku")
    def product_sku(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::License.ProductSKU``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productsku
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productSku"))

    @product_sku.setter
    def product_sku(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "productSku", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::License.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "status", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-licensemanager.CfnLicense.BorrowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_early_check_in": "allowEarlyCheckIn",
            "max_time_to_live_in_minutes": "maxTimeToLiveInMinutes",
        },
    )
    class BorrowConfigurationProperty:
        def __init__(
            self,
            *,
            allow_early_check_in: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            max_time_to_live_in_minutes: jsii.Number,
        ) -> None:
            '''
            :param allow_early_check_in: ``CfnLicense.BorrowConfigurationProperty.AllowEarlyCheckIn``.
            :param max_time_to_live_in_minutes: ``CfnLicense.BorrowConfigurationProperty.MaxTimeToLiveInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "allow_early_check_in": allow_early_check_in,
                "max_time_to_live_in_minutes": max_time_to_live_in_minutes,
            }

        @builtins.property
        def allow_early_check_in(
            self,
        ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnLicense.BorrowConfigurationProperty.AllowEarlyCheckIn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html#cfn-licensemanager-license-borrowconfiguration-allowearlycheckin
            '''
            result = self._values.get("allow_early_check_in")
            assert result is not None, "Required property 'allow_early_check_in' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def max_time_to_live_in_minutes(self) -> jsii.Number:
            '''``CfnLicense.BorrowConfigurationProperty.MaxTimeToLiveInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html#cfn-licensemanager-license-borrowconfiguration-maxtimetoliveinminutes
            '''
            result = self._values.get("max_time_to_live_in_minutes")
            assert result is not None, "Required property 'max_time_to_live_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BorrowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-licensemanager.CfnLicense.ConsumptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "borrow_configuration": "borrowConfiguration",
            "provisional_configuration": "provisionalConfiguration",
            "renew_type": "renewType",
        },
    )
    class ConsumptionConfigurationProperty:
        def __init__(
            self,
            *,
            borrow_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.BorrowConfigurationProperty"]] = None,
            provisional_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.ProvisionalConfigurationProperty"]] = None,
            renew_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param borrow_configuration: ``CfnLicense.ConsumptionConfigurationProperty.BorrowConfiguration``.
            :param provisional_configuration: ``CfnLicense.ConsumptionConfigurationProperty.ProvisionalConfiguration``.
            :param renew_type: ``CfnLicense.ConsumptionConfigurationProperty.RenewType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if borrow_configuration is not None:
                self._values["borrow_configuration"] = borrow_configuration
            if provisional_configuration is not None:
                self._values["provisional_configuration"] = provisional_configuration
            if renew_type is not None:
                self._values["renew_type"] = renew_type

        @builtins.property
        def borrow_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.BorrowConfigurationProperty"]]:
            '''``CfnLicense.ConsumptionConfigurationProperty.BorrowConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-borrowconfiguration
            '''
            result = self._values.get("borrow_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.BorrowConfigurationProperty"]], result)

        @builtins.property
        def provisional_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.ProvisionalConfigurationProperty"]]:
            '''``CfnLicense.ConsumptionConfigurationProperty.ProvisionalConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-provisionalconfiguration
            '''
            result = self._values.get("provisional_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLicense.ProvisionalConfigurationProperty"]], result)

        @builtins.property
        def renew_type(self) -> typing.Optional[builtins.str]:
            '''``CfnLicense.ConsumptionConfigurationProperty.RenewType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-renewtype
            '''
            result = self._values.get("renew_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConsumptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-licensemanager.CfnLicense.EntitlementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "unit": "unit",
            "allow_check_in": "allowCheckIn",
            "max_count": "maxCount",
            "overage": "overage",
            "value": "value",
        },
    )
    class EntitlementProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            unit: builtins.str,
            allow_check_in: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            max_count: typing.Optional[jsii.Number] = None,
            overage: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnLicense.EntitlementProperty.Name``.
            :param unit: ``CfnLicense.EntitlementProperty.Unit``.
            :param allow_check_in: ``CfnLicense.EntitlementProperty.AllowCheckIn``.
            :param max_count: ``CfnLicense.EntitlementProperty.MaxCount``.
            :param overage: ``CfnLicense.EntitlementProperty.Overage``.
            :param value: ``CfnLicense.EntitlementProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "unit": unit,
            }
            if allow_check_in is not None:
                self._values["allow_check_in"] = allow_check_in
            if max_count is not None:
                self._values["max_count"] = max_count
            if overage is not None:
                self._values["overage"] = overage
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnLicense.EntitlementProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit(self) -> builtins.str:
            '''``CfnLicense.EntitlementProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allow_check_in(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnLicense.EntitlementProperty.AllowCheckIn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-allowcheckin
            '''
            result = self._values.get("allow_check_in")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def max_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnLicense.EntitlementProperty.MaxCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-maxcount
            '''
            result = self._values.get("max_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def overage(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnLicense.EntitlementProperty.Overage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-overage
            '''
            result = self._values.get("overage")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnLicense.EntitlementProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntitlementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-licensemanager.CfnLicense.IssuerDataProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sign_key": "signKey"},
    )
    class IssuerDataProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            sign_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnLicense.IssuerDataProperty.Name``.
            :param sign_key: ``CfnLicense.IssuerDataProperty.SignKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if sign_key is not None:
                self._values["sign_key"] = sign_key

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnLicense.IssuerDataProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html#cfn-licensemanager-license-issuerdata-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sign_key(self) -> typing.Optional[builtins.str]:
            '''``CfnLicense.IssuerDataProperty.SignKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html#cfn-licensemanager-license-issuerdata-signkey
            '''
            result = self._values.get("sign_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IssuerDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-licensemanager.CfnLicense.MetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class MetadataProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''
            :param name: ``CfnLicense.MetadataProperty.Name``.
            :param value: ``CfnLicense.MetadataProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnLicense.MetadataProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html#cfn-licensemanager-license-metadata-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnLicense.MetadataProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html#cfn-licensemanager-license-metadata-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-licensemanager.CfnLicense.ProvisionalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"max_time_to_live_in_minutes": "maxTimeToLiveInMinutes"},
    )
    class ProvisionalConfigurationProperty:
        def __init__(self, *, max_time_to_live_in_minutes: jsii.Number) -> None:
            '''
            :param max_time_to_live_in_minutes: ``CfnLicense.ProvisionalConfigurationProperty.MaxTimeToLiveInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_time_to_live_in_minutes": max_time_to_live_in_minutes,
            }

        @builtins.property
        def max_time_to_live_in_minutes(self) -> jsii.Number:
            '''``CfnLicense.ProvisionalConfigurationProperty.MaxTimeToLiveInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html#cfn-licensemanager-license-provisionalconfiguration-maxtimetoliveinminutes
            '''
            result = self._values.get("max_time_to_live_in_minutes")
            assert result is not None, "Required property 'max_time_to_live_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-licensemanager.CfnLicense.ValidityDateFormatProperty",
        jsii_struct_bases=[],
        name_mapping={"begin": "begin", "end": "end"},
    )
    class ValidityDateFormatProperty:
        def __init__(self, *, begin: builtins.str, end: builtins.str) -> None:
            '''
            :param begin: ``CfnLicense.ValidityDateFormatProperty.Begin``.
            :param end: ``CfnLicense.ValidityDateFormatProperty.End``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "begin": begin,
                "end": end,
            }

        @builtins.property
        def begin(self) -> builtins.str:
            '''``CfnLicense.ValidityDateFormatProperty.Begin``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html#cfn-licensemanager-license-validitydateformat-begin
            '''
            result = self._values.get("begin")
            assert result is not None, "Required property 'begin' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end(self) -> builtins.str:
            '''``CfnLicense.ValidityDateFormatProperty.End``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html#cfn-licensemanager-license-validitydateformat-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidityDateFormatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-licensemanager.CfnLicenseProps",
    jsii_struct_bases=[],
    name_mapping={
        "consumption_configuration": "consumptionConfiguration",
        "entitlements": "entitlements",
        "home_region": "homeRegion",
        "issuer": "issuer",
        "license_name": "licenseName",
        "product_name": "productName",
        "validity": "validity",
        "beneficiary": "beneficiary",
        "license_metadata": "licenseMetadata",
        "product_sku": "productSku",
        "status": "status",
    },
)
class CfnLicenseProps:
    def __init__(
        self,
        *,
        consumption_configuration: typing.Union[CfnLicense.ConsumptionConfigurationProperty, aws_cdk.core.IResolvable],
        entitlements: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnLicense.EntitlementProperty]]],
        home_region: builtins.str,
        issuer: typing.Union[aws_cdk.core.IResolvable, CfnLicense.IssuerDataProperty],
        license_name: builtins.str,
        product_name: builtins.str,
        validity: typing.Union[aws_cdk.core.IResolvable, CfnLicense.ValidityDateFormatProperty],
        beneficiary: typing.Optional[builtins.str] = None,
        license_metadata: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnLicense.MetadataProperty]]]] = None,
        product_sku: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::LicenseManager::License``.

        :param consumption_configuration: ``AWS::LicenseManager::License.ConsumptionConfiguration``.
        :param entitlements: ``AWS::LicenseManager::License.Entitlements``.
        :param home_region: ``AWS::LicenseManager::License.HomeRegion``.
        :param issuer: ``AWS::LicenseManager::License.Issuer``.
        :param license_name: ``AWS::LicenseManager::License.LicenseName``.
        :param product_name: ``AWS::LicenseManager::License.ProductName``.
        :param validity: ``AWS::LicenseManager::License.Validity``.
        :param beneficiary: ``AWS::LicenseManager::License.Beneficiary``.
        :param license_metadata: ``AWS::LicenseManager::License.LicenseMetadata``.
        :param product_sku: ``AWS::LicenseManager::License.ProductSKU``.
        :param status: ``AWS::LicenseManager::License.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "consumption_configuration": consumption_configuration,
            "entitlements": entitlements,
            "home_region": home_region,
            "issuer": issuer,
            "license_name": license_name,
            "product_name": product_name,
            "validity": validity,
        }
        if beneficiary is not None:
            self._values["beneficiary"] = beneficiary
        if license_metadata is not None:
            self._values["license_metadata"] = license_metadata
        if product_sku is not None:
            self._values["product_sku"] = product_sku
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def consumption_configuration(
        self,
    ) -> typing.Union[CfnLicense.ConsumptionConfigurationProperty, aws_cdk.core.IResolvable]:
        '''``AWS::LicenseManager::License.ConsumptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-consumptionconfiguration
        '''
        result = self._values.get("consumption_configuration")
        assert result is not None, "Required property 'consumption_configuration' is missing"
        return typing.cast(typing.Union[CfnLicense.ConsumptionConfigurationProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def entitlements(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnLicense.EntitlementProperty]]]:
        '''``AWS::LicenseManager::License.Entitlements``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-entitlements
        '''
        result = self._values.get("entitlements")
        assert result is not None, "Required property 'entitlements' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnLicense.EntitlementProperty]]], result)

    @builtins.property
    def home_region(self) -> builtins.str:
        '''``AWS::LicenseManager::License.HomeRegion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-homeregion
        '''
        result = self._values.get("home_region")
        assert result is not None, "Required property 'home_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def issuer(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnLicense.IssuerDataProperty]:
        '''``AWS::LicenseManager::License.Issuer``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-issuer
        '''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnLicense.IssuerDataProperty], result)

    @builtins.property
    def license_name(self) -> builtins.str:
        '''``AWS::LicenseManager::License.LicenseName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensename
        '''
        result = self._values.get("license_name")
        assert result is not None, "Required property 'license_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_name(self) -> builtins.str:
        '''``AWS::LicenseManager::License.ProductName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productname
        '''
        result = self._values.get("product_name")
        assert result is not None, "Required property 'product_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnLicense.ValidityDateFormatProperty]:
        '''``AWS::LicenseManager::License.Validity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-validity
        '''
        result = self._values.get("validity")
        assert result is not None, "Required property 'validity' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnLicense.ValidityDateFormatProperty], result)

    @builtins.property
    def beneficiary(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::License.Beneficiary``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-beneficiary
        '''
        result = self._values.get("beneficiary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_metadata(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnLicense.MetadataProperty]]]]:
        '''``AWS::LicenseManager::License.LicenseMetadata``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensemetadata
        '''
        result = self._values.get("license_metadata")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnLicense.MetadataProperty]]]], result)

    @builtins.property
    def product_sku(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::License.ProductSKU``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productsku
        '''
        result = self._values.get("product_sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::LicenseManager::License.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLicenseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGrant",
    "CfnGrantProps",
    "CfnLicense",
    "CfnLicenseProps",
]

publication.publish()
