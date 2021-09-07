'''
# AWS Directory Service Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.
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
class CfnMicrosoftAD(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-directoryservice.CfnMicrosoftAD",
):
    '''A CloudFormation ``AWS::DirectoryService::MicrosoftAD``.

    :cloudformationResource: AWS::DirectoryService::MicrosoftAD
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        password: builtins.str,
        vpc_settings: typing.Union["CfnMicrosoftAD.VpcSettingsProperty", aws_cdk.core.IResolvable],
        create_alias: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DirectoryService::MicrosoftAD``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::DirectoryService::MicrosoftAD.Name``.
        :param password: ``AWS::DirectoryService::MicrosoftAD.Password``.
        :param vpc_settings: ``AWS::DirectoryService::MicrosoftAD.VpcSettings``.
        :param create_alias: ``AWS::DirectoryService::MicrosoftAD.CreateAlias``.
        :param edition: ``AWS::DirectoryService::MicrosoftAD.Edition``.
        :param enable_sso: ``AWS::DirectoryService::MicrosoftAD.EnableSso``.
        :param short_name: ``AWS::DirectoryService::MicrosoftAD.ShortName``.
        '''
        props = CfnMicrosoftADProps(
            name=name,
            password=password,
            vpc_settings=vpc_settings,
            create_alias=create_alias,
            edition=edition,
            enable_sso=enable_sso,
            short_name=short_name,
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
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''
        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::DirectoryService::MicrosoftAD.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        '''``AWS::DirectoryService::MicrosoftAD.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        '''
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        jsii.set(self, "password", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union["CfnMicrosoftAD.VpcSettingsProperty", aws_cdk.core.IResolvable]:
        '''``AWS::DirectoryService::MicrosoftAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        '''
        return typing.cast(typing.Union["CfnMicrosoftAD.VpcSettingsProperty", aws_cdk.core.IResolvable], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union["CfnMicrosoftAD.VpcSettingsProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "vpcSettings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::DirectoryService::MicrosoftAD.CreateAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "createAlias", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="edition")
    def edition(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::MicrosoftAD.Edition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "edition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::DirectoryService::MicrosoftAD.EnableSso``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enableSso", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::MicrosoftAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "shortName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-directoryservice.CfnMicrosoftAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''
            :param subnet_ids: ``CfnMicrosoftAD.VpcSettingsProperty.SubnetIds``.
            :param vpc_id: ``CfnMicrosoftAD.VpcSettingsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''``CfnMicrosoftAD.VpcSettingsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''``CfnMicrosoftAD.VpcSettingsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-directoryservice.CfnMicrosoftADProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "password": "password",
        "vpc_settings": "vpcSettings",
        "create_alias": "createAlias",
        "edition": "edition",
        "enable_sso": "enableSso",
        "short_name": "shortName",
    },
)
class CfnMicrosoftADProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        password: builtins.str,
        vpc_settings: typing.Union[CfnMicrosoftAD.VpcSettingsProperty, aws_cdk.core.IResolvable],
        create_alias: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DirectoryService::MicrosoftAD``.

        :param name: ``AWS::DirectoryService::MicrosoftAD.Name``.
        :param password: ``AWS::DirectoryService::MicrosoftAD.Password``.
        :param vpc_settings: ``AWS::DirectoryService::MicrosoftAD.VpcSettings``.
        :param create_alias: ``AWS::DirectoryService::MicrosoftAD.CreateAlias``.
        :param edition: ``AWS::DirectoryService::MicrosoftAD.Edition``.
        :param enable_sso: ``AWS::DirectoryService::MicrosoftAD.EnableSso``.
        :param short_name: ``AWS::DirectoryService::MicrosoftAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "password": password,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if edition is not None:
            self._values["edition"] = edition
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::DirectoryService::MicrosoftAD.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''``AWS::DirectoryService::MicrosoftAD.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[CfnMicrosoftAD.VpcSettingsProperty, aws_cdk.core.IResolvable]:
        '''``AWS::DirectoryService::MicrosoftAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[CfnMicrosoftAD.VpcSettingsProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::DirectoryService::MicrosoftAD.CreateAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def edition(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::MicrosoftAD.Edition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        '''
        result = self._values.get("edition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::DirectoryService::MicrosoftAD.EnableSso``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::MicrosoftAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMicrosoftADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSimpleAD(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-directoryservice.CfnSimpleAD",
):
    '''A CloudFormation ``AWS::DirectoryService::SimpleAD``.

    :cloudformationResource: AWS::DirectoryService::SimpleAD
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        password: builtins.str,
        size: builtins.str,
        vpc_settings: typing.Union[aws_cdk.core.IResolvable, "CfnSimpleAD.VpcSettingsProperty"],
        create_alias: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DirectoryService::SimpleAD``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::DirectoryService::SimpleAD.Name``.
        :param password: ``AWS::DirectoryService::SimpleAD.Password``.
        :param size: ``AWS::DirectoryService::SimpleAD.Size``.
        :param vpc_settings: ``AWS::DirectoryService::SimpleAD.VpcSettings``.
        :param create_alias: ``AWS::DirectoryService::SimpleAD.CreateAlias``.
        :param description: ``AWS::DirectoryService::SimpleAD.Description``.
        :param enable_sso: ``AWS::DirectoryService::SimpleAD.EnableSso``.
        :param short_name: ``AWS::DirectoryService::SimpleAD.ShortName``.
        '''
        props = CfnSimpleADProps(
            name=name,
            password=password,
            size=size,
            vpc_settings=vpc_settings,
            create_alias=create_alias,
            description=description,
            enable_sso=enable_sso,
            short_name=short_name,
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
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''
        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        '''
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        jsii.set(self, "password", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Size``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        '''
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        jsii.set(self, "size", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnSimpleAD.VpcSettingsProperty"]:
        '''``AWS::DirectoryService::SimpleAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnSimpleAD.VpcSettingsProperty"], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnSimpleAD.VpcSettingsProperty"],
    ) -> None:
        jsii.set(self, "vpcSettings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::DirectoryService::SimpleAD.CreateAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "createAlias", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::SimpleAD.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::DirectoryService::SimpleAD.EnableSso``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enableSso", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::SimpleAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "shortName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-directoryservice.CfnSimpleAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''
            :param subnet_ids: ``CfnSimpleAD.VpcSettingsProperty.SubnetIds``.
            :param vpc_id: ``CfnSimpleAD.VpcSettingsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''``CfnSimpleAD.VpcSettingsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''``CfnSimpleAD.VpcSettingsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-directoryservice.CfnSimpleADProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "password": "password",
        "size": "size",
        "vpc_settings": "vpcSettings",
        "create_alias": "createAlias",
        "description": "description",
        "enable_sso": "enableSso",
        "short_name": "shortName",
    },
)
class CfnSimpleADProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        password: builtins.str,
        size: builtins.str,
        vpc_settings: typing.Union[aws_cdk.core.IResolvable, CfnSimpleAD.VpcSettingsProperty],
        create_alias: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DirectoryService::SimpleAD``.

        :param name: ``AWS::DirectoryService::SimpleAD.Name``.
        :param password: ``AWS::DirectoryService::SimpleAD.Password``.
        :param size: ``AWS::DirectoryService::SimpleAD.Size``.
        :param vpc_settings: ``AWS::DirectoryService::SimpleAD.VpcSettings``.
        :param create_alias: ``AWS::DirectoryService::SimpleAD.CreateAlias``.
        :param description: ``AWS::DirectoryService::SimpleAD.Description``.
        :param enable_sso: ``AWS::DirectoryService::SimpleAD.EnableSso``.
        :param short_name: ``AWS::DirectoryService::SimpleAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "password": password,
            "size": size,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if description is not None:
            self._values["description"] = description
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Size``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        '''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnSimpleAD.VpcSettingsProperty]:
        '''``AWS::DirectoryService::SimpleAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnSimpleAD.VpcSettingsProperty], result)

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::DirectoryService::SimpleAD.CreateAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::SimpleAD.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::DirectoryService::SimpleAD.EnableSso``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::SimpleAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSimpleADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMicrosoftAD",
    "CfnMicrosoftADProps",
    "CfnSimpleAD",
    "CfnSimpleADProps",
]

publication.publish()
