'''
# AWS::Route53RecoveryReadiness Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_route53recoveryreadiness as route53recoveryreadiness
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
class CfnCell(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnCell",
):
    '''A CloudFormation ``AWS::Route53RecoveryReadiness::Cell``.

    :cloudformationResource: AWS::Route53RecoveryReadiness::Cell
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cell_name: builtins.str,
        cells: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53RecoveryReadiness::Cell``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cell_name: ``AWS::Route53RecoveryReadiness::Cell.CellName``.
        :param cells: ``AWS::Route53RecoveryReadiness::Cell.Cells``.
        :param tags: ``AWS::Route53RecoveryReadiness::Cell.Tags``.
        '''
        props = CfnCellProps(cell_name=cell_name, cells=cells, tags=tags)

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
    @jsii.member(jsii_name="attrCellArn")
    def attr_cell_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: CellArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCellArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrParentReadinessScopes")
    def attr_parent_readiness_scopes(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: ParentReadinessScopes
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrParentReadinessScopes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Route53RecoveryReadiness::Cell.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cellName")
    def cell_name(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::Cell.CellName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cellname
        '''
        return typing.cast(builtins.str, jsii.get(self, "cellName"))

    @cell_name.setter
    def cell_name(self, value: builtins.str) -> None:
        jsii.set(self, "cellName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cells")
    def cells(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Route53RecoveryReadiness::Cell.Cells``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cells
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cells"))

    @cells.setter
    def cells(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "cells", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnCellProps",
    jsii_struct_bases=[],
    name_mapping={"cell_name": "cellName", "cells": "cells", "tags": "tags"},
)
class CfnCellProps:
    def __init__(
        self,
        *,
        cell_name: builtins.str,
        cells: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53RecoveryReadiness::Cell``.

        :param cell_name: ``AWS::Route53RecoveryReadiness::Cell.CellName``.
        :param cells: ``AWS::Route53RecoveryReadiness::Cell.Cells``.
        :param tags: ``AWS::Route53RecoveryReadiness::Cell.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cell_name": cell_name,
        }
        if cells is not None:
            self._values["cells"] = cells
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cell_name(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::Cell.CellName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cellname
        '''
        result = self._values.get("cell_name")
        assert result is not None, "Required property 'cell_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cells(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Route53RecoveryReadiness::Cell.Cells``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cells
        '''
        result = self._values.get("cells")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Route53RecoveryReadiness::Cell.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCellProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnReadinessCheck(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnReadinessCheck",
):
    '''A CloudFormation ``AWS::Route53RecoveryReadiness::ReadinessCheck``.

    :cloudformationResource: AWS::Route53RecoveryReadiness::ReadinessCheck
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        readiness_check_name: builtins.str,
        resource_set_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53RecoveryReadiness::ReadinessCheck``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param readiness_check_name: ``AWS::Route53RecoveryReadiness::ReadinessCheck.ReadinessCheckName``.
        :param resource_set_name: ``AWS::Route53RecoveryReadiness::ReadinessCheck.ResourceSetName``.
        :param tags: ``AWS::Route53RecoveryReadiness::ReadinessCheck.Tags``.
        '''
        props = CfnReadinessCheckProps(
            readiness_check_name=readiness_check_name,
            resource_set_name=resource_set_name,
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
    @jsii.member(jsii_name="attrReadinessCheckArn")
    def attr_readiness_check_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ReadinessCheckArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReadinessCheckArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Route53RecoveryReadiness::ReadinessCheck.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="readinessCheckName")
    def readiness_check_name(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::ReadinessCheck.ReadinessCheckName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-readinesscheckname
        '''
        return typing.cast(builtins.str, jsii.get(self, "readinessCheckName"))

    @readiness_check_name.setter
    def readiness_check_name(self, value: builtins.str) -> None:
        jsii.set(self, "readinessCheckName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceSetName")
    def resource_set_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryReadiness::ReadinessCheck.ResourceSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-resourcesetname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceSetName"))

    @resource_set_name.setter
    def resource_set_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "resourceSetName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnReadinessCheckProps",
    jsii_struct_bases=[],
    name_mapping={
        "readiness_check_name": "readinessCheckName",
        "resource_set_name": "resourceSetName",
        "tags": "tags",
    },
)
class CfnReadinessCheckProps:
    def __init__(
        self,
        *,
        readiness_check_name: builtins.str,
        resource_set_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53RecoveryReadiness::ReadinessCheck``.

        :param readiness_check_name: ``AWS::Route53RecoveryReadiness::ReadinessCheck.ReadinessCheckName``.
        :param resource_set_name: ``AWS::Route53RecoveryReadiness::ReadinessCheck.ResourceSetName``.
        :param tags: ``AWS::Route53RecoveryReadiness::ReadinessCheck.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "readiness_check_name": readiness_check_name,
        }
        if resource_set_name is not None:
            self._values["resource_set_name"] = resource_set_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def readiness_check_name(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::ReadinessCheck.ReadinessCheckName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-readinesscheckname
        '''
        result = self._values.get("readiness_check_name")
        assert result is not None, "Required property 'readiness_check_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_set_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53RecoveryReadiness::ReadinessCheck.ResourceSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-resourcesetname
        '''
        result = self._values.get("resource_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Route53RecoveryReadiness::ReadinessCheck.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReadinessCheckProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRecoveryGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnRecoveryGroup",
):
    '''A CloudFormation ``AWS::Route53RecoveryReadiness::RecoveryGroup``.

    :cloudformationResource: AWS::Route53RecoveryReadiness::RecoveryGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        recovery_group_name: builtins.str,
        cells: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53RecoveryReadiness::RecoveryGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param recovery_group_name: ``AWS::Route53RecoveryReadiness::RecoveryGroup.RecoveryGroupName``.
        :param cells: ``AWS::Route53RecoveryReadiness::RecoveryGroup.Cells``.
        :param tags: ``AWS::Route53RecoveryReadiness::RecoveryGroup.Tags``.
        '''
        props = CfnRecoveryGroupProps(
            recovery_group_name=recovery_group_name, cells=cells, tags=tags
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
    @jsii.member(jsii_name="attrRecoveryGroupArn")
    def attr_recovery_group_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: RecoveryGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRecoveryGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Route53RecoveryReadiness::RecoveryGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="recoveryGroupName")
    def recovery_group_name(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::RecoveryGroup.RecoveryGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-recoverygroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "recoveryGroupName"))

    @recovery_group_name.setter
    def recovery_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "recoveryGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cells")
    def cells(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Route53RecoveryReadiness::RecoveryGroup.Cells``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-cells
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cells"))

    @cells.setter
    def cells(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "cells", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnRecoveryGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "recovery_group_name": "recoveryGroupName",
        "cells": "cells",
        "tags": "tags",
    },
)
class CfnRecoveryGroupProps:
    def __init__(
        self,
        *,
        recovery_group_name: builtins.str,
        cells: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53RecoveryReadiness::RecoveryGroup``.

        :param recovery_group_name: ``AWS::Route53RecoveryReadiness::RecoveryGroup.RecoveryGroupName``.
        :param cells: ``AWS::Route53RecoveryReadiness::RecoveryGroup.Cells``.
        :param tags: ``AWS::Route53RecoveryReadiness::RecoveryGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "recovery_group_name": recovery_group_name,
        }
        if cells is not None:
            self._values["cells"] = cells
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def recovery_group_name(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::RecoveryGroup.RecoveryGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-recoverygroupname
        '''
        result = self._values.get("recovery_group_name")
        assert result is not None, "Required property 'recovery_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cells(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Route53RecoveryReadiness::RecoveryGroup.Cells``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-cells
        '''
        result = self._values.get("cells")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Route53RecoveryReadiness::RecoveryGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecoveryGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResourceSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnResourceSet",
):
    '''A CloudFormation ``AWS::Route53RecoveryReadiness::ResourceSet``.

    :cloudformationResource: AWS::Route53RecoveryReadiness::ResourceSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resources: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnResourceSet.ResourceProperty", aws_cdk.core.IResolvable]]],
        resource_set_name: builtins.str,
        resource_set_type: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53RecoveryReadiness::ResourceSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resources: ``AWS::Route53RecoveryReadiness::ResourceSet.Resources``.
        :param resource_set_name: ``AWS::Route53RecoveryReadiness::ResourceSet.ResourceSetName``.
        :param resource_set_type: ``AWS::Route53RecoveryReadiness::ResourceSet.ResourceSetType``.
        :param tags: ``AWS::Route53RecoveryReadiness::ResourceSet.Tags``.
        '''
        props = CfnResourceSetProps(
            resources=resources,
            resource_set_name=resource_set_name,
            resource_set_type=resource_set_type,
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
    @jsii.member(jsii_name="attrResourceSetArn")
    def attr_resource_set_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResourceSetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceSetArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Route53RecoveryReadiness::ResourceSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resources")
    def resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnResourceSet.ResourceProperty", aws_cdk.core.IResolvable]]]:
        '''``AWS::Route53RecoveryReadiness::ResourceSet.Resources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resources
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnResourceSet.ResourceProperty", aws_cdk.core.IResolvable]]], jsii.get(self, "resources"))

    @resources.setter
    def resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnResourceSet.ResourceProperty", aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "resources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceSetName")
    def resource_set_name(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::ResourceSet.ResourceSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceSetName"))

    @resource_set_name.setter
    def resource_set_name(self, value: builtins.str) -> None:
        jsii.set(self, "resourceSetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceSetType")
    def resource_set_type(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::ResourceSet.ResourceSetType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceSetType"))

    @resource_set_type.setter
    def resource_set_type(self, value: builtins.str) -> None:
        jsii.set(self, "resourceSetType", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnResourceSet.DNSTargetResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "domain_name": "domainName",
            "hosted_zone_arn": "hostedZoneArn",
            "record_set_id": "recordSetId",
            "record_type": "recordType",
            "target_resource": "targetResource",
        },
    )
    class DNSTargetResourceProperty:
        def __init__(
            self,
            *,
            domain_name: typing.Optional[builtins.str] = None,
            hosted_zone_arn: typing.Optional[builtins.str] = None,
            record_set_id: typing.Optional[builtins.str] = None,
            record_type: typing.Optional[builtins.str] = None,
            target_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.TargetResourceProperty"]] = None,
        ) -> None:
            '''
            :param domain_name: ``CfnResourceSet.DNSTargetResourceProperty.DomainName``.
            :param hosted_zone_arn: ``CfnResourceSet.DNSTargetResourceProperty.HostedZoneArn``.
            :param record_set_id: ``CfnResourceSet.DNSTargetResourceProperty.RecordSetId``.
            :param record_type: ``CfnResourceSet.DNSTargetResourceProperty.RecordType``.
            :param target_resource: ``CfnResourceSet.DNSTargetResourceProperty.TargetResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if domain_name is not None:
                self._values["domain_name"] = domain_name
            if hosted_zone_arn is not None:
                self._values["hosted_zone_arn"] = hosted_zone_arn
            if record_set_id is not None:
                self._values["record_set_id"] = record_set_id
            if record_type is not None:
                self._values["record_type"] = record_type
            if target_resource is not None:
                self._values["target_resource"] = target_resource

        @builtins.property
        def domain_name(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceSet.DNSTargetResourceProperty.DomainName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-domainname
            '''
            result = self._values.get("domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hosted_zone_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceSet.DNSTargetResourceProperty.HostedZoneArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-hostedzonearn
            '''
            result = self._values.get("hosted_zone_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_set_id(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceSet.DNSTargetResourceProperty.RecordSetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordsetid
            '''
            result = self._values.get("record_set_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_type(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceSet.DNSTargetResourceProperty.RecordType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordtype
            '''
            result = self._values.get("record_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.TargetResourceProperty"]]:
            '''``CfnResourceSet.DNSTargetResourceProperty.TargetResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-targetresource
            '''
            result = self._values.get("target_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.TargetResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DNSTargetResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnResourceSet.NLBResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class NLBResourceProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''
            :param arn: ``CfnResourceSet.NLBResourceProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceSet.NLBResourceProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html#cfn-route53recoveryreadiness-resourceset-nlbresource-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NLBResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnResourceSet.R53ResourceRecordProperty",
        jsii_struct_bases=[],
        name_mapping={"domain_name": "domainName", "record_set_id": "recordSetId"},
    )
    class R53ResourceRecordProperty:
        def __init__(
            self,
            *,
            domain_name: typing.Optional[builtins.str] = None,
            record_set_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param domain_name: ``CfnResourceSet.R53ResourceRecordProperty.DomainName``.
            :param record_set_id: ``CfnResourceSet.R53ResourceRecordProperty.RecordSetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if domain_name is not None:
                self._values["domain_name"] = domain_name
            if record_set_id is not None:
                self._values["record_set_id"] = record_set_id

        @builtins.property
        def domain_name(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceSet.R53ResourceRecordProperty.DomainName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-domainname
            '''
            result = self._values.get("domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_set_id(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceSet.R53ResourceRecordProperty.RecordSetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-recordsetid
            '''
            result = self._values.get("record_set_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "R53ResourceRecordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnResourceSet.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_id": "componentId",
            "dns_target_resource": "dnsTargetResource",
            "readiness_scopes": "readinessScopes",
            "resource_arn": "resourceArn",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            component_id: typing.Optional[builtins.str] = None,
            dns_target_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.DNSTargetResourceProperty"]] = None,
            readiness_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param component_id: ``CfnResourceSet.ResourceProperty.ComponentId``.
            :param dns_target_resource: ``CfnResourceSet.ResourceProperty.DnsTargetResource``.
            :param readiness_scopes: ``CfnResourceSet.ResourceProperty.ReadinessScopes``.
            :param resource_arn: ``CfnResourceSet.ResourceProperty.ResourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if component_id is not None:
                self._values["component_id"] = component_id
            if dns_target_resource is not None:
                self._values["dns_target_resource"] = dns_target_resource
            if readiness_scopes is not None:
                self._values["readiness_scopes"] = readiness_scopes
            if resource_arn is not None:
                self._values["resource_arn"] = resource_arn

        @builtins.property
        def component_id(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceSet.ResourceProperty.ComponentId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-componentid
            '''
            result = self._values.get("component_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dns_target_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.DNSTargetResourceProperty"]]:
            '''``CfnResourceSet.ResourceProperty.DnsTargetResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-dnstargetresource
            '''
            result = self._values.get("dns_target_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.DNSTargetResourceProperty"]], result)

        @builtins.property
        def readiness_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnResourceSet.ResourceProperty.ReadinessScopes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-readinessscopes
            '''
            result = self._values.get("readiness_scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceSet.ResourceProperty.ResourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-resourcearn
            '''
            result = self._values.get("resource_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnResourceSet.TargetResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"nlb_resource": "nlbResource", "r53_resource": "r53Resource"},
    )
    class TargetResourceProperty:
        def __init__(
            self,
            *,
            nlb_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.NLBResourceProperty"]] = None,
            r53_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.R53ResourceRecordProperty"]] = None,
        ) -> None:
            '''
            :param nlb_resource: ``CfnResourceSet.TargetResourceProperty.NLBResource``.
            :param r53_resource: ``CfnResourceSet.TargetResourceProperty.R53Resource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if nlb_resource is not None:
                self._values["nlb_resource"] = nlb_resource
            if r53_resource is not None:
                self._values["r53_resource"] = r53_resource

        @builtins.property
        def nlb_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.NLBResourceProperty"]]:
            '''``CfnResourceSet.TargetResourceProperty.NLBResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-nlbresource
            '''
            result = self._values.get("nlb_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.NLBResourceProperty"]], result)

        @builtins.property
        def r53_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.R53ResourceRecordProperty"]]:
            '''``CfnResourceSet.TargetResourceProperty.R53Resource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-r53resource
            '''
            result = self._values.get("r53_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnResourceSet.R53ResourceRecordProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53recoveryreadiness.CfnResourceSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "resources": "resources",
        "resource_set_name": "resourceSetName",
        "resource_set_type": "resourceSetType",
        "tags": "tags",
    },
)
class CfnResourceSetProps:
    def __init__(
        self,
        *,
        resources: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnResourceSet.ResourceProperty, aws_cdk.core.IResolvable]]],
        resource_set_name: builtins.str,
        resource_set_type: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53RecoveryReadiness::ResourceSet``.

        :param resources: ``AWS::Route53RecoveryReadiness::ResourceSet.Resources``.
        :param resource_set_name: ``AWS::Route53RecoveryReadiness::ResourceSet.ResourceSetName``.
        :param resource_set_type: ``AWS::Route53RecoveryReadiness::ResourceSet.ResourceSetType``.
        :param tags: ``AWS::Route53RecoveryReadiness::ResourceSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resources": resources,
            "resource_set_name": resource_set_name,
            "resource_set_type": resource_set_type,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnResourceSet.ResourceProperty, aws_cdk.core.IResolvable]]]:
        '''``AWS::Route53RecoveryReadiness::ResourceSet.Resources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resources
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnResourceSet.ResourceProperty, aws_cdk.core.IResolvable]]], result)

    @builtins.property
    def resource_set_name(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::ResourceSet.ResourceSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesetname
        '''
        result = self._values.get("resource_set_name")
        assert result is not None, "Required property 'resource_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_set_type(self) -> builtins.str:
        '''``AWS::Route53RecoveryReadiness::ResourceSet.ResourceSetType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesettype
        '''
        result = self._values.get("resource_set_type")
        assert result is not None, "Required property 'resource_set_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Route53RecoveryReadiness::ResourceSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCell",
    "CfnCellProps",
    "CfnReadinessCheck",
    "CfnReadinessCheckProps",
    "CfnRecoveryGroup",
    "CfnRecoveryGroupProps",
    "CfnResourceSet",
    "CfnResourceSetProps",
]

publication.publish()
