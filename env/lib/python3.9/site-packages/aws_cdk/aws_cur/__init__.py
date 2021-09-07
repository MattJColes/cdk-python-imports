'''
# AWS::CUR Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_cur as cur
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
class CfnReportDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cur.CfnReportDefinition",
):
    '''A CloudFormation ``AWS::CUR::ReportDefinition``.

    :cloudformationResource: AWS::CUR::ReportDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        compression: builtins.str,
        format: builtins.str,
        refresh_closed_reports: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        report_name: builtins.str,
        report_versioning: builtins.str,
        s3_bucket: builtins.str,
        s3_prefix: builtins.str,
        s3_region: builtins.str,
        time_unit: builtins.str,
        additional_artifacts: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_schema_elements: typing.Optional[typing.Sequence[builtins.str]] = None,
        billing_view_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CUR::ReportDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param compression: ``AWS::CUR::ReportDefinition.Compression``.
        :param format: ``AWS::CUR::ReportDefinition.Format``.
        :param refresh_closed_reports: ``AWS::CUR::ReportDefinition.RefreshClosedReports``.
        :param report_name: ``AWS::CUR::ReportDefinition.ReportName``.
        :param report_versioning: ``AWS::CUR::ReportDefinition.ReportVersioning``.
        :param s3_bucket: ``AWS::CUR::ReportDefinition.S3Bucket``.
        :param s3_prefix: ``AWS::CUR::ReportDefinition.S3Prefix``.
        :param s3_region: ``AWS::CUR::ReportDefinition.S3Region``.
        :param time_unit: ``AWS::CUR::ReportDefinition.TimeUnit``.
        :param additional_artifacts: ``AWS::CUR::ReportDefinition.AdditionalArtifacts``.
        :param additional_schema_elements: ``AWS::CUR::ReportDefinition.AdditionalSchemaElements``.
        :param billing_view_arn: ``AWS::CUR::ReportDefinition.BillingViewArn``.
        '''
        props = CfnReportDefinitionProps(
            compression=compression,
            format=format,
            refresh_closed_reports=refresh_closed_reports,
            report_name=report_name,
            report_versioning=report_versioning,
            s3_bucket=s3_bucket,
            s3_prefix=s3_prefix,
            s3_region=s3_region,
            time_unit=time_unit,
            additional_artifacts=additional_artifacts,
            additional_schema_elements=additional_schema_elements,
            billing_view_arn=billing_view_arn,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.Compression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-compression
        '''
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        jsii.set(self, "compression", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.Format``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-format
        '''
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        jsii.set(self, "format", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="refreshClosedReports")
    def refresh_closed_reports(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::CUR::ReportDefinition.RefreshClosedReports``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-refreshclosedreports
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "refreshClosedReports"))

    @refresh_closed_reports.setter
    def refresh_closed_reports(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "refreshClosedReports", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="reportName")
    def report_name(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.ReportName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-reportname
        '''
        return typing.cast(builtins.str, jsii.get(self, "reportName"))

    @report_name.setter
    def report_name(self, value: builtins.str) -> None:
        jsii.set(self, "reportName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="reportVersioning")
    def report_versioning(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.ReportVersioning``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-reportversioning
        '''
        return typing.cast(builtins.str, jsii.get(self, "reportVersioning"))

    @report_versioning.setter
    def report_versioning(self, value: builtins.str) -> None:
        jsii.set(self, "reportVersioning", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.S3Bucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3bucket
        '''
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @s3_bucket.setter
    def s3_bucket(self, value: builtins.str) -> None:
        jsii.set(self, "s3Bucket", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3Prefix")
    def s3_prefix(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.S3Prefix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3prefix
        '''
        return typing.cast(builtins.str, jsii.get(self, "s3Prefix"))

    @s3_prefix.setter
    def s3_prefix(self, value: builtins.str) -> None:
        jsii.set(self, "s3Prefix", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3Region")
    def s3_region(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.S3Region``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3region
        '''
        return typing.cast(builtins.str, jsii.get(self, "s3Region"))

    @s3_region.setter
    def s3_region(self, value: builtins.str) -> None:
        jsii.set(self, "s3Region", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeUnit")
    def time_unit(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.TimeUnit``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-timeunit
        '''
        return typing.cast(builtins.str, jsii.get(self, "timeUnit"))

    @time_unit.setter
    def time_unit(self, value: builtins.str) -> None:
        jsii.set(self, "timeUnit", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="additionalArtifacts")
    def additional_artifacts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CUR::ReportDefinition.AdditionalArtifacts``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-additionalartifacts
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalArtifacts"))

    @additional_artifacts.setter
    def additional_artifacts(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "additionalArtifacts", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="additionalSchemaElements")
    def additional_schema_elements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CUR::ReportDefinition.AdditionalSchemaElements``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-additionalschemaelements
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalSchemaElements"))

    @additional_schema_elements.setter
    def additional_schema_elements(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "additionalSchemaElements", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="billingViewArn")
    def billing_view_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CUR::ReportDefinition.BillingViewArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-billingviewarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingViewArn"))

    @billing_view_arn.setter
    def billing_view_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "billingViewArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cur.CfnReportDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "compression": "compression",
        "format": "format",
        "refresh_closed_reports": "refreshClosedReports",
        "report_name": "reportName",
        "report_versioning": "reportVersioning",
        "s3_bucket": "s3Bucket",
        "s3_prefix": "s3Prefix",
        "s3_region": "s3Region",
        "time_unit": "timeUnit",
        "additional_artifacts": "additionalArtifacts",
        "additional_schema_elements": "additionalSchemaElements",
        "billing_view_arn": "billingViewArn",
    },
)
class CfnReportDefinitionProps:
    def __init__(
        self,
        *,
        compression: builtins.str,
        format: builtins.str,
        refresh_closed_reports: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        report_name: builtins.str,
        report_versioning: builtins.str,
        s3_bucket: builtins.str,
        s3_prefix: builtins.str,
        s3_region: builtins.str,
        time_unit: builtins.str,
        additional_artifacts: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_schema_elements: typing.Optional[typing.Sequence[builtins.str]] = None,
        billing_view_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CUR::ReportDefinition``.

        :param compression: ``AWS::CUR::ReportDefinition.Compression``.
        :param format: ``AWS::CUR::ReportDefinition.Format``.
        :param refresh_closed_reports: ``AWS::CUR::ReportDefinition.RefreshClosedReports``.
        :param report_name: ``AWS::CUR::ReportDefinition.ReportName``.
        :param report_versioning: ``AWS::CUR::ReportDefinition.ReportVersioning``.
        :param s3_bucket: ``AWS::CUR::ReportDefinition.S3Bucket``.
        :param s3_prefix: ``AWS::CUR::ReportDefinition.S3Prefix``.
        :param s3_region: ``AWS::CUR::ReportDefinition.S3Region``.
        :param time_unit: ``AWS::CUR::ReportDefinition.TimeUnit``.
        :param additional_artifacts: ``AWS::CUR::ReportDefinition.AdditionalArtifacts``.
        :param additional_schema_elements: ``AWS::CUR::ReportDefinition.AdditionalSchemaElements``.
        :param billing_view_arn: ``AWS::CUR::ReportDefinition.BillingViewArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "compression": compression,
            "format": format,
            "refresh_closed_reports": refresh_closed_reports,
            "report_name": report_name,
            "report_versioning": report_versioning,
            "s3_bucket": s3_bucket,
            "s3_prefix": s3_prefix,
            "s3_region": s3_region,
            "time_unit": time_unit,
        }
        if additional_artifacts is not None:
            self._values["additional_artifacts"] = additional_artifacts
        if additional_schema_elements is not None:
            self._values["additional_schema_elements"] = additional_schema_elements
        if billing_view_arn is not None:
            self._values["billing_view_arn"] = billing_view_arn

    @builtins.property
    def compression(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.Compression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-compression
        '''
        result = self._values.get("compression")
        assert result is not None, "Required property 'compression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.Format``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-format
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def refresh_closed_reports(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::CUR::ReportDefinition.RefreshClosedReports``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-refreshclosedreports
        '''
        result = self._values.get("refresh_closed_reports")
        assert result is not None, "Required property 'refresh_closed_reports' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def report_name(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.ReportName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-reportname
        '''
        result = self._values.get("report_name")
        assert result is not None, "Required property 'report_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def report_versioning(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.ReportVersioning``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-reportversioning
        '''
        result = self._values.get("report_versioning")
        assert result is not None, "Required property 'report_versioning' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_bucket(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.S3Bucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3bucket
        '''
        result = self._values.get("s3_bucket")
        assert result is not None, "Required property 's3_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_prefix(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.S3Prefix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3prefix
        '''
        result = self._values.get("s3_prefix")
        assert result is not None, "Required property 's3_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_region(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.S3Region``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3region
        '''
        result = self._values.get("s3_region")
        assert result is not None, "Required property 's3_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_unit(self) -> builtins.str:
        '''``AWS::CUR::ReportDefinition.TimeUnit``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-timeunit
        '''
        result = self._values.get("time_unit")
        assert result is not None, "Required property 'time_unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_artifacts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CUR::ReportDefinition.AdditionalArtifacts``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-additionalartifacts
        '''
        result = self._values.get("additional_artifacts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def additional_schema_elements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CUR::ReportDefinition.AdditionalSchemaElements``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-additionalschemaelements
        '''
        result = self._values.get("additional_schema_elements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def billing_view_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CUR::ReportDefinition.BillingViewArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-billingviewarn
        '''
        result = self._values.get("billing_view_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReportDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnReportDefinition",
    "CfnReportDefinitionProps",
]

publication.publish()
