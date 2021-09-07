'''
# AWS::IoTFleetHub Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iotfleethub as iotfleethub
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
class CfnApplication(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotfleethub.CfnApplication",
):
    '''A CloudFormation ``AWS::IoTFleetHub::Application``.

    :cloudformationResource: AWS::IoTFleetHub::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        role_arn: builtins.str,
        application_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetHub::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: ``AWS::IoTFleetHub::Application.ApplicationName``.
        :param role_arn: ``AWS::IoTFleetHub::Application.RoleArn``.
        :param application_description: ``AWS::IoTFleetHub::Application.ApplicationDescription``.
        :param tags: ``AWS::IoTFleetHub::Application.Tags``.
        '''
        props = CfnApplicationProps(
            application_name=application_name,
            role_arn=role_arn,
            application_description=application_description,
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
    @jsii.member(jsii_name="attrApplicationArn")
    def attr_application_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrApplicationCreationDate")
    def attr_application_creation_date(self) -> jsii.Number:
        '''
        :cloudformationAttribute: ApplicationCreationDate
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrApplicationCreationDate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrApplicationId")
    def attr_application_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApplicationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrApplicationLastUpdateDate")
    def attr_application_last_update_date(self) -> jsii.Number:
        '''
        :cloudformationAttribute: ApplicationLastUpdateDate
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrApplicationLastUpdateDate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrApplicationState")
    def attr_application_state(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApplicationState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrApplicationUrl")
    def attr_application_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApplicationUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrErrorMessage")
    def attr_error_message(self) -> builtins.str:
        '''
        :cloudformationAttribute: ErrorMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrErrorMessage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSsoClientId")
    def attr_sso_client_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SsoClientId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSsoClientId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::IoTFleetHub::Application.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''``AWS::IoTFleetHub::Application.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        jsii.set(self, "applicationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::IoTFleetHub::Application.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationDescription")
    def application_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetHub::Application.ApplicationDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-applicationdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationDescription"))

    @application_description.setter
    def application_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "applicationDescription", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotfleethub.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "role_arn": "roleArn",
        "application_description": "applicationDescription",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        role_arn: builtins.str,
        application_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTFleetHub::Application``.

        :param application_name: ``AWS::IoTFleetHub::Application.ApplicationName``.
        :param role_arn: ``AWS::IoTFleetHub::Application.RoleArn``.
        :param application_description: ``AWS::IoTFleetHub::Application.ApplicationDescription``.
        :param tags: ``AWS::IoTFleetHub::Application.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_name": application_name,
            "role_arn": role_arn,
        }
        if application_description is not None:
            self._values["application_description"] = application_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_name(self) -> builtins.str:
        '''``AWS::IoTFleetHub::Application.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::IoTFleetHub::Application.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetHub::Application.ApplicationDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-applicationdescription
        '''
        result = self._values.get("application_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTFleetHub::Application.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
]

publication.publish()
