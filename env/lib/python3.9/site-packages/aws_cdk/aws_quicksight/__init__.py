'''
# AWS::QuickSight Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_quicksight as quicksight
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
class CfnAnalysis(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis",
):
    '''A CloudFormation ``AWS::QuickSight::Analysis``.

    :cloudformationResource: AWS::QuickSight::Analysis
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
        errors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisErrorProperty"]]]] = None,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.ParametersProperty"]] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.ResourcePermissionProperty"]]]] = None,
        source_entity: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisSourceEntityProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::QuickSight::Analysis``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param analysis_id: ``AWS::QuickSight::Analysis.AnalysisId``.
        :param aws_account_id: ``AWS::QuickSight::Analysis.AwsAccountId``.
        :param errors: ``AWS::QuickSight::Analysis.Errors``.
        :param name: ``AWS::QuickSight::Analysis.Name``.
        :param parameters: ``AWS::QuickSight::Analysis.Parameters``.
        :param permissions: ``AWS::QuickSight::Analysis.Permissions``.
        :param source_entity: ``AWS::QuickSight::Analysis.SourceEntity``.
        :param tags: ``AWS::QuickSight::Analysis.Tags``.
        :param theme_arn: ``AWS::QuickSight::Analysis.ThemeArn``.
        '''
        props = CfnAnalysisProps(
            analysis_id=analysis_id,
            aws_account_id=aws_account_id,
            errors=errors,
            name=name,
            parameters=parameters,
            permissions=permissions,
            source_entity=source_entity,
            tags=tags,
            theme_arn=theme_arn,
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
    @jsii.member(jsii_name="attrDataSetArns")
    def attr_data_set_arns(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: DataSetArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDataSetArns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSheets")
    def attr_sheets(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: Sheets
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrSheets"))

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::QuickSight::Analysis.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="analysisId")
    def analysis_id(self) -> builtins.str:
        '''``AWS::QuickSight::Analysis.AnalysisId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-analysisid
        '''
        return typing.cast(builtins.str, jsii.get(self, "analysisId"))

    @analysis_id.setter
    def analysis_id(self, value: builtins.str) -> None:
        jsii.set(self, "analysisId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        '''``AWS::QuickSight::Analysis.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-awsaccountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="errors")
    def errors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisErrorProperty"]]]]:
        '''``AWS::QuickSight::Analysis.Errors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-errors
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisErrorProperty"]]]], jsii.get(self, "errors"))

    @errors.setter
    def errors(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisErrorProperty"]]]],
    ) -> None:
        jsii.set(self, "errors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Analysis.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.ParametersProperty"]]:
        '''``AWS::QuickSight::Analysis.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.ParametersProperty"]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.ParametersProperty"]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.ResourcePermissionProperty"]]]]:
        '''``AWS::QuickSight::Analysis.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-permissions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.ResourcePermissionProperty"]]]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.ResourcePermissionProperty"]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceEntity")
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisSourceEntityProperty"]]:
        '''``AWS::QuickSight::Analysis.SourceEntity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-sourceentity
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisSourceEntityProperty"]], jsii.get(self, "sourceEntity"))

    @source_entity.setter
    def source_entity(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisSourceEntityProperty"]],
    ) -> None:
        jsii.set(self, "sourceEntity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="themeArn")
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Analysis.ThemeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-themearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "themeArn"))

    @theme_arn.setter
    def theme_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "themeArn", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.AnalysisErrorProperty",
        jsii_struct_bases=[],
        name_mapping={"message": "message", "type": "type"},
    )
    class AnalysisErrorProperty:
        def __init__(
            self,
            *,
            message: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param message: ``CfnAnalysis.AnalysisErrorProperty.Message``.
            :param type: ``CfnAnalysis.AnalysisErrorProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if message is not None:
                self._values["message"] = message
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            '''``CfnAnalysis.AnalysisErrorProperty.Message``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html#cfn-quicksight-analysis-analysiserror-message
            '''
            result = self._values.get("message")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnAnalysis.AnalysisErrorProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html#cfn-quicksight-analysis-analysiserror-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisErrorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.AnalysisSourceEntityProperty",
        jsii_struct_bases=[],
        name_mapping={"source_template": "sourceTemplate"},
    )
    class AnalysisSourceEntityProperty:
        def __init__(
            self,
            *,
            source_template: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisSourceTemplateProperty"]] = None,
        ) -> None:
            '''
            :param source_template: ``CfnAnalysis.AnalysisSourceEntityProperty.SourceTemplate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourceentity.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if source_template is not None:
                self._values["source_template"] = source_template

        @builtins.property
        def source_template(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisSourceTemplateProperty"]]:
            '''``CfnAnalysis.AnalysisSourceEntityProperty.SourceTemplate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourceentity.html#cfn-quicksight-analysis-analysissourceentity-sourcetemplate
            '''
            result = self._values.get("source_template")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.AnalysisSourceTemplateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisSourceEntityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.AnalysisSourceTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "data_set_references": "dataSetReferences"},
    )
    class AnalysisSourceTemplateProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            data_set_references: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.DataSetReferenceProperty"]]],
        ) -> None:
            '''
            :param arn: ``CfnAnalysis.AnalysisSourceTemplateProperty.Arn``.
            :param data_set_references: ``CfnAnalysis.AnalysisSourceTemplateProperty.DataSetReferences``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "data_set_references": data_set_references,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''``CfnAnalysis.AnalysisSourceTemplateProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html#cfn-quicksight-analysis-analysissourcetemplate-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_set_references(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.DataSetReferenceProperty"]]]:
            '''``CfnAnalysis.AnalysisSourceTemplateProperty.DataSetReferences``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html#cfn-quicksight-analysis-analysissourcetemplate-datasetreferences
            '''
            result = self._values.get("data_set_references")
            assert result is not None, "Required property 'data_set_references' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.DataSetReferenceProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisSourceTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.DataSetReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_set_arn": "dataSetArn",
            "data_set_placeholder": "dataSetPlaceholder",
        },
    )
    class DataSetReferenceProperty:
        def __init__(
            self,
            *,
            data_set_arn: builtins.str,
            data_set_placeholder: builtins.str,
        ) -> None:
            '''
            :param data_set_arn: ``CfnAnalysis.DataSetReferenceProperty.DataSetArn``.
            :param data_set_placeholder: ``CfnAnalysis.DataSetReferenceProperty.DataSetPlaceholder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_set_arn": data_set_arn,
                "data_set_placeholder": data_set_placeholder,
            }

        @builtins.property
        def data_set_arn(self) -> builtins.str:
            '''``CfnAnalysis.DataSetReferenceProperty.DataSetArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html#cfn-quicksight-analysis-datasetreference-datasetarn
            '''
            result = self._values.get("data_set_arn")
            assert result is not None, "Required property 'data_set_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_set_placeholder(self) -> builtins.str:
            '''``CfnAnalysis.DataSetReferenceProperty.DataSetPlaceholder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html#cfn-quicksight-analysis-datasetreference-datasetplaceholder
            '''
            result = self._values.get("data_set_placeholder")
            assert result is not None, "Required property 'data_set_placeholder' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSetReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.DateTimeParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class DateTimeParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param name: ``CfnAnalysis.DateTimeParameterProperty.Name``.
            :param values: ``CfnAnalysis.DateTimeParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAnalysis.DateTimeParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html#cfn-quicksight-analysis-datetimeparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''``CfnAnalysis.DateTimeParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html#cfn-quicksight-analysis-datetimeparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateTimeParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.DecimalParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class DecimalParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[jsii.Number]],
        ) -> None:
            '''
            :param name: ``CfnAnalysis.DecimalParameterProperty.Name``.
            :param values: ``CfnAnalysis.DecimalParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAnalysis.DecimalParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html#cfn-quicksight-analysis-decimalparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]:
            '''``CfnAnalysis.DecimalParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html#cfn-quicksight-analysis-decimalparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DecimalParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.IntegerParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class IntegerParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[jsii.Number]],
        ) -> None:
            '''
            :param name: ``CfnAnalysis.IntegerParameterProperty.Name``.
            :param values: ``CfnAnalysis.IntegerParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAnalysis.IntegerParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html#cfn-quicksight-analysis-integerparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]:
            '''``CfnAnalysis.IntegerParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html#cfn-quicksight-analysis-integerparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegerParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.ParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "date_time_parameters": "dateTimeParameters",
            "decimal_parameters": "decimalParameters",
            "integer_parameters": "integerParameters",
            "string_parameters": "stringParameters",
        },
    )
    class ParametersProperty:
        def __init__(
            self,
            *,
            date_time_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.DateTimeParameterProperty"]]]] = None,
            decimal_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.DecimalParameterProperty"]]]] = None,
            integer_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.IntegerParameterProperty"]]]] = None,
            string_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.StringParameterProperty"]]]] = None,
        ) -> None:
            '''
            :param date_time_parameters: ``CfnAnalysis.ParametersProperty.DateTimeParameters``.
            :param decimal_parameters: ``CfnAnalysis.ParametersProperty.DecimalParameters``.
            :param integer_parameters: ``CfnAnalysis.ParametersProperty.IntegerParameters``.
            :param string_parameters: ``CfnAnalysis.ParametersProperty.StringParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if date_time_parameters is not None:
                self._values["date_time_parameters"] = date_time_parameters
            if decimal_parameters is not None:
                self._values["decimal_parameters"] = decimal_parameters
            if integer_parameters is not None:
                self._values["integer_parameters"] = integer_parameters
            if string_parameters is not None:
                self._values["string_parameters"] = string_parameters

        @builtins.property
        def date_time_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.DateTimeParameterProperty"]]]]:
            '''``CfnAnalysis.ParametersProperty.DateTimeParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-datetimeparameters
            '''
            result = self._values.get("date_time_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.DateTimeParameterProperty"]]]], result)

        @builtins.property
        def decimal_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.DecimalParameterProperty"]]]]:
            '''``CfnAnalysis.ParametersProperty.DecimalParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-decimalparameters
            '''
            result = self._values.get("decimal_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.DecimalParameterProperty"]]]], result)

        @builtins.property
        def integer_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.IntegerParameterProperty"]]]]:
            '''``CfnAnalysis.ParametersProperty.IntegerParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-integerparameters
            '''
            result = self._values.get("integer_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.IntegerParameterProperty"]]]], result)

        @builtins.property
        def string_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.StringParameterProperty"]]]]:
            '''``CfnAnalysis.ParametersProperty.StringParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-stringparameters
            '''
            result = self._values.get("string_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalysis.StringParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            principal: builtins.str,
        ) -> None:
            '''
            :param actions: ``CfnAnalysis.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnAnalysis.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''``CfnAnalysis.ResourcePermissionProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html#cfn-quicksight-analysis-resourcepermission-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def principal(self) -> builtins.str:
            '''``CfnAnalysis.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html#cfn-quicksight-analysis-resourcepermission-principal
            '''
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.SheetProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sheet_id": "sheetId"},
    )
    class SheetProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            sheet_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnAnalysis.SheetProperty.Name``.
            :param sheet_id: ``CfnAnalysis.SheetProperty.SheetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if sheet_id is not None:
                self._values["sheet_id"] = sheet_id

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnAnalysis.SheetProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html#cfn-quicksight-analysis-sheet-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sheet_id(self) -> typing.Optional[builtins.str]:
            '''``CfnAnalysis.SheetProperty.SheetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html#cfn-quicksight-analysis-sheet-sheetid
            '''
            result = self._values.get("sheet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SheetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnAnalysis.StringParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class StringParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param name: ``CfnAnalysis.StringParameterProperty.Name``.
            :param values: ``CfnAnalysis.StringParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAnalysis.StringParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html#cfn-quicksight-analysis-stringparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''``CfnAnalysis.StringParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html#cfn-quicksight-analysis-stringparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StringParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-quicksight.CfnAnalysisProps",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "aws_account_id": "awsAccountId",
        "errors": "errors",
        "name": "name",
        "parameters": "parameters",
        "permissions": "permissions",
        "source_entity": "sourceEntity",
        "tags": "tags",
        "theme_arn": "themeArn",
    },
)
class CfnAnalysisProps:
    def __init__(
        self,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
        errors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.AnalysisErrorProperty]]]] = None,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.ParametersProperty]] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.ResourcePermissionProperty]]]] = None,
        source_entity: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.AnalysisSourceEntityProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::QuickSight::Analysis``.

        :param analysis_id: ``AWS::QuickSight::Analysis.AnalysisId``.
        :param aws_account_id: ``AWS::QuickSight::Analysis.AwsAccountId``.
        :param errors: ``AWS::QuickSight::Analysis.Errors``.
        :param name: ``AWS::QuickSight::Analysis.Name``.
        :param parameters: ``AWS::QuickSight::Analysis.Parameters``.
        :param permissions: ``AWS::QuickSight::Analysis.Permissions``.
        :param source_entity: ``AWS::QuickSight::Analysis.SourceEntity``.
        :param tags: ``AWS::QuickSight::Analysis.Tags``.
        :param theme_arn: ``AWS::QuickSight::Analysis.ThemeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
        }
        if errors is not None:
            self._values["errors"] = errors
        if name is not None:
            self._values["name"] = name
        if parameters is not None:
            self._values["parameters"] = parameters
        if permissions is not None:
            self._values["permissions"] = permissions
        if source_entity is not None:
            self._values["source_entity"] = source_entity
        if tags is not None:
            self._values["tags"] = tags
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''``AWS::QuickSight::Analysis.AnalysisId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-analysisid
        '''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''``AWS::QuickSight::Analysis.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-awsaccountid
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def errors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.AnalysisErrorProperty]]]]:
        '''``AWS::QuickSight::Analysis.Errors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-errors
        '''
        result = self._values.get("errors")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.AnalysisErrorProperty]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Analysis.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.ParametersProperty]]:
        '''``AWS::QuickSight::Analysis.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.ParametersProperty]], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.ResourcePermissionProperty]]]]:
        '''``AWS::QuickSight::Analysis.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.ResourcePermissionProperty]]]], result)

    @builtins.property
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.AnalysisSourceEntityProperty]]:
        '''``AWS::QuickSight::Analysis.SourceEntity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-sourceentity
        '''
        result = self._values.get("source_entity")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAnalysis.AnalysisSourceEntityProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::QuickSight::Analysis.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Analysis.ThemeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-themearn
        '''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnalysisProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDashboard(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-quicksight.CfnDashboard",
):
    '''A CloudFormation ``AWS::QuickSight::Dashboard``.

    :cloudformationResource: AWS::QuickSight::Dashboard
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        dashboard_publish_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardPublishOptionsProperty"]] = None,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ParametersProperty"]] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ResourcePermissionProperty"]]]] = None,
        source_entity: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardSourceEntityProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::QuickSight::Dashboard``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param aws_account_id: ``AWS::QuickSight::Dashboard.AwsAccountId``.
        :param dashboard_id: ``AWS::QuickSight::Dashboard.DashboardId``.
        :param dashboard_publish_options: ``AWS::QuickSight::Dashboard.DashboardPublishOptions``.
        :param name: ``AWS::QuickSight::Dashboard.Name``.
        :param parameters: ``AWS::QuickSight::Dashboard.Parameters``.
        :param permissions: ``AWS::QuickSight::Dashboard.Permissions``.
        :param source_entity: ``AWS::QuickSight::Dashboard.SourceEntity``.
        :param tags: ``AWS::QuickSight::Dashboard.Tags``.
        :param theme_arn: ``AWS::QuickSight::Dashboard.ThemeArn``.
        :param version_description: ``AWS::QuickSight::Dashboard.VersionDescription``.
        '''
        props = CfnDashboardProps(
            aws_account_id=aws_account_id,
            dashboard_id=dashboard_id,
            dashboard_publish_options=dashboard_publish_options,
            name=name,
            parameters=parameters,
            permissions=permissions,
            source_entity=source_entity,
            tags=tags,
            theme_arn=theme_arn,
            version_description=version_description,
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
    @jsii.member(jsii_name="attrLastPublishedTime")
    def attr_last_published_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastPublishedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastPublishedTime"))

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
        '''``AWS::QuickSight::Dashboard.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        '''``AWS::QuickSight::Dashboard.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-awsaccountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dashboardId")
    def dashboard_id(self) -> builtins.str:
        '''``AWS::QuickSight::Dashboard.DashboardId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardid
        '''
        return typing.cast(builtins.str, jsii.get(self, "dashboardId"))

    @dashboard_id.setter
    def dashboard_id(self, value: builtins.str) -> None:
        jsii.set(self, "dashboardId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dashboardPublishOptions")
    def dashboard_publish_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardPublishOptionsProperty"]]:
        '''``AWS::QuickSight::Dashboard.DashboardPublishOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardpublishoptions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardPublishOptionsProperty"]], jsii.get(self, "dashboardPublishOptions"))

    @dashboard_publish_options.setter
    def dashboard_publish_options(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardPublishOptionsProperty"]],
    ) -> None:
        jsii.set(self, "dashboardPublishOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Dashboard.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ParametersProperty"]]:
        '''``AWS::QuickSight::Dashboard.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ParametersProperty"]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ParametersProperty"]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ResourcePermissionProperty"]]]]:
        '''``AWS::QuickSight::Dashboard.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-permissions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ResourcePermissionProperty"]]]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ResourcePermissionProperty"]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceEntity")
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardSourceEntityProperty"]]:
        '''``AWS::QuickSight::Dashboard.SourceEntity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-sourceentity
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardSourceEntityProperty"]], jsii.get(self, "sourceEntity"))

    @source_entity.setter
    def source_entity(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardSourceEntityProperty"]],
    ) -> None:
        jsii.set(self, "sourceEntity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="themeArn")
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Dashboard.ThemeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-themearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "themeArn"))

    @theme_arn.setter
    def theme_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "themeArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Dashboard.VersionDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-versiondescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionDescription"))

    @version_description.setter
    def version_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionDescription", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.AdHocFilteringOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"availability_status": "availabilityStatus"},
    )
    class AdHocFilteringOptionProperty:
        def __init__(
            self,
            *,
            availability_status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param availability_status: ``CfnDashboard.AdHocFilteringOptionProperty.AvailabilityStatus``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-adhocfilteringoption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if availability_status is not None:
                self._values["availability_status"] = availability_status

        @builtins.property
        def availability_status(self) -> typing.Optional[builtins.str]:
            '''``CfnDashboard.AdHocFilteringOptionProperty.AvailabilityStatus``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-adhocfilteringoption.html#cfn-quicksight-dashboard-adhocfilteringoption-availabilitystatus
            '''
            result = self._values.get("availability_status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdHocFilteringOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.DashboardPublishOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_hoc_filtering_option": "adHocFilteringOption",
            "export_to_csv_option": "exportToCsvOption",
            "sheet_controls_option": "sheetControlsOption",
        },
    )
    class DashboardPublishOptionsProperty:
        def __init__(
            self,
            *,
            ad_hoc_filtering_option: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.AdHocFilteringOptionProperty"]] = None,
            export_to_csv_option: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ExportToCSVOptionProperty"]] = None,
            sheet_controls_option: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.SheetControlsOptionProperty"]] = None,
        ) -> None:
            '''
            :param ad_hoc_filtering_option: ``CfnDashboard.DashboardPublishOptionsProperty.AdHocFilteringOption``.
            :param export_to_csv_option: ``CfnDashboard.DashboardPublishOptionsProperty.ExportToCSVOption``.
            :param sheet_controls_option: ``CfnDashboard.DashboardPublishOptionsProperty.SheetControlsOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ad_hoc_filtering_option is not None:
                self._values["ad_hoc_filtering_option"] = ad_hoc_filtering_option
            if export_to_csv_option is not None:
                self._values["export_to_csv_option"] = export_to_csv_option
            if sheet_controls_option is not None:
                self._values["sheet_controls_option"] = sheet_controls_option

        @builtins.property
        def ad_hoc_filtering_option(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.AdHocFilteringOptionProperty"]]:
            '''``CfnDashboard.DashboardPublishOptionsProperty.AdHocFilteringOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-adhocfilteringoption
            '''
            result = self._values.get("ad_hoc_filtering_option")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.AdHocFilteringOptionProperty"]], result)

        @builtins.property
        def export_to_csv_option(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ExportToCSVOptionProperty"]]:
            '''``CfnDashboard.DashboardPublishOptionsProperty.ExportToCSVOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-exporttocsvoption
            '''
            result = self._values.get("export_to_csv_option")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.ExportToCSVOptionProperty"]], result)

        @builtins.property
        def sheet_controls_option(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.SheetControlsOptionProperty"]]:
            '''``CfnDashboard.DashboardPublishOptionsProperty.SheetControlsOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-sheetcontrolsoption
            '''
            result = self._values.get("sheet_controls_option")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.SheetControlsOptionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardPublishOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.DashboardSourceEntityProperty",
        jsii_struct_bases=[],
        name_mapping={"source_template": "sourceTemplate"},
    )
    class DashboardSourceEntityProperty:
        def __init__(
            self,
            *,
            source_template: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardSourceTemplateProperty"]] = None,
        ) -> None:
            '''
            :param source_template: ``CfnDashboard.DashboardSourceEntityProperty.SourceTemplate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourceentity.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if source_template is not None:
                self._values["source_template"] = source_template

        @builtins.property
        def source_template(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardSourceTemplateProperty"]]:
            '''``CfnDashboard.DashboardSourceEntityProperty.SourceTemplate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourceentity.html#cfn-quicksight-dashboard-dashboardsourceentity-sourcetemplate
            '''
            result = self._values.get("source_template")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DashboardSourceTemplateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardSourceEntityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.DashboardSourceTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "data_set_references": "dataSetReferences"},
    )
    class DashboardSourceTemplateProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            data_set_references: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DataSetReferenceProperty"]]],
        ) -> None:
            '''
            :param arn: ``CfnDashboard.DashboardSourceTemplateProperty.Arn``.
            :param data_set_references: ``CfnDashboard.DashboardSourceTemplateProperty.DataSetReferences``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "data_set_references": data_set_references,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''``CfnDashboard.DashboardSourceTemplateProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html#cfn-quicksight-dashboard-dashboardsourcetemplate-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_set_references(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DataSetReferenceProperty"]]]:
            '''``CfnDashboard.DashboardSourceTemplateProperty.DataSetReferences``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html#cfn-quicksight-dashboard-dashboardsourcetemplate-datasetreferences
            '''
            result = self._values.get("data_set_references")
            assert result is not None, "Required property 'data_set_references' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DataSetReferenceProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardSourceTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.DataSetReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_set_arn": "dataSetArn",
            "data_set_placeholder": "dataSetPlaceholder",
        },
    )
    class DataSetReferenceProperty:
        def __init__(
            self,
            *,
            data_set_arn: builtins.str,
            data_set_placeholder: builtins.str,
        ) -> None:
            '''
            :param data_set_arn: ``CfnDashboard.DataSetReferenceProperty.DataSetArn``.
            :param data_set_placeholder: ``CfnDashboard.DataSetReferenceProperty.DataSetPlaceholder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_set_arn": data_set_arn,
                "data_set_placeholder": data_set_placeholder,
            }

        @builtins.property
        def data_set_arn(self) -> builtins.str:
            '''``CfnDashboard.DataSetReferenceProperty.DataSetArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html#cfn-quicksight-dashboard-datasetreference-datasetarn
            '''
            result = self._values.get("data_set_arn")
            assert result is not None, "Required property 'data_set_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_set_placeholder(self) -> builtins.str:
            '''``CfnDashboard.DataSetReferenceProperty.DataSetPlaceholder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html#cfn-quicksight-dashboard-datasetreference-datasetplaceholder
            '''
            result = self._values.get("data_set_placeholder")
            assert result is not None, "Required property 'data_set_placeholder' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSetReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.DateTimeParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class DateTimeParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param name: ``CfnDashboard.DateTimeParameterProperty.Name``.
            :param values: ``CfnDashboard.DateTimeParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDashboard.DateTimeParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html#cfn-quicksight-dashboard-datetimeparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''``CfnDashboard.DateTimeParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html#cfn-quicksight-dashboard-datetimeparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateTimeParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.DecimalParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class DecimalParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[jsii.Number]],
        ) -> None:
            '''
            :param name: ``CfnDashboard.DecimalParameterProperty.Name``.
            :param values: ``CfnDashboard.DecimalParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDashboard.DecimalParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html#cfn-quicksight-dashboard-decimalparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]:
            '''``CfnDashboard.DecimalParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html#cfn-quicksight-dashboard-decimalparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DecimalParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.ExportToCSVOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"availability_status": "availabilityStatus"},
    )
    class ExportToCSVOptionProperty:
        def __init__(
            self,
            *,
            availability_status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param availability_status: ``CfnDashboard.ExportToCSVOptionProperty.AvailabilityStatus``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-exporttocsvoption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if availability_status is not None:
                self._values["availability_status"] = availability_status

        @builtins.property
        def availability_status(self) -> typing.Optional[builtins.str]:
            '''``CfnDashboard.ExportToCSVOptionProperty.AvailabilityStatus``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-exporttocsvoption.html#cfn-quicksight-dashboard-exporttocsvoption-availabilitystatus
            '''
            result = self._values.get("availability_status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExportToCSVOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.IntegerParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class IntegerParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[jsii.Number]],
        ) -> None:
            '''
            :param name: ``CfnDashboard.IntegerParameterProperty.Name``.
            :param values: ``CfnDashboard.IntegerParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDashboard.IntegerParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html#cfn-quicksight-dashboard-integerparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]:
            '''``CfnDashboard.IntegerParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html#cfn-quicksight-dashboard-integerparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegerParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.ParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "date_time_parameters": "dateTimeParameters",
            "decimal_parameters": "decimalParameters",
            "integer_parameters": "integerParameters",
            "string_parameters": "stringParameters",
        },
    )
    class ParametersProperty:
        def __init__(
            self,
            *,
            date_time_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DateTimeParameterProperty"]]]] = None,
            decimal_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DecimalParameterProperty"]]]] = None,
            integer_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.IntegerParameterProperty"]]]] = None,
            string_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.StringParameterProperty"]]]] = None,
        ) -> None:
            '''
            :param date_time_parameters: ``CfnDashboard.ParametersProperty.DateTimeParameters``.
            :param decimal_parameters: ``CfnDashboard.ParametersProperty.DecimalParameters``.
            :param integer_parameters: ``CfnDashboard.ParametersProperty.IntegerParameters``.
            :param string_parameters: ``CfnDashboard.ParametersProperty.StringParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if date_time_parameters is not None:
                self._values["date_time_parameters"] = date_time_parameters
            if decimal_parameters is not None:
                self._values["decimal_parameters"] = decimal_parameters
            if integer_parameters is not None:
                self._values["integer_parameters"] = integer_parameters
            if string_parameters is not None:
                self._values["string_parameters"] = string_parameters

        @builtins.property
        def date_time_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DateTimeParameterProperty"]]]]:
            '''``CfnDashboard.ParametersProperty.DateTimeParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-datetimeparameters
            '''
            result = self._values.get("date_time_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DateTimeParameterProperty"]]]], result)

        @builtins.property
        def decimal_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DecimalParameterProperty"]]]]:
            '''``CfnDashboard.ParametersProperty.DecimalParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-decimalparameters
            '''
            result = self._values.get("decimal_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.DecimalParameterProperty"]]]], result)

        @builtins.property
        def integer_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.IntegerParameterProperty"]]]]:
            '''``CfnDashboard.ParametersProperty.IntegerParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-integerparameters
            '''
            result = self._values.get("integer_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.IntegerParameterProperty"]]]], result)

        @builtins.property
        def string_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.StringParameterProperty"]]]]:
            '''``CfnDashboard.ParametersProperty.StringParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-stringparameters
            '''
            result = self._values.get("string_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDashboard.StringParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            principal: builtins.str,
        ) -> None:
            '''
            :param actions: ``CfnDashboard.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnDashboard.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''``CfnDashboard.ResourcePermissionProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html#cfn-quicksight-dashboard-resourcepermission-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def principal(self) -> builtins.str:
            '''``CfnDashboard.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html#cfn-quicksight-dashboard-resourcepermission-principal
            '''
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.SheetControlsOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"visibility_state": "visibilityState"},
    )
    class SheetControlsOptionProperty:
        def __init__(
            self,
            *,
            visibility_state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param visibility_state: ``CfnDashboard.SheetControlsOptionProperty.VisibilityState``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheetcontrolsoption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if visibility_state is not None:
                self._values["visibility_state"] = visibility_state

        @builtins.property
        def visibility_state(self) -> typing.Optional[builtins.str]:
            '''``CfnDashboard.SheetControlsOptionProperty.VisibilityState``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheetcontrolsoption.html#cfn-quicksight-dashboard-sheetcontrolsoption-visibilitystate
            '''
            result = self._values.get("visibility_state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SheetControlsOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDashboard.StringParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class StringParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param name: ``CfnDashboard.StringParameterProperty.Name``.
            :param values: ``CfnDashboard.StringParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDashboard.StringParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html#cfn-quicksight-dashboard-stringparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''``CfnDashboard.StringParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html#cfn-quicksight-dashboard-stringparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StringParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-quicksight.CfnDashboardProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "dashboard_publish_options": "dashboardPublishOptions",
        "name": "name",
        "parameters": "parameters",
        "permissions": "permissions",
        "source_entity": "sourceEntity",
        "tags": "tags",
        "theme_arn": "themeArn",
        "version_description": "versionDescription",
    },
)
class CfnDashboardProps:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        dashboard_publish_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.DashboardPublishOptionsProperty]] = None,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.ParametersProperty]] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.ResourcePermissionProperty]]]] = None,
        source_entity: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.DashboardSourceEntityProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::QuickSight::Dashboard``.

        :param aws_account_id: ``AWS::QuickSight::Dashboard.AwsAccountId``.
        :param dashboard_id: ``AWS::QuickSight::Dashboard.DashboardId``.
        :param dashboard_publish_options: ``AWS::QuickSight::Dashboard.DashboardPublishOptions``.
        :param name: ``AWS::QuickSight::Dashboard.Name``.
        :param parameters: ``AWS::QuickSight::Dashboard.Parameters``.
        :param permissions: ``AWS::QuickSight::Dashboard.Permissions``.
        :param source_entity: ``AWS::QuickSight::Dashboard.SourceEntity``.
        :param tags: ``AWS::QuickSight::Dashboard.Tags``.
        :param theme_arn: ``AWS::QuickSight::Dashboard.ThemeArn``.
        :param version_description: ``AWS::QuickSight::Dashboard.VersionDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
        }
        if dashboard_publish_options is not None:
            self._values["dashboard_publish_options"] = dashboard_publish_options
        if name is not None:
            self._values["name"] = name
        if parameters is not None:
            self._values["parameters"] = parameters
        if permissions is not None:
            self._values["permissions"] = permissions
        if source_entity is not None:
            self._values["source_entity"] = source_entity
        if tags is not None:
            self._values["tags"] = tags
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''``AWS::QuickSight::Dashboard.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-awsaccountid
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''``AWS::QuickSight::Dashboard.DashboardId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardid
        '''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_publish_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.DashboardPublishOptionsProperty]]:
        '''``AWS::QuickSight::Dashboard.DashboardPublishOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardpublishoptions
        '''
        result = self._values.get("dashboard_publish_options")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.DashboardPublishOptionsProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Dashboard.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.ParametersProperty]]:
        '''``AWS::QuickSight::Dashboard.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.ParametersProperty]], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.ResourcePermissionProperty]]]]:
        '''``AWS::QuickSight::Dashboard.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.ResourcePermissionProperty]]]], result)

    @builtins.property
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.DashboardSourceEntityProperty]]:
        '''``AWS::QuickSight::Dashboard.SourceEntity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-sourceentity
        '''
        result = self._values.get("source_entity")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDashboard.DashboardSourceEntityProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::QuickSight::Dashboard.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Dashboard.ThemeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-themearn
        '''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Dashboard.VersionDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-versiondescription
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDataSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-quicksight.CfnDataSet",
):
    '''A CloudFormation ``AWS::QuickSight::DataSet``.

    :cloudformationResource: AWS::QuickSight::DataSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        aws_account_id: typing.Optional[builtins.str] = None,
        column_groups: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnGroupProperty"]]]] = None,
        column_level_permission_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnLevelPermissionRuleProperty"]]]] = None,
        data_set_id: typing.Optional[builtins.str] = None,
        field_folders: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.FieldFolderProperty"]]]] = None,
        import_mode: typing.Optional[builtins.str] = None,
        ingestion_wait_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.IngestionWaitPolicyProperty"]] = None,
        logical_table_map: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.LogicalTableProperty"]]]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ResourcePermissionProperty"]]]] = None,
        physical_table_map: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.PhysicalTableProperty"]]]] = None,
        row_level_permission_data_set: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RowLevelPermissionDataSetProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::QuickSight::DataSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param aws_account_id: ``AWS::QuickSight::DataSet.AwsAccountId``.
        :param column_groups: ``AWS::QuickSight::DataSet.ColumnGroups``.
        :param column_level_permission_rules: ``AWS::QuickSight::DataSet.ColumnLevelPermissionRules``.
        :param data_set_id: ``AWS::QuickSight::DataSet.DataSetId``.
        :param field_folders: ``AWS::QuickSight::DataSet.FieldFolders``.
        :param import_mode: ``AWS::QuickSight::DataSet.ImportMode``.
        :param ingestion_wait_policy: ``AWS::QuickSight::DataSet.IngestionWaitPolicy``.
        :param logical_table_map: ``AWS::QuickSight::DataSet.LogicalTableMap``.
        :param name: ``AWS::QuickSight::DataSet.Name``.
        :param permissions: ``AWS::QuickSight::DataSet.Permissions``.
        :param physical_table_map: ``AWS::QuickSight::DataSet.PhysicalTableMap``.
        :param row_level_permission_data_set: ``AWS::QuickSight::DataSet.RowLevelPermissionDataSet``.
        :param tags: ``AWS::QuickSight::DataSet.Tags``.
        '''
        props = CfnDataSetProps(
            aws_account_id=aws_account_id,
            column_groups=column_groups,
            column_level_permission_rules=column_level_permission_rules,
            data_set_id=data_set_id,
            field_folders=field_folders,
            import_mode=import_mode,
            ingestion_wait_policy=ingestion_wait_policy,
            logical_table_map=logical_table_map,
            name=name,
            permissions=permissions,
            physical_table_map=physical_table_map,
            row_level_permission_data_set=row_level_permission_data_set,
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
    @jsii.member(jsii_name="attrConsumedSpiceCapacityInBytes")
    def attr_consumed_spice_capacity_in_bytes(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: ConsumedSpiceCapacityInBytes
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrConsumedSpiceCapacityInBytes"))

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
    @jsii.member(jsii_name="attrOutputColumns")
    def attr_output_columns(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: OutputColumns
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrOutputColumns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::QuickSight::DataSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSet.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-awsaccountid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="columnGroups")
    def column_groups(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnGroupProperty"]]]]:
        '''``AWS::QuickSight::DataSet.ColumnGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columngroups
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnGroupProperty"]]]], jsii.get(self, "columnGroups"))

    @column_groups.setter
    def column_groups(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnGroupProperty"]]]],
    ) -> None:
        jsii.set(self, "columnGroups", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="columnLevelPermissionRules")
    def column_level_permission_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnLevelPermissionRuleProperty"]]]]:
        '''``AWS::QuickSight::DataSet.ColumnLevelPermissionRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columnlevelpermissionrules
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnLevelPermissionRuleProperty"]]]], jsii.get(self, "columnLevelPermissionRules"))

    @column_level_permission_rules.setter
    def column_level_permission_rules(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnLevelPermissionRuleProperty"]]]],
    ) -> None:
        jsii.set(self, "columnLevelPermissionRules", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSetId")
    def data_set_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSet.DataSetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-datasetid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSetId"))

    @data_set_id.setter
    def data_set_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dataSetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fieldFolders")
    def field_folders(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.FieldFolderProperty"]]]]:
        '''``AWS::QuickSight::DataSet.FieldFolders``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-fieldfolders
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.FieldFolderProperty"]]]], jsii.get(self, "fieldFolders"))

    @field_folders.setter
    def field_folders(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.FieldFolderProperty"]]]],
    ) -> None:
        jsii.set(self, "fieldFolders", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="importMode")
    def import_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSet.ImportMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-importmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "importMode"))

    @import_mode.setter
    def import_mode(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "importMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ingestionWaitPolicy")
    def ingestion_wait_policy(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.IngestionWaitPolicyProperty"]]:
        '''``AWS::QuickSight::DataSet.IngestionWaitPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-ingestionwaitpolicy
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.IngestionWaitPolicyProperty"]], jsii.get(self, "ingestionWaitPolicy"))

    @ingestion_wait_policy.setter
    def ingestion_wait_policy(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.IngestionWaitPolicyProperty"]],
    ) -> None:
        jsii.set(self, "ingestionWaitPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logicalTableMap")
    def logical_table_map(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.LogicalTableProperty"]]]]:
        '''``AWS::QuickSight::DataSet.LogicalTableMap``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-logicaltablemap
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.LogicalTableProperty"]]]], jsii.get(self, "logicalTableMap"))

    @logical_table_map.setter
    def logical_table_map(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.LogicalTableProperty"]]]],
    ) -> None:
        jsii.set(self, "logicalTableMap", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ResourcePermissionProperty"]]]]:
        '''``AWS::QuickSight::DataSet.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-permissions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ResourcePermissionProperty"]]]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ResourcePermissionProperty"]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="physicalTableMap")
    def physical_table_map(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.PhysicalTableProperty"]]]]:
        '''``AWS::QuickSight::DataSet.PhysicalTableMap``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-physicaltablemap
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.PhysicalTableProperty"]]]], jsii.get(self, "physicalTableMap"))

    @physical_table_map.setter
    def physical_table_map(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.PhysicalTableProperty"]]]],
    ) -> None:
        jsii.set(self, "physicalTableMap", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rowLevelPermissionDataSet")
    def row_level_permission_data_set(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RowLevelPermissionDataSetProperty"]]:
        '''``AWS::QuickSight::DataSet.RowLevelPermissionDataSet``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RowLevelPermissionDataSetProperty"]], jsii.get(self, "rowLevelPermissionDataSet"))

    @row_level_permission_data_set.setter
    def row_level_permission_data_set(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RowLevelPermissionDataSetProperty"]],
    ) -> None:
        jsii.set(self, "rowLevelPermissionDataSet", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.CalculatedColumnProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_id": "columnId",
            "column_name": "columnName",
            "expression": "expression",
        },
    )
    class CalculatedColumnProperty:
        def __init__(
            self,
            *,
            column_id: builtins.str,
            column_name: builtins.str,
            expression: builtins.str,
        ) -> None:
            '''
            :param column_id: ``CfnDataSet.CalculatedColumnProperty.ColumnId``.
            :param column_name: ``CfnDataSet.CalculatedColumnProperty.ColumnName``.
            :param expression: ``CfnDataSet.CalculatedColumnProperty.Expression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "column_id": column_id,
                "column_name": column_name,
                "expression": expression,
            }

        @builtins.property
        def column_id(self) -> builtins.str:
            '''``CfnDataSet.CalculatedColumnProperty.ColumnId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html#cfn-quicksight-dataset-calculatedcolumn-columnid
            '''
            result = self._values.get("column_id")
            assert result is not None, "Required property 'column_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_name(self) -> builtins.str:
            '''``CfnDataSet.CalculatedColumnProperty.ColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html#cfn-quicksight-dataset-calculatedcolumn-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def expression(self) -> builtins.str:
            '''``CfnDataSet.CalculatedColumnProperty.Expression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html#cfn-quicksight-dataset-calculatedcolumn-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CalculatedColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.CastColumnTypeOperationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_name": "columnName",
            "new_column_type": "newColumnType",
            "format": "format",
        },
    )
    class CastColumnTypeOperationProperty:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            new_column_type: builtins.str,
            format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param column_name: ``CfnDataSet.CastColumnTypeOperationProperty.ColumnName``.
            :param new_column_type: ``CfnDataSet.CastColumnTypeOperationProperty.NewColumnType``.
            :param format: ``CfnDataSet.CastColumnTypeOperationProperty.Format``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "column_name": column_name,
                "new_column_type": new_column_type,
            }
            if format is not None:
                self._values["format"] = format

        @builtins.property
        def column_name(self) -> builtins.str:
            '''``CfnDataSet.CastColumnTypeOperationProperty.ColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html#cfn-quicksight-dataset-castcolumntypeoperation-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def new_column_type(self) -> builtins.str:
            '''``CfnDataSet.CastColumnTypeOperationProperty.NewColumnType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html#cfn-quicksight-dataset-castcolumntypeoperation-newcolumntype
            '''
            result = self._values.get("new_column_type")
            assert result is not None, "Required property 'new_column_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def format(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.CastColumnTypeOperationProperty.Format``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html#cfn-quicksight-dataset-castcolumntypeoperation-format
            '''
            result = self._values.get("format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CastColumnTypeOperationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.ColumnDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={"text": "text"},
    )
    class ColumnDescriptionProperty:
        def __init__(self, *, text: typing.Optional[builtins.str] = None) -> None:
            '''
            :param text: ``CfnDataSet.ColumnDescriptionProperty.Text``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columndescription.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if text is not None:
                self._values["text"] = text

        @builtins.property
        def text(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.ColumnDescriptionProperty.Text``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columndescription.html#cfn-quicksight-dataset-columndescription-text
            '''
            result = self._values.get("text")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.ColumnGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"geo_spatial_column_group": "geoSpatialColumnGroup"},
    )
    class ColumnGroupProperty:
        def __init__(
            self,
            *,
            geo_spatial_column_group: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.GeoSpatialColumnGroupProperty"]] = None,
        ) -> None:
            '''
            :param geo_spatial_column_group: ``CfnDataSet.ColumnGroupProperty.GeoSpatialColumnGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columngroup.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if geo_spatial_column_group is not None:
                self._values["geo_spatial_column_group"] = geo_spatial_column_group

        @builtins.property
        def geo_spatial_column_group(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.GeoSpatialColumnGroupProperty"]]:
            '''``CfnDataSet.ColumnGroupProperty.GeoSpatialColumnGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columngroup.html#cfn-quicksight-dataset-columngroup-geospatialcolumngroup
            '''
            result = self._values.get("geo_spatial_column_group")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.GeoSpatialColumnGroupProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.ColumnLevelPermissionRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"column_names": "columnNames", "principals": "principals"},
    )
    class ColumnLevelPermissionRuleProperty:
        def __init__(
            self,
            *,
            column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param column_names: ``CfnDataSet.ColumnLevelPermissionRuleProperty.ColumnNames``.
            :param principals: ``CfnDataSet.ColumnLevelPermissionRuleProperty.Principals``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columnlevelpermissionrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if column_names is not None:
                self._values["column_names"] = column_names
            if principals is not None:
                self._values["principals"] = principals

        @builtins.property
        def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSet.ColumnLevelPermissionRuleProperty.ColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columnlevelpermissionrule.html#cfn-quicksight-dataset-columnlevelpermissionrule-columnnames
            '''
            result = self._values.get("column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def principals(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSet.ColumnLevelPermissionRuleProperty.Principals``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columnlevelpermissionrule.html#cfn-quicksight-dataset-columnlevelpermissionrule-principals
            '''
            result = self._values.get("principals")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnLevelPermissionRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.ColumnTagProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_description": "columnDescription",
            "column_geographic_role": "columnGeographicRole",
        },
    )
    class ColumnTagProperty:
        def __init__(
            self,
            *,
            column_description: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnDescriptionProperty"]] = None,
            column_geographic_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param column_description: ``CfnDataSet.ColumnTagProperty.ColumnDescription``.
            :param column_geographic_role: ``CfnDataSet.ColumnTagProperty.ColumnGeographicRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columntag.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if column_description is not None:
                self._values["column_description"] = column_description
            if column_geographic_role is not None:
                self._values["column_geographic_role"] = column_geographic_role

        @builtins.property
        def column_description(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnDescriptionProperty"]]:
            '''``CfnDataSet.ColumnTagProperty.ColumnDescription``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columntag.html#cfn-quicksight-dataset-columntag-columndescription
            '''
            result = self._values.get("column_description")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ColumnDescriptionProperty"]], result)

        @builtins.property
        def column_geographic_role(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.ColumnTagProperty.ColumnGeographicRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columntag.html#cfn-quicksight-dataset-columntag-columngeographicrole
            '''
            result = self._values.get("column_geographic_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.CreateColumnsOperationProperty",
        jsii_struct_bases=[],
        name_mapping={"columns": "columns"},
    )
    class CreateColumnsOperationProperty:
        def __init__(
            self,
            *,
            columns: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CalculatedColumnProperty"]]],
        ) -> None:
            '''
            :param columns: ``CfnDataSet.CreateColumnsOperationProperty.Columns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-createcolumnsoperation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "columns": columns,
            }

        @builtins.property
        def columns(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CalculatedColumnProperty"]]]:
            '''``CfnDataSet.CreateColumnsOperationProperty.Columns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-createcolumnsoperation.html#cfn-quicksight-dataset-createcolumnsoperation-columns
            '''
            result = self._values.get("columns")
            assert result is not None, "Required property 'columns' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CalculatedColumnProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreateColumnsOperationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.CustomSqlProperty",
        jsii_struct_bases=[],
        name_mapping={
            "columns": "columns",
            "data_source_arn": "dataSourceArn",
            "name": "name",
            "sql_query": "sqlQuery",
        },
    )
    class CustomSqlProperty:
        def __init__(
            self,
            *,
            columns: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.InputColumnProperty"]]],
            data_source_arn: builtins.str,
            name: builtins.str,
            sql_query: builtins.str,
        ) -> None:
            '''
            :param columns: ``CfnDataSet.CustomSqlProperty.Columns``.
            :param data_source_arn: ``CfnDataSet.CustomSqlProperty.DataSourceArn``.
            :param name: ``CfnDataSet.CustomSqlProperty.Name``.
            :param sql_query: ``CfnDataSet.CustomSqlProperty.SqlQuery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "columns": columns,
                "data_source_arn": data_source_arn,
                "name": name,
                "sql_query": sql_query,
            }

        @builtins.property
        def columns(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.InputColumnProperty"]]]:
            '''``CfnDataSet.CustomSqlProperty.Columns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-columns
            '''
            result = self._values.get("columns")
            assert result is not None, "Required property 'columns' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.InputColumnProperty"]]], result)

        @builtins.property
        def data_source_arn(self) -> builtins.str:
            '''``CfnDataSet.CustomSqlProperty.DataSourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-datasourcearn
            '''
            result = self._values.get("data_source_arn")
            assert result is not None, "Required property 'data_source_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDataSet.CustomSqlProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sql_query(self) -> builtins.str:
            '''``CfnDataSet.CustomSqlProperty.SqlQuery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-sqlquery
            '''
            result = self._values.get("sql_query")
            assert result is not None, "Required property 'sql_query' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomSqlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.FieldFolderProperty",
        jsii_struct_bases=[],
        name_mapping={"columns": "columns", "description": "description"},
    )
    class FieldFolderProperty:
        def __init__(
            self,
            *,
            columns: typing.Optional[typing.Sequence[builtins.str]] = None,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param columns: ``CfnDataSet.FieldFolderProperty.Columns``.
            :param description: ``CfnDataSet.FieldFolderProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-fieldfolder.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if columns is not None:
                self._values["columns"] = columns
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def columns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSet.FieldFolderProperty.Columns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-fieldfolder.html#cfn-quicksight-dataset-fieldfolder-columns
            '''
            result = self._values.get("columns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.FieldFolderProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-fieldfolder.html#cfn-quicksight-dataset-fieldfolder-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldFolderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.FilterOperationProperty",
        jsii_struct_bases=[],
        name_mapping={"condition_expression": "conditionExpression"},
    )
    class FilterOperationProperty:
        def __init__(self, *, condition_expression: builtins.str) -> None:
            '''
            :param condition_expression: ``CfnDataSet.FilterOperationProperty.ConditionExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-filteroperation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "condition_expression": condition_expression,
            }

        @builtins.property
        def condition_expression(self) -> builtins.str:
            '''``CfnDataSet.FilterOperationProperty.ConditionExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-filteroperation.html#cfn-quicksight-dataset-filteroperation-conditionexpression
            '''
            result = self._values.get("condition_expression")
            assert result is not None, "Required property 'condition_expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterOperationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.GeoSpatialColumnGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "columns": "columns",
            "name": "name",
            "country_code": "countryCode",
        },
    )
    class GeoSpatialColumnGroupProperty:
        def __init__(
            self,
            *,
            columns: typing.Sequence[builtins.str],
            name: builtins.str,
            country_code: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param columns: ``CfnDataSet.GeoSpatialColumnGroupProperty.Columns``.
            :param name: ``CfnDataSet.GeoSpatialColumnGroupProperty.Name``.
            :param country_code: ``CfnDataSet.GeoSpatialColumnGroupProperty.CountryCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "columns": columns,
                "name": name,
            }
            if country_code is not None:
                self._values["country_code"] = country_code

        @builtins.property
        def columns(self) -> typing.List[builtins.str]:
            '''``CfnDataSet.GeoSpatialColumnGroupProperty.Columns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html#cfn-quicksight-dataset-geospatialcolumngroup-columns
            '''
            result = self._values.get("columns")
            assert result is not None, "Required property 'columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDataSet.GeoSpatialColumnGroupProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html#cfn-quicksight-dataset-geospatialcolumngroup-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def country_code(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.GeoSpatialColumnGroupProperty.CountryCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html#cfn-quicksight-dataset-geospatialcolumngroup-countrycode
            '''
            result = self._values.get("country_code")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoSpatialColumnGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.IngestionWaitPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ingestion_wait_time_in_hours": "ingestionWaitTimeInHours",
            "wait_for_spice_ingestion": "waitForSpiceIngestion",
        },
    )
    class IngestionWaitPolicyProperty:
        def __init__(
            self,
            *,
            ingestion_wait_time_in_hours: typing.Optional[jsii.Number] = None,
            wait_for_spice_ingestion: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param ingestion_wait_time_in_hours: ``CfnDataSet.IngestionWaitPolicyProperty.IngestionWaitTimeInHours``.
            :param wait_for_spice_ingestion: ``CfnDataSet.IngestionWaitPolicyProperty.WaitForSpiceIngestion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-ingestionwaitpolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ingestion_wait_time_in_hours is not None:
                self._values["ingestion_wait_time_in_hours"] = ingestion_wait_time_in_hours
            if wait_for_spice_ingestion is not None:
                self._values["wait_for_spice_ingestion"] = wait_for_spice_ingestion

        @builtins.property
        def ingestion_wait_time_in_hours(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataSet.IngestionWaitPolicyProperty.IngestionWaitTimeInHours``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-ingestionwaitpolicy.html#cfn-quicksight-dataset-ingestionwaitpolicy-ingestionwaittimeinhours
            '''
            result = self._values.get("ingestion_wait_time_in_hours")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def wait_for_spice_ingestion(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDataSet.IngestionWaitPolicyProperty.WaitForSpiceIngestion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-ingestionwaitpolicy.html#cfn-quicksight-dataset-ingestionwaitpolicy-waitforspiceingestion
            '''
            result = self._values.get("wait_for_spice_ingestion")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IngestionWaitPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.InputColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "type": "type"},
    )
    class InputColumnProperty:
        def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
            '''
            :param name: ``CfnDataSet.InputColumnProperty.Name``.
            :param type: ``CfnDataSet.InputColumnProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-inputcolumn.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "type": type,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDataSet.InputColumnProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-inputcolumn.html#cfn-quicksight-dataset-inputcolumn-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDataSet.InputColumnProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-inputcolumn.html#cfn-quicksight-dataset-inputcolumn-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.JoinInstructionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "left_operand": "leftOperand",
            "on_clause": "onClause",
            "right_operand": "rightOperand",
            "type": "type",
            "left_join_key_properties": "leftJoinKeyProperties",
            "right_join_key_properties": "rightJoinKeyProperties",
        },
    )
    class JoinInstructionProperty:
        def __init__(
            self,
            *,
            left_operand: builtins.str,
            on_clause: builtins.str,
            right_operand: builtins.str,
            type: builtins.str,
            left_join_key_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.JoinKeyPropertiesProperty"]] = None,
            right_join_key_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.JoinKeyPropertiesProperty"]] = None,
        ) -> None:
            '''
            :param left_operand: ``CfnDataSet.JoinInstructionProperty.LeftOperand``.
            :param on_clause: ``CfnDataSet.JoinInstructionProperty.OnClause``.
            :param right_operand: ``CfnDataSet.JoinInstructionProperty.RightOperand``.
            :param type: ``CfnDataSet.JoinInstructionProperty.Type``.
            :param left_join_key_properties: ``CfnDataSet.JoinInstructionProperty.LeftJoinKeyProperties``.
            :param right_join_key_properties: ``CfnDataSet.JoinInstructionProperty.RightJoinKeyProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "left_operand": left_operand,
                "on_clause": on_clause,
                "right_operand": right_operand,
                "type": type,
            }
            if left_join_key_properties is not None:
                self._values["left_join_key_properties"] = left_join_key_properties
            if right_join_key_properties is not None:
                self._values["right_join_key_properties"] = right_join_key_properties

        @builtins.property
        def left_operand(self) -> builtins.str:
            '''``CfnDataSet.JoinInstructionProperty.LeftOperand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-leftoperand
            '''
            result = self._values.get("left_operand")
            assert result is not None, "Required property 'left_operand' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def on_clause(self) -> builtins.str:
            '''``CfnDataSet.JoinInstructionProperty.OnClause``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-onclause
            '''
            result = self._values.get("on_clause")
            assert result is not None, "Required property 'on_clause' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def right_operand(self) -> builtins.str:
            '''``CfnDataSet.JoinInstructionProperty.RightOperand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-rightoperand
            '''
            result = self._values.get("right_operand")
            assert result is not None, "Required property 'right_operand' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDataSet.JoinInstructionProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def left_join_key_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.JoinKeyPropertiesProperty"]]:
            '''``CfnDataSet.JoinInstructionProperty.LeftJoinKeyProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-leftjoinkeyproperties
            '''
            result = self._values.get("left_join_key_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.JoinKeyPropertiesProperty"]], result)

        @builtins.property
        def right_join_key_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.JoinKeyPropertiesProperty"]]:
            '''``CfnDataSet.JoinInstructionProperty.RightJoinKeyProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-rightjoinkeyproperties
            '''
            result = self._values.get("right_join_key_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.JoinKeyPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JoinInstructionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.JoinKeyPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"unique_key": "uniqueKey"},
    )
    class JoinKeyPropertiesProperty:
        def __init__(
            self,
            *,
            unique_key: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param unique_key: ``CfnDataSet.JoinKeyPropertiesProperty.UniqueKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joinkeyproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if unique_key is not None:
                self._values["unique_key"] = unique_key

        @builtins.property
        def unique_key(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDataSet.JoinKeyPropertiesProperty.UniqueKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joinkeyproperties.html#cfn-quicksight-dataset-joinkeyproperties-uniquekey
            '''
            result = self._values.get("unique_key")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JoinKeyPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.LogicalTableProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alias": "alias",
            "source": "source",
            "data_transforms": "dataTransforms",
        },
    )
    class LogicalTableProperty:
        def __init__(
            self,
            *,
            alias: builtins.str,
            source: typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.LogicalTableSourceProperty"],
            data_transforms: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.TransformOperationProperty"]]]] = None,
        ) -> None:
            '''
            :param alias: ``CfnDataSet.LogicalTableProperty.Alias``.
            :param source: ``CfnDataSet.LogicalTableProperty.Source``.
            :param data_transforms: ``CfnDataSet.LogicalTableProperty.DataTransforms``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "alias": alias,
                "source": source,
            }
            if data_transforms is not None:
                self._values["data_transforms"] = data_transforms

        @builtins.property
        def alias(self) -> builtins.str:
            '''``CfnDataSet.LogicalTableProperty.Alias``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html#cfn-quicksight-dataset-logicaltable-alias
            '''
            result = self._values.get("alias")
            assert result is not None, "Required property 'alias' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.LogicalTableSourceProperty"]:
            '''``CfnDataSet.LogicalTableProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html#cfn-quicksight-dataset-logicaltable-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.LogicalTableSourceProperty"], result)

        @builtins.property
        def data_transforms(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.TransformOperationProperty"]]]]:
            '''``CfnDataSet.LogicalTableProperty.DataTransforms``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html#cfn-quicksight-dataset-logicaltable-datatransforms
            '''
            result = self._values.get("data_transforms")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.TransformOperationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogicalTableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.LogicalTableSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "join_instruction": "joinInstruction",
            "physical_table_id": "physicalTableId",
        },
    )
    class LogicalTableSourceProperty:
        def __init__(
            self,
            *,
            join_instruction: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.JoinInstructionProperty"]] = None,
            physical_table_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param join_instruction: ``CfnDataSet.LogicalTableSourceProperty.JoinInstruction``.
            :param physical_table_id: ``CfnDataSet.LogicalTableSourceProperty.PhysicalTableId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltablesource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if join_instruction is not None:
                self._values["join_instruction"] = join_instruction
            if physical_table_id is not None:
                self._values["physical_table_id"] = physical_table_id

        @builtins.property
        def join_instruction(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.JoinInstructionProperty"]]:
            '''``CfnDataSet.LogicalTableSourceProperty.JoinInstruction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltablesource.html#cfn-quicksight-dataset-logicaltablesource-joininstruction
            '''
            result = self._values.get("join_instruction")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.JoinInstructionProperty"]], result)

        @builtins.property
        def physical_table_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.LogicalTableSourceProperty.PhysicalTableId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltablesource.html#cfn-quicksight-dataset-logicaltablesource-physicaltableid
            '''
            result = self._values.get("physical_table_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogicalTableSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.OutputColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"description": "description", "name": "name", "type": "type"},
    )
    class OutputColumnProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param description: ``CfnDataSet.OutputColumnProperty.Description``.
            :param name: ``CfnDataSet.OutputColumnProperty.Name``.
            :param type: ``CfnDataSet.OutputColumnProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if description is not None:
                self._values["description"] = description
            if name is not None:
                self._values["name"] = name
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.OutputColumnProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html#cfn-quicksight-dataset-outputcolumn-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.OutputColumnProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html#cfn-quicksight-dataset-outputcolumn-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.OutputColumnProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html#cfn-quicksight-dataset-outputcolumn-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.PhysicalTableProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_sql": "customSql",
            "relational_table": "relationalTable",
            "s3_source": "s3Source",
        },
    )
    class PhysicalTableProperty:
        def __init__(
            self,
            *,
            custom_sql: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CustomSqlProperty"]] = None,
            relational_table: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RelationalTableProperty"]] = None,
            s3_source: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.S3SourceProperty"]] = None,
        ) -> None:
            '''
            :param custom_sql: ``CfnDataSet.PhysicalTableProperty.CustomSql``.
            :param relational_table: ``CfnDataSet.PhysicalTableProperty.RelationalTable``.
            :param s3_source: ``CfnDataSet.PhysicalTableProperty.S3Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_sql is not None:
                self._values["custom_sql"] = custom_sql
            if relational_table is not None:
                self._values["relational_table"] = relational_table
            if s3_source is not None:
                self._values["s3_source"] = s3_source

        @builtins.property
        def custom_sql(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CustomSqlProperty"]]:
            '''``CfnDataSet.PhysicalTableProperty.CustomSql``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html#cfn-quicksight-dataset-physicaltable-customsql
            '''
            result = self._values.get("custom_sql")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CustomSqlProperty"]], result)

        @builtins.property
        def relational_table(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RelationalTableProperty"]]:
            '''``CfnDataSet.PhysicalTableProperty.RelationalTable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html#cfn-quicksight-dataset-physicaltable-relationaltable
            '''
            result = self._values.get("relational_table")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RelationalTableProperty"]], result)

        @builtins.property
        def s3_source(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.S3SourceProperty"]]:
            '''``CfnDataSet.PhysicalTableProperty.S3Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html#cfn-quicksight-dataset-physicaltable-s3source
            '''
            result = self._values.get("s3_source")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.S3SourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhysicalTableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.ProjectOperationProperty",
        jsii_struct_bases=[],
        name_mapping={"projected_columns": "projectedColumns"},
    )
    class ProjectOperationProperty:
        def __init__(self, *, projected_columns: typing.Sequence[builtins.str]) -> None:
            '''
            :param projected_columns: ``CfnDataSet.ProjectOperationProperty.ProjectedColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-projectoperation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "projected_columns": projected_columns,
            }

        @builtins.property
        def projected_columns(self) -> typing.List[builtins.str]:
            '''``CfnDataSet.ProjectOperationProperty.ProjectedColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-projectoperation.html#cfn-quicksight-dataset-projectoperation-projectedcolumns
            '''
            result = self._values.get("projected_columns")
            assert result is not None, "Required property 'projected_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProjectOperationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.RelationalTableProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_arn": "dataSourceArn",
            "input_columns": "inputColumns",
            "name": "name",
            "catalog": "catalog",
            "schema": "schema",
        },
    )
    class RelationalTableProperty:
        def __init__(
            self,
            *,
            data_source_arn: builtins.str,
            input_columns: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.InputColumnProperty"]]],
            name: builtins.str,
            catalog: typing.Optional[builtins.str] = None,
            schema: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_source_arn: ``CfnDataSet.RelationalTableProperty.DataSourceArn``.
            :param input_columns: ``CfnDataSet.RelationalTableProperty.InputColumns``.
            :param name: ``CfnDataSet.RelationalTableProperty.Name``.
            :param catalog: ``CfnDataSet.RelationalTableProperty.Catalog``.
            :param schema: ``CfnDataSet.RelationalTableProperty.Schema``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_source_arn": data_source_arn,
                "input_columns": input_columns,
                "name": name,
            }
            if catalog is not None:
                self._values["catalog"] = catalog
            if schema is not None:
                self._values["schema"] = schema

        @builtins.property
        def data_source_arn(self) -> builtins.str:
            '''``CfnDataSet.RelationalTableProperty.DataSourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-datasourcearn
            '''
            result = self._values.get("data_source_arn")
            assert result is not None, "Required property 'data_source_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input_columns(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.InputColumnProperty"]]]:
            '''``CfnDataSet.RelationalTableProperty.InputColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-inputcolumns
            '''
            result = self._values.get("input_columns")
            assert result is not None, "Required property 'input_columns' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.InputColumnProperty"]]], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDataSet.RelationalTableProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def catalog(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.RelationalTableProperty.Catalog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-catalog
            '''
            result = self._values.get("catalog")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.RelationalTableProperty.Schema``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-schema
            '''
            result = self._values.get("schema")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalTableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.RenameColumnOperationProperty",
        jsii_struct_bases=[],
        name_mapping={"column_name": "columnName", "new_column_name": "newColumnName"},
    )
    class RenameColumnOperationProperty:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            new_column_name: builtins.str,
        ) -> None:
            '''
            :param column_name: ``CfnDataSet.RenameColumnOperationProperty.ColumnName``.
            :param new_column_name: ``CfnDataSet.RenameColumnOperationProperty.NewColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-renamecolumnoperation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "column_name": column_name,
                "new_column_name": new_column_name,
            }

        @builtins.property
        def column_name(self) -> builtins.str:
            '''``CfnDataSet.RenameColumnOperationProperty.ColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-renamecolumnoperation.html#cfn-quicksight-dataset-renamecolumnoperation-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def new_column_name(self) -> builtins.str:
            '''``CfnDataSet.RenameColumnOperationProperty.NewColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-renamecolumnoperation.html#cfn-quicksight-dataset-renamecolumnoperation-newcolumnname
            '''
            result = self._values.get("new_column_name")
            assert result is not None, "Required property 'new_column_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RenameColumnOperationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            principal: builtins.str,
        ) -> None:
            '''
            :param actions: ``CfnDataSet.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnDataSet.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-resourcepermission.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''``CfnDataSet.ResourcePermissionProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-resourcepermission.html#cfn-quicksight-dataset-resourcepermission-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def principal(self) -> builtins.str:
            '''``CfnDataSet.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-resourcepermission.html#cfn-quicksight-dataset-resourcepermission-principal
            '''
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.RowLevelPermissionDataSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "permission_policy": "permissionPolicy",
            "format_version": "formatVersion",
            "namespace": "namespace",
        },
    )
    class RowLevelPermissionDataSetProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            permission_policy: builtins.str,
            format_version: typing.Optional[builtins.str] = None,
            namespace: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param arn: ``CfnDataSet.RowLevelPermissionDataSetProperty.Arn``.
            :param permission_policy: ``CfnDataSet.RowLevelPermissionDataSetProperty.PermissionPolicy``.
            :param format_version: ``CfnDataSet.RowLevelPermissionDataSetProperty.FormatVersion``.
            :param namespace: ``CfnDataSet.RowLevelPermissionDataSetProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "permission_policy": permission_policy,
            }
            if format_version is not None:
                self._values["format_version"] = format_version
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def arn(self) -> builtins.str:
            '''``CfnDataSet.RowLevelPermissionDataSetProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def permission_policy(self) -> builtins.str:
            '''``CfnDataSet.RowLevelPermissionDataSetProperty.PermissionPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-permissionpolicy
            '''
            result = self._values.get("permission_policy")
            assert result is not None, "Required property 'permission_policy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def format_version(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.RowLevelPermissionDataSetProperty.FormatVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-formatversion
            '''
            result = self._values.get("format_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.RowLevelPermissionDataSetProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RowLevelPermissionDataSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.S3SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_arn": "dataSourceArn",
            "input_columns": "inputColumns",
            "upload_settings": "uploadSettings",
        },
    )
    class S3SourceProperty:
        def __init__(
            self,
            *,
            data_source_arn: builtins.str,
            input_columns: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.InputColumnProperty"]]],
            upload_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.UploadSettingsProperty"]] = None,
        ) -> None:
            '''
            :param data_source_arn: ``CfnDataSet.S3SourceProperty.DataSourceArn``.
            :param input_columns: ``CfnDataSet.S3SourceProperty.InputColumns``.
            :param upload_settings: ``CfnDataSet.S3SourceProperty.UploadSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_source_arn": data_source_arn,
                "input_columns": input_columns,
            }
            if upload_settings is not None:
                self._values["upload_settings"] = upload_settings

        @builtins.property
        def data_source_arn(self) -> builtins.str:
            '''``CfnDataSet.S3SourceProperty.DataSourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html#cfn-quicksight-dataset-s3source-datasourcearn
            '''
            result = self._values.get("data_source_arn")
            assert result is not None, "Required property 'data_source_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input_columns(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.InputColumnProperty"]]]:
            '''``CfnDataSet.S3SourceProperty.InputColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html#cfn-quicksight-dataset-s3source-inputcolumns
            '''
            result = self._values.get("input_columns")
            assert result is not None, "Required property 'input_columns' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.InputColumnProperty"]]], result)

        @builtins.property
        def upload_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.UploadSettingsProperty"]]:
            '''``CfnDataSet.S3SourceProperty.UploadSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html#cfn-quicksight-dataset-s3source-uploadsettings
            '''
            result = self._values.get("upload_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.UploadSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.TagColumnOperationProperty",
        jsii_struct_bases=[],
        name_mapping={"column_name": "columnName", "tags": "tags"},
    )
    class TagColumnOperationProperty:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            tags: typing.Sequence["CfnDataSet.ColumnTagProperty"],
        ) -> None:
            '''
            :param column_name: ``CfnDataSet.TagColumnOperationProperty.ColumnName``.
            :param tags: ``CfnDataSet.TagColumnOperationProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-tagcolumnoperation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "column_name": column_name,
                "tags": tags,
            }

        @builtins.property
        def column_name(self) -> builtins.str:
            '''``CfnDataSet.TagColumnOperationProperty.ColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-tagcolumnoperation.html#cfn-quicksight-dataset-tagcolumnoperation-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tags(self) -> typing.List["CfnDataSet.ColumnTagProperty"]:
            '''``CfnDataSet.TagColumnOperationProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-tagcolumnoperation.html#cfn-quicksight-dataset-tagcolumnoperation-tags
            '''
            result = self._values.get("tags")
            assert result is not None, "Required property 'tags' is missing"
            return typing.cast(typing.List["CfnDataSet.ColumnTagProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagColumnOperationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.TransformOperationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cast_column_type_operation": "castColumnTypeOperation",
            "create_columns_operation": "createColumnsOperation",
            "filter_operation": "filterOperation",
            "project_operation": "projectOperation",
            "rename_column_operation": "renameColumnOperation",
            "tag_column_operation": "tagColumnOperation",
        },
    )
    class TransformOperationProperty:
        def __init__(
            self,
            *,
            cast_column_type_operation: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CastColumnTypeOperationProperty"]] = None,
            create_columns_operation: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CreateColumnsOperationProperty"]] = None,
            filter_operation: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.FilterOperationProperty"]] = None,
            project_operation: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ProjectOperationProperty"]] = None,
            rename_column_operation: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RenameColumnOperationProperty"]] = None,
            tag_column_operation: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.TagColumnOperationProperty"]] = None,
        ) -> None:
            '''
            :param cast_column_type_operation: ``CfnDataSet.TransformOperationProperty.CastColumnTypeOperation``.
            :param create_columns_operation: ``CfnDataSet.TransformOperationProperty.CreateColumnsOperation``.
            :param filter_operation: ``CfnDataSet.TransformOperationProperty.FilterOperation``.
            :param project_operation: ``CfnDataSet.TransformOperationProperty.ProjectOperation``.
            :param rename_column_operation: ``CfnDataSet.TransformOperationProperty.RenameColumnOperation``.
            :param tag_column_operation: ``CfnDataSet.TransformOperationProperty.TagColumnOperation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cast_column_type_operation is not None:
                self._values["cast_column_type_operation"] = cast_column_type_operation
            if create_columns_operation is not None:
                self._values["create_columns_operation"] = create_columns_operation
            if filter_operation is not None:
                self._values["filter_operation"] = filter_operation
            if project_operation is not None:
                self._values["project_operation"] = project_operation
            if rename_column_operation is not None:
                self._values["rename_column_operation"] = rename_column_operation
            if tag_column_operation is not None:
                self._values["tag_column_operation"] = tag_column_operation

        @builtins.property
        def cast_column_type_operation(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CastColumnTypeOperationProperty"]]:
            '''``CfnDataSet.TransformOperationProperty.CastColumnTypeOperation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-castcolumntypeoperation
            '''
            result = self._values.get("cast_column_type_operation")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CastColumnTypeOperationProperty"]], result)

        @builtins.property
        def create_columns_operation(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CreateColumnsOperationProperty"]]:
            '''``CfnDataSet.TransformOperationProperty.CreateColumnsOperation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-createcolumnsoperation
            '''
            result = self._values.get("create_columns_operation")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.CreateColumnsOperationProperty"]], result)

        @builtins.property
        def filter_operation(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.FilterOperationProperty"]]:
            '''``CfnDataSet.TransformOperationProperty.FilterOperation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-filteroperation
            '''
            result = self._values.get("filter_operation")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.FilterOperationProperty"]], result)

        @builtins.property
        def project_operation(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ProjectOperationProperty"]]:
            '''``CfnDataSet.TransformOperationProperty.ProjectOperation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-projectoperation
            '''
            result = self._values.get("project_operation")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.ProjectOperationProperty"]], result)

        @builtins.property
        def rename_column_operation(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RenameColumnOperationProperty"]]:
            '''``CfnDataSet.TransformOperationProperty.RenameColumnOperation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-renamecolumnoperation
            '''
            result = self._values.get("rename_column_operation")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.RenameColumnOperationProperty"]], result)

        @builtins.property
        def tag_column_operation(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.TagColumnOperationProperty"]]:
            '''``CfnDataSet.TransformOperationProperty.TagColumnOperation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-tagcolumnoperation
            '''
            result = self._values.get("tag_column_operation")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSet.TagColumnOperationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransformOperationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSet.UploadSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "contains_header": "containsHeader",
            "delimiter": "delimiter",
            "format": "format",
            "start_from_row": "startFromRow",
            "text_qualifier": "textQualifier",
        },
    )
    class UploadSettingsProperty:
        def __init__(
            self,
            *,
            contains_header: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            delimiter: typing.Optional[builtins.str] = None,
            format: typing.Optional[builtins.str] = None,
            start_from_row: typing.Optional[jsii.Number] = None,
            text_qualifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param contains_header: ``CfnDataSet.UploadSettingsProperty.ContainsHeader``.
            :param delimiter: ``CfnDataSet.UploadSettingsProperty.Delimiter``.
            :param format: ``CfnDataSet.UploadSettingsProperty.Format``.
            :param start_from_row: ``CfnDataSet.UploadSettingsProperty.StartFromRow``.
            :param text_qualifier: ``CfnDataSet.UploadSettingsProperty.TextQualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if contains_header is not None:
                self._values["contains_header"] = contains_header
            if delimiter is not None:
                self._values["delimiter"] = delimiter
            if format is not None:
                self._values["format"] = format
            if start_from_row is not None:
                self._values["start_from_row"] = start_from_row
            if text_qualifier is not None:
                self._values["text_qualifier"] = text_qualifier

        @builtins.property
        def contains_header(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDataSet.UploadSettingsProperty.ContainsHeader``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-containsheader
            '''
            result = self._values.get("contains_header")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def delimiter(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.UploadSettingsProperty.Delimiter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-delimiter
            '''
            result = self._values.get("delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.UploadSettingsProperty.Format``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-format
            '''
            result = self._values.get("format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_from_row(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataSet.UploadSettingsProperty.StartFromRow``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-startfromrow
            '''
            result = self._values.get("start_from_row")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def text_qualifier(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSet.UploadSettingsProperty.TextQualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-textqualifier
            '''
            result = self._values.get("text_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UploadSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-quicksight.CfnDataSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "column_groups": "columnGroups",
        "column_level_permission_rules": "columnLevelPermissionRules",
        "data_set_id": "dataSetId",
        "field_folders": "fieldFolders",
        "import_mode": "importMode",
        "ingestion_wait_policy": "ingestionWaitPolicy",
        "logical_table_map": "logicalTableMap",
        "name": "name",
        "permissions": "permissions",
        "physical_table_map": "physicalTableMap",
        "row_level_permission_data_set": "rowLevelPermissionDataSet",
        "tags": "tags",
    },
)
class CfnDataSetProps:
    def __init__(
        self,
        *,
        aws_account_id: typing.Optional[builtins.str] = None,
        column_groups: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.ColumnGroupProperty]]]] = None,
        column_level_permission_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.ColumnLevelPermissionRuleProperty]]]] = None,
        data_set_id: typing.Optional[builtins.str] = None,
        field_folders: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnDataSet.FieldFolderProperty]]]] = None,
        import_mode: typing.Optional[builtins.str] = None,
        ingestion_wait_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.IngestionWaitPolicyProperty]] = None,
        logical_table_map: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnDataSet.LogicalTableProperty]]]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.ResourcePermissionProperty]]]] = None,
        physical_table_map: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnDataSet.PhysicalTableProperty]]]] = None,
        row_level_permission_data_set: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.RowLevelPermissionDataSetProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::QuickSight::DataSet``.

        :param aws_account_id: ``AWS::QuickSight::DataSet.AwsAccountId``.
        :param column_groups: ``AWS::QuickSight::DataSet.ColumnGroups``.
        :param column_level_permission_rules: ``AWS::QuickSight::DataSet.ColumnLevelPermissionRules``.
        :param data_set_id: ``AWS::QuickSight::DataSet.DataSetId``.
        :param field_folders: ``AWS::QuickSight::DataSet.FieldFolders``.
        :param import_mode: ``AWS::QuickSight::DataSet.ImportMode``.
        :param ingestion_wait_policy: ``AWS::QuickSight::DataSet.IngestionWaitPolicy``.
        :param logical_table_map: ``AWS::QuickSight::DataSet.LogicalTableMap``.
        :param name: ``AWS::QuickSight::DataSet.Name``.
        :param permissions: ``AWS::QuickSight::DataSet.Permissions``.
        :param physical_table_map: ``AWS::QuickSight::DataSet.PhysicalTableMap``.
        :param row_level_permission_data_set: ``AWS::QuickSight::DataSet.RowLevelPermissionDataSet``.
        :param tags: ``AWS::QuickSight::DataSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if column_groups is not None:
            self._values["column_groups"] = column_groups
        if column_level_permission_rules is not None:
            self._values["column_level_permission_rules"] = column_level_permission_rules
        if data_set_id is not None:
            self._values["data_set_id"] = data_set_id
        if field_folders is not None:
            self._values["field_folders"] = field_folders
        if import_mode is not None:
            self._values["import_mode"] = import_mode
        if ingestion_wait_policy is not None:
            self._values["ingestion_wait_policy"] = ingestion_wait_policy
        if logical_table_map is not None:
            self._values["logical_table_map"] = logical_table_map
        if name is not None:
            self._values["name"] = name
        if permissions is not None:
            self._values["permissions"] = permissions
        if physical_table_map is not None:
            self._values["physical_table_map"] = physical_table_map
        if row_level_permission_data_set is not None:
            self._values["row_level_permission_data_set"] = row_level_permission_data_set
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSet.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-awsaccountid
        '''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column_groups(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.ColumnGroupProperty]]]]:
        '''``AWS::QuickSight::DataSet.ColumnGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columngroups
        '''
        result = self._values.get("column_groups")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.ColumnGroupProperty]]]], result)

    @builtins.property
    def column_level_permission_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.ColumnLevelPermissionRuleProperty]]]]:
        '''``AWS::QuickSight::DataSet.ColumnLevelPermissionRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columnlevelpermissionrules
        '''
        result = self._values.get("column_level_permission_rules")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.ColumnLevelPermissionRuleProperty]]]], result)

    @builtins.property
    def data_set_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSet.DataSetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-datasetid
        '''
        result = self._values.get("data_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_folders(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnDataSet.FieldFolderProperty]]]]:
        '''``AWS::QuickSight::DataSet.FieldFolders``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-fieldfolders
        '''
        result = self._values.get("field_folders")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnDataSet.FieldFolderProperty]]]], result)

    @builtins.property
    def import_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSet.ImportMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-importmode
        '''
        result = self._values.get("import_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_wait_policy(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.IngestionWaitPolicyProperty]]:
        '''``AWS::QuickSight::DataSet.IngestionWaitPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-ingestionwaitpolicy
        '''
        result = self._values.get("ingestion_wait_policy")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.IngestionWaitPolicyProperty]], result)

    @builtins.property
    def logical_table_map(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnDataSet.LogicalTableProperty]]]]:
        '''``AWS::QuickSight::DataSet.LogicalTableMap``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-logicaltablemap
        '''
        result = self._values.get("logical_table_map")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnDataSet.LogicalTableProperty]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.ResourcePermissionProperty]]]]:
        '''``AWS::QuickSight::DataSet.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.ResourcePermissionProperty]]]], result)

    @builtins.property
    def physical_table_map(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnDataSet.PhysicalTableProperty]]]]:
        '''``AWS::QuickSight::DataSet.PhysicalTableMap``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-physicaltablemap
        '''
        result = self._values.get("physical_table_map")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnDataSet.PhysicalTableProperty]]]], result)

    @builtins.property
    def row_level_permission_data_set(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.RowLevelPermissionDataSetProperty]]:
        '''``AWS::QuickSight::DataSet.RowLevelPermissionDataSet``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset
        '''
        result = self._values.get("row_level_permission_data_set")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSet.RowLevelPermissionDataSetProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::QuickSight::DataSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDataSource(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-quicksight.CfnDataSource",
):
    '''A CloudFormation ``AWS::QuickSight::DataSource``.

    :cloudformationResource: AWS::QuickSight::DataSource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        alternate_data_source_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]]]] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.DataSourceCredentialsProperty"]] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        data_source_parameters: typing.Optional[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]] = None,
        error_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.DataSourceErrorInfoProperty"]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.ResourcePermissionProperty"]]]] = None,
        ssl_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SslPropertiesProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        type: typing.Optional[builtins.str] = None,
        vpc_connection_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.VpcConnectionPropertiesProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::QuickSight::DataSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param alternate_data_source_parameters: ``AWS::QuickSight::DataSource.AlternateDataSourceParameters``.
        :param aws_account_id: ``AWS::QuickSight::DataSource.AwsAccountId``.
        :param credentials: ``AWS::QuickSight::DataSource.Credentials``.
        :param data_source_id: ``AWS::QuickSight::DataSource.DataSourceId``.
        :param data_source_parameters: ``AWS::QuickSight::DataSource.DataSourceParameters``.
        :param error_info: ``AWS::QuickSight::DataSource.ErrorInfo``.
        :param name: ``AWS::QuickSight::DataSource.Name``.
        :param permissions: ``AWS::QuickSight::DataSource.Permissions``.
        :param ssl_properties: ``AWS::QuickSight::DataSource.SslProperties``.
        :param tags: ``AWS::QuickSight::DataSource.Tags``.
        :param type: ``AWS::QuickSight::DataSource.Type``.
        :param vpc_connection_properties: ``AWS::QuickSight::DataSource.VpcConnectionProperties``.
        '''
        props = CfnDataSourceProps(
            alternate_data_source_parameters=alternate_data_source_parameters,
            aws_account_id=aws_account_id,
            credentials=credentials,
            data_source_id=data_source_id,
            data_source_parameters=data_source_parameters,
            error_info=error_info,
            name=name,
            permissions=permissions,
            ssl_properties=ssl_properties,
            tags=tags,
            type=type,
            vpc_connection_properties=vpc_connection_properties,
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::QuickSight::DataSource.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alternateDataSourceParameters")
    def alternate_data_source_parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::QuickSight::DataSource.AlternateDataSourceParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-alternatedatasourceparameters
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "alternateDataSourceParameters"))

    @alternate_data_source_parameters.setter
    def alternate_data_source_parameters(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "alternateDataSourceParameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSource.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-awsaccountid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="credentials")
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.DataSourceCredentialsProperty"]]:
        '''``AWS::QuickSight::DataSource.Credentials``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-credentials
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.DataSourceCredentialsProperty"]], jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.DataSourceCredentialsProperty"]],
    ) -> None:
        jsii.set(self, "credentials", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSourceId")
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSource.DataSourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-datasourceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceId"))

    @data_source_id.setter
    def data_source_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dataSourceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSourceParameters")
    def data_source_parameters(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::QuickSight::DataSource.DataSourceParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-datasourceparameters
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]], jsii.get(self, "dataSourceParameters"))

    @data_source_parameters.setter
    def data_source_parameters(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "dataSourceParameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="errorInfo")
    def error_info(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.DataSourceErrorInfoProperty"]]:
        '''``AWS::QuickSight::DataSource.ErrorInfo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-errorinfo
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.DataSourceErrorInfoProperty"]], jsii.get(self, "errorInfo"))

    @error_info.setter
    def error_info(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.DataSourceErrorInfoProperty"]],
    ) -> None:
        jsii.set(self, "errorInfo", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSource.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.ResourcePermissionProperty"]]]]:
        '''``AWS::QuickSight::DataSource.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-permissions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.ResourcePermissionProperty"]]]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.ResourcePermissionProperty"]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sslProperties")
    def ssl_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SslPropertiesProperty"]]:
        '''``AWS::QuickSight::DataSource.SslProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-sslproperties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SslPropertiesProperty"]], jsii.get(self, "sslProperties"))

    @ssl_properties.setter
    def ssl_properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SslPropertiesProperty"]],
    ) -> None:
        jsii.set(self, "sslProperties", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSource.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConnectionProperties")
    def vpc_connection_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.VpcConnectionPropertiesProperty"]]:
        '''``AWS::QuickSight::DataSource.VpcConnectionProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-vpcconnectionproperties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.VpcConnectionPropertiesProperty"]], jsii.get(self, "vpcConnectionProperties"))

    @vpc_connection_properties.setter
    def vpc_connection_properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.VpcConnectionPropertiesProperty"]],
    ) -> None:
        jsii.set(self, "vpcConnectionProperties", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.AmazonElasticsearchParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"domain": "domain"},
    )
    class AmazonElasticsearchParametersProperty:
        def __init__(self, *, domain: builtins.str) -> None:
            '''
            :param domain: ``CfnDataSource.AmazonElasticsearchParametersProperty.Domain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-amazonelasticsearchparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "domain": domain,
            }

        @builtins.property
        def domain(self) -> builtins.str:
            '''``CfnDataSource.AmazonElasticsearchParametersProperty.Domain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-amazonelasticsearchparameters.html#cfn-quicksight-datasource-amazonelasticsearchparameters-domain
            '''
            result = self._values.get("domain")
            assert result is not None, "Required property 'domain' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonElasticsearchParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.AthenaParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"work_group": "workGroup"},
    )
    class AthenaParametersProperty:
        def __init__(self, *, work_group: typing.Optional[builtins.str] = None) -> None:
            '''
            :param work_group: ``CfnDataSource.AthenaParametersProperty.WorkGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-athenaparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if work_group is not None:
                self._values["work_group"] = work_group

        @builtins.property
        def work_group(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.AthenaParametersProperty.WorkGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-athenaparameters.html#cfn-quicksight-datasource-athenaparameters-workgroup
            '''
            result = self._values.get("work_group")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AthenaParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.AuroraParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"database": "database", "host": "host", "port": "port"},
    )
    class AuroraParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param database: ``CfnDataSource.AuroraParametersProperty.Database``.
            :param host: ``CfnDataSource.AuroraParametersProperty.Host``.
            :param port: ``CfnDataSource.AuroraParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "host": host,
                "port": port,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.AuroraParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html#cfn-quicksight-datasource-auroraparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.AuroraParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html#cfn-quicksight-datasource-auroraparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.AuroraParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html#cfn-quicksight-datasource-auroraparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuroraParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.AuroraPostgreSqlParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"database": "database", "host": "host", "port": "port"},
    )
    class AuroraPostgreSqlParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param database: ``CfnDataSource.AuroraPostgreSqlParametersProperty.Database``.
            :param host: ``CfnDataSource.AuroraPostgreSqlParametersProperty.Host``.
            :param port: ``CfnDataSource.AuroraPostgreSqlParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "host": host,
                "port": port,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.AuroraPostgreSqlParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html#cfn-quicksight-datasource-aurorapostgresqlparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.AuroraPostgreSqlParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html#cfn-quicksight-datasource-aurorapostgresqlparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.AuroraPostgreSqlParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html#cfn-quicksight-datasource-aurorapostgresqlparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuroraPostgreSqlParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.CredentialPairProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password": "password",
            "username": "username",
            "alternate_data_source_parameters": "alternateDataSourceParameters",
        },
    )
    class CredentialPairProperty:
        def __init__(
            self,
            *,
            password: builtins.str,
            username: builtins.str,
            alternate_data_source_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]]]] = None,
        ) -> None:
            '''
            :param password: ``CfnDataSource.CredentialPairProperty.Password``.
            :param username: ``CfnDataSource.CredentialPairProperty.Username``.
            :param alternate_data_source_parameters: ``CfnDataSource.CredentialPairProperty.AlternateDataSourceParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "password": password,
                "username": username,
            }
            if alternate_data_source_parameters is not None:
                self._values["alternate_data_source_parameters"] = alternate_data_source_parameters

        @builtins.property
        def password(self) -> builtins.str:
            '''``CfnDataSource.CredentialPairProperty.Password``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html#cfn-quicksight-datasource-credentialpair-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def username(self) -> builtins.str:
            '''``CfnDataSource.CredentialPairProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html#cfn-quicksight-datasource-credentialpair-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def alternate_data_source_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]]]]:
            '''``CfnDataSource.CredentialPairProperty.AlternateDataSourceParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html#cfn-quicksight-datasource-credentialpair-alternatedatasourceparameters
            '''
            result = self._values.get("alternate_data_source_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataSource.DataSourceParametersProperty", aws_cdk.core.IResolvable]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CredentialPairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.DataSourceCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "copy_source_arn": "copySourceArn",
            "credential_pair": "credentialPair",
        },
    )
    class DataSourceCredentialsProperty:
        def __init__(
            self,
            *,
            copy_source_arn: typing.Optional[builtins.str] = None,
            credential_pair: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.CredentialPairProperty"]] = None,
        ) -> None:
            '''
            :param copy_source_arn: ``CfnDataSource.DataSourceCredentialsProperty.CopySourceArn``.
            :param credential_pair: ``CfnDataSource.DataSourceCredentialsProperty.CredentialPair``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourcecredentials.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if copy_source_arn is not None:
                self._values["copy_source_arn"] = copy_source_arn
            if credential_pair is not None:
                self._values["credential_pair"] = credential_pair

        @builtins.property
        def copy_source_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.DataSourceCredentialsProperty.CopySourceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourcecredentials.html#cfn-quicksight-datasource-datasourcecredentials-copysourcearn
            '''
            result = self._values.get("copy_source_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def credential_pair(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.CredentialPairProperty"]]:
            '''``CfnDataSource.DataSourceCredentialsProperty.CredentialPair``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourcecredentials.html#cfn-quicksight-datasource-datasourcecredentials-credentialpair
            '''
            result = self._values.get("credential_pair")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.CredentialPairProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.DataSourceErrorInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"message": "message", "type": "type"},
    )
    class DataSourceErrorInfoProperty:
        def __init__(
            self,
            *,
            message: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param message: ``CfnDataSource.DataSourceErrorInfoProperty.Message``.
            :param type: ``CfnDataSource.DataSourceErrorInfoProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceerrorinfo.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if message is not None:
                self._values["message"] = message
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.DataSourceErrorInfoProperty.Message``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceerrorinfo.html#cfn-quicksight-datasource-datasourceerrorinfo-message
            '''
            result = self._values.get("message")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.DataSourceErrorInfoProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceerrorinfo.html#cfn-quicksight-datasource-datasourceerrorinfo-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceErrorInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.DataSourceParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "amazon_elasticsearch_parameters": "amazonElasticsearchParameters",
            "athena_parameters": "athenaParameters",
            "aurora_parameters": "auroraParameters",
            "aurora_postgre_sql_parameters": "auroraPostgreSqlParameters",
            "maria_db_parameters": "mariaDbParameters",
            "my_sql_parameters": "mySqlParameters",
            "oracle_parameters": "oracleParameters",
            "postgre_sql_parameters": "postgreSqlParameters",
            "presto_parameters": "prestoParameters",
            "rds_parameters": "rdsParameters",
            "redshift_parameters": "redshiftParameters",
            "s3_parameters": "s3Parameters",
            "snowflake_parameters": "snowflakeParameters",
            "spark_parameters": "sparkParameters",
            "sql_server_parameters": "sqlServerParameters",
            "teradata_parameters": "teradataParameters",
        },
    )
    class DataSourceParametersProperty:
        def __init__(
            self,
            *,
            amazon_elasticsearch_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AmazonElasticsearchParametersProperty"]] = None,
            athena_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AthenaParametersProperty"]] = None,
            aurora_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AuroraParametersProperty"]] = None,
            aurora_postgre_sql_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AuroraPostgreSqlParametersProperty"]] = None,
            maria_db_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.MariaDbParametersProperty"]] = None,
            my_sql_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.MySqlParametersProperty"]] = None,
            oracle_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.OracleParametersProperty"]] = None,
            postgre_sql_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.PostgreSqlParametersProperty"]] = None,
            presto_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.PrestoParametersProperty"]] = None,
            rds_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.RdsParametersProperty"]] = None,
            redshift_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.RedshiftParametersProperty"]] = None,
            s3_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.S3ParametersProperty"]] = None,
            snowflake_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SnowflakeParametersProperty"]] = None,
            spark_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SparkParametersProperty"]] = None,
            sql_server_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SqlServerParametersProperty"]] = None,
            teradata_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.TeradataParametersProperty"]] = None,
        ) -> None:
            '''
            :param amazon_elasticsearch_parameters: ``CfnDataSource.DataSourceParametersProperty.AmazonElasticsearchParameters``.
            :param athena_parameters: ``CfnDataSource.DataSourceParametersProperty.AthenaParameters``.
            :param aurora_parameters: ``CfnDataSource.DataSourceParametersProperty.AuroraParameters``.
            :param aurora_postgre_sql_parameters: ``CfnDataSource.DataSourceParametersProperty.AuroraPostgreSqlParameters``.
            :param maria_db_parameters: ``CfnDataSource.DataSourceParametersProperty.MariaDbParameters``.
            :param my_sql_parameters: ``CfnDataSource.DataSourceParametersProperty.MySqlParameters``.
            :param oracle_parameters: ``CfnDataSource.DataSourceParametersProperty.OracleParameters``.
            :param postgre_sql_parameters: ``CfnDataSource.DataSourceParametersProperty.PostgreSqlParameters``.
            :param presto_parameters: ``CfnDataSource.DataSourceParametersProperty.PrestoParameters``.
            :param rds_parameters: ``CfnDataSource.DataSourceParametersProperty.RdsParameters``.
            :param redshift_parameters: ``CfnDataSource.DataSourceParametersProperty.RedshiftParameters``.
            :param s3_parameters: ``CfnDataSource.DataSourceParametersProperty.S3Parameters``.
            :param snowflake_parameters: ``CfnDataSource.DataSourceParametersProperty.SnowflakeParameters``.
            :param spark_parameters: ``CfnDataSource.DataSourceParametersProperty.SparkParameters``.
            :param sql_server_parameters: ``CfnDataSource.DataSourceParametersProperty.SqlServerParameters``.
            :param teradata_parameters: ``CfnDataSource.DataSourceParametersProperty.TeradataParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if amazon_elasticsearch_parameters is not None:
                self._values["amazon_elasticsearch_parameters"] = amazon_elasticsearch_parameters
            if athena_parameters is not None:
                self._values["athena_parameters"] = athena_parameters
            if aurora_parameters is not None:
                self._values["aurora_parameters"] = aurora_parameters
            if aurora_postgre_sql_parameters is not None:
                self._values["aurora_postgre_sql_parameters"] = aurora_postgre_sql_parameters
            if maria_db_parameters is not None:
                self._values["maria_db_parameters"] = maria_db_parameters
            if my_sql_parameters is not None:
                self._values["my_sql_parameters"] = my_sql_parameters
            if oracle_parameters is not None:
                self._values["oracle_parameters"] = oracle_parameters
            if postgre_sql_parameters is not None:
                self._values["postgre_sql_parameters"] = postgre_sql_parameters
            if presto_parameters is not None:
                self._values["presto_parameters"] = presto_parameters
            if rds_parameters is not None:
                self._values["rds_parameters"] = rds_parameters
            if redshift_parameters is not None:
                self._values["redshift_parameters"] = redshift_parameters
            if s3_parameters is not None:
                self._values["s3_parameters"] = s3_parameters
            if snowflake_parameters is not None:
                self._values["snowflake_parameters"] = snowflake_parameters
            if spark_parameters is not None:
                self._values["spark_parameters"] = spark_parameters
            if sql_server_parameters is not None:
                self._values["sql_server_parameters"] = sql_server_parameters
            if teradata_parameters is not None:
                self._values["teradata_parameters"] = teradata_parameters

        @builtins.property
        def amazon_elasticsearch_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AmazonElasticsearchParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.AmazonElasticsearchParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-amazonelasticsearchparameters
            '''
            result = self._values.get("amazon_elasticsearch_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AmazonElasticsearchParametersProperty"]], result)

        @builtins.property
        def athena_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AthenaParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.AthenaParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-athenaparameters
            '''
            result = self._values.get("athena_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AthenaParametersProperty"]], result)

        @builtins.property
        def aurora_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AuroraParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.AuroraParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-auroraparameters
            '''
            result = self._values.get("aurora_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AuroraParametersProperty"]], result)

        @builtins.property
        def aurora_postgre_sql_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AuroraPostgreSqlParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.AuroraPostgreSqlParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-aurorapostgresqlparameters
            '''
            result = self._values.get("aurora_postgre_sql_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.AuroraPostgreSqlParametersProperty"]], result)

        @builtins.property
        def maria_db_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.MariaDbParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.MariaDbParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-mariadbparameters
            '''
            result = self._values.get("maria_db_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.MariaDbParametersProperty"]], result)

        @builtins.property
        def my_sql_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.MySqlParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.MySqlParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-mysqlparameters
            '''
            result = self._values.get("my_sql_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.MySqlParametersProperty"]], result)

        @builtins.property
        def oracle_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.OracleParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.OracleParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-oracleparameters
            '''
            result = self._values.get("oracle_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.OracleParametersProperty"]], result)

        @builtins.property
        def postgre_sql_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.PostgreSqlParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.PostgreSqlParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-postgresqlparameters
            '''
            result = self._values.get("postgre_sql_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.PostgreSqlParametersProperty"]], result)

        @builtins.property
        def presto_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.PrestoParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.PrestoParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-prestoparameters
            '''
            result = self._values.get("presto_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.PrestoParametersProperty"]], result)

        @builtins.property
        def rds_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.RdsParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.RdsParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-rdsparameters
            '''
            result = self._values.get("rds_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.RdsParametersProperty"]], result)

        @builtins.property
        def redshift_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.RedshiftParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.RedshiftParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-redshiftparameters
            '''
            result = self._values.get("redshift_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.RedshiftParametersProperty"]], result)

        @builtins.property
        def s3_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.S3ParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.S3Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-s3parameters
            '''
            result = self._values.get("s3_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.S3ParametersProperty"]], result)

        @builtins.property
        def snowflake_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SnowflakeParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.SnowflakeParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-snowflakeparameters
            '''
            result = self._values.get("snowflake_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SnowflakeParametersProperty"]], result)

        @builtins.property
        def spark_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SparkParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.SparkParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-sparkparameters
            '''
            result = self._values.get("spark_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SparkParametersProperty"]], result)

        @builtins.property
        def sql_server_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SqlServerParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.SqlServerParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-sqlserverparameters
            '''
            result = self._values.get("sql_server_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.SqlServerParametersProperty"]], result)

        @builtins.property
        def teradata_parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.TeradataParametersProperty"]]:
            '''``CfnDataSource.DataSourceParametersProperty.TeradataParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-teradataparameters
            '''
            result = self._values.get("teradata_parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.TeradataParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.ManifestFileLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class ManifestFileLocationProperty:
        def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
            '''
            :param bucket: ``CfnDataSource.ManifestFileLocationProperty.Bucket``.
            :param key: ``CfnDataSource.ManifestFileLocationProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-manifestfilelocation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''``CfnDataSource.ManifestFileLocationProperty.Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-manifestfilelocation.html#cfn-quicksight-datasource-manifestfilelocation-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnDataSource.ManifestFileLocationProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-manifestfilelocation.html#cfn-quicksight-datasource-manifestfilelocation-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManifestFileLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.MariaDbParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"database": "database", "host": "host", "port": "port"},
    )
    class MariaDbParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param database: ``CfnDataSource.MariaDbParametersProperty.Database``.
            :param host: ``CfnDataSource.MariaDbParametersProperty.Host``.
            :param port: ``CfnDataSource.MariaDbParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "host": host,
                "port": port,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.MariaDbParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html#cfn-quicksight-datasource-mariadbparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.MariaDbParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html#cfn-quicksight-datasource-mariadbparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.MariaDbParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html#cfn-quicksight-datasource-mariadbparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MariaDbParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.MySqlParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"database": "database", "host": "host", "port": "port"},
    )
    class MySqlParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param database: ``CfnDataSource.MySqlParametersProperty.Database``.
            :param host: ``CfnDataSource.MySqlParametersProperty.Host``.
            :param port: ``CfnDataSource.MySqlParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "host": host,
                "port": port,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.MySqlParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html#cfn-quicksight-datasource-mysqlparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.MySqlParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html#cfn-quicksight-datasource-mysqlparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.MySqlParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html#cfn-quicksight-datasource-mysqlparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MySqlParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.OracleParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"database": "database", "host": "host", "port": "port"},
    )
    class OracleParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param database: ``CfnDataSource.OracleParametersProperty.Database``.
            :param host: ``CfnDataSource.OracleParametersProperty.Host``.
            :param port: ``CfnDataSource.OracleParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "host": host,
                "port": port,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.OracleParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html#cfn-quicksight-datasource-oracleparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.OracleParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html#cfn-quicksight-datasource-oracleparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.OracleParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html#cfn-quicksight-datasource-oracleparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OracleParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.PostgreSqlParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"database": "database", "host": "host", "port": "port"},
    )
    class PostgreSqlParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param database: ``CfnDataSource.PostgreSqlParametersProperty.Database``.
            :param host: ``CfnDataSource.PostgreSqlParametersProperty.Host``.
            :param port: ``CfnDataSource.PostgreSqlParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "host": host,
                "port": port,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.PostgreSqlParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html#cfn-quicksight-datasource-postgresqlparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.PostgreSqlParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html#cfn-quicksight-datasource-postgresqlparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.PostgreSqlParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html#cfn-quicksight-datasource-postgresqlparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PostgreSqlParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.PrestoParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog": "catalog", "host": "host", "port": "port"},
    )
    class PrestoParametersProperty:
        def __init__(
            self,
            *,
            catalog: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param catalog: ``CfnDataSource.PrestoParametersProperty.Catalog``.
            :param host: ``CfnDataSource.PrestoParametersProperty.Host``.
            :param port: ``CfnDataSource.PrestoParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "catalog": catalog,
                "host": host,
                "port": port,
            }

        @builtins.property
        def catalog(self) -> builtins.str:
            '''``CfnDataSource.PrestoParametersProperty.Catalog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html#cfn-quicksight-datasource-prestoparameters-catalog
            '''
            result = self._values.get("catalog")
            assert result is not None, "Required property 'catalog' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.PrestoParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html#cfn-quicksight-datasource-prestoparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.PrestoParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html#cfn-quicksight-datasource-prestoparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrestoParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.RdsParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"database": "database", "instance_id": "instanceId"},
    )
    class RdsParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            instance_id: builtins.str,
        ) -> None:
            '''
            :param database: ``CfnDataSource.RdsParametersProperty.Database``.
            :param instance_id: ``CfnDataSource.RdsParametersProperty.InstanceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-rdsparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "instance_id": instance_id,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.RdsParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-rdsparameters.html#cfn-quicksight-datasource-rdsparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def instance_id(self) -> builtins.str:
            '''``CfnDataSource.RdsParametersProperty.InstanceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-rdsparameters.html#cfn-quicksight-datasource-rdsparameters-instanceid
            '''
            result = self._values.get("instance_id")
            assert result is not None, "Required property 'instance_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RdsParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.RedshiftParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database": "database",
            "cluster_id": "clusterId",
            "host": "host",
            "port": "port",
        },
    )
    class RedshiftParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            cluster_id: typing.Optional[builtins.str] = None,
            host: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param database: ``CfnDataSource.RedshiftParametersProperty.Database``.
            :param cluster_id: ``CfnDataSource.RedshiftParametersProperty.ClusterId``.
            :param host: ``CfnDataSource.RedshiftParametersProperty.Host``.
            :param port: ``CfnDataSource.RedshiftParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
            }
            if cluster_id is not None:
                self._values["cluster_id"] = cluster_id
            if host is not None:
                self._values["host"] = host
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.RedshiftParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cluster_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.RedshiftParametersProperty.ClusterId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-clusterid
            '''
            result = self._values.get("cluster_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def host(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.RedshiftParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-host
            '''
            result = self._values.get("host")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataSource.RedshiftParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            principal: builtins.str,
        ) -> None:
            '''
            :param actions: ``CfnDataSource.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnDataSource.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-resourcepermission.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''``CfnDataSource.ResourcePermissionProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-resourcepermission.html#cfn-quicksight-datasource-resourcepermission-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def principal(self) -> builtins.str:
            '''``CfnDataSource.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-resourcepermission.html#cfn-quicksight-datasource-resourcepermission-principal
            '''
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.S3ParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"manifest_file_location": "manifestFileLocation"},
    )
    class S3ParametersProperty:
        def __init__(
            self,
            *,
            manifest_file_location: typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.ManifestFileLocationProperty"],
        ) -> None:
            '''
            :param manifest_file_location: ``CfnDataSource.S3ParametersProperty.ManifestFileLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-s3parameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "manifest_file_location": manifest_file_location,
            }

        @builtins.property
        def manifest_file_location(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.ManifestFileLocationProperty"]:
            '''``CfnDataSource.S3ParametersProperty.ManifestFileLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-s3parameters.html#cfn-quicksight-datasource-s3parameters-manifestfilelocation
            '''
            result = self._values.get("manifest_file_location")
            assert result is not None, "Required property 'manifest_file_location' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataSource.ManifestFileLocationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.SnowflakeParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database": "database",
            "host": "host",
            "warehouse": "warehouse",
        },
    )
    class SnowflakeParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            host: builtins.str,
            warehouse: builtins.str,
        ) -> None:
            '''
            :param database: ``CfnDataSource.SnowflakeParametersProperty.Database``.
            :param host: ``CfnDataSource.SnowflakeParametersProperty.Host``.
            :param warehouse: ``CfnDataSource.SnowflakeParametersProperty.Warehouse``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "host": host,
                "warehouse": warehouse,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.SnowflakeParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html#cfn-quicksight-datasource-snowflakeparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.SnowflakeParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html#cfn-quicksight-datasource-snowflakeparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def warehouse(self) -> builtins.str:
            '''``CfnDataSource.SnowflakeParametersProperty.Warehouse``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html#cfn-quicksight-datasource-snowflakeparameters-warehouse
            '''
            result = self._values.get("warehouse")
            assert result is not None, "Required property 'warehouse' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.SparkParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"host": "host", "port": "port"},
    )
    class SparkParametersProperty:
        def __init__(self, *, host: builtins.str, port: jsii.Number) -> None:
            '''
            :param host: ``CfnDataSource.SparkParametersProperty.Host``.
            :param port: ``CfnDataSource.SparkParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sparkparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "host": host,
                "port": port,
            }

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.SparkParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sparkparameters.html#cfn-quicksight-datasource-sparkparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.SparkParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sparkparameters.html#cfn-quicksight-datasource-sparkparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SparkParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.SqlServerParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"database": "database", "host": "host", "port": "port"},
    )
    class SqlServerParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param database: ``CfnDataSource.SqlServerParametersProperty.Database``.
            :param host: ``CfnDataSource.SqlServerParametersProperty.Host``.
            :param port: ``CfnDataSource.SqlServerParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "host": host,
                "port": port,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.SqlServerParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html#cfn-quicksight-datasource-sqlserverparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.SqlServerParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html#cfn-quicksight-datasource-sqlserverparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.SqlServerParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html#cfn-quicksight-datasource-sqlserverparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqlServerParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.SslPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"disable_ssl": "disableSsl"},
    )
    class SslPropertiesProperty:
        def __init__(
            self,
            *,
            disable_ssl: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param disable_ssl: ``CfnDataSource.SslPropertiesProperty.DisableSsl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sslproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if disable_ssl is not None:
                self._values["disable_ssl"] = disable_ssl

        @builtins.property
        def disable_ssl(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDataSource.SslPropertiesProperty.DisableSsl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sslproperties.html#cfn-quicksight-datasource-sslproperties-disablessl
            '''
            result = self._values.get("disable_ssl")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SslPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.TeradataParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"database": "database", "host": "host", "port": "port"},
    )
    class TeradataParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param database: ``CfnDataSource.TeradataParametersProperty.Database``.
            :param host: ``CfnDataSource.TeradataParametersProperty.Host``.
            :param port: ``CfnDataSource.TeradataParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database": database,
                "host": host,
                "port": port,
            }

        @builtins.property
        def database(self) -> builtins.str:
            '''``CfnDataSource.TeradataParametersProperty.Database``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html#cfn-quicksight-datasource-teradataparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.TeradataParametersProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html#cfn-quicksight-datasource-teradataparameters-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.TeradataParametersProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html#cfn-quicksight-datasource-teradataparameters-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TeradataParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnDataSource.VpcConnectionPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_connection_arn": "vpcConnectionArn"},
    )
    class VpcConnectionPropertiesProperty:
        def __init__(self, *, vpc_connection_arn: builtins.str) -> None:
            '''
            :param vpc_connection_arn: ``CfnDataSource.VpcConnectionPropertiesProperty.VpcConnectionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-vpcconnectionproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "vpc_connection_arn": vpc_connection_arn,
            }

        @builtins.property
        def vpc_connection_arn(self) -> builtins.str:
            '''``CfnDataSource.VpcConnectionPropertiesProperty.VpcConnectionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-vpcconnectionproperties.html#cfn-quicksight-datasource-vpcconnectionproperties-vpcconnectionarn
            '''
            result = self._values.get("vpc_connection_arn")
            assert result is not None, "Required property 'vpc_connection_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConnectionPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-quicksight.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "alternate_data_source_parameters": "alternateDataSourceParameters",
        "aws_account_id": "awsAccountId",
        "credentials": "credentials",
        "data_source_id": "dataSourceId",
        "data_source_parameters": "dataSourceParameters",
        "error_info": "errorInfo",
        "name": "name",
        "permissions": "permissions",
        "ssl_properties": "sslProperties",
        "tags": "tags",
        "type": "type",
        "vpc_connection_properties": "vpcConnectionProperties",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        alternate_data_source_parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnDataSource.DataSourceParametersProperty, aws_cdk.core.IResolvable]]]] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.DataSourceCredentialsProperty]] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        data_source_parameters: typing.Optional[typing.Union[CfnDataSource.DataSourceParametersProperty, aws_cdk.core.IResolvable]] = None,
        error_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.DataSourceErrorInfoProperty]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.ResourcePermissionProperty]]]] = None,
        ssl_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.SslPropertiesProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        type: typing.Optional[builtins.str] = None,
        vpc_connection_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.VpcConnectionPropertiesProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::QuickSight::DataSource``.

        :param alternate_data_source_parameters: ``AWS::QuickSight::DataSource.AlternateDataSourceParameters``.
        :param aws_account_id: ``AWS::QuickSight::DataSource.AwsAccountId``.
        :param credentials: ``AWS::QuickSight::DataSource.Credentials``.
        :param data_source_id: ``AWS::QuickSight::DataSource.DataSourceId``.
        :param data_source_parameters: ``AWS::QuickSight::DataSource.DataSourceParameters``.
        :param error_info: ``AWS::QuickSight::DataSource.ErrorInfo``.
        :param name: ``AWS::QuickSight::DataSource.Name``.
        :param permissions: ``AWS::QuickSight::DataSource.Permissions``.
        :param ssl_properties: ``AWS::QuickSight::DataSource.SslProperties``.
        :param tags: ``AWS::QuickSight::DataSource.Tags``.
        :param type: ``AWS::QuickSight::DataSource.Type``.
        :param vpc_connection_properties: ``AWS::QuickSight::DataSource.VpcConnectionProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if alternate_data_source_parameters is not None:
            self._values["alternate_data_source_parameters"] = alternate_data_source_parameters
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if credentials is not None:
            self._values["credentials"] = credentials
        if data_source_id is not None:
            self._values["data_source_id"] = data_source_id
        if data_source_parameters is not None:
            self._values["data_source_parameters"] = data_source_parameters
        if error_info is not None:
            self._values["error_info"] = error_info
        if name is not None:
            self._values["name"] = name
        if permissions is not None:
            self._values["permissions"] = permissions
        if ssl_properties is not None:
            self._values["ssl_properties"] = ssl_properties
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if vpc_connection_properties is not None:
            self._values["vpc_connection_properties"] = vpc_connection_properties

    @builtins.property
    def alternate_data_source_parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnDataSource.DataSourceParametersProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::QuickSight::DataSource.AlternateDataSourceParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-alternatedatasourceparameters
        '''
        result = self._values.get("alternate_data_source_parameters")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnDataSource.DataSourceParametersProperty, aws_cdk.core.IResolvable]]]], result)

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSource.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-awsaccountid
        '''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.DataSourceCredentialsProperty]]:
        '''``AWS::QuickSight::DataSource.Credentials``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-credentials
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.DataSourceCredentialsProperty]], result)

    @builtins.property
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSource.DataSourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-datasourceid
        '''
        result = self._values.get("data_source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_parameters(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.DataSourceParametersProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::QuickSight::DataSource.DataSourceParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-datasourceparameters
        '''
        result = self._values.get("data_source_parameters")
        return typing.cast(typing.Optional[typing.Union[CfnDataSource.DataSourceParametersProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def error_info(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.DataSourceErrorInfoProperty]]:
        '''``AWS::QuickSight::DataSource.ErrorInfo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-errorinfo
        '''
        result = self._values.get("error_info")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.DataSourceErrorInfoProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSource.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.ResourcePermissionProperty]]]]:
        '''``AWS::QuickSight::DataSource.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.ResourcePermissionProperty]]]], result)

    @builtins.property
    def ssl_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.SslPropertiesProperty]]:
        '''``AWS::QuickSight::DataSource.SslProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-sslproperties
        '''
        result = self._values.get("ssl_properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.SslPropertiesProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::QuickSight::DataSource.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::DataSource.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_connection_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.VpcConnectionPropertiesProperty]]:
        '''``AWS::QuickSight::DataSource.VpcConnectionProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-vpcconnectionproperties
        '''
        result = self._values.get("vpc_connection_properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataSource.VpcConnectionPropertiesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTemplate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-quicksight.CfnTemplate",
):
    '''A CloudFormation ``AWS::QuickSight::Template``.

    :cloudformationResource: AWS::QuickSight::Template
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.ResourcePermissionProperty"]]]] = None,
        source_entity: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceEntityProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::QuickSight::Template``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param aws_account_id: ``AWS::QuickSight::Template.AwsAccountId``.
        :param template_id: ``AWS::QuickSight::Template.TemplateId``.
        :param name: ``AWS::QuickSight::Template.Name``.
        :param permissions: ``AWS::QuickSight::Template.Permissions``.
        :param source_entity: ``AWS::QuickSight::Template.SourceEntity``.
        :param tags: ``AWS::QuickSight::Template.Tags``.
        :param version_description: ``AWS::QuickSight::Template.VersionDescription``.
        '''
        props = CfnTemplateProps(
            aws_account_id=aws_account_id,
            template_id=template_id,
            name=name,
            permissions=permissions,
            source_entity=source_entity,
            tags=tags,
            version_description=version_description,
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
        '''``AWS::QuickSight::Template.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        '''``AWS::QuickSight::Template.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-awsaccountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateId")
    def template_id(self) -> builtins.str:
        '''``AWS::QuickSight::Template.TemplateId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-templateid
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateId"))

    @template_id.setter
    def template_id(self, value: builtins.str) -> None:
        jsii.set(self, "templateId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Template.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.ResourcePermissionProperty"]]]]:
        '''``AWS::QuickSight::Template.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-permissions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.ResourcePermissionProperty"]]]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.ResourcePermissionProperty"]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceEntity")
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceEntityProperty"]]:
        '''``AWS::QuickSight::Template.SourceEntity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-sourceentity
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceEntityProperty"]], jsii.get(self, "sourceEntity"))

    @source_entity.setter
    def source_entity(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceEntityProperty"]],
    ) -> None:
        jsii.set(self, "sourceEntity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Template.VersionDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-versiondescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionDescription"))

    @version_description.setter
    def version_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionDescription", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTemplate.DataSetReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_set_arn": "dataSetArn",
            "data_set_placeholder": "dataSetPlaceholder",
        },
    )
    class DataSetReferenceProperty:
        def __init__(
            self,
            *,
            data_set_arn: builtins.str,
            data_set_placeholder: builtins.str,
        ) -> None:
            '''
            :param data_set_arn: ``CfnTemplate.DataSetReferenceProperty.DataSetArn``.
            :param data_set_placeholder: ``CfnTemplate.DataSetReferenceProperty.DataSetPlaceholder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_set_arn": data_set_arn,
                "data_set_placeholder": data_set_placeholder,
            }

        @builtins.property
        def data_set_arn(self) -> builtins.str:
            '''``CfnTemplate.DataSetReferenceProperty.DataSetArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html#cfn-quicksight-template-datasetreference-datasetarn
            '''
            result = self._values.get("data_set_arn")
            assert result is not None, "Required property 'data_set_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_set_placeholder(self) -> builtins.str:
            '''``CfnTemplate.DataSetReferenceProperty.DataSetPlaceholder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html#cfn-quicksight-template-datasetreference-datasetplaceholder
            '''
            result = self._values.get("data_set_placeholder")
            assert result is not None, "Required property 'data_set_placeholder' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSetReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTemplate.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            principal: builtins.str,
        ) -> None:
            '''
            :param actions: ``CfnTemplate.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnTemplate.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''``CfnTemplate.ResourcePermissionProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html#cfn-quicksight-template-resourcepermission-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def principal(self) -> builtins.str:
            '''``CfnTemplate.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html#cfn-quicksight-template-resourcepermission-principal
            '''
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTemplate.TemplateSourceAnalysisProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "data_set_references": "dataSetReferences"},
    )
    class TemplateSourceAnalysisProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            data_set_references: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.DataSetReferenceProperty"]]],
        ) -> None:
            '''
            :param arn: ``CfnTemplate.TemplateSourceAnalysisProperty.Arn``.
            :param data_set_references: ``CfnTemplate.TemplateSourceAnalysisProperty.DataSetReferences``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "data_set_references": data_set_references,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''``CfnTemplate.TemplateSourceAnalysisProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html#cfn-quicksight-template-templatesourceanalysis-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_set_references(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.DataSetReferenceProperty"]]]:
            '''``CfnTemplate.TemplateSourceAnalysisProperty.DataSetReferences``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html#cfn-quicksight-template-templatesourceanalysis-datasetreferences
            '''
            result = self._values.get("data_set_references")
            assert result is not None, "Required property 'data_set_references' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.DataSetReferenceProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateSourceAnalysisProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTemplate.TemplateSourceEntityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_analysis": "sourceAnalysis",
            "source_template": "sourceTemplate",
        },
    )
    class TemplateSourceEntityProperty:
        def __init__(
            self,
            *,
            source_analysis: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceAnalysisProperty"]] = None,
            source_template: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceTemplateProperty"]] = None,
        ) -> None:
            '''
            :param source_analysis: ``CfnTemplate.TemplateSourceEntityProperty.SourceAnalysis``.
            :param source_template: ``CfnTemplate.TemplateSourceEntityProperty.SourceTemplate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if source_analysis is not None:
                self._values["source_analysis"] = source_analysis
            if source_template is not None:
                self._values["source_template"] = source_template

        @builtins.property
        def source_analysis(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceAnalysisProperty"]]:
            '''``CfnTemplate.TemplateSourceEntityProperty.SourceAnalysis``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html#cfn-quicksight-template-templatesourceentity-sourceanalysis
            '''
            result = self._values.get("source_analysis")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceAnalysisProperty"]], result)

        @builtins.property
        def source_template(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceTemplateProperty"]]:
            '''``CfnTemplate.TemplateSourceEntityProperty.SourceTemplate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html#cfn-quicksight-template-templatesourceentity-sourcetemplate
            '''
            result = self._values.get("source_template")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateSourceTemplateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateSourceEntityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTemplate.TemplateSourceTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class TemplateSourceTemplateProperty:
        def __init__(self, *, arn: builtins.str) -> None:
            '''
            :param arn: ``CfnTemplate.TemplateSourceTemplateProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourcetemplate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''``CfnTemplate.TemplateSourceTemplateProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourcetemplate.html#cfn-quicksight-template-templatesourcetemplate-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateSourceTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-quicksight.CfnTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
        "name": "name",
        "permissions": "permissions",
        "source_entity": "sourceEntity",
        "tags": "tags",
        "version_description": "versionDescription",
    },
)
class CfnTemplateProps:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnTemplate.ResourcePermissionProperty]]]] = None,
        source_entity: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTemplate.TemplateSourceEntityProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::QuickSight::Template``.

        :param aws_account_id: ``AWS::QuickSight::Template.AwsAccountId``.
        :param template_id: ``AWS::QuickSight::Template.TemplateId``.
        :param name: ``AWS::QuickSight::Template.Name``.
        :param permissions: ``AWS::QuickSight::Template.Permissions``.
        :param source_entity: ``AWS::QuickSight::Template.SourceEntity``.
        :param tags: ``AWS::QuickSight::Template.Tags``.
        :param version_description: ``AWS::QuickSight::Template.VersionDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }
        if name is not None:
            self._values["name"] = name
        if permissions is not None:
            self._values["permissions"] = permissions
        if source_entity is not None:
            self._values["source_entity"] = source_entity
        if tags is not None:
            self._values["tags"] = tags
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''``AWS::QuickSight::Template.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-awsaccountid
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''``AWS::QuickSight::Template.TemplateId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-templateid
        '''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Template.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTemplate.ResourcePermissionProperty]]]]:
        '''``AWS::QuickSight::Template.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTemplate.ResourcePermissionProperty]]]], result)

    @builtins.property
    def source_entity(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTemplate.TemplateSourceEntityProperty]]:
        '''``AWS::QuickSight::Template.SourceEntity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-sourceentity
        '''
        result = self._values.get("source_entity")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTemplate.TemplateSourceEntityProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::QuickSight::Template.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Template.VersionDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-versiondescription
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTheme(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-quicksight.CfnTheme",
):
    '''A CloudFormation ``AWS::QuickSight::Theme``.

    :cloudformationResource: AWS::QuickSight::Theme
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        base_theme_id: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.ThemeConfigurationProperty"]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.ResourcePermissionProperty"]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::QuickSight::Theme``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param aws_account_id: ``AWS::QuickSight::Theme.AwsAccountId``.
        :param theme_id: ``AWS::QuickSight::Theme.ThemeId``.
        :param base_theme_id: ``AWS::QuickSight::Theme.BaseThemeId``.
        :param configuration: ``AWS::QuickSight::Theme.Configuration``.
        :param name: ``AWS::QuickSight::Theme.Name``.
        :param permissions: ``AWS::QuickSight::Theme.Permissions``.
        :param tags: ``AWS::QuickSight::Theme.Tags``.
        :param version_description: ``AWS::QuickSight::Theme.VersionDescription``.
        '''
        props = CfnThemeProps(
            aws_account_id=aws_account_id,
            theme_id=theme_id,
            base_theme_id=base_theme_id,
            configuration=configuration,
            name=name,
            permissions=permissions,
            tags=tags,
            version_description=version_description,
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
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::QuickSight::Theme.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        '''``AWS::QuickSight::Theme.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-awsaccountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        jsii.set(self, "awsAccountId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="themeId")
    def theme_id(self) -> builtins.str:
        '''``AWS::QuickSight::Theme.ThemeId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-themeid
        '''
        return typing.cast(builtins.str, jsii.get(self, "themeId"))

    @theme_id.setter
    def theme_id(self, value: builtins.str) -> None:
        jsii.set(self, "themeId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="baseThemeId")
    def base_theme_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Theme.BaseThemeId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-basethemeid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseThemeId"))

    @base_theme_id.setter
    def base_theme_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "baseThemeId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.ThemeConfigurationProperty"]]:
        '''``AWS::QuickSight::Theme.Configuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-configuration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.ThemeConfigurationProperty"]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.ThemeConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "configuration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Theme.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.ResourcePermissionProperty"]]]]:
        '''``AWS::QuickSight::Theme.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-permissions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.ResourcePermissionProperty"]]]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.ResourcePermissionProperty"]]]],
    ) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Theme.VersionDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-versiondescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionDescription"))

    @version_description.setter
    def version_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionDescription", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.BorderStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"show": "show"},
    )
    class BorderStyleProperty:
        def __init__(
            self,
            *,
            show: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param show: ``CfnTheme.BorderStyleProperty.Show``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-borderstyle.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if show is not None:
                self._values["show"] = show

        @builtins.property
        def show(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnTheme.BorderStyleProperty.Show``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-borderstyle.html#cfn-quicksight-theme-borderstyle-show
            '''
            result = self._values.get("show")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BorderStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.DataColorPaletteProperty",
        jsii_struct_bases=[],
        name_mapping={
            "colors": "colors",
            "empty_fill_color": "emptyFillColor",
            "min_max_gradient": "minMaxGradient",
        },
    )
    class DataColorPaletteProperty:
        def __init__(
            self,
            *,
            colors: typing.Optional[typing.Sequence[builtins.str]] = None,
            empty_fill_color: typing.Optional[builtins.str] = None,
            min_max_gradient: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param colors: ``CfnTheme.DataColorPaletteProperty.Colors``.
            :param empty_fill_color: ``CfnTheme.DataColorPaletteProperty.EmptyFillColor``.
            :param min_max_gradient: ``CfnTheme.DataColorPaletteProperty.MinMaxGradient``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if colors is not None:
                self._values["colors"] = colors
            if empty_fill_color is not None:
                self._values["empty_fill_color"] = empty_fill_color
            if min_max_gradient is not None:
                self._values["min_max_gradient"] = min_max_gradient

        @builtins.property
        def colors(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnTheme.DataColorPaletteProperty.Colors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-colors
            '''
            result = self._values.get("colors")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def empty_fill_color(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.DataColorPaletteProperty.EmptyFillColor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-emptyfillcolor
            '''
            result = self._values.get("empty_fill_color")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def min_max_gradient(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnTheme.DataColorPaletteProperty.MinMaxGradient``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-minmaxgradient
            '''
            result = self._values.get("min_max_gradient")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataColorPaletteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.FontProperty",
        jsii_struct_bases=[],
        name_mapping={"font_family": "fontFamily"},
    )
    class FontProperty:
        def __init__(
            self,
            *,
            font_family: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param font_family: ``CfnTheme.FontProperty.FontFamily``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-font.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if font_family is not None:
                self._values["font_family"] = font_family

        @builtins.property
        def font_family(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.FontProperty.FontFamily``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-font.html#cfn-quicksight-theme-font-fontfamily
            '''
            result = self._values.get("font_family")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FontProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.GutterStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"show": "show"},
    )
    class GutterStyleProperty:
        def __init__(
            self,
            *,
            show: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param show: ``CfnTheme.GutterStyleProperty.Show``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-gutterstyle.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if show is not None:
                self._values["show"] = show

        @builtins.property
        def show(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnTheme.GutterStyleProperty.Show``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-gutterstyle.html#cfn-quicksight-theme-gutterstyle-show
            '''
            result = self._values.get("show")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GutterStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.MarginStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"show": "show"},
    )
    class MarginStyleProperty:
        def __init__(
            self,
            *,
            show: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param show: ``CfnTheme.MarginStyleProperty.Show``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-marginstyle.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if show is not None:
                self._values["show"] = show

        @builtins.property
        def show(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnTheme.MarginStyleProperty.Show``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-marginstyle.html#cfn-quicksight-theme-marginstyle-show
            '''
            result = self._values.get("show")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MarginStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.ResourcePermissionProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "principal": "principal"},
    )
    class ResourcePermissionProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            principal: builtins.str,
        ) -> None:
            '''
            :param actions: ``CfnTheme.ResourcePermissionProperty.Actions``.
            :param principal: ``CfnTheme.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "principal": principal,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''``CfnTheme.ResourcePermissionProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html#cfn-quicksight-theme-resourcepermission-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def principal(self) -> builtins.str:
            '''``CfnTheme.ResourcePermissionProperty.Principal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html#cfn-quicksight-theme-resourcepermission-principal
            '''
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcePermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.SheetStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"tile": "tile", "tile_layout": "tileLayout"},
    )
    class SheetStyleProperty:
        def __init__(
            self,
            *,
            tile: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.TileStyleProperty"]] = None,
            tile_layout: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.TileLayoutStyleProperty"]] = None,
        ) -> None:
            '''
            :param tile: ``CfnTheme.SheetStyleProperty.Tile``.
            :param tile_layout: ``CfnTheme.SheetStyleProperty.TileLayout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if tile is not None:
                self._values["tile"] = tile
            if tile_layout is not None:
                self._values["tile_layout"] = tile_layout

        @builtins.property
        def tile(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.TileStyleProperty"]]:
            '''``CfnTheme.SheetStyleProperty.Tile``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html#cfn-quicksight-theme-sheetstyle-tile
            '''
            result = self._values.get("tile")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.TileStyleProperty"]], result)

        @builtins.property
        def tile_layout(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.TileLayoutStyleProperty"]]:
            '''``CfnTheme.SheetStyleProperty.TileLayout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html#cfn-quicksight-theme-sheetstyle-tilelayout
            '''
            result = self._values.get("tile_layout")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.TileLayoutStyleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SheetStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.ThemeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_color_palette": "dataColorPalette",
            "sheet": "sheet",
            "typography": "typography",
            "ui_color_palette": "uiColorPalette",
        },
    )
    class ThemeConfigurationProperty:
        def __init__(
            self,
            *,
            data_color_palette: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.DataColorPaletteProperty"]] = None,
            sheet: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.SheetStyleProperty"]] = None,
            typography: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.TypographyProperty"]] = None,
            ui_color_palette: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.UIColorPaletteProperty"]] = None,
        ) -> None:
            '''
            :param data_color_palette: ``CfnTheme.ThemeConfigurationProperty.DataColorPalette``.
            :param sheet: ``CfnTheme.ThemeConfigurationProperty.Sheet``.
            :param typography: ``CfnTheme.ThemeConfigurationProperty.Typography``.
            :param ui_color_palette: ``CfnTheme.ThemeConfigurationProperty.UIColorPalette``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if data_color_palette is not None:
                self._values["data_color_palette"] = data_color_palette
            if sheet is not None:
                self._values["sheet"] = sheet
            if typography is not None:
                self._values["typography"] = typography
            if ui_color_palette is not None:
                self._values["ui_color_palette"] = ui_color_palette

        @builtins.property
        def data_color_palette(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.DataColorPaletteProperty"]]:
            '''``CfnTheme.ThemeConfigurationProperty.DataColorPalette``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-datacolorpalette
            '''
            result = self._values.get("data_color_palette")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.DataColorPaletteProperty"]], result)

        @builtins.property
        def sheet(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.SheetStyleProperty"]]:
            '''``CfnTheme.ThemeConfigurationProperty.Sheet``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-sheet
            '''
            result = self._values.get("sheet")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.SheetStyleProperty"]], result)

        @builtins.property
        def typography(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.TypographyProperty"]]:
            '''``CfnTheme.ThemeConfigurationProperty.Typography``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-typography
            '''
            result = self._values.get("typography")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.TypographyProperty"]], result)

        @builtins.property
        def ui_color_palette(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.UIColorPaletteProperty"]]:
            '''``CfnTheme.ThemeConfigurationProperty.UIColorPalette``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-uicolorpalette
            '''
            result = self._values.get("ui_color_palette")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.UIColorPaletteProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThemeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.TileLayoutStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"gutter": "gutter", "margin": "margin"},
    )
    class TileLayoutStyleProperty:
        def __init__(
            self,
            *,
            gutter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.GutterStyleProperty"]] = None,
            margin: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.MarginStyleProperty"]] = None,
        ) -> None:
            '''
            :param gutter: ``CfnTheme.TileLayoutStyleProperty.Gutter``.
            :param margin: ``CfnTheme.TileLayoutStyleProperty.Margin``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if gutter is not None:
                self._values["gutter"] = gutter
            if margin is not None:
                self._values["margin"] = margin

        @builtins.property
        def gutter(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.GutterStyleProperty"]]:
            '''``CfnTheme.TileLayoutStyleProperty.Gutter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html#cfn-quicksight-theme-tilelayoutstyle-gutter
            '''
            result = self._values.get("gutter")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.GutterStyleProperty"]], result)

        @builtins.property
        def margin(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.MarginStyleProperty"]]:
            '''``CfnTheme.TileLayoutStyleProperty.Margin``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html#cfn-quicksight-theme-tilelayoutstyle-margin
            '''
            result = self._values.get("margin")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.MarginStyleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TileLayoutStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.TileStyleProperty",
        jsii_struct_bases=[],
        name_mapping={"border": "border"},
    )
    class TileStyleProperty:
        def __init__(
            self,
            *,
            border: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.BorderStyleProperty"]] = None,
        ) -> None:
            '''
            :param border: ``CfnTheme.TileStyleProperty.Border``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilestyle.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if border is not None:
                self._values["border"] = border

        @builtins.property
        def border(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.BorderStyleProperty"]]:
            '''``CfnTheme.TileStyleProperty.Border``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilestyle.html#cfn-quicksight-theme-tilestyle-border
            '''
            result = self._values.get("border")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.BorderStyleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TileStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.TypographyProperty",
        jsii_struct_bases=[],
        name_mapping={"font_families": "fontFamilies"},
    )
    class TypographyProperty:
        def __init__(
            self,
            *,
            font_families: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.FontProperty"]]]] = None,
        ) -> None:
            '''
            :param font_families: ``CfnTheme.TypographyProperty.FontFamilies``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-typography.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if font_families is not None:
                self._values["font_families"] = font_families

        @builtins.property
        def font_families(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.FontProperty"]]]]:
            '''``CfnTheme.TypographyProperty.FontFamilies``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-typography.html#cfn-quicksight-theme-typography-fontfamilies
            '''
            result = self._values.get("font_families")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTheme.FontProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TypographyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-quicksight.CfnTheme.UIColorPaletteProperty",
        jsii_struct_bases=[],
        name_mapping={
            "accent": "accent",
            "accent_foreground": "accentForeground",
            "danger": "danger",
            "danger_foreground": "dangerForeground",
            "dimension": "dimension",
            "dimension_foreground": "dimensionForeground",
            "measure": "measure",
            "measure_foreground": "measureForeground",
            "primary_background": "primaryBackground",
            "primary_foreground": "primaryForeground",
            "secondary_background": "secondaryBackground",
            "secondary_foreground": "secondaryForeground",
            "success": "success",
            "success_foreground": "successForeground",
            "warning": "warning",
            "warning_foreground": "warningForeground",
        },
    )
    class UIColorPaletteProperty:
        def __init__(
            self,
            *,
            accent: typing.Optional[builtins.str] = None,
            accent_foreground: typing.Optional[builtins.str] = None,
            danger: typing.Optional[builtins.str] = None,
            danger_foreground: typing.Optional[builtins.str] = None,
            dimension: typing.Optional[builtins.str] = None,
            dimension_foreground: typing.Optional[builtins.str] = None,
            measure: typing.Optional[builtins.str] = None,
            measure_foreground: typing.Optional[builtins.str] = None,
            primary_background: typing.Optional[builtins.str] = None,
            primary_foreground: typing.Optional[builtins.str] = None,
            secondary_background: typing.Optional[builtins.str] = None,
            secondary_foreground: typing.Optional[builtins.str] = None,
            success: typing.Optional[builtins.str] = None,
            success_foreground: typing.Optional[builtins.str] = None,
            warning: typing.Optional[builtins.str] = None,
            warning_foreground: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param accent: ``CfnTheme.UIColorPaletteProperty.Accent``.
            :param accent_foreground: ``CfnTheme.UIColorPaletteProperty.AccentForeground``.
            :param danger: ``CfnTheme.UIColorPaletteProperty.Danger``.
            :param danger_foreground: ``CfnTheme.UIColorPaletteProperty.DangerForeground``.
            :param dimension: ``CfnTheme.UIColorPaletteProperty.Dimension``.
            :param dimension_foreground: ``CfnTheme.UIColorPaletteProperty.DimensionForeground``.
            :param measure: ``CfnTheme.UIColorPaletteProperty.Measure``.
            :param measure_foreground: ``CfnTheme.UIColorPaletteProperty.MeasureForeground``.
            :param primary_background: ``CfnTheme.UIColorPaletteProperty.PrimaryBackground``.
            :param primary_foreground: ``CfnTheme.UIColorPaletteProperty.PrimaryForeground``.
            :param secondary_background: ``CfnTheme.UIColorPaletteProperty.SecondaryBackground``.
            :param secondary_foreground: ``CfnTheme.UIColorPaletteProperty.SecondaryForeground``.
            :param success: ``CfnTheme.UIColorPaletteProperty.Success``.
            :param success_foreground: ``CfnTheme.UIColorPaletteProperty.SuccessForeground``.
            :param warning: ``CfnTheme.UIColorPaletteProperty.Warning``.
            :param warning_foreground: ``CfnTheme.UIColorPaletteProperty.WarningForeground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if accent is not None:
                self._values["accent"] = accent
            if accent_foreground is not None:
                self._values["accent_foreground"] = accent_foreground
            if danger is not None:
                self._values["danger"] = danger
            if danger_foreground is not None:
                self._values["danger_foreground"] = danger_foreground
            if dimension is not None:
                self._values["dimension"] = dimension
            if dimension_foreground is not None:
                self._values["dimension_foreground"] = dimension_foreground
            if measure is not None:
                self._values["measure"] = measure
            if measure_foreground is not None:
                self._values["measure_foreground"] = measure_foreground
            if primary_background is not None:
                self._values["primary_background"] = primary_background
            if primary_foreground is not None:
                self._values["primary_foreground"] = primary_foreground
            if secondary_background is not None:
                self._values["secondary_background"] = secondary_background
            if secondary_foreground is not None:
                self._values["secondary_foreground"] = secondary_foreground
            if success is not None:
                self._values["success"] = success
            if success_foreground is not None:
                self._values["success_foreground"] = success_foreground
            if warning is not None:
                self._values["warning"] = warning
            if warning_foreground is not None:
                self._values["warning_foreground"] = warning_foreground

        @builtins.property
        def accent(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.Accent``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-accent
            '''
            result = self._values.get("accent")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def accent_foreground(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.AccentForeground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-accentforeground
            '''
            result = self._values.get("accent_foreground")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def danger(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.Danger``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-danger
            '''
            result = self._values.get("danger")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def danger_foreground(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.DangerForeground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dangerforeground
            '''
            result = self._values.get("danger_foreground")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dimension(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.Dimension``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dimension
            '''
            result = self._values.get("dimension")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dimension_foreground(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.DimensionForeground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dimensionforeground
            '''
            result = self._values.get("dimension_foreground")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def measure(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.Measure``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-measure
            '''
            result = self._values.get("measure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def measure_foreground(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.MeasureForeground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-measureforeground
            '''
            result = self._values.get("measure_foreground")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def primary_background(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.PrimaryBackground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-primarybackground
            '''
            result = self._values.get("primary_background")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def primary_foreground(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.PrimaryForeground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-primaryforeground
            '''
            result = self._values.get("primary_foreground")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secondary_background(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.SecondaryBackground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-secondarybackground
            '''
            result = self._values.get("secondary_background")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secondary_foreground(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.SecondaryForeground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-secondaryforeground
            '''
            result = self._values.get("secondary_foreground")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def success(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.Success``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-success
            '''
            result = self._values.get("success")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def success_foreground(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.SuccessForeground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-successforeground
            '''
            result = self._values.get("success_foreground")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def warning(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.Warning``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-warning
            '''
            result = self._values.get("warning")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def warning_foreground(self) -> typing.Optional[builtins.str]:
            '''``CfnTheme.UIColorPaletteProperty.WarningForeground``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-warningforeground
            '''
            result = self._values.get("warning_foreground")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UIColorPaletteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-quicksight.CfnThemeProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
        "base_theme_id": "baseThemeId",
        "configuration": "configuration",
        "name": "name",
        "permissions": "permissions",
        "tags": "tags",
        "version_description": "versionDescription",
    },
)
class CfnThemeProps:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        base_theme_id: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTheme.ThemeConfigurationProperty]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnTheme.ResourcePermissionProperty]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::QuickSight::Theme``.

        :param aws_account_id: ``AWS::QuickSight::Theme.AwsAccountId``.
        :param theme_id: ``AWS::QuickSight::Theme.ThemeId``.
        :param base_theme_id: ``AWS::QuickSight::Theme.BaseThemeId``.
        :param configuration: ``AWS::QuickSight::Theme.Configuration``.
        :param name: ``AWS::QuickSight::Theme.Name``.
        :param permissions: ``AWS::QuickSight::Theme.Permissions``.
        :param tags: ``AWS::QuickSight::Theme.Tags``.
        :param version_description: ``AWS::QuickSight::Theme.VersionDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }
        if base_theme_id is not None:
            self._values["base_theme_id"] = base_theme_id
        if configuration is not None:
            self._values["configuration"] = configuration
        if name is not None:
            self._values["name"] = name
        if permissions is not None:
            self._values["permissions"] = permissions
        if tags is not None:
            self._values["tags"] = tags
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''``AWS::QuickSight::Theme.AwsAccountId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-awsaccountid
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''``AWS::QuickSight::Theme.ThemeId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-themeid
        '''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_theme_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Theme.BaseThemeId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-basethemeid
        '''
        result = self._values.get("base_theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTheme.ThemeConfigurationProperty]]:
        '''``AWS::QuickSight::Theme.Configuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTheme.ThemeConfigurationProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Theme.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTheme.ResourcePermissionProperty]]]]:
        '''``AWS::QuickSight::Theme.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTheme.ResourcePermissionProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::QuickSight::Theme.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::QuickSight::Theme.VersionDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-versiondescription
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThemeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAnalysis",
    "CfnAnalysisProps",
    "CfnDashboard",
    "CfnDashboardProps",
    "CfnDataSet",
    "CfnDataSetProps",
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnTemplate",
    "CfnTemplateProps",
    "CfnTheme",
    "CfnThemeProps",
]

publication.publish()
