'''
# AWS::FIS Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_fis as fis
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
class CfnExperimentTemplate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-fis.CfnExperimentTemplate",
):
    '''A CloudFormation ``AWS::FIS::ExperimentTemplate``.

    :cloudformationResource: AWS::FIS::ExperimentTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        role_arn: builtins.str,
        stop_conditions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnExperimentTemplate.ExperimentTemplateStopConditionProperty", aws_cdk.core.IResolvable]]],
        tags: typing.Mapping[builtins.str, builtins.str],
        targets: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateTargetProperty"]]],
        actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateActionProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::FIS::ExperimentTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::FIS::ExperimentTemplate.Description``.
        :param role_arn: ``AWS::FIS::ExperimentTemplate.RoleArn``.
        :param stop_conditions: ``AWS::FIS::ExperimentTemplate.StopConditions``.
        :param tags: ``AWS::FIS::ExperimentTemplate.Tags``.
        :param targets: ``AWS::FIS::ExperimentTemplate.Targets``.
        :param actions: ``AWS::FIS::ExperimentTemplate.Actions``.
        '''
        props = CfnExperimentTemplateProps(
            description=description,
            role_arn=role_arn,
            stop_conditions=stop_conditions,
            tags=tags,
            targets=targets,
            actions=actions,
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::FIS::ExperimentTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''``AWS::FIS::ExperimentTemplate.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::FIS::ExperimentTemplate.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stopConditions")
    def stop_conditions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnExperimentTemplate.ExperimentTemplateStopConditionProperty", aws_cdk.core.IResolvable]]]:
        '''``AWS::FIS::ExperimentTemplate.StopConditions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-stopconditions
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnExperimentTemplate.ExperimentTemplateStopConditionProperty", aws_cdk.core.IResolvable]]], jsii.get(self, "stopConditions"))

    @stop_conditions.setter
    def stop_conditions(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnExperimentTemplate.ExperimentTemplateStopConditionProperty", aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "stopConditions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateTargetProperty"]]]:
        '''``AWS::FIS::ExperimentTemplate.Targets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-targets
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateTargetProperty"]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateTargetProperty"]]],
    ) -> None:
        jsii.set(self, "targets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateActionProperty"]]]]:
        '''``AWS::FIS::ExperimentTemplate.Actions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-actions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateActionProperty"]]]], jsii.get(self, "actions"))

    @actions.setter
    def actions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateActionProperty"]]]],
    ) -> None:
        jsii.set(self, "actions", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-fis.CfnExperimentTemplate.ExperimentTemplateActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_id": "actionId",
            "description": "description",
            "parameters": "parameters",
            "start_after": "startAfter",
            "targets": "targets",
        },
    )
    class ExperimentTemplateActionProperty:
        def __init__(
            self,
            *,
            action_id: builtins.str,
            description: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            start_after: typing.Optional[typing.Sequence[builtins.str]] = None,
            targets: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''
            :param action_id: ``CfnExperimentTemplate.ExperimentTemplateActionProperty.ActionId``.
            :param description: ``CfnExperimentTemplate.ExperimentTemplateActionProperty.Description``.
            :param parameters: ``CfnExperimentTemplate.ExperimentTemplateActionProperty.Parameters``.
            :param start_after: ``CfnExperimentTemplate.ExperimentTemplateActionProperty.StartAfter``.
            :param targets: ``CfnExperimentTemplate.ExperimentTemplateActionProperty.Targets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action_id": action_id,
            }
            if description is not None:
                self._values["description"] = description
            if parameters is not None:
                self._values["parameters"] = parameters
            if start_after is not None:
                self._values["start_after"] = start_after
            if targets is not None:
                self._values["targets"] = targets

        @builtins.property
        def action_id(self) -> builtins.str:
            '''``CfnExperimentTemplate.ExperimentTemplateActionProperty.ActionId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-actionid
            '''
            result = self._values.get("action_id")
            assert result is not None, "Required property 'action_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnExperimentTemplate.ExperimentTemplateActionProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnExperimentTemplate.ExperimentTemplateActionProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def start_after(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnExperimentTemplate.ExperimentTemplateActionProperty.StartAfter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-startafter
            '''
            result = self._values.get("start_after")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def targets(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnExperimentTemplate.ExperimentTemplateActionProperty.Targets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-targets
            '''
            result = self._values.get("targets")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExperimentTemplateActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-fis.CfnExperimentTemplate.ExperimentTemplateStopConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source", "value": "value"},
    )
    class ExperimentTemplateStopConditionProperty:
        def __init__(
            self,
            *,
            source: builtins.str,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param source: ``CfnExperimentTemplate.ExperimentTemplateStopConditionProperty.Source``.
            :param value: ``CfnExperimentTemplate.ExperimentTemplateStopConditionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "source": source,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def source(self) -> builtins.str:
            '''``CfnExperimentTemplate.ExperimentTemplateStopConditionProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html#cfn-fis-experimenttemplate-experimenttemplatestopcondition-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnExperimentTemplate.ExperimentTemplateStopConditionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html#cfn-fis-experimenttemplate-experimenttemplatestopcondition-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExperimentTemplateStopConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-fis.CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path", "values": "values"},
    )
    class ExperimentTemplateTargetFilterProperty:
        def __init__(
            self,
            *,
            path: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param path: ``CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty.Path``.
            :param values: ``CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "path": path,
                "values": values,
            }

        @builtins.property
        def path(self) -> builtins.str:
            '''``CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''``CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExperimentTemplateTargetFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-fis.CfnExperimentTemplate.ExperimentTemplateTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_type": "resourceType",
            "selection_mode": "selectionMode",
            "filters": "filters",
            "resource_arns": "resourceArns",
            "resource_tags": "resourceTags",
        },
    )
    class ExperimentTemplateTargetProperty:
        def __init__(
            self,
            *,
            resource_type: builtins.str,
            selection_mode: builtins.str,
            filters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty"]]]] = None,
            resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_tags: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''
            :param resource_type: ``CfnExperimentTemplate.ExperimentTemplateTargetProperty.ResourceType``.
            :param selection_mode: ``CfnExperimentTemplate.ExperimentTemplateTargetProperty.SelectionMode``.
            :param filters: ``CfnExperimentTemplate.ExperimentTemplateTargetProperty.Filters``.
            :param resource_arns: ``CfnExperimentTemplate.ExperimentTemplateTargetProperty.ResourceArns``.
            :param resource_tags: ``CfnExperimentTemplate.ExperimentTemplateTargetProperty.ResourceTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "resource_type": resource_type,
                "selection_mode": selection_mode,
            }
            if filters is not None:
                self._values["filters"] = filters
            if resource_arns is not None:
                self._values["resource_arns"] = resource_arns
            if resource_tags is not None:
                self._values["resource_tags"] = resource_tags

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''``CfnExperimentTemplate.ExperimentTemplateTargetProperty.ResourceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def selection_mode(self) -> builtins.str:
            '''``CfnExperimentTemplate.ExperimentTemplateTargetProperty.SelectionMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-selectionmode
            '''
            result = self._values.get("selection_mode")
            assert result is not None, "Required property 'selection_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def filters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty"]]]]:
            '''``CfnExperimentTemplate.ExperimentTemplateTargetProperty.Filters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty"]]]], result)

        @builtins.property
        def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnExperimentTemplate.ExperimentTemplateTargetProperty.ResourceArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcearns
            '''
            result = self._values.get("resource_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_tags(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnExperimentTemplate.ExperimentTemplateTargetProperty.ResourceTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetags
            '''
            result = self._values.get("resource_tags")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExperimentTemplateTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-fis.CfnExperimentTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "role_arn": "roleArn",
        "stop_conditions": "stopConditions",
        "tags": "tags",
        "targets": "targets",
        "actions": "actions",
    },
)
class CfnExperimentTemplateProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        role_arn: builtins.str,
        stop_conditions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnExperimentTemplate.ExperimentTemplateStopConditionProperty, aws_cdk.core.IResolvable]]],
        tags: typing.Mapping[builtins.str, builtins.str],
        targets: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnExperimentTemplate.ExperimentTemplateTargetProperty]]],
        actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnExperimentTemplate.ExperimentTemplateActionProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::FIS::ExperimentTemplate``.

        :param description: ``AWS::FIS::ExperimentTemplate.Description``.
        :param role_arn: ``AWS::FIS::ExperimentTemplate.RoleArn``.
        :param stop_conditions: ``AWS::FIS::ExperimentTemplate.StopConditions``.
        :param tags: ``AWS::FIS::ExperimentTemplate.Tags``.
        :param targets: ``AWS::FIS::ExperimentTemplate.Targets``.
        :param actions: ``AWS::FIS::ExperimentTemplate.Actions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "role_arn": role_arn,
            "stop_conditions": stop_conditions,
            "tags": tags,
            "targets": targets,
        }
        if actions is not None:
            self._values["actions"] = actions

    @builtins.property
    def description(self) -> builtins.str:
        '''``AWS::FIS::ExperimentTemplate.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::FIS::ExperimentTemplate.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stop_conditions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnExperimentTemplate.ExperimentTemplateStopConditionProperty, aws_cdk.core.IResolvable]]]:
        '''``AWS::FIS::ExperimentTemplate.StopConditions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-stopconditions
        '''
        result = self._values.get("stop_conditions")
        assert result is not None, "Required property 'stop_conditions' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnExperimentTemplate.ExperimentTemplateStopConditionProperty, aws_cdk.core.IResolvable]]], result)

    @builtins.property
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''``AWS::FIS::ExperimentTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-tags
        '''
        result = self._values.get("tags")
        assert result is not None, "Required property 'tags' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnExperimentTemplate.ExperimentTemplateTargetProperty]]]:
        '''``AWS::FIS::ExperimentTemplate.Targets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-targets
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnExperimentTemplate.ExperimentTemplateTargetProperty]]], result)

    @builtins.property
    def actions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnExperimentTemplate.ExperimentTemplateActionProperty]]]]:
        '''``AWS::FIS::ExperimentTemplate.Actions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-actions
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnExperimentTemplate.ExperimentTemplateActionProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExperimentTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnExperimentTemplate",
    "CfnExperimentTemplateProps",
]

publication.publish()
