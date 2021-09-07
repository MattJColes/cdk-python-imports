'''
# AWS::S3Outposts Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_s3outposts as s3outposts
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
class CfnAccessPoint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-s3outposts.CfnAccessPoint",
):
    '''A CloudFormation ``AWS::S3Outposts::AccessPoint``.

    :cloudformationResource: AWS::S3Outposts::AccessPoint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        bucket: builtins.str,
        name: builtins.str,
        vpc_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnAccessPoint.VpcConfigurationProperty"],
        policy: typing.Any = None,
    ) -> None:
        '''Create a new ``AWS::S3Outposts::AccessPoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bucket: ``AWS::S3Outposts::AccessPoint.Bucket``.
        :param name: ``AWS::S3Outposts::AccessPoint.Name``.
        :param vpc_configuration: ``AWS::S3Outposts::AccessPoint.VpcConfiguration``.
        :param policy: ``AWS::S3Outposts::AccessPoint.Policy``.
        '''
        props = CfnAccessPointProps(
            bucket=bucket,
            name=name,
            vpc_configuration=vpc_configuration,
            policy=policy,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        '''``AWS::S3Outposts::AccessPoint.Bucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-bucket
        '''
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        jsii.set(self, "bucket", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::S3Outposts::AccessPoint.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''``AWS::S3Outposts::AccessPoint.Policy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-policy
        '''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        jsii.set(self, "policy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnAccessPoint.VpcConfigurationProperty"]:
        '''``AWS::S3Outposts::AccessPoint.VpcConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-vpcconfiguration
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnAccessPoint.VpcConfigurationProperty"], jsii.get(self, "vpcConfiguration"))

    @vpc_configuration.setter
    def vpc_configuration(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnAccessPoint.VpcConfigurationProperty"],
    ) -> None:
        jsii.set(self, "vpcConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-s3outposts.CfnAccessPoint.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_id": "vpcId"},
    )
    class VpcConfigurationProperty:
        def __init__(self, *, vpc_id: typing.Optional[builtins.str] = None) -> None:
            '''
            :param vpc_id: ``CfnAccessPoint.VpcConfigurationProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''``CfnAccessPoint.VpcConfigurationProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html#cfn-s3outposts-accesspoint-vpcconfiguration-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-s3outposts.CfnAccessPointProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "name": "name",
        "vpc_configuration": "vpcConfiguration",
        "policy": "policy",
    },
)
class CfnAccessPointProps:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        name: builtins.str,
        vpc_configuration: typing.Union[aws_cdk.core.IResolvable, CfnAccessPoint.VpcConfigurationProperty],
        policy: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``AWS::S3Outposts::AccessPoint``.

        :param bucket: ``AWS::S3Outposts::AccessPoint.Bucket``.
        :param name: ``AWS::S3Outposts::AccessPoint.Name``.
        :param vpc_configuration: ``AWS::S3Outposts::AccessPoint.VpcConfiguration``.
        :param policy: ``AWS::S3Outposts::AccessPoint.Policy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "name": name,
            "vpc_configuration": vpc_configuration,
        }
        if policy is not None:
            self._values["policy"] = policy

    @builtins.property
    def bucket(self) -> builtins.str:
        '''``AWS::S3Outposts::AccessPoint.Bucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-bucket
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::S3Outposts::AccessPoint.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnAccessPoint.VpcConfigurationProperty]:
        '''``AWS::S3Outposts::AccessPoint.VpcConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-vpcconfiguration
        '''
        result = self._values.get("vpc_configuration")
        assert result is not None, "Required property 'vpc_configuration' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnAccessPoint.VpcConfigurationProperty], result)

    @builtins.property
    def policy(self) -> typing.Any:
        '''``AWS::S3Outposts::AccessPoint.Policy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-policy
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnBucket(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-s3outposts.CfnBucket",
):
    '''A CloudFormation ``AWS::S3Outposts::Bucket``.

    :cloudformationResource: AWS::S3Outposts::Bucket
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        bucket_name: builtins.str,
        outpost_id: builtins.str,
        lifecycle_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.LifecycleConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::S3Outposts::Bucket``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bucket_name: ``AWS::S3Outposts::Bucket.BucketName``.
        :param outpost_id: ``AWS::S3Outposts::Bucket.OutpostId``.
        :param lifecycle_configuration: ``AWS::S3Outposts::Bucket.LifecycleConfiguration``.
        :param tags: ``AWS::S3Outposts::Bucket.Tags``.
        '''
        props = CfnBucketProps(
            bucket_name=bucket_name,
            outpost_id=outpost_id,
            lifecycle_configuration=lifecycle_configuration,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::S3Outposts::Bucket.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        '''``AWS::S3Outposts::Bucket.BucketName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-bucketname
        '''
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        jsii.set(self, "bucketName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outpostId")
    def outpost_id(self) -> builtins.str:
        '''``AWS::S3Outposts::Bucket.OutpostId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-outpostid
        '''
        return typing.cast(builtins.str, jsii.get(self, "outpostId"))

    @outpost_id.setter
    def outpost_id(self, value: builtins.str) -> None:
        jsii.set(self, "outpostId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lifecycleConfiguration")
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.LifecycleConfigurationProperty"]]:
        '''``AWS::S3Outposts::Bucket.LifecycleConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-lifecycleconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.LifecycleConfigurationProperty"]], jsii.get(self, "lifecycleConfiguration"))

    @lifecycle_configuration.setter
    def lifecycle_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.LifecycleConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "lifecycleConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-s3outposts.CfnBucket.AbortIncompleteMultipartUploadProperty",
        jsii_struct_bases=[],
        name_mapping={"days_after_initiation": "daysAfterInitiation"},
    )
    class AbortIncompleteMultipartUploadProperty:
        def __init__(self, *, days_after_initiation: jsii.Number) -> None:
            '''
            :param days_after_initiation: ``CfnBucket.AbortIncompleteMultipartUploadProperty.DaysAfterInitiation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "days_after_initiation": days_after_initiation,
            }

        @builtins.property
        def days_after_initiation(self) -> jsii.Number:
            '''``CfnBucket.AbortIncompleteMultipartUploadProperty.DaysAfterInitiation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html#cfn-s3outposts-bucket-abortincompletemultipartupload-daysafterinitiation
            '''
            result = self._values.get("days_after_initiation")
            assert result is not None, "Required property 'days_after_initiation' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbortIncompleteMultipartUploadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-s3outposts.CfnBucket.LifecycleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"rules": "rules"},
    )
    class LifecycleConfigurationProperty:
        def __init__(
            self,
            *,
            rules: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.RuleProperty"]]],
        ) -> None:
            '''
            :param rules: ``CfnBucket.LifecycleConfigurationProperty.Rules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "rules": rules,
            }

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.RuleProperty"]]]:
            '''``CfnBucket.LifecycleConfigurationProperty.Rules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html#cfn-s3outposts-bucket-lifecycleconfiguration-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.RuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-s3outposts.CfnBucket.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "abort_incomplete_multipart_upload": "abortIncompleteMultipartUpload",
            "expiration_date": "expirationDate",
            "expiration_in_days": "expirationInDays",
            "filter": "filter",
            "id": "id",
            "status": "status",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            abort_incomplete_multipart_upload: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.AbortIncompleteMultipartUploadProperty"]] = None,
            expiration_date: typing.Optional[builtins.str] = None,
            expiration_in_days: typing.Optional[jsii.Number] = None,
            filter: typing.Any = None,
            id: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param abort_incomplete_multipart_upload: ``CfnBucket.RuleProperty.AbortIncompleteMultipartUpload``.
            :param expiration_date: ``CfnBucket.RuleProperty.ExpirationDate``.
            :param expiration_in_days: ``CfnBucket.RuleProperty.ExpirationInDays``.
            :param filter: ``CfnBucket.RuleProperty.Filter``.
            :param id: ``CfnBucket.RuleProperty.Id``.
            :param status: ``CfnBucket.RuleProperty.Status``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if abort_incomplete_multipart_upload is not None:
                self._values["abort_incomplete_multipart_upload"] = abort_incomplete_multipart_upload
            if expiration_date is not None:
                self._values["expiration_date"] = expiration_date
            if expiration_in_days is not None:
                self._values["expiration_in_days"] = expiration_in_days
            if filter is not None:
                self._values["filter"] = filter
            if id is not None:
                self._values["id"] = id
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def abort_incomplete_multipart_upload(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.AbortIncompleteMultipartUploadProperty"]]:
            '''``CfnBucket.RuleProperty.AbortIncompleteMultipartUpload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-abortincompletemultipartupload
            '''
            result = self._values.get("abort_incomplete_multipart_upload")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBucket.AbortIncompleteMultipartUploadProperty"]], result)

        @builtins.property
        def expiration_date(self) -> typing.Optional[builtins.str]:
            '''``CfnBucket.RuleProperty.ExpirationDate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationdate
            '''
            result = self._values.get("expiration_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expiration_in_days(self) -> typing.Optional[jsii.Number]:
            '''``CfnBucket.RuleProperty.ExpirationInDays``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationindays
            '''
            result = self._values.get("expiration_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def filter(self) -> typing.Any:
            '''``CfnBucket.RuleProperty.Filter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-filter
            '''
            result = self._values.get("filter")
            return typing.cast(typing.Any, result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''``CfnBucket.RuleProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''``CfnBucket.RuleProperty.Status``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnBucketPolicy(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-s3outposts.CfnBucketPolicy",
):
    '''A CloudFormation ``AWS::S3Outposts::BucketPolicy``.

    :cloudformationResource: AWS::S3Outposts::BucketPolicy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        bucket: builtins.str,
        policy_document: typing.Any,
    ) -> None:
        '''Create a new ``AWS::S3Outposts::BucketPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bucket: ``AWS::S3Outposts::BucketPolicy.Bucket``.
        :param policy_document: ``AWS::S3Outposts::BucketPolicy.PolicyDocument``.
        '''
        props = CfnBucketPolicyProps(bucket=bucket, policy_document=policy_document)

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
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        '''``AWS::S3Outposts::BucketPolicy.Bucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-bucket
        '''
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        jsii.set(self, "bucket", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''``AWS::S3Outposts::BucketPolicy.PolicyDocument``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-policydocument
        '''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        jsii.set(self, "policyDocument", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-s3outposts.CfnBucketPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "policy_document": "policyDocument"},
)
class CfnBucketPolicyProps:
    def __init__(self, *, bucket: builtins.str, policy_document: typing.Any) -> None:
        '''Properties for defining a ``AWS::S3Outposts::BucketPolicy``.

        :param bucket: ``AWS::S3Outposts::BucketPolicy.Bucket``.
        :param policy_document: ``AWS::S3Outposts::BucketPolicy.PolicyDocument``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "policy_document": policy_document,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''``AWS::S3Outposts::BucketPolicy.Bucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-bucket
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''``AWS::S3Outposts::BucketPolicy.PolicyDocument``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBucketPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-s3outposts.CfnBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "outpost_id": "outpostId",
        "lifecycle_configuration": "lifecycleConfiguration",
        "tags": "tags",
    },
)
class CfnBucketProps:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        outpost_id: builtins.str,
        lifecycle_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnBucket.LifecycleConfigurationProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::S3Outposts::Bucket``.

        :param bucket_name: ``AWS::S3Outposts::Bucket.BucketName``.
        :param outpost_id: ``AWS::S3Outposts::Bucket.OutpostId``.
        :param lifecycle_configuration: ``AWS::S3Outposts::Bucket.LifecycleConfiguration``.
        :param tags: ``AWS::S3Outposts::Bucket.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "outpost_id": outpost_id,
        }
        if lifecycle_configuration is not None:
            self._values["lifecycle_configuration"] = lifecycle_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''``AWS::S3Outposts::Bucket.BucketName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-bucketname
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def outpost_id(self) -> builtins.str:
        '''``AWS::S3Outposts::Bucket.OutpostId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-outpostid
        '''
        result = self._values.get("outpost_id")
        assert result is not None, "Required property 'outpost_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnBucket.LifecycleConfigurationProperty]]:
        '''``AWS::S3Outposts::Bucket.LifecycleConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-lifecycleconfiguration
        '''
        result = self._values.get("lifecycle_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnBucket.LifecycleConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::S3Outposts::Bucket.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEndpoint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-s3outposts.CfnEndpoint",
):
    '''A CloudFormation ``AWS::S3Outposts::Endpoint``.

    :cloudformationResource: AWS::S3Outposts::Endpoint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        outpost_id: builtins.str,
        security_group_id: builtins.str,
        subnet_id: builtins.str,
        access_type: typing.Optional[builtins.str] = None,
        customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::S3Outposts::Endpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param outpost_id: ``AWS::S3Outposts::Endpoint.OutpostId``.
        :param security_group_id: ``AWS::S3Outposts::Endpoint.SecurityGroupId``.
        :param subnet_id: ``AWS::S3Outposts::Endpoint.SubnetId``.
        :param access_type: ``AWS::S3Outposts::Endpoint.AccessType``.
        :param customer_owned_ipv4_pool: ``AWS::S3Outposts::Endpoint.CustomerOwnedIpv4Pool``.
        '''
        props = CfnEndpointProps(
            outpost_id=outpost_id,
            security_group_id=security_group_id,
            subnet_id=subnet_id,
            access_type=access_type,
            customer_owned_ipv4_pool=customer_owned_ipv4_pool,
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
    @jsii.member(jsii_name="attrCidrBlock")
    def attr_cidr_block(self) -> builtins.str:
        '''
        :cloudformationAttribute: CidrBlock
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCidrBlock"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrNetworkInterfaces")
    def attr_network_interfaces(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: NetworkInterfaces
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrNetworkInterfaces"))

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
    @jsii.member(jsii_name="outpostId")
    def outpost_id(self) -> builtins.str:
        '''``AWS::S3Outposts::Endpoint.OutpostId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-outpostid
        '''
        return typing.cast(builtins.str, jsii.get(self, "outpostId"))

    @outpost_id.setter
    def outpost_id(self, value: builtins.str) -> None:
        jsii.set(self, "outpostId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        '''``AWS::S3Outposts::Endpoint.SecurityGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-securitygroupid
        '''
        return typing.cast(builtins.str, jsii.get(self, "securityGroupId"))

    @security_group_id.setter
    def security_group_id(self, value: builtins.str) -> None:
        jsii.set(self, "securityGroupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        '''``AWS::S3Outposts::Endpoint.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-subnetid
        '''
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        jsii.set(self, "subnetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessType")
    def access_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::S3Outposts::Endpoint.AccessType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-accesstype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessType"))

    @access_type.setter
    def access_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "accessType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> typing.Optional[builtins.str]:
        '''``AWS::S3Outposts::Endpoint.CustomerOwnedIpv4Pool``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-customerownedipv4pool
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerOwnedIpv4Pool"))

    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "customerOwnedIpv4Pool", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-s3outposts.CfnEndpoint.NetworkInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={"network_interface_id": "networkInterfaceId"},
    )
    class NetworkInterfaceProperty:
        def __init__(self, *, network_interface_id: builtins.str) -> None:
            '''
            :param network_interface_id: ``CfnEndpoint.NetworkInterfaceProperty.NetworkInterfaceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-networkinterface.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "network_interface_id": network_interface_id,
            }

        @builtins.property
        def network_interface_id(self) -> builtins.str:
            '''``CfnEndpoint.NetworkInterfaceProperty.NetworkInterfaceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-networkinterface.html#cfn-s3outposts-endpoint-networkinterface-networkinterfaceid
            '''
            result = self._values.get("network_interface_id")
            assert result is not None, "Required property 'network_interface_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-s3outposts.CfnEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "outpost_id": "outpostId",
        "security_group_id": "securityGroupId",
        "subnet_id": "subnetId",
        "access_type": "accessType",
        "customer_owned_ipv4_pool": "customerOwnedIpv4Pool",
    },
)
class CfnEndpointProps:
    def __init__(
        self,
        *,
        outpost_id: builtins.str,
        security_group_id: builtins.str,
        subnet_id: builtins.str,
        access_type: typing.Optional[builtins.str] = None,
        customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::S3Outposts::Endpoint``.

        :param outpost_id: ``AWS::S3Outposts::Endpoint.OutpostId``.
        :param security_group_id: ``AWS::S3Outposts::Endpoint.SecurityGroupId``.
        :param subnet_id: ``AWS::S3Outposts::Endpoint.SubnetId``.
        :param access_type: ``AWS::S3Outposts::Endpoint.AccessType``.
        :param customer_owned_ipv4_pool: ``AWS::S3Outposts::Endpoint.CustomerOwnedIpv4Pool``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "outpost_id": outpost_id,
            "security_group_id": security_group_id,
            "subnet_id": subnet_id,
        }
        if access_type is not None:
            self._values["access_type"] = access_type
        if customer_owned_ipv4_pool is not None:
            self._values["customer_owned_ipv4_pool"] = customer_owned_ipv4_pool

    @builtins.property
    def outpost_id(self) -> builtins.str:
        '''``AWS::S3Outposts::Endpoint.OutpostId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-outpostid
        '''
        result = self._values.get("outpost_id")
        assert result is not None, "Required property 'outpost_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_id(self) -> builtins.str:
        '''``AWS::S3Outposts::Endpoint.SecurityGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-securitygroupid
        '''
        result = self._values.get("security_group_id")
        assert result is not None, "Required property 'security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''``AWS::S3Outposts::Endpoint.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-subnetid
        '''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::S3Outposts::Endpoint.AccessType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-accesstype
        '''
        result = self._values.get("access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_owned_ipv4_pool(self) -> typing.Optional[builtins.str]:
        '''``AWS::S3Outposts::Endpoint.CustomerOwnedIpv4Pool``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-customerownedipv4pool
        '''
        result = self._values.get("customer_owned_ipv4_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessPoint",
    "CfnAccessPointProps",
    "CfnBucket",
    "CfnBucketPolicy",
    "CfnBucketPolicyProps",
    "CfnBucketProps",
    "CfnEndpoint",
    "CfnEndpointProps",
]

publication.publish()
