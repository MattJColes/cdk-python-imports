'''
# AWS::FraudDetector Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_frauddetector as frauddetector
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
class CfnDetector(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-frauddetector.CfnDetector",
):
    '''A CloudFormation ``AWS::FraudDetector::Detector``.

    :cloudformationResource: AWS::FraudDetector::Detector
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        detector_id: builtins.str,
        event_type: typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EventTypeProperty"],
        rules: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.RuleProperty"]]],
        associated_models: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.ModelProperty"]]]] = None,
        description: typing.Optional[builtins.str] = None,
        detector_version_status: typing.Optional[builtins.str] = None,
        rule_execution_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::FraudDetector::Detector``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param detector_id: ``AWS::FraudDetector::Detector.DetectorId``.
        :param event_type: ``AWS::FraudDetector::Detector.EventType``.
        :param rules: ``AWS::FraudDetector::Detector.Rules``.
        :param associated_models: ``AWS::FraudDetector::Detector.AssociatedModels``.
        :param description: ``AWS::FraudDetector::Detector.Description``.
        :param detector_version_status: ``AWS::FraudDetector::Detector.DetectorVersionStatus``.
        :param rule_execution_mode: ``AWS::FraudDetector::Detector.RuleExecutionMode``.
        :param tags: ``AWS::FraudDetector::Detector.Tags``.
        '''
        props = CfnDetectorProps(
            detector_id=detector_id,
            event_type=event_type,
            rules=rules,
            associated_models=associated_models,
            description=description,
            detector_version_status=detector_version_status,
            rule_execution_mode=rule_execution_mode,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDetectorVersionId")
    def attr_detector_version_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DetectorVersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDetectorVersionId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEventTypeArn")
    def attr_event_type_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: EventType.Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventTypeArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEventTypeCreatedTime")
    def attr_event_type_created_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: EventType.CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventTypeCreatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEventTypeLastUpdatedTime")
    def attr_event_type_last_updated_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: EventType.LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventTypeLastUpdatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::FraudDetector::Detector.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''``AWS::FraudDetector::Detector.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventType")
    def event_type(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EventTypeProperty"]:
        '''``AWS::FraudDetector::Detector.EventType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-eventtype
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EventTypeProperty"], jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EventTypeProperty"],
    ) -> None:
        jsii.set(self, "eventType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.RuleProperty"]]]:
        '''``AWS::FraudDetector::Detector.Rules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-rules
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.RuleProperty"]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.RuleProperty"]]],
    ) -> None:
        jsii.set(self, "rules", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="associatedModels")
    def associated_models(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.ModelProperty"]]]]:
        '''``AWS::FraudDetector::Detector.AssociatedModels``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-associatedmodels
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.ModelProperty"]]]], jsii.get(self, "associatedModels"))

    @associated_models.setter
    def associated_models(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.ModelProperty"]]]],
    ) -> None:
        jsii.set(self, "associatedModels", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Detector.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorVersionStatus")
    def detector_version_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Detector.DetectorVersionStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorversionstatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorVersionStatus"))

    @detector_version_status.setter
    def detector_version_status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "detectorVersionStatus", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleExecutionMode")
    def rule_execution_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Detector.RuleExecutionMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-ruleexecutionmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleExecutionMode"))

    @rule_execution_mode.setter
    def rule_execution_mode(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ruleExecutionMode", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnDetector.EntityTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class EntityTypeProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        ) -> None:
            '''
            :param arn: ``CfnDetector.EntityTypeProperty.Arn``.
            :param created_time: ``CfnDetector.EntityTypeProperty.CreatedTime``.
            :param description: ``CfnDetector.EntityTypeProperty.Description``.
            :param inline: ``CfnDetector.EntityTypeProperty.Inline``.
            :param last_updated_time: ``CfnDetector.EntityTypeProperty.LastUpdatedTime``.
            :param name: ``CfnDetector.EntityTypeProperty.Name``.
            :param tags: ``CfnDetector.EntityTypeProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EntityTypeProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EntityTypeProperty.CreatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EntityTypeProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDetector.EntityTypeProperty.Inline``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EntityTypeProperty.LastUpdatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EntityTypeProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            '''``CfnDetector.EntityTypeProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnDetector.EventTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "entity_types": "entityTypes",
            "event_variables": "eventVariables",
            "inline": "inline",
            "labels": "labels",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class EventTypeProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            entity_types: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EntityTypeProperty"]]]] = None,
            event_variables: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EventVariableProperty"]]]] = None,
            inline: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            labels: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.LabelProperty"]]]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        ) -> None:
            '''
            :param arn: ``CfnDetector.EventTypeProperty.Arn``.
            :param created_time: ``CfnDetector.EventTypeProperty.CreatedTime``.
            :param description: ``CfnDetector.EventTypeProperty.Description``.
            :param entity_types: ``CfnDetector.EventTypeProperty.EntityTypes``.
            :param event_variables: ``CfnDetector.EventTypeProperty.EventVariables``.
            :param inline: ``CfnDetector.EventTypeProperty.Inline``.
            :param labels: ``CfnDetector.EventTypeProperty.Labels``.
            :param last_updated_time: ``CfnDetector.EventTypeProperty.LastUpdatedTime``.
            :param name: ``CfnDetector.EventTypeProperty.Name``.
            :param tags: ``CfnDetector.EventTypeProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if entity_types is not None:
                self._values["entity_types"] = entity_types
            if event_variables is not None:
                self._values["event_variables"] = event_variables
            if inline is not None:
                self._values["inline"] = inline
            if labels is not None:
                self._values["labels"] = labels
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventTypeProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventTypeProperty.CreatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventTypeProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entity_types(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EntityTypeProperty"]]]]:
            '''``CfnDetector.EventTypeProperty.EntityTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-entitytypes
            '''
            result = self._values.get("entity_types")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EntityTypeProperty"]]]], result)

        @builtins.property
        def event_variables(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EventVariableProperty"]]]]:
            '''``CfnDetector.EventTypeProperty.EventVariables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-eventvariables
            '''
            result = self._values.get("event_variables")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.EventVariableProperty"]]]], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDetector.EventTypeProperty.Inline``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def labels(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.LabelProperty"]]]]:
            '''``CfnDetector.EventTypeProperty.Labels``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-labels
            '''
            result = self._values.get("labels")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.LabelProperty"]]]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventTypeProperty.LastUpdatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventTypeProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            '''``CfnDetector.EventTypeProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnDetector.EventVariableProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "data_source": "dataSource",
            "data_type": "dataType",
            "default_value": "defaultValue",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
            "variable_type": "variableType",
        },
    )
    class EventVariableProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            data_source: typing.Optional[builtins.str] = None,
            data_type: typing.Optional[builtins.str] = None,
            default_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
            variable_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param arn: ``CfnDetector.EventVariableProperty.Arn``.
            :param created_time: ``CfnDetector.EventVariableProperty.CreatedTime``.
            :param data_source: ``CfnDetector.EventVariableProperty.DataSource``.
            :param data_type: ``CfnDetector.EventVariableProperty.DataType``.
            :param default_value: ``CfnDetector.EventVariableProperty.DefaultValue``.
            :param description: ``CfnDetector.EventVariableProperty.Description``.
            :param inline: ``CfnDetector.EventVariableProperty.Inline``.
            :param last_updated_time: ``CfnDetector.EventVariableProperty.LastUpdatedTime``.
            :param name: ``CfnDetector.EventVariableProperty.Name``.
            :param tags: ``CfnDetector.EventVariableProperty.Tags``.
            :param variable_type: ``CfnDetector.EventVariableProperty.VariableType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if data_source is not None:
                self._values["data_source"] = data_source
            if data_type is not None:
                self._values["data_type"] = data_type
            if default_value is not None:
                self._values["default_value"] = default_value
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags
            if variable_type is not None:
                self._values["variable_type"] = variable_type

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventVariableProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventVariableProperty.CreatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_source(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventVariableProperty.DataSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-datasource
            '''
            result = self._values.get("data_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventVariableProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-datatype
            '''
            result = self._values.get("data_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventVariableProperty.DefaultValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventVariableProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDetector.EventVariableProperty.Inline``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventVariableProperty.LastUpdatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventVariableProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            '''``CfnDetector.EventVariableProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

        @builtins.property
        def variable_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.EventVariableProperty.VariableType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-variabletype
            '''
            result = self._values.get("variable_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnDetector.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class LabelProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        ) -> None:
            '''
            :param arn: ``CfnDetector.LabelProperty.Arn``.
            :param created_time: ``CfnDetector.LabelProperty.CreatedTime``.
            :param description: ``CfnDetector.LabelProperty.Description``.
            :param inline: ``CfnDetector.LabelProperty.Inline``.
            :param last_updated_time: ``CfnDetector.LabelProperty.LastUpdatedTime``.
            :param name: ``CfnDetector.LabelProperty.Name``.
            :param tags: ``CfnDetector.LabelProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.LabelProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.LabelProperty.CreatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.LabelProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDetector.LabelProperty.Inline``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.LabelProperty.LastUpdatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.LabelProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            '''``CfnDetector.LabelProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnDetector.ModelProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class ModelProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''
            :param arn: ``CfnDetector.ModelProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-model.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.ModelProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-model.html#cfn-frauddetector-detector-model-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnDetector.OutcomeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class OutcomeProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        ) -> None:
            '''
            :param arn: ``CfnDetector.OutcomeProperty.Arn``.
            :param created_time: ``CfnDetector.OutcomeProperty.CreatedTime``.
            :param description: ``CfnDetector.OutcomeProperty.Description``.
            :param inline: ``CfnDetector.OutcomeProperty.Inline``.
            :param last_updated_time: ``CfnDetector.OutcomeProperty.LastUpdatedTime``.
            :param name: ``CfnDetector.OutcomeProperty.Name``.
            :param tags: ``CfnDetector.OutcomeProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.OutcomeProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.OutcomeProperty.CreatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.OutcomeProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDetector.OutcomeProperty.Inline``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.OutcomeProperty.LastUpdatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.OutcomeProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            '''``CfnDetector.OutcomeProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutcomeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnDetector.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "detector_id": "detectorId",
            "expression": "expression",
            "language": "language",
            "last_updated_time": "lastUpdatedTime",
            "outcomes": "outcomes",
            "rule_id": "ruleId",
            "rule_version": "ruleVersion",
            "tags": "tags",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            detector_id: typing.Optional[builtins.str] = None,
            expression: typing.Optional[builtins.str] = None,
            language: typing.Optional[builtins.str] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            outcomes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.OutcomeProperty"]]]] = None,
            rule_id: typing.Optional[builtins.str] = None,
            rule_version: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        ) -> None:
            '''
            :param arn: ``CfnDetector.RuleProperty.Arn``.
            :param created_time: ``CfnDetector.RuleProperty.CreatedTime``.
            :param description: ``CfnDetector.RuleProperty.Description``.
            :param detector_id: ``CfnDetector.RuleProperty.DetectorId``.
            :param expression: ``CfnDetector.RuleProperty.Expression``.
            :param language: ``CfnDetector.RuleProperty.Language``.
            :param last_updated_time: ``CfnDetector.RuleProperty.LastUpdatedTime``.
            :param outcomes: ``CfnDetector.RuleProperty.Outcomes``.
            :param rule_id: ``CfnDetector.RuleProperty.RuleId``.
            :param rule_version: ``CfnDetector.RuleProperty.RuleVersion``.
            :param tags: ``CfnDetector.RuleProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if detector_id is not None:
                self._values["detector_id"] = detector_id
            if expression is not None:
                self._values["expression"] = expression
            if language is not None:
                self._values["language"] = language
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if outcomes is not None:
                self._values["outcomes"] = outcomes
            if rule_id is not None:
                self._values["rule_id"] = rule_id
            if rule_version is not None:
                self._values["rule_version"] = rule_version
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.RuleProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.RuleProperty.CreatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.RuleProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def detector_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.RuleProperty.DetectorId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-detectorid
            '''
            result = self._values.get("detector_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.RuleProperty.Expression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def language(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.RuleProperty.Language``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-language
            '''
            result = self._values.get("language")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.RuleProperty.LastUpdatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def outcomes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.OutcomeProperty"]]]]:
            '''``CfnDetector.RuleProperty.Outcomes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-outcomes
            '''
            result = self._values.get("outcomes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.OutcomeProperty"]]]], result)

        @builtins.property
        def rule_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.RuleProperty.RuleId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-ruleid
            '''
            result = self._values.get("rule_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_version(self) -> typing.Optional[builtins.str]:
            '''``CfnDetector.RuleProperty.RuleVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-ruleversion
            '''
            result = self._values.get("rule_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            '''``CfnDetector.RuleProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-frauddetector.CfnDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "event_type": "eventType",
        "rules": "rules",
        "associated_models": "associatedModels",
        "description": "description",
        "detector_version_status": "detectorVersionStatus",
        "rule_execution_mode": "ruleExecutionMode",
        "tags": "tags",
    },
)
class CfnDetectorProps:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        event_type: typing.Union[aws_cdk.core.IResolvable, CfnDetector.EventTypeProperty],
        rules: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDetector.RuleProperty]]],
        associated_models: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDetector.ModelProperty]]]] = None,
        description: typing.Optional[builtins.str] = None,
        detector_version_status: typing.Optional[builtins.str] = None,
        rule_execution_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::FraudDetector::Detector``.

        :param detector_id: ``AWS::FraudDetector::Detector.DetectorId``.
        :param event_type: ``AWS::FraudDetector::Detector.EventType``.
        :param rules: ``AWS::FraudDetector::Detector.Rules``.
        :param associated_models: ``AWS::FraudDetector::Detector.AssociatedModels``.
        :param description: ``AWS::FraudDetector::Detector.Description``.
        :param detector_version_status: ``AWS::FraudDetector::Detector.DetectorVersionStatus``.
        :param rule_execution_mode: ``AWS::FraudDetector::Detector.RuleExecutionMode``.
        :param tags: ``AWS::FraudDetector::Detector.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "detector_id": detector_id,
            "event_type": event_type,
            "rules": rules,
        }
        if associated_models is not None:
            self._values["associated_models"] = associated_models
        if description is not None:
            self._values["description"] = description
        if detector_version_status is not None:
            self._values["detector_version_status"] = detector_version_status
        if rule_execution_mode is not None:
            self._values["rule_execution_mode"] = rule_execution_mode
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''``AWS::FraudDetector::Detector.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_type(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDetector.EventTypeProperty]:
        '''``AWS::FraudDetector::Detector.EventType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-eventtype
        '''
        result = self._values.get("event_type")
        assert result is not None, "Required property 'event_type' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDetector.EventTypeProperty], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDetector.RuleProperty]]]:
        '''``AWS::FraudDetector::Detector.Rules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-rules
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDetector.RuleProperty]]], result)

    @builtins.property
    def associated_models(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDetector.ModelProperty]]]]:
        '''``AWS::FraudDetector::Detector.AssociatedModels``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-associatedmodels
        '''
        result = self._values.get("associated_models")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDetector.ModelProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Detector.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def detector_version_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Detector.DetectorVersionStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorversionstatus
        '''
        result = self._values.get("detector_version_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_execution_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Detector.RuleExecutionMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-ruleexecutionmode
        '''
        result = self._values.get("rule_execution_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::FraudDetector::Detector.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEntityType(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-frauddetector.CfnEntityType",
):
    '''A CloudFormation ``AWS::FraudDetector::EntityType``.

    :cloudformationResource: AWS::FraudDetector::EntityType
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::FraudDetector::EntityType``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::FraudDetector::EntityType.Name``.
        :param description: ``AWS::FraudDetector::EntityType.Description``.
        :param tags: ``AWS::FraudDetector::EntityType.Tags``.
        '''
        props = CfnEntityTypeProps(name=name, description=description, tags=tags)

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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::FraudDetector::EntityType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::EntityType.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::EntityType.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-frauddetector.CfnEntityTypeProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnEntityTypeProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::FraudDetector::EntityType``.

        :param name: ``AWS::FraudDetector::EntityType.Name``.
        :param description: ``AWS::FraudDetector::EntityType.Description``.
        :param tags: ``AWS::FraudDetector::EntityType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::EntityType.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::EntityType.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::FraudDetector::EntityType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEntityTypeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEventType(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-frauddetector.CfnEventType",
):
    '''A CloudFormation ``AWS::FraudDetector::EventType``.

    :cloudformationResource: AWS::FraudDetector::EventType
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        entity_types: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnEventType.EntityTypeProperty", aws_cdk.core.IResolvable]]],
        event_variables: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEventType.EventVariableProperty"]]],
        labels: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEventType.LabelProperty"]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::FraudDetector::EventType``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param entity_types: ``AWS::FraudDetector::EventType.EntityTypes``.
        :param event_variables: ``AWS::FraudDetector::EventType.EventVariables``.
        :param labels: ``AWS::FraudDetector::EventType.Labels``.
        :param name: ``AWS::FraudDetector::EventType.Name``.
        :param description: ``AWS::FraudDetector::EventType.Description``.
        :param tags: ``AWS::FraudDetector::EventType.Tags``.
        '''
        props = CfnEventTypeProps(
            entity_types=entity_types,
            event_variables=event_variables,
            labels=labels,
            name=name,
            description=description,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::FraudDetector::EventType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="entityTypes")
    def entity_types(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEventType.EntityTypeProperty", aws_cdk.core.IResolvable]]]:
        '''``AWS::FraudDetector::EventType.EntityTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-entitytypes
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEventType.EntityTypeProperty", aws_cdk.core.IResolvable]]], jsii.get(self, "entityTypes"))

    @entity_types.setter
    def entity_types(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEventType.EntityTypeProperty", aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "entityTypes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventVariables")
    def event_variables(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEventType.EventVariableProperty"]]]:
        '''``AWS::FraudDetector::EventType.EventVariables``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-eventvariables
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEventType.EventVariableProperty"]]], jsii.get(self, "eventVariables"))

    @event_variables.setter
    def event_variables(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEventType.EventVariableProperty"]]],
    ) -> None:
        jsii.set(self, "eventVariables", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="labels")
    def labels(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEventType.LabelProperty"]]]:
        '''``AWS::FraudDetector::EventType.Labels``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-labels
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEventType.LabelProperty"]]], jsii.get(self, "labels"))

    @labels.setter
    def labels(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEventType.LabelProperty"]]],
    ) -> None:
        jsii.set(self, "labels", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::EventType.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::EventType.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnEventType.EntityTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class EntityTypeProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        ) -> None:
            '''
            :param arn: ``CfnEventType.EntityTypeProperty.Arn``.
            :param created_time: ``CfnEventType.EntityTypeProperty.CreatedTime``.
            :param description: ``CfnEventType.EntityTypeProperty.Description``.
            :param inline: ``CfnEventType.EntityTypeProperty.Inline``.
            :param last_updated_time: ``CfnEventType.EntityTypeProperty.LastUpdatedTime``.
            :param name: ``CfnEventType.EntityTypeProperty.Name``.
            :param tags: ``CfnEventType.EntityTypeProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EntityTypeProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EntityTypeProperty.CreatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EntityTypeProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnEventType.EntityTypeProperty.Inline``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EntityTypeProperty.LastUpdatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EntityTypeProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            '''``CfnEventType.EntityTypeProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnEventType.EventVariableProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "data_source": "dataSource",
            "data_type": "dataType",
            "default_value": "defaultValue",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
            "variable_type": "variableType",
        },
    )
    class EventVariableProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            data_source: typing.Optional[builtins.str] = None,
            data_type: typing.Optional[builtins.str] = None,
            default_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
            variable_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param arn: ``CfnEventType.EventVariableProperty.Arn``.
            :param created_time: ``CfnEventType.EventVariableProperty.CreatedTime``.
            :param data_source: ``CfnEventType.EventVariableProperty.DataSource``.
            :param data_type: ``CfnEventType.EventVariableProperty.DataType``.
            :param default_value: ``CfnEventType.EventVariableProperty.DefaultValue``.
            :param description: ``CfnEventType.EventVariableProperty.Description``.
            :param inline: ``CfnEventType.EventVariableProperty.Inline``.
            :param last_updated_time: ``CfnEventType.EventVariableProperty.LastUpdatedTime``.
            :param name: ``CfnEventType.EventVariableProperty.Name``.
            :param tags: ``CfnEventType.EventVariableProperty.Tags``.
            :param variable_type: ``CfnEventType.EventVariableProperty.VariableType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if data_source is not None:
                self._values["data_source"] = data_source
            if data_type is not None:
                self._values["data_type"] = data_type
            if default_value is not None:
                self._values["default_value"] = default_value
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags
            if variable_type is not None:
                self._values["variable_type"] = variable_type

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EventVariableProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EventVariableProperty.CreatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_source(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EventVariableProperty.DataSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-datasource
            '''
            result = self._values.get("data_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_type(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EventVariableProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-datatype
            '''
            result = self._values.get("data_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EventVariableProperty.DefaultValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EventVariableProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnEventType.EventVariableProperty.Inline``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EventVariableProperty.LastUpdatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EventVariableProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            '''``CfnEventType.EventVariableProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

        @builtins.property
        def variable_type(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.EventVariableProperty.VariableType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-variabletype
            '''
            result = self._values.get("variable_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-frauddetector.CfnEventType.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class LabelProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        ) -> None:
            '''
            :param arn: ``CfnEventType.LabelProperty.Arn``.
            :param created_time: ``CfnEventType.LabelProperty.CreatedTime``.
            :param description: ``CfnEventType.LabelProperty.Description``.
            :param inline: ``CfnEventType.LabelProperty.Inline``.
            :param last_updated_time: ``CfnEventType.LabelProperty.LastUpdatedTime``.
            :param name: ``CfnEventType.LabelProperty.Name``.
            :param tags: ``CfnEventType.LabelProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.LabelProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.LabelProperty.CreatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.LabelProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnEventType.LabelProperty.Inline``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.LabelProperty.LastUpdatedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnEventType.LabelProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            '''``CfnEventType.LabelProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-frauddetector.CfnEventTypeProps",
    jsii_struct_bases=[],
    name_mapping={
        "entity_types": "entityTypes",
        "event_variables": "eventVariables",
        "labels": "labels",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnEventTypeProps:
    def __init__(
        self,
        *,
        entity_types: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnEventType.EntityTypeProperty, aws_cdk.core.IResolvable]]],
        event_variables: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnEventType.EventVariableProperty]]],
        labels: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnEventType.LabelProperty]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::FraudDetector::EventType``.

        :param entity_types: ``AWS::FraudDetector::EventType.EntityTypes``.
        :param event_variables: ``AWS::FraudDetector::EventType.EventVariables``.
        :param labels: ``AWS::FraudDetector::EventType.Labels``.
        :param name: ``AWS::FraudDetector::EventType.Name``.
        :param description: ``AWS::FraudDetector::EventType.Description``.
        :param tags: ``AWS::FraudDetector::EventType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "entity_types": entity_types,
            "event_variables": event_variables,
            "labels": labels,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def entity_types(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnEventType.EntityTypeProperty, aws_cdk.core.IResolvable]]]:
        '''``AWS::FraudDetector::EventType.EntityTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-entitytypes
        '''
        result = self._values.get("entity_types")
        assert result is not None, "Required property 'entity_types' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnEventType.EntityTypeProperty, aws_cdk.core.IResolvable]]], result)

    @builtins.property
    def event_variables(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEventType.EventVariableProperty]]]:
        '''``AWS::FraudDetector::EventType.EventVariables``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-eventvariables
        '''
        result = self._values.get("event_variables")
        assert result is not None, "Required property 'event_variables' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEventType.EventVariableProperty]]], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEventType.LabelProperty]]]:
        '''``AWS::FraudDetector::EventType.Labels``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-labels
        '''
        result = self._values.get("labels")
        assert result is not None, "Required property 'labels' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEventType.LabelProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::EventType.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::EventType.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::FraudDetector::EventType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventTypeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLabel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-frauddetector.CfnLabel",
):
    '''A CloudFormation ``AWS::FraudDetector::Label``.

    :cloudformationResource: AWS::FraudDetector::Label
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::FraudDetector::Label``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::FraudDetector::Label.Name``.
        :param description: ``AWS::FraudDetector::Label.Description``.
        :param tags: ``AWS::FraudDetector::Label.Tags``.
        '''
        props = CfnLabelProps(name=name, description=description, tags=tags)

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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::FraudDetector::Label.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::Label.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Label.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-frauddetector.CfnLabelProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnLabelProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::FraudDetector::Label``.

        :param name: ``AWS::FraudDetector::Label.Name``.
        :param description: ``AWS::FraudDetector::Label.Description``.
        :param tags: ``AWS::FraudDetector::Label.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::Label.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Label.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::FraudDetector::Label.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLabelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnOutcome(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-frauddetector.CfnOutcome",
):
    '''A CloudFormation ``AWS::FraudDetector::Outcome``.

    :cloudformationResource: AWS::FraudDetector::Outcome
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::FraudDetector::Outcome``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::FraudDetector::Outcome.Name``.
        :param description: ``AWS::FraudDetector::Outcome.Description``.
        :param tags: ``AWS::FraudDetector::Outcome.Tags``.
        '''
        props = CfnOutcomeProps(name=name, description=description, tags=tags)

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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::FraudDetector::Outcome.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::Outcome.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Outcome.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-frauddetector.CfnOutcomeProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnOutcomeProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::FraudDetector::Outcome``.

        :param name: ``AWS::FraudDetector::Outcome.Name``.
        :param description: ``AWS::FraudDetector::Outcome.Description``.
        :param tags: ``AWS::FraudDetector::Outcome.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::Outcome.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Outcome.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::FraudDetector::Outcome.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOutcomeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnVariable(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-frauddetector.CfnVariable",
):
    '''A CloudFormation ``AWS::FraudDetector::Variable``.

    :cloudformationResource: AWS::FraudDetector::Variable
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        data_source: builtins.str,
        data_type: builtins.str,
        default_value: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        variable_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::FraudDetector::Variable``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_source: ``AWS::FraudDetector::Variable.DataSource``.
        :param data_type: ``AWS::FraudDetector::Variable.DataType``.
        :param default_value: ``AWS::FraudDetector::Variable.DefaultValue``.
        :param name: ``AWS::FraudDetector::Variable.Name``.
        :param description: ``AWS::FraudDetector::Variable.Description``.
        :param tags: ``AWS::FraudDetector::Variable.Tags``.
        :param variable_type: ``AWS::FraudDetector::Variable.VariableType``.
        '''
        props = CfnVariableProps(
            data_source=data_source,
            data_type=data_type,
            default_value=default_value,
            name=name,
            description=description,
            tags=tags,
            variable_type=variable_type,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::FraudDetector::Variable.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        '''``AWS::FraudDetector::Variable.DataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datasource
        '''
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        jsii.set(self, "dataSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        '''``AWS::FraudDetector::Variable.DataType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datatype
        '''
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        jsii.set(self, "dataType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        '''``AWS::FraudDetector::Variable.DefaultValue``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-defaultvalue
        '''
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        jsii.set(self, "defaultValue", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::Variable.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Variable.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="variableType")
    def variable_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Variable.VariableType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-variabletype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variableType"))

    @variable_type.setter
    def variable_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "variableType", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-frauddetector.CfnVariableProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_source": "dataSource",
        "data_type": "dataType",
        "default_value": "defaultValue",
        "name": "name",
        "description": "description",
        "tags": "tags",
        "variable_type": "variableType",
    },
)
class CfnVariableProps:
    def __init__(
        self,
        *,
        data_source: builtins.str,
        data_type: builtins.str,
        default_value: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        variable_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::FraudDetector::Variable``.

        :param data_source: ``AWS::FraudDetector::Variable.DataSource``.
        :param data_type: ``AWS::FraudDetector::Variable.DataType``.
        :param default_value: ``AWS::FraudDetector::Variable.DefaultValue``.
        :param name: ``AWS::FraudDetector::Variable.Name``.
        :param description: ``AWS::FraudDetector::Variable.Description``.
        :param tags: ``AWS::FraudDetector::Variable.Tags``.
        :param variable_type: ``AWS::FraudDetector::Variable.VariableType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_source": data_source,
            "data_type": data_type,
            "default_value": default_value,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if variable_type is not None:
            self._values["variable_type"] = variable_type

    @builtins.property
    def data_source(self) -> builtins.str:
        '''``AWS::FraudDetector::Variable.DataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datasource
        '''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_type(self) -> builtins.str:
        '''``AWS::FraudDetector::Variable.DataType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datatype
        '''
        result = self._values.get("data_type")
        assert result is not None, "Required property 'data_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> builtins.str:
        '''``AWS::FraudDetector::Variable.DefaultValue``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-defaultvalue
        '''
        result = self._values.get("default_value")
        assert result is not None, "Required property 'default_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::FraudDetector::Variable.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Variable.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::FraudDetector::Variable.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def variable_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::FraudDetector::Variable.VariableType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-variabletype
        '''
        result = self._values.get("variable_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVariableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDetector",
    "CfnDetectorProps",
    "CfnEntityType",
    "CfnEntityTypeProps",
    "CfnEventType",
    "CfnEventTypeProps",
    "CfnLabel",
    "CfnLabelProps",
    "CfnOutcome",
    "CfnOutcomeProps",
    "CfnVariable",
    "CfnVariableProps",
]

publication.publish()
