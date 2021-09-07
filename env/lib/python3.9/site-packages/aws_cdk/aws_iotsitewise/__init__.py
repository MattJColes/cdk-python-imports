'''
# AWS::IoTSiteWise Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iotsitewise as iotsitewise
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
class CfnAccessPolicy(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotsitewise.CfnAccessPolicy",
):
    '''A CloudFormation ``AWS::IoTSiteWise::AccessPolicy``.

    :cloudformationResource: AWS::IoTSiteWise::AccessPolicy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        access_policy_identity: typing.Union["CfnAccessPolicy.AccessPolicyIdentityProperty", aws_cdk.core.IResolvable],
        access_policy_permission: builtins.str,
        access_policy_resource: typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.AccessPolicyResourceProperty"],
    ) -> None:
        '''Create a new ``AWS::IoTSiteWise::AccessPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param access_policy_identity: ``AWS::IoTSiteWise::AccessPolicy.AccessPolicyIdentity``.
        :param access_policy_permission: ``AWS::IoTSiteWise::AccessPolicy.AccessPolicyPermission``.
        :param access_policy_resource: ``AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource``.
        '''
        props = CfnAccessPolicyProps(
            access_policy_identity=access_policy_identity,
            access_policy_permission=access_policy_permission,
            access_policy_resource=access_policy_resource,
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
    @jsii.member(jsii_name="attrAccessPolicyArn")
    def attr_access_policy_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AccessPolicyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccessPolicyArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAccessPolicyId")
    def attr_access_policy_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AccessPolicyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccessPolicyId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessPolicyIdentity")
    def access_policy_identity(
        self,
    ) -> typing.Union["CfnAccessPolicy.AccessPolicyIdentityProperty", aws_cdk.core.IResolvable]:
        '''``AWS::IoTSiteWise::AccessPolicy.AccessPolicyIdentity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity
        '''
        return typing.cast(typing.Union["CfnAccessPolicy.AccessPolicyIdentityProperty", aws_cdk.core.IResolvable], jsii.get(self, "accessPolicyIdentity"))

    @access_policy_identity.setter
    def access_policy_identity(
        self,
        value: typing.Union["CfnAccessPolicy.AccessPolicyIdentityProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "accessPolicyIdentity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessPolicyPermission")
    def access_policy_permission(self) -> builtins.str:
        '''``AWS::IoTSiteWise::AccessPolicy.AccessPolicyPermission``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicypermission
        '''
        return typing.cast(builtins.str, jsii.get(self, "accessPolicyPermission"))

    @access_policy_permission.setter
    def access_policy_permission(self, value: builtins.str) -> None:
        jsii.set(self, "accessPolicyPermission", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessPolicyResource")
    def access_policy_resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.AccessPolicyResourceProperty"]:
        '''``AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyresource
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.AccessPolicyResourceProperty"], jsii.get(self, "accessPolicyResource"))

    @access_policy_resource.setter
    def access_policy_resource(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.AccessPolicyResourceProperty"],
    ) -> None:
        jsii.set(self, "accessPolicyResource", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAccessPolicy.AccessPolicyIdentityProperty",
        jsii_struct_bases=[],
        name_mapping={"iam_role": "iamRole", "iam_user": "iamUser", "user": "user"},
    )
    class AccessPolicyIdentityProperty:
        def __init__(
            self,
            *,
            iam_role: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.IamRoleProperty"]] = None,
            iam_user: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.IamUserProperty"]] = None,
            user: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.UserProperty"]] = None,
        ) -> None:
            '''
            :param iam_role: ``CfnAccessPolicy.AccessPolicyIdentityProperty.IamRole``.
            :param iam_user: ``CfnAccessPolicy.AccessPolicyIdentityProperty.IamUser``.
            :param user: ``CfnAccessPolicy.AccessPolicyIdentityProperty.User``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if iam_role is not None:
                self._values["iam_role"] = iam_role
            if iam_user is not None:
                self._values["iam_user"] = iam_user
            if user is not None:
                self._values["user"] = user

        @builtins.property
        def iam_role(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.IamRoleProperty"]]:
            '''``CfnAccessPolicy.AccessPolicyIdentityProperty.IamRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamrole
            '''
            result = self._values.get("iam_role")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.IamRoleProperty"]], result)

        @builtins.property
        def iam_user(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.IamUserProperty"]]:
            '''``CfnAccessPolicy.AccessPolicyIdentityProperty.IamUser``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamuser
            '''
            result = self._values.get("iam_user")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.IamUserProperty"]], result)

        @builtins.property
        def user(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.UserProperty"]]:
            '''``CfnAccessPolicy.AccessPolicyIdentityProperty.User``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity-user
            '''
            result = self._values.get("user")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.UserProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessPolicyIdentityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAccessPolicy.AccessPolicyResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"portal": "portal", "project": "project"},
    )
    class AccessPolicyResourceProperty:
        def __init__(
            self,
            *,
            portal: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.PortalProperty"]] = None,
            project: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.ProjectProperty"]] = None,
        ) -> None:
            '''
            :param portal: ``CfnAccessPolicy.AccessPolicyResourceProperty.Portal``.
            :param project: ``CfnAccessPolicy.AccessPolicyResourceProperty.Project``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if portal is not None:
                self._values["portal"] = portal
            if project is not None:
                self._values["project"] = project

        @builtins.property
        def portal(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.PortalProperty"]]:
            '''``CfnAccessPolicy.AccessPolicyResourceProperty.Portal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html#cfn-iotsitewise-accesspolicy-accesspolicyresource-portal
            '''
            result = self._values.get("portal")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.PortalProperty"]], result)

        @builtins.property
        def project(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.ProjectProperty"]]:
            '''``CfnAccessPolicy.AccessPolicyResourceProperty.Project``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html#cfn-iotsitewise-accesspolicy-accesspolicyresource-project
            '''
            result = self._values.get("project")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAccessPolicy.ProjectProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessPolicyResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAccessPolicy.IamRoleProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class IamRoleProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''
            :param arn: ``CfnAccessPolicy.IamRoleProperty.arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamrole.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnAccessPolicy.IamRoleProperty.arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamrole.html#cfn-iotsitewise-accesspolicy-iamrole-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamRoleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAccessPolicy.IamUserProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class IamUserProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''
            :param arn: ``CfnAccessPolicy.IamUserProperty.arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamuser.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnAccessPolicy.IamUserProperty.arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamuser.html#cfn-iotsitewise-accesspolicy-iamuser-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamUserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAccessPolicy.PortalProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class PortalProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            '''
            :param id: ``CfnAccessPolicy.PortalProperty.id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-portal.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''``CfnAccessPolicy.PortalProperty.id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-portal.html#cfn-iotsitewise-accesspolicy-portal-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAccessPolicy.ProjectProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class ProjectProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            '''
            :param id: ``CfnAccessPolicy.ProjectProperty.id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-project.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''``CfnAccessPolicy.ProjectProperty.id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-project.html#cfn-iotsitewise-accesspolicy-project-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAccessPolicy.UserProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class UserProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            '''
            :param id: ``CfnAccessPolicy.UserProperty.id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-user.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''``CfnAccessPolicy.UserProperty.id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-user.html#cfn-iotsitewise-accesspolicy-user-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotsitewise.CfnAccessPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_policy_identity": "accessPolicyIdentity",
        "access_policy_permission": "accessPolicyPermission",
        "access_policy_resource": "accessPolicyResource",
    },
)
class CfnAccessPolicyProps:
    def __init__(
        self,
        *,
        access_policy_identity: typing.Union[CfnAccessPolicy.AccessPolicyIdentityProperty, aws_cdk.core.IResolvable],
        access_policy_permission: builtins.str,
        access_policy_resource: typing.Union[aws_cdk.core.IResolvable, CfnAccessPolicy.AccessPolicyResourceProperty],
    ) -> None:
        '''Properties for defining a ``AWS::IoTSiteWise::AccessPolicy``.

        :param access_policy_identity: ``AWS::IoTSiteWise::AccessPolicy.AccessPolicyIdentity``.
        :param access_policy_permission: ``AWS::IoTSiteWise::AccessPolicy.AccessPolicyPermission``.
        :param access_policy_resource: ``AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "access_policy_identity": access_policy_identity,
            "access_policy_permission": access_policy_permission,
            "access_policy_resource": access_policy_resource,
        }

    @builtins.property
    def access_policy_identity(
        self,
    ) -> typing.Union[CfnAccessPolicy.AccessPolicyIdentityProperty, aws_cdk.core.IResolvable]:
        '''``AWS::IoTSiteWise::AccessPolicy.AccessPolicyIdentity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity
        '''
        result = self._values.get("access_policy_identity")
        assert result is not None, "Required property 'access_policy_identity' is missing"
        return typing.cast(typing.Union[CfnAccessPolicy.AccessPolicyIdentityProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def access_policy_permission(self) -> builtins.str:
        '''``AWS::IoTSiteWise::AccessPolicy.AccessPolicyPermission``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicypermission
        '''
        result = self._values.get("access_policy_permission")
        assert result is not None, "Required property 'access_policy_permission' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policy_resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnAccessPolicy.AccessPolicyResourceProperty]:
        '''``AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyresource
        '''
        result = self._values.get("access_policy_resource")
        assert result is not None, "Required property 'access_policy_resource' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnAccessPolicy.AccessPolicyResourceProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAsset(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotsitewise.CfnAsset",
):
    '''A CloudFormation ``AWS::IoTSiteWise::Asset``.

    :cloudformationResource: AWS::IoTSiteWise::Asset
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        asset_model_id: builtins.str,
        asset_name: builtins.str,
        asset_hierarchies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAsset.AssetHierarchyProperty"]]]] = None,
        asset_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAsset.AssetPropertyProperty"]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTSiteWise::Asset``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param asset_model_id: ``AWS::IoTSiteWise::Asset.AssetModelId``.
        :param asset_name: ``AWS::IoTSiteWise::Asset.AssetName``.
        :param asset_hierarchies: ``AWS::IoTSiteWise::Asset.AssetHierarchies``.
        :param asset_properties: ``AWS::IoTSiteWise::Asset.AssetProperties``.
        :param tags: ``AWS::IoTSiteWise::Asset.Tags``.
        '''
        props = CfnAssetProps(
            asset_model_id=asset_model_id,
            asset_name=asset_name,
            asset_hierarchies=asset_hierarchies,
            asset_properties=asset_properties,
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
    @jsii.member(jsii_name="attrAssetArn")
    def attr_asset_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AssetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssetArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAssetId")
    def attr_asset_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AssetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssetId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTSiteWise::Asset.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetModelId")
    def asset_model_id(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Asset.AssetModelId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetmodelid
        '''
        return typing.cast(builtins.str, jsii.get(self, "assetModelId"))

    @asset_model_id.setter
    def asset_model_id(self, value: builtins.str) -> None:
        jsii.set(self, "assetModelId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetName")
    def asset_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Asset.AssetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "assetName"))

    @asset_name.setter
    def asset_name(self, value: builtins.str) -> None:
        jsii.set(self, "assetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetHierarchies")
    def asset_hierarchies(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAsset.AssetHierarchyProperty"]]]]:
        '''``AWS::IoTSiteWise::Asset.AssetHierarchies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assethierarchies
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAsset.AssetHierarchyProperty"]]]], jsii.get(self, "assetHierarchies"))

    @asset_hierarchies.setter
    def asset_hierarchies(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAsset.AssetHierarchyProperty"]]]],
    ) -> None:
        jsii.set(self, "assetHierarchies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetProperties")
    def asset_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAsset.AssetPropertyProperty"]]]]:
        '''``AWS::IoTSiteWise::Asset.AssetProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetproperties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAsset.AssetPropertyProperty"]]]], jsii.get(self, "assetProperties"))

    @asset_properties.setter
    def asset_properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAsset.AssetPropertyProperty"]]]],
    ) -> None:
        jsii.set(self, "assetProperties", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAsset.AssetHierarchyProperty",
        jsii_struct_bases=[],
        name_mapping={"child_asset_id": "childAssetId", "logical_id": "logicalId"},
    )
    class AssetHierarchyProperty:
        def __init__(
            self,
            *,
            child_asset_id: builtins.str,
            logical_id: builtins.str,
        ) -> None:
            '''
            :param child_asset_id: ``CfnAsset.AssetHierarchyProperty.ChildAssetId``.
            :param logical_id: ``CfnAsset.AssetHierarchyProperty.LogicalId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "child_asset_id": child_asset_id,
                "logical_id": logical_id,
            }

        @builtins.property
        def child_asset_id(self) -> builtins.str:
            '''``CfnAsset.AssetHierarchyProperty.ChildAssetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html#cfn-iotsitewise-asset-assethierarchy-childassetid
            '''
            result = self._values.get("child_asset_id")
            assert result is not None, "Required property 'child_asset_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def logical_id(self) -> builtins.str:
            '''``CfnAsset.AssetHierarchyProperty.LogicalId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html#cfn-iotsitewise-asset-assethierarchy-logicalid
            '''
            result = self._values.get("logical_id")
            assert result is not None, "Required property 'logical_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetHierarchyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAsset.AssetPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "logical_id": "logicalId",
            "alias": "alias",
            "notification_state": "notificationState",
        },
    )
    class AssetPropertyProperty:
        def __init__(
            self,
            *,
            logical_id: builtins.str,
            alias: typing.Optional[builtins.str] = None,
            notification_state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param logical_id: ``CfnAsset.AssetPropertyProperty.LogicalId``.
            :param alias: ``CfnAsset.AssetPropertyProperty.Alias``.
            :param notification_state: ``CfnAsset.AssetPropertyProperty.NotificationState``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "logical_id": logical_id,
            }
            if alias is not None:
                self._values["alias"] = alias
            if notification_state is not None:
                self._values["notification_state"] = notification_state

        @builtins.property
        def logical_id(self) -> builtins.str:
            '''``CfnAsset.AssetPropertyProperty.LogicalId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-logicalid
            '''
            result = self._values.get("logical_id")
            assert result is not None, "Required property 'logical_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def alias(self) -> typing.Optional[builtins.str]:
            '''``CfnAsset.AssetPropertyProperty.Alias``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-alias
            '''
            result = self._values.get("alias")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def notification_state(self) -> typing.Optional[builtins.str]:
            '''``CfnAsset.AssetPropertyProperty.NotificationState``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-notificationstate
            '''
            result = self._values.get("notification_state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAssetModel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel",
):
    '''A CloudFormation ``AWS::IoTSiteWise::AssetModel``.

    :cloudformationResource: AWS::IoTSiteWise::AssetModel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        asset_model_name: builtins.str,
        asset_model_composite_models: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelCompositeModelProperty"]]]] = None,
        asset_model_description: typing.Optional[builtins.str] = None,
        asset_model_hierarchies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelHierarchyProperty"]]]] = None,
        asset_model_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelPropertyProperty"]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTSiteWise::AssetModel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param asset_model_name: ``AWS::IoTSiteWise::AssetModel.AssetModelName``.
        :param asset_model_composite_models: ``AWS::IoTSiteWise::AssetModel.AssetModelCompositeModels``.
        :param asset_model_description: ``AWS::IoTSiteWise::AssetModel.AssetModelDescription``.
        :param asset_model_hierarchies: ``AWS::IoTSiteWise::AssetModel.AssetModelHierarchies``.
        :param asset_model_properties: ``AWS::IoTSiteWise::AssetModel.AssetModelProperties``.
        :param tags: ``AWS::IoTSiteWise::AssetModel.Tags``.
        '''
        props = CfnAssetModelProps(
            asset_model_name=asset_model_name,
            asset_model_composite_models=asset_model_composite_models,
            asset_model_description=asset_model_description,
            asset_model_hierarchies=asset_model_hierarchies,
            asset_model_properties=asset_model_properties,
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
    @jsii.member(jsii_name="attrAssetModelArn")
    def attr_asset_model_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AssetModelArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssetModelArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAssetModelId")
    def attr_asset_model_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AssetModelId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssetModelId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTSiteWise::AssetModel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetModelName")
    def asset_model_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelname
        '''
        return typing.cast(builtins.str, jsii.get(self, "assetModelName"))

    @asset_model_name.setter
    def asset_model_name(self, value: builtins.str) -> None:
        jsii.set(self, "assetModelName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetModelCompositeModels")
    def asset_model_composite_models(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelCompositeModelProperty"]]]]:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelCompositeModels``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodels
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelCompositeModelProperty"]]]], jsii.get(self, "assetModelCompositeModels"))

    @asset_model_composite_models.setter
    def asset_model_composite_models(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelCompositeModelProperty"]]]],
    ) -> None:
        jsii.set(self, "assetModelCompositeModels", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetModelDescription")
    def asset_model_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodeldescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetModelDescription"))

    @asset_model_description.setter
    def asset_model_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "assetModelDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetModelHierarchies")
    def asset_model_hierarchies(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelHierarchyProperty"]]]]:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelHierarchies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelhierarchies
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelHierarchyProperty"]]]], jsii.get(self, "assetModelHierarchies"))

    @asset_model_hierarchies.setter
    def asset_model_hierarchies(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelHierarchyProperty"]]]],
    ) -> None:
        jsii.set(self, "assetModelHierarchies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetModelProperties")
    def asset_model_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelPropertyProperty"]]]]:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelproperties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelPropertyProperty"]]]], jsii.get(self, "assetModelProperties"))

    @asset_model_properties.setter
    def asset_model_properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelPropertyProperty"]]]],
    ) -> None:
        jsii.set(self, "assetModelProperties", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.AssetModelCompositeModelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "type": "type",
            "composite_model_properties": "compositeModelProperties",
            "description": "description",
        },
    )
    class AssetModelCompositeModelProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            type: builtins.str,
            composite_model_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelPropertyProperty"]]]] = None,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnAssetModel.AssetModelCompositeModelProperty.Name``.
            :param type: ``CfnAssetModel.AssetModelCompositeModelProperty.Type``.
            :param composite_model_properties: ``CfnAssetModel.AssetModelCompositeModelProperty.CompositeModelProperties``.
            :param description: ``CfnAssetModel.AssetModelCompositeModelProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if composite_model_properties is not None:
                self._values["composite_model_properties"] = composite_model_properties
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAssetModel.AssetModelCompositeModelProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnAssetModel.AssetModelCompositeModelProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def composite_model_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelPropertyProperty"]]]]:
            '''``CfnAssetModel.AssetModelCompositeModelProperty.CompositeModelProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-compositemodelproperties
            '''
            result = self._values.get("composite_model_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AssetModelPropertyProperty"]]]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnAssetModel.AssetModelCompositeModelProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetModelCompositeModelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.AssetModelHierarchyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "child_asset_model_id": "childAssetModelId",
            "logical_id": "logicalId",
            "name": "name",
        },
    )
    class AssetModelHierarchyProperty:
        def __init__(
            self,
            *,
            child_asset_model_id: builtins.str,
            logical_id: builtins.str,
            name: builtins.str,
        ) -> None:
            '''
            :param child_asset_model_id: ``CfnAssetModel.AssetModelHierarchyProperty.ChildAssetModelId``.
            :param logical_id: ``CfnAssetModel.AssetModelHierarchyProperty.LogicalId``.
            :param name: ``CfnAssetModel.AssetModelHierarchyProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "child_asset_model_id": child_asset_model_id,
                "logical_id": logical_id,
                "name": name,
            }

        @builtins.property
        def child_asset_model_id(self) -> builtins.str:
            '''``CfnAssetModel.AssetModelHierarchyProperty.ChildAssetModelId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-childassetmodelid
            '''
            result = self._values.get("child_asset_model_id")
            assert result is not None, "Required property 'child_asset_model_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def logical_id(self) -> builtins.str:
            '''``CfnAssetModel.AssetModelHierarchyProperty.LogicalId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-logicalid
            '''
            result = self._values.get("logical_id")
            assert result is not None, "Required property 'logical_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAssetModel.AssetModelHierarchyProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetModelHierarchyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.AssetModelPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "logical_id": "logicalId",
            "name": "name",
            "type": "type",
            "data_type_spec": "dataTypeSpec",
            "unit": "unit",
        },
    )
    class AssetModelPropertyProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            logical_id: builtins.str,
            name: builtins.str,
            type: typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.PropertyTypeProperty"],
            data_type_spec: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_type: ``CfnAssetModel.AssetModelPropertyProperty.DataType``.
            :param logical_id: ``CfnAssetModel.AssetModelPropertyProperty.LogicalId``.
            :param name: ``CfnAssetModel.AssetModelPropertyProperty.Name``.
            :param type: ``CfnAssetModel.AssetModelPropertyProperty.Type``.
            :param data_type_spec: ``CfnAssetModel.AssetModelPropertyProperty.DataTypeSpec``.
            :param unit: ``CfnAssetModel.AssetModelPropertyProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_type": data_type,
                "logical_id": logical_id,
                "name": name,
                "type": type,
            }
            if data_type_spec is not None:
                self._values["data_type_spec"] = data_type_spec
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''``CfnAssetModel.AssetModelPropertyProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def logical_id(self) -> builtins.str:
            '''``CfnAssetModel.AssetModelPropertyProperty.LogicalId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-logicalid
            '''
            result = self._values.get("logical_id")
            assert result is not None, "Required property 'logical_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAssetModel.AssetModelPropertyProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.PropertyTypeProperty"]:
            '''``CfnAssetModel.AssetModelPropertyProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.PropertyTypeProperty"], result)

        @builtins.property
        def data_type_spec(self) -> typing.Optional[builtins.str]:
            '''``CfnAssetModel.AssetModelPropertyProperty.DataTypeSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-datatypespec
            '''
            result = self._values.get("data_type_spec")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnAssetModel.AssetModelPropertyProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetModelPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.AttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"default_value": "defaultValue"},
    )
    class AttributeProperty:
        def __init__(
            self,
            *,
            default_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param default_value: ``CfnAssetModel.AttributeProperty.DefaultValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-attribute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_value is not None:
                self._values["default_value"] = default_value

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''``CfnAssetModel.AttributeProperty.DefaultValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-attribute.html#cfn-iotsitewise-assetmodel-attribute-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.ExpressionVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ExpressionVariableProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            value: typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.VariableValueProperty"],
        ) -> None:
            '''
            :param name: ``CfnAssetModel.ExpressionVariableProperty.Name``.
            :param value: ``CfnAssetModel.ExpressionVariableProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAssetModel.ExpressionVariableProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html#cfn-iotsitewise-assetmodel-expressionvariable-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.VariableValueProperty"]:
            '''``CfnAssetModel.ExpressionVariableProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html#cfn-iotsitewise-assetmodel-expressionvariable-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.VariableValueProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExpressionVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.MetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expression": "expression",
            "variables": "variables",
            "window": "window",
        },
    )
    class MetricProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            variables: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.ExpressionVariableProperty"]]],
            window: typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.MetricWindowProperty"],
        ) -> None:
            '''
            :param expression: ``CfnAssetModel.MetricProperty.Expression``.
            :param variables: ``CfnAssetModel.MetricProperty.Variables``.
            :param window: ``CfnAssetModel.MetricProperty.Window``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "expression": expression,
                "variables": variables,
                "window": window,
            }

        @builtins.property
        def expression(self) -> builtins.str:
            '''``CfnAssetModel.MetricProperty.Expression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html#cfn-iotsitewise-assetmodel-metric-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variables(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.ExpressionVariableProperty"]]]:
            '''``CfnAssetModel.MetricProperty.Variables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html#cfn-iotsitewise-assetmodel-metric-variables
            '''
            result = self._values.get("variables")
            assert result is not None, "Required property 'variables' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.ExpressionVariableProperty"]]], result)

        @builtins.property
        def window(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.MetricWindowProperty"]:
            '''``CfnAssetModel.MetricProperty.Window``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html#cfn-iotsitewise-assetmodel-metric-window
            '''
            result = self._values.get("window")
            assert result is not None, "Required property 'window' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.MetricWindowProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.MetricWindowProperty",
        jsii_struct_bases=[],
        name_mapping={"tumbling": "tumbling"},
    )
    class MetricWindowProperty:
        def __init__(
            self,
            *,
            tumbling: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.TumblingWindowProperty"]] = None,
        ) -> None:
            '''
            :param tumbling: ``CfnAssetModel.MetricWindowProperty.Tumbling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metricwindow.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if tumbling is not None:
                self._values["tumbling"] = tumbling

        @builtins.property
        def tumbling(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.TumblingWindowProperty"]]:
            '''``CfnAssetModel.MetricWindowProperty.Tumbling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metricwindow.html#cfn-iotsitewise-assetmodel-metricwindow-tumbling
            '''
            result = self._values.get("tumbling")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.TumblingWindowProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.PropertyTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type_name": "typeName",
            "attribute": "attribute",
            "metric": "metric",
            "transform": "transform",
        },
    )
    class PropertyTypeProperty:
        def __init__(
            self,
            *,
            type_name: builtins.str,
            attribute: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AttributeProperty"]] = None,
            metric: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.MetricProperty"]] = None,
            transform: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.TransformProperty"]] = None,
        ) -> None:
            '''
            :param type_name: ``CfnAssetModel.PropertyTypeProperty.TypeName``.
            :param attribute: ``CfnAssetModel.PropertyTypeProperty.Attribute``.
            :param metric: ``CfnAssetModel.PropertyTypeProperty.Metric``.
            :param transform: ``CfnAssetModel.PropertyTypeProperty.Transform``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type_name": type_name,
            }
            if attribute is not None:
                self._values["attribute"] = attribute
            if metric is not None:
                self._values["metric"] = metric
            if transform is not None:
                self._values["transform"] = transform

        @builtins.property
        def type_name(self) -> builtins.str:
            '''``CfnAssetModel.PropertyTypeProperty.TypeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-typename
            '''
            result = self._values.get("type_name")
            assert result is not None, "Required property 'type_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attribute(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AttributeProperty"]]:
            '''``CfnAssetModel.PropertyTypeProperty.Attribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-attribute
            '''
            result = self._values.get("attribute")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.AttributeProperty"]], result)

        @builtins.property
        def metric(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.MetricProperty"]]:
            '''``CfnAssetModel.PropertyTypeProperty.Metric``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-metric
            '''
            result = self._values.get("metric")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.MetricProperty"]], result)

        @builtins.property
        def transform(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.TransformProperty"]]:
            '''``CfnAssetModel.PropertyTypeProperty.Transform``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-transform
            '''
            result = self._values.get("transform")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.TransformProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropertyTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.TransformProperty",
        jsii_struct_bases=[],
        name_mapping={"expression": "expression", "variables": "variables"},
    )
    class TransformProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            variables: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.ExpressionVariableProperty"]]],
        ) -> None:
            '''
            :param expression: ``CfnAssetModel.TransformProperty.Expression``.
            :param variables: ``CfnAssetModel.TransformProperty.Variables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "expression": expression,
                "variables": variables,
            }

        @builtins.property
        def expression(self) -> builtins.str:
            '''``CfnAssetModel.TransformProperty.Expression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html#cfn-iotsitewise-assetmodel-transform-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variables(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.ExpressionVariableProperty"]]]:
            '''``CfnAssetModel.TransformProperty.Variables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html#cfn-iotsitewise-assetmodel-transform-variables
            '''
            result = self._values.get("variables")
            assert result is not None, "Required property 'variables' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssetModel.ExpressionVariableProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransformProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.TumblingWindowProperty",
        jsii_struct_bases=[],
        name_mapping={"interval": "interval", "offset": "offset"},
    )
    class TumblingWindowProperty:
        def __init__(
            self,
            *,
            interval: builtins.str,
            offset: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param interval: ``CfnAssetModel.TumblingWindowProperty.Interval``.
            :param offset: ``CfnAssetModel.TumblingWindowProperty.Offset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "interval": interval,
            }
            if offset is not None:
                self._values["offset"] = offset

        @builtins.property
        def interval(self) -> builtins.str:
            '''``CfnAssetModel.TumblingWindowProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html#cfn-iotsitewise-assetmodel-tumblingwindow-interval
            '''
            result = self._values.get("interval")
            assert result is not None, "Required property 'interval' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset(self) -> typing.Optional[builtins.str]:
            '''``CfnAssetModel.TumblingWindowProperty.Offset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html#cfn-iotsitewise-assetmodel-tumblingwindow-offset
            '''
            result = self._values.get("offset")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TumblingWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModel.VariableValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property_logical_id": "propertyLogicalId",
            "hierarchy_logical_id": "hierarchyLogicalId",
        },
    )
    class VariableValueProperty:
        def __init__(
            self,
            *,
            property_logical_id: builtins.str,
            hierarchy_logical_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param property_logical_id: ``CfnAssetModel.VariableValueProperty.PropertyLogicalId``.
            :param hierarchy_logical_id: ``CfnAssetModel.VariableValueProperty.HierarchyLogicalId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "property_logical_id": property_logical_id,
            }
            if hierarchy_logical_id is not None:
                self._values["hierarchy_logical_id"] = hierarchy_logical_id

        @builtins.property
        def property_logical_id(self) -> builtins.str:
            '''``CfnAssetModel.VariableValueProperty.PropertyLogicalId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-propertylogicalid
            '''
            result = self._values.get("property_logical_id")
            assert result is not None, "Required property 'property_logical_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hierarchy_logical_id(self) -> typing.Optional[builtins.str]:
            '''``CfnAssetModel.VariableValueProperty.HierarchyLogicalId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-hierarchylogicalid
            '''
            result = self._values.get("hierarchy_logical_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VariableValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "asset_model_name": "assetModelName",
        "asset_model_composite_models": "assetModelCompositeModels",
        "asset_model_description": "assetModelDescription",
        "asset_model_hierarchies": "assetModelHierarchies",
        "asset_model_properties": "assetModelProperties",
        "tags": "tags",
    },
)
class CfnAssetModelProps:
    def __init__(
        self,
        *,
        asset_model_name: builtins.str,
        asset_model_composite_models: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnAssetModel.AssetModelCompositeModelProperty]]]] = None,
        asset_model_description: typing.Optional[builtins.str] = None,
        asset_model_hierarchies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnAssetModel.AssetModelHierarchyProperty]]]] = None,
        asset_model_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnAssetModel.AssetModelPropertyProperty]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTSiteWise::AssetModel``.

        :param asset_model_name: ``AWS::IoTSiteWise::AssetModel.AssetModelName``.
        :param asset_model_composite_models: ``AWS::IoTSiteWise::AssetModel.AssetModelCompositeModels``.
        :param asset_model_description: ``AWS::IoTSiteWise::AssetModel.AssetModelDescription``.
        :param asset_model_hierarchies: ``AWS::IoTSiteWise::AssetModel.AssetModelHierarchies``.
        :param asset_model_properties: ``AWS::IoTSiteWise::AssetModel.AssetModelProperties``.
        :param tags: ``AWS::IoTSiteWise::AssetModel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "asset_model_name": asset_model_name,
        }
        if asset_model_composite_models is not None:
            self._values["asset_model_composite_models"] = asset_model_composite_models
        if asset_model_description is not None:
            self._values["asset_model_description"] = asset_model_description
        if asset_model_hierarchies is not None:
            self._values["asset_model_hierarchies"] = asset_model_hierarchies
        if asset_model_properties is not None:
            self._values["asset_model_properties"] = asset_model_properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def asset_model_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelname
        '''
        result = self._values.get("asset_model_name")
        assert result is not None, "Required property 'asset_model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_model_composite_models(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAssetModel.AssetModelCompositeModelProperty]]]]:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelCompositeModels``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodels
        '''
        result = self._values.get("asset_model_composite_models")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAssetModel.AssetModelCompositeModelProperty]]]], result)

    @builtins.property
    def asset_model_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodeldescription
        '''
        result = self._values.get("asset_model_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_model_hierarchies(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAssetModel.AssetModelHierarchyProperty]]]]:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelHierarchies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelhierarchies
        '''
        result = self._values.get("asset_model_hierarchies")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAssetModel.AssetModelHierarchyProperty]]]], result)

    @builtins.property
    def asset_model_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAssetModel.AssetModelPropertyProperty]]]]:
        '''``AWS::IoTSiteWise::AssetModel.AssetModelProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelproperties
        '''
        result = self._values.get("asset_model_properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAssetModel.AssetModelPropertyProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTSiteWise::AssetModel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssetModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotsitewise.CfnAssetProps",
    jsii_struct_bases=[],
    name_mapping={
        "asset_model_id": "assetModelId",
        "asset_name": "assetName",
        "asset_hierarchies": "assetHierarchies",
        "asset_properties": "assetProperties",
        "tags": "tags",
    },
)
class CfnAssetProps:
    def __init__(
        self,
        *,
        asset_model_id: builtins.str,
        asset_name: builtins.str,
        asset_hierarchies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnAsset.AssetHierarchyProperty]]]] = None,
        asset_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnAsset.AssetPropertyProperty]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTSiteWise::Asset``.

        :param asset_model_id: ``AWS::IoTSiteWise::Asset.AssetModelId``.
        :param asset_name: ``AWS::IoTSiteWise::Asset.AssetName``.
        :param asset_hierarchies: ``AWS::IoTSiteWise::Asset.AssetHierarchies``.
        :param asset_properties: ``AWS::IoTSiteWise::Asset.AssetProperties``.
        :param tags: ``AWS::IoTSiteWise::Asset.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "asset_model_id": asset_model_id,
            "asset_name": asset_name,
        }
        if asset_hierarchies is not None:
            self._values["asset_hierarchies"] = asset_hierarchies
        if asset_properties is not None:
            self._values["asset_properties"] = asset_properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def asset_model_id(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Asset.AssetModelId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetmodelid
        '''
        result = self._values.get("asset_model_id")
        assert result is not None, "Required property 'asset_model_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Asset.AssetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetname
        '''
        result = self._values.get("asset_name")
        assert result is not None, "Required property 'asset_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_hierarchies(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAsset.AssetHierarchyProperty]]]]:
        '''``AWS::IoTSiteWise::Asset.AssetHierarchies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assethierarchies
        '''
        result = self._values.get("asset_hierarchies")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAsset.AssetHierarchyProperty]]]], result)

    @builtins.property
    def asset_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAsset.AssetPropertyProperty]]]]:
        '''``AWS::IoTSiteWise::Asset.AssetProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetproperties
        '''
        result = self._values.get("asset_properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAsset.AssetPropertyProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTSiteWise::Asset.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDashboard(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotsitewise.CfnDashboard",
):
    '''A CloudFormation ``AWS::IoTSiteWise::Dashboard``.

    :cloudformationResource: AWS::IoTSiteWise::Dashboard
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        dashboard_definition: builtins.str,
        dashboard_description: builtins.str,
        dashboard_name: builtins.str,
        project_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTSiteWise::Dashboard``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dashboard_definition: ``AWS::IoTSiteWise::Dashboard.DashboardDefinition``.
        :param dashboard_description: ``AWS::IoTSiteWise::Dashboard.DashboardDescription``.
        :param dashboard_name: ``AWS::IoTSiteWise::Dashboard.DashboardName``.
        :param project_id: ``AWS::IoTSiteWise::Dashboard.ProjectId``.
        :param tags: ``AWS::IoTSiteWise::Dashboard.Tags``.
        '''
        props = CfnDashboardProps(
            dashboard_definition=dashboard_definition,
            dashboard_description=dashboard_description,
            dashboard_name=dashboard_name,
            project_id=project_id,
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
    @jsii.member(jsii_name="attrDashboardArn")
    def attr_dashboard_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: DashboardArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDashboardArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDashboardId")
    def attr_dashboard_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DashboardId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDashboardId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTSiteWise::Dashboard.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dashboardDefinition")
    def dashboard_definition(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Dashboard.DashboardDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboarddefinition
        '''
        return typing.cast(builtins.str, jsii.get(self, "dashboardDefinition"))

    @dashboard_definition.setter
    def dashboard_definition(self, value: builtins.str) -> None:
        jsii.set(self, "dashboardDefinition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dashboardDescription")
    def dashboard_description(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Dashboard.DashboardDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboarddescription
        '''
        return typing.cast(builtins.str, jsii.get(self, "dashboardDescription"))

    @dashboard_description.setter
    def dashboard_description(self, value: builtins.str) -> None:
        jsii.set(self, "dashboardDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dashboardName")
    def dashboard_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Dashboard.DashboardName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboardname
        '''
        return typing.cast(builtins.str, jsii.get(self, "dashboardName"))

    @dashboard_name.setter
    def dashboard_name(self, value: builtins.str) -> None:
        jsii.set(self, "dashboardName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Dashboard.ProjectId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-projectid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "projectId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotsitewise.CfnDashboardProps",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_definition": "dashboardDefinition",
        "dashboard_description": "dashboardDescription",
        "dashboard_name": "dashboardName",
        "project_id": "projectId",
        "tags": "tags",
    },
)
class CfnDashboardProps:
    def __init__(
        self,
        *,
        dashboard_definition: builtins.str,
        dashboard_description: builtins.str,
        dashboard_name: builtins.str,
        project_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTSiteWise::Dashboard``.

        :param dashboard_definition: ``AWS::IoTSiteWise::Dashboard.DashboardDefinition``.
        :param dashboard_description: ``AWS::IoTSiteWise::Dashboard.DashboardDescription``.
        :param dashboard_name: ``AWS::IoTSiteWise::Dashboard.DashboardName``.
        :param project_id: ``AWS::IoTSiteWise::Dashboard.ProjectId``.
        :param tags: ``AWS::IoTSiteWise::Dashboard.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dashboard_definition": dashboard_definition,
            "dashboard_description": dashboard_description,
            "dashboard_name": dashboard_name,
        }
        if project_id is not None:
            self._values["project_id"] = project_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dashboard_definition(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Dashboard.DashboardDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboarddefinition
        '''
        result = self._values.get("dashboard_definition")
        assert result is not None, "Required property 'dashboard_definition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_description(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Dashboard.DashboardDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboarddescription
        '''
        result = self._values.get("dashboard_description")
        assert result is not None, "Required property 'dashboard_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Dashboard.DashboardName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboardname
        '''
        result = self._values.get("dashboard_name")
        assert result is not None, "Required property 'dashboard_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Dashboard.ProjectId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-projectid
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTSiteWise::Dashboard.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnGateway(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotsitewise.CfnGateway",
):
    '''A CloudFormation ``AWS::IoTSiteWise::Gateway``.

    :cloudformationResource: AWS::IoTSiteWise::Gateway
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        gateway_name: builtins.str,
        gateway_platform: typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GatewayPlatformProperty"],
        gateway_capability_summaries: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GatewayCapabilitySummaryProperty"]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTSiteWise::Gateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param gateway_name: ``AWS::IoTSiteWise::Gateway.GatewayName``.
        :param gateway_platform: ``AWS::IoTSiteWise::Gateway.GatewayPlatform``.
        :param gateway_capability_summaries: ``AWS::IoTSiteWise::Gateway.GatewayCapabilitySummaries``.
        :param tags: ``AWS::IoTSiteWise::Gateway.Tags``.
        '''
        props = CfnGatewayProps(
            gateway_name=gateway_name,
            gateway_platform=gateway_platform,
            gateway_capability_summaries=gateway_capability_summaries,
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
    @jsii.member(jsii_name="attrGatewayId")
    def attr_gateway_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: GatewayId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTSiteWise::Gateway.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayName")
    def gateway_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Gateway.GatewayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayname
        '''
        return typing.cast(builtins.str, jsii.get(self, "gatewayName"))

    @gateway_name.setter
    def gateway_name(self, value: builtins.str) -> None:
        jsii.set(self, "gatewayName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayPlatform")
    def gateway_platform(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GatewayPlatformProperty"]:
        '''``AWS::IoTSiteWise::Gateway.GatewayPlatform``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayplatform
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GatewayPlatformProperty"], jsii.get(self, "gatewayPlatform"))

    @gateway_platform.setter
    def gateway_platform(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GatewayPlatformProperty"],
    ) -> None:
        jsii.set(self, "gatewayPlatform", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gatewayCapabilitySummaries")
    def gateway_capability_summaries(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GatewayCapabilitySummaryProperty"]]]]:
        '''``AWS::IoTSiteWise::Gateway.GatewayCapabilitySummaries``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewaycapabilitysummaries
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GatewayCapabilitySummaryProperty"]]]], jsii.get(self, "gatewayCapabilitySummaries"))

    @gateway_capability_summaries.setter
    def gateway_capability_summaries(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GatewayCapabilitySummaryProperty"]]]],
    ) -> None:
        jsii.set(self, "gatewayCapabilitySummaries", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnGateway.GatewayCapabilitySummaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capability_namespace": "capabilityNamespace",
            "capability_configuration": "capabilityConfiguration",
        },
    )
    class GatewayCapabilitySummaryProperty:
        def __init__(
            self,
            *,
            capability_namespace: builtins.str,
            capability_configuration: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param capability_namespace: ``CfnGateway.GatewayCapabilitySummaryProperty.CapabilityNamespace``.
            :param capability_configuration: ``CfnGateway.GatewayCapabilitySummaryProperty.CapabilityConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "capability_namespace": capability_namespace,
            }
            if capability_configuration is not None:
                self._values["capability_configuration"] = capability_configuration

        @builtins.property
        def capability_namespace(self) -> builtins.str:
            '''``CfnGateway.GatewayCapabilitySummaryProperty.CapabilityNamespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html#cfn-iotsitewise-gateway-gatewaycapabilitysummary-capabilitynamespace
            '''
            result = self._values.get("capability_namespace")
            assert result is not None, "Required property 'capability_namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def capability_configuration(self) -> typing.Optional[builtins.str]:
            '''``CfnGateway.GatewayCapabilitySummaryProperty.CapabilityConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html#cfn-iotsitewise-gateway-gatewaycapabilitysummary-capabilityconfiguration
            '''
            result = self._values.get("capability_configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayCapabilitySummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnGateway.GatewayPlatformProperty",
        jsii_struct_bases=[],
        name_mapping={"greengrass": "greengrass"},
    )
    class GatewayPlatformProperty:
        def __init__(
            self,
            *,
            greengrass: typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GreengrassProperty"],
        ) -> None:
            '''
            :param greengrass: ``CfnGateway.GatewayPlatformProperty.Greengrass``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "greengrass": greengrass,
            }

        @builtins.property
        def greengrass(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GreengrassProperty"]:
            '''``CfnGateway.GatewayPlatformProperty.Greengrass``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html#cfn-iotsitewise-gateway-gatewayplatform-greengrass
            '''
            result = self._values.get("greengrass")
            assert result is not None, "Required property 'greengrass' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnGateway.GreengrassProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayPlatformProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotsitewise.CfnGateway.GreengrassProperty",
        jsii_struct_bases=[],
        name_mapping={"group_arn": "groupArn"},
    )
    class GreengrassProperty:
        def __init__(self, *, group_arn: builtins.str) -> None:
            '''
            :param group_arn: ``CfnGateway.GreengrassProperty.GroupArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrass.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "group_arn": group_arn,
            }

        @builtins.property
        def group_arn(self) -> builtins.str:
            '''``CfnGateway.GreengrassProperty.GroupArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrass.html#cfn-iotsitewise-gateway-greengrass-grouparn
            '''
            result = self._values.get("group_arn")
            assert result is not None, "Required property 'group_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GreengrassProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotsitewise.CfnGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_name": "gatewayName",
        "gateway_platform": "gatewayPlatform",
        "gateway_capability_summaries": "gatewayCapabilitySummaries",
        "tags": "tags",
    },
)
class CfnGatewayProps:
    def __init__(
        self,
        *,
        gateway_name: builtins.str,
        gateway_platform: typing.Union[aws_cdk.core.IResolvable, CfnGateway.GatewayPlatformProperty],
        gateway_capability_summaries: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnGateway.GatewayCapabilitySummaryProperty]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTSiteWise::Gateway``.

        :param gateway_name: ``AWS::IoTSiteWise::Gateway.GatewayName``.
        :param gateway_platform: ``AWS::IoTSiteWise::Gateway.GatewayPlatform``.
        :param gateway_capability_summaries: ``AWS::IoTSiteWise::Gateway.GatewayCapabilitySummaries``.
        :param tags: ``AWS::IoTSiteWise::Gateway.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "gateway_name": gateway_name,
            "gateway_platform": gateway_platform,
        }
        if gateway_capability_summaries is not None:
            self._values["gateway_capability_summaries"] = gateway_capability_summaries
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def gateway_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Gateway.GatewayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayname
        '''
        result = self._values.get("gateway_name")
        assert result is not None, "Required property 'gateway_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gateway_platform(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnGateway.GatewayPlatformProperty]:
        '''``AWS::IoTSiteWise::Gateway.GatewayPlatform``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayplatform
        '''
        result = self._values.get("gateway_platform")
        assert result is not None, "Required property 'gateway_platform' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnGateway.GatewayPlatformProperty], result)

    @builtins.property
    def gateway_capability_summaries(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnGateway.GatewayCapabilitySummaryProperty]]]]:
        '''``AWS::IoTSiteWise::Gateway.GatewayCapabilitySummaries``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewaycapabilitysummaries
        '''
        result = self._values.get("gateway_capability_summaries")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnGateway.GatewayCapabilitySummaryProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTSiteWise::Gateway.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPortal(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotsitewise.CfnPortal",
):
    '''A CloudFormation ``AWS::IoTSiteWise::Portal``.

    :cloudformationResource: AWS::IoTSiteWise::Portal
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        portal_contact_email: builtins.str,
        portal_name: builtins.str,
        role_arn: builtins.str,
        alarms: typing.Any = None,
        notification_sender_email: typing.Optional[builtins.str] = None,
        portal_auth_mode: typing.Optional[builtins.str] = None,
        portal_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTSiteWise::Portal``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portal_contact_email: ``AWS::IoTSiteWise::Portal.PortalContactEmail``.
        :param portal_name: ``AWS::IoTSiteWise::Portal.PortalName``.
        :param role_arn: ``AWS::IoTSiteWise::Portal.RoleArn``.
        :param alarms: ``AWS::IoTSiteWise::Portal.Alarms``.
        :param notification_sender_email: ``AWS::IoTSiteWise::Portal.NotificationSenderEmail``.
        :param portal_auth_mode: ``AWS::IoTSiteWise::Portal.PortalAuthMode``.
        :param portal_description: ``AWS::IoTSiteWise::Portal.PortalDescription``.
        :param tags: ``AWS::IoTSiteWise::Portal.Tags``.
        '''
        props = CfnPortalProps(
            portal_contact_email=portal_contact_email,
            portal_name=portal_name,
            role_arn=role_arn,
            alarms=alarms,
            notification_sender_email=notification_sender_email,
            portal_auth_mode=portal_auth_mode,
            portal_description=portal_description,
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
    @jsii.member(jsii_name="attrPortalArn")
    def attr_portal_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: PortalArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPortalClientId")
    def attr_portal_client_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: PortalClientId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalClientId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPortalId")
    def attr_portal_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: PortalId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPortalStartUrl")
    def attr_portal_start_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: PortalStartUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalStartUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTSiteWise::Portal.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarms")
    def alarms(self) -> typing.Any:
        '''``AWS::IoTSiteWise::Portal.Alarms``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-alarms
        '''
        return typing.cast(typing.Any, jsii.get(self, "alarms"))

    @alarms.setter
    def alarms(self, value: typing.Any) -> None:
        jsii.set(self, "alarms", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portalContactEmail")
    def portal_contact_email(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Portal.PortalContactEmail``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalcontactemail
        '''
        return typing.cast(builtins.str, jsii.get(self, "portalContactEmail"))

    @portal_contact_email.setter
    def portal_contact_email(self, value: builtins.str) -> None:
        jsii.set(self, "portalContactEmail", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portalName")
    def portal_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Portal.PortalName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalname
        '''
        return typing.cast(builtins.str, jsii.get(self, "portalName"))

    @portal_name.setter
    def portal_name(self, value: builtins.str) -> None:
        jsii.set(self, "portalName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Portal.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationSenderEmail")
    def notification_sender_email(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Portal.NotificationSenderEmail``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-notificationsenderemail
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationSenderEmail"))

    @notification_sender_email.setter
    def notification_sender_email(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "notificationSenderEmail", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portalAuthMode")
    def portal_auth_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Portal.PortalAuthMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalauthmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portalAuthMode"))

    @portal_auth_mode.setter
    def portal_auth_mode(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "portalAuthMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portalDescription")
    def portal_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Portal.PortalDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portaldescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portalDescription"))

    @portal_description.setter
    def portal_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "portalDescription", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotsitewise.CfnPortalProps",
    jsii_struct_bases=[],
    name_mapping={
        "portal_contact_email": "portalContactEmail",
        "portal_name": "portalName",
        "role_arn": "roleArn",
        "alarms": "alarms",
        "notification_sender_email": "notificationSenderEmail",
        "portal_auth_mode": "portalAuthMode",
        "portal_description": "portalDescription",
        "tags": "tags",
    },
)
class CfnPortalProps:
    def __init__(
        self,
        *,
        portal_contact_email: builtins.str,
        portal_name: builtins.str,
        role_arn: builtins.str,
        alarms: typing.Any = None,
        notification_sender_email: typing.Optional[builtins.str] = None,
        portal_auth_mode: typing.Optional[builtins.str] = None,
        portal_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTSiteWise::Portal``.

        :param portal_contact_email: ``AWS::IoTSiteWise::Portal.PortalContactEmail``.
        :param portal_name: ``AWS::IoTSiteWise::Portal.PortalName``.
        :param role_arn: ``AWS::IoTSiteWise::Portal.RoleArn``.
        :param alarms: ``AWS::IoTSiteWise::Portal.Alarms``.
        :param notification_sender_email: ``AWS::IoTSiteWise::Portal.NotificationSenderEmail``.
        :param portal_auth_mode: ``AWS::IoTSiteWise::Portal.PortalAuthMode``.
        :param portal_description: ``AWS::IoTSiteWise::Portal.PortalDescription``.
        :param tags: ``AWS::IoTSiteWise::Portal.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "portal_contact_email": portal_contact_email,
            "portal_name": portal_name,
            "role_arn": role_arn,
        }
        if alarms is not None:
            self._values["alarms"] = alarms
        if notification_sender_email is not None:
            self._values["notification_sender_email"] = notification_sender_email
        if portal_auth_mode is not None:
            self._values["portal_auth_mode"] = portal_auth_mode
        if portal_description is not None:
            self._values["portal_description"] = portal_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def portal_contact_email(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Portal.PortalContactEmail``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalcontactemail
        '''
        result = self._values.get("portal_contact_email")
        assert result is not None, "Required property 'portal_contact_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def portal_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Portal.PortalName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalname
        '''
        result = self._values.get("portal_name")
        assert result is not None, "Required property 'portal_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Portal.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarms(self) -> typing.Any:
        '''``AWS::IoTSiteWise::Portal.Alarms``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-alarms
        '''
        result = self._values.get("alarms")
        return typing.cast(typing.Any, result)

    @builtins.property
    def notification_sender_email(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Portal.NotificationSenderEmail``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-notificationsenderemail
        '''
        result = self._values.get("notification_sender_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def portal_auth_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Portal.PortalAuthMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalauthmode
        '''
        result = self._values.get("portal_auth_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def portal_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Portal.PortalDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portaldescription
        '''
        result = self._values.get("portal_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTSiteWise::Portal.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortalProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnProject(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotsitewise.CfnProject",
):
    '''A CloudFormation ``AWS::IoTSiteWise::Project``.

    :cloudformationResource: AWS::IoTSiteWise::Project
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        portal_id: builtins.str,
        project_name: builtins.str,
        project_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTSiteWise::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portal_id: ``AWS::IoTSiteWise::Project.PortalId``.
        :param project_name: ``AWS::IoTSiteWise::Project.ProjectName``.
        :param project_description: ``AWS::IoTSiteWise::Project.ProjectDescription``.
        :param tags: ``AWS::IoTSiteWise::Project.Tags``.
        '''
        props = CfnProjectProps(
            portal_id=portal_id,
            project_name=project_name,
            project_description=project_description,
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
    @jsii.member(jsii_name="attrProjectArn")
    def attr_project_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTSiteWise::Project.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portalId")
    def portal_id(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Project.PortalId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-portalid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portalId"))

    @portal_id.setter
    def portal_id(self, value: builtins.str) -> None:
        jsii.set(self, "portalId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Project.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-projectname
        '''
        return typing.cast(builtins.str, jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: builtins.str) -> None:
        jsii.set(self, "projectName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectDescription")
    def project_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Project.ProjectDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-projectdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectDescription"))

    @project_description.setter
    def project_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "projectDescription", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotsitewise.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "portal_id": "portalId",
        "project_name": "projectName",
        "project_description": "projectDescription",
        "tags": "tags",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        portal_id: builtins.str,
        project_name: builtins.str,
        project_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTSiteWise::Project``.

        :param portal_id: ``AWS::IoTSiteWise::Project.PortalId``.
        :param project_name: ``AWS::IoTSiteWise::Project.ProjectName``.
        :param project_description: ``AWS::IoTSiteWise::Project.ProjectDescription``.
        :param tags: ``AWS::IoTSiteWise::Project.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "portal_id": portal_id,
            "project_name": project_name,
        }
        if project_description is not None:
            self._values["project_description"] = project_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def portal_id(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Project.PortalId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-portalid
        '''
        result = self._values.get("portal_id")
        assert result is not None, "Required property 'portal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_name(self) -> builtins.str:
        '''``AWS::IoTSiteWise::Project.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-projectname
        '''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTSiteWise::Project.ProjectDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-projectdescription
        '''
        result = self._values.get("project_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTSiteWise::Project.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessPolicy",
    "CfnAccessPolicyProps",
    "CfnAsset",
    "CfnAssetModel",
    "CfnAssetModelProps",
    "CfnAssetProps",
    "CfnDashboard",
    "CfnDashboardProps",
    "CfnGateway",
    "CfnGatewayProps",
    "CfnPortal",
    "CfnPortalProps",
    "CfnProject",
    "CfnProjectProps",
]

publication.publish()
