'''
# AWS::MWAA Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_mwaa as mwaa
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
class CfnEnvironment(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-mwaa.CfnEnvironment",
):
    '''A CloudFormation ``AWS::MWAA::Environment``.

    :cloudformationResource: AWS::MWAA::Environment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        airflow_configuration_options: typing.Any = None,
        airflow_version: typing.Optional[builtins.str] = None,
        dag_s3_path: typing.Optional[builtins.str] = None,
        environment_class: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.LoggingConfigurationProperty"]] = None,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        network_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.NetworkConfigurationProperty"]] = None,
        plugins_s3_object_version: typing.Optional[builtins.str] = None,
        plugins_s3_path: typing.Optional[builtins.str] = None,
        requirements_s3_object_version: typing.Optional[builtins.str] = None,
        requirements_s3_path: typing.Optional[builtins.str] = None,
        schedulers: typing.Optional[jsii.Number] = None,
        source_bucket_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional["CfnEnvironment.TagMapProperty"] = None,
        webserver_access_mode: typing.Optional[builtins.str] = None,
        weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::MWAA::Environment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::MWAA::Environment.Name``.
        :param airflow_configuration_options: ``AWS::MWAA::Environment.AirflowConfigurationOptions``.
        :param airflow_version: ``AWS::MWAA::Environment.AirflowVersion``.
        :param dag_s3_path: ``AWS::MWAA::Environment.DagS3Path``.
        :param environment_class: ``AWS::MWAA::Environment.EnvironmentClass``.
        :param execution_role_arn: ``AWS::MWAA::Environment.ExecutionRoleArn``.
        :param kms_key: ``AWS::MWAA::Environment.KmsKey``.
        :param logging_configuration: ``AWS::MWAA::Environment.LoggingConfiguration``.
        :param max_workers: ``AWS::MWAA::Environment.MaxWorkers``.
        :param min_workers: ``AWS::MWAA::Environment.MinWorkers``.
        :param network_configuration: ``AWS::MWAA::Environment.NetworkConfiguration``.
        :param plugins_s3_object_version: ``AWS::MWAA::Environment.PluginsS3ObjectVersion``.
        :param plugins_s3_path: ``AWS::MWAA::Environment.PluginsS3Path``.
        :param requirements_s3_object_version: ``AWS::MWAA::Environment.RequirementsS3ObjectVersion``.
        :param requirements_s3_path: ``AWS::MWAA::Environment.RequirementsS3Path``.
        :param schedulers: ``AWS::MWAA::Environment.Schedulers``.
        :param source_bucket_arn: ``AWS::MWAA::Environment.SourceBucketArn``.
        :param tags: ``AWS::MWAA::Environment.Tags``.
        :param webserver_access_mode: ``AWS::MWAA::Environment.WebserverAccessMode``.
        :param weekly_maintenance_window_start: ``AWS::MWAA::Environment.WeeklyMaintenanceWindowStart``.
        '''
        props = CfnEnvironmentProps(
            name=name,
            airflow_configuration_options=airflow_configuration_options,
            airflow_version=airflow_version,
            dag_s3_path=dag_s3_path,
            environment_class=environment_class,
            execution_role_arn=execution_role_arn,
            kms_key=kms_key,
            logging_configuration=logging_configuration,
            max_workers=max_workers,
            min_workers=min_workers,
            network_configuration=network_configuration,
            plugins_s3_object_version=plugins_s3_object_version,
            plugins_s3_path=plugins_s3_path,
            requirements_s3_object_version=requirements_s3_object_version,
            requirements_s3_path=requirements_s3_path,
            schedulers=schedulers,
            source_bucket_arn=source_bucket_arn,
            tags=tags,
            webserver_access_mode=webserver_access_mode,
            weekly_maintenance_window_start=weekly_maintenance_window_start,
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
    @jsii.member(jsii_name="attrLoggingConfigurationDagProcessingLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_dag_processing_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''
        :cloudformationAttribute: LoggingConfiguration.DagProcessingLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationDagProcessingLogsCloudWatchLogGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoggingConfigurationSchedulerLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_scheduler_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''
        :cloudformationAttribute: LoggingConfiguration.SchedulerLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationSchedulerLogsCloudWatchLogGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoggingConfigurationTaskLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_task_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''
        :cloudformationAttribute: LoggingConfiguration.TaskLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationTaskLogsCloudWatchLogGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoggingConfigurationWebserverLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_webserver_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''
        :cloudformationAttribute: LoggingConfiguration.WebserverLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationWebserverLogsCloudWatchLogGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLoggingConfigurationWorkerLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_worker_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''
        :cloudformationAttribute: LoggingConfiguration.WorkerLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationWorkerLogsCloudWatchLogGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrWebserverUrl")
    def attr_webserver_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: WebserverUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWebserverUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="airflowConfigurationOptions")
    def airflow_configuration_options(self) -> typing.Any:
        '''``AWS::MWAA::Environment.AirflowConfigurationOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowconfigurationoptions
        '''
        return typing.cast(typing.Any, jsii.get(self, "airflowConfigurationOptions"))

    @airflow_configuration_options.setter
    def airflow_configuration_options(self, value: typing.Any) -> None:
        jsii.set(self, "airflowConfigurationOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::MWAA::Environment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="airflowVersion")
    def airflow_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.AirflowVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "airflowVersion"))

    @airflow_version.setter
    def airflow_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "airflowVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dagS3Path")
    def dag_s3_path(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.DagS3Path``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-dags3path
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dagS3Path"))

    @dag_s3_path.setter
    def dag_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dagS3Path", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentClass")
    def environment_class(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.EnvironmentClass``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-environmentclass
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentClass"))

    @environment_class.setter
    def environment_class(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "environmentClass", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-executionrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.KmsKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-kmskey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.LoggingConfigurationProperty"]]:
        '''``AWS::MWAA::Environment.LoggingConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-loggingconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.LoggingConfigurationProperty"]], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.LoggingConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "loggingConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxWorkers")
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MWAA::Environment.MaxWorkers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-maxworkers
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkers"))

    @max_workers.setter
    def max_workers(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maxWorkers", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minWorkers")
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MWAA::Environment.MinWorkers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-minworkers
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkers"))

    @min_workers.setter
    def min_workers(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "minWorkers", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.NetworkConfigurationProperty"]]:
        '''``AWS::MWAA::Environment.NetworkConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-networkconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.NetworkConfigurationProperty"]], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.NetworkConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "networkConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pluginsS3ObjectVersion")
    def plugins_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.PluginsS3ObjectVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3objectversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsS3ObjectVersion"))

    @plugins_s3_object_version.setter
    def plugins_s3_object_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pluginsS3ObjectVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pluginsS3Path")
    def plugins_s3_path(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.PluginsS3Path``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3path
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsS3Path"))

    @plugins_s3_path.setter
    def plugins_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pluginsS3Path", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="requirementsS3ObjectVersion")
    def requirements_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.RequirementsS3ObjectVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3objectversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementsS3ObjectVersion"))

    @requirements_s3_object_version.setter
    def requirements_s3_object_version(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "requirementsS3ObjectVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="requirementsS3Path")
    def requirements_s3_path(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.RequirementsS3Path``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3path
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementsS3Path"))

    @requirements_s3_path.setter
    def requirements_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "requirementsS3Path", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schedulers")
    def schedulers(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MWAA::Environment.Schedulers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-schedulers
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "schedulers"))

    @schedulers.setter
    def schedulers(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "schedulers", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceBucketArn")
    def source_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.SourceBucketArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-sourcebucketarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceBucketArn"))

    @source_bucket_arn.setter
    def source_bucket_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sourceBucketArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional["CfnEnvironment.TagMapProperty"]:
        '''``AWS::MWAA::Environment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-tags
        '''
        return typing.cast(typing.Optional["CfnEnvironment.TagMapProperty"], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional["CfnEnvironment.TagMapProperty"]) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="webserverAccessMode")
    def webserver_access_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.WebserverAccessMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-webserveraccessmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webserverAccessMode"))

    @webserver_access_mode.setter
    def webserver_access_mode(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "webserverAccessMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.WeeklyMaintenanceWindowStart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-weeklymaintenancewindowstart
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weeklyMaintenanceWindowStart"))

    @weekly_maintenance_window_start.setter
    def weekly_maintenance_window_start(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "weeklyMaintenanceWindowStart", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mwaa.CfnEnvironment.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dag_processing_logs": "dagProcessingLogs",
            "scheduler_logs": "schedulerLogs",
            "task_logs": "taskLogs",
            "webserver_logs": "webserverLogs",
            "worker_logs": "workerLogs",
        },
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            dag_processing_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]] = None,
            scheduler_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]] = None,
            task_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]] = None,
            webserver_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]] = None,
            worker_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param dag_processing_logs: ``CfnEnvironment.LoggingConfigurationProperty.DagProcessingLogs``.
            :param scheduler_logs: ``CfnEnvironment.LoggingConfigurationProperty.SchedulerLogs``.
            :param task_logs: ``CfnEnvironment.LoggingConfigurationProperty.TaskLogs``.
            :param webserver_logs: ``CfnEnvironment.LoggingConfigurationProperty.WebserverLogs``.
            :param worker_logs: ``CfnEnvironment.LoggingConfigurationProperty.WorkerLogs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dag_processing_logs is not None:
                self._values["dag_processing_logs"] = dag_processing_logs
            if scheduler_logs is not None:
                self._values["scheduler_logs"] = scheduler_logs
            if task_logs is not None:
                self._values["task_logs"] = task_logs
            if webserver_logs is not None:
                self._values["webserver_logs"] = webserver_logs
            if worker_logs is not None:
                self._values["worker_logs"] = worker_logs

        @builtins.property
        def dag_processing_logs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''``CfnEnvironment.LoggingConfigurationProperty.DagProcessingLogs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-dagprocessinglogs
            '''
            result = self._values.get("dag_processing_logs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        @builtins.property
        def scheduler_logs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''``CfnEnvironment.LoggingConfigurationProperty.SchedulerLogs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-schedulerlogs
            '''
            result = self._values.get("scheduler_logs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        @builtins.property
        def task_logs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''``CfnEnvironment.LoggingConfigurationProperty.TaskLogs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-tasklogs
            '''
            result = self._values.get("task_logs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        @builtins.property
        def webserver_logs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''``CfnEnvironment.LoggingConfigurationProperty.WebserverLogs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-webserverlogs
            '''
            result = self._values.get("webserver_logs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        @builtins.property
        def worker_logs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''``CfnEnvironment.LoggingConfigurationProperty.WorkerLogs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-workerlogs
            '''
            result = self._values.get("worker_logs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_log_group_arn": "cloudWatchLogGroupArn",
            "enabled": "enabled",
            "log_level": "logLevel",
        },
    )
    class ModuleLoggingConfigurationProperty:
        def __init__(
            self,
            *,
            cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            log_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param cloud_watch_log_group_arn: ``CfnEnvironment.ModuleLoggingConfigurationProperty.CloudWatchLogGroupArn``.
            :param enabled: ``CfnEnvironment.ModuleLoggingConfigurationProperty.Enabled``.
            :param log_level: ``CfnEnvironment.ModuleLoggingConfigurationProperty.LogLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_watch_log_group_arn is not None:
                self._values["cloud_watch_log_group_arn"] = cloud_watch_log_group_arn
            if enabled is not None:
                self._values["enabled"] = enabled
            if log_level is not None:
                self._values["log_level"] = log_level

        @builtins.property
        def cloud_watch_log_group_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.ModuleLoggingConfigurationProperty.CloudWatchLogGroupArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-cloudwatchloggrouparn
            '''
            result = self._values.get("cloud_watch_log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnEnvironment.ModuleLoggingConfigurationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.ModuleLoggingConfigurationProperty.LogLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModuleLoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mwaa.CfnEnvironment.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param security_group_ids: ``CfnEnvironment.NetworkConfigurationProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnEnvironment.NetworkConfigurationProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnEnvironment.NetworkConfigurationProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnEnvironment.NetworkConfigurationProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-mwaa.CfnEnvironment.TagMapProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class TagMapProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-tagmap.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-mwaa.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "airflow_configuration_options": "airflowConfigurationOptions",
        "airflow_version": "airflowVersion",
        "dag_s3_path": "dagS3Path",
        "environment_class": "environmentClass",
        "execution_role_arn": "executionRoleArn",
        "kms_key": "kmsKey",
        "logging_configuration": "loggingConfiguration",
        "max_workers": "maxWorkers",
        "min_workers": "minWorkers",
        "network_configuration": "networkConfiguration",
        "plugins_s3_object_version": "pluginsS3ObjectVersion",
        "plugins_s3_path": "pluginsS3Path",
        "requirements_s3_object_version": "requirementsS3ObjectVersion",
        "requirements_s3_path": "requirementsS3Path",
        "schedulers": "schedulers",
        "source_bucket_arn": "sourceBucketArn",
        "tags": "tags",
        "webserver_access_mode": "webserverAccessMode",
        "weekly_maintenance_window_start": "weeklyMaintenanceWindowStart",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        airflow_configuration_options: typing.Any = None,
        airflow_version: typing.Optional[builtins.str] = None,
        dag_s3_path: typing.Optional[builtins.str] = None,
        environment_class: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.LoggingConfigurationProperty]] = None,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        network_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.NetworkConfigurationProperty]] = None,
        plugins_s3_object_version: typing.Optional[builtins.str] = None,
        plugins_s3_path: typing.Optional[builtins.str] = None,
        requirements_s3_object_version: typing.Optional[builtins.str] = None,
        requirements_s3_path: typing.Optional[builtins.str] = None,
        schedulers: typing.Optional[jsii.Number] = None,
        source_bucket_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[CfnEnvironment.TagMapProperty] = None,
        webserver_access_mode: typing.Optional[builtins.str] = None,
        weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::MWAA::Environment``.

        :param name: ``AWS::MWAA::Environment.Name``.
        :param airflow_configuration_options: ``AWS::MWAA::Environment.AirflowConfigurationOptions``.
        :param airflow_version: ``AWS::MWAA::Environment.AirflowVersion``.
        :param dag_s3_path: ``AWS::MWAA::Environment.DagS3Path``.
        :param environment_class: ``AWS::MWAA::Environment.EnvironmentClass``.
        :param execution_role_arn: ``AWS::MWAA::Environment.ExecutionRoleArn``.
        :param kms_key: ``AWS::MWAA::Environment.KmsKey``.
        :param logging_configuration: ``AWS::MWAA::Environment.LoggingConfiguration``.
        :param max_workers: ``AWS::MWAA::Environment.MaxWorkers``.
        :param min_workers: ``AWS::MWAA::Environment.MinWorkers``.
        :param network_configuration: ``AWS::MWAA::Environment.NetworkConfiguration``.
        :param plugins_s3_object_version: ``AWS::MWAA::Environment.PluginsS3ObjectVersion``.
        :param plugins_s3_path: ``AWS::MWAA::Environment.PluginsS3Path``.
        :param requirements_s3_object_version: ``AWS::MWAA::Environment.RequirementsS3ObjectVersion``.
        :param requirements_s3_path: ``AWS::MWAA::Environment.RequirementsS3Path``.
        :param schedulers: ``AWS::MWAA::Environment.Schedulers``.
        :param source_bucket_arn: ``AWS::MWAA::Environment.SourceBucketArn``.
        :param tags: ``AWS::MWAA::Environment.Tags``.
        :param webserver_access_mode: ``AWS::MWAA::Environment.WebserverAccessMode``.
        :param weekly_maintenance_window_start: ``AWS::MWAA::Environment.WeeklyMaintenanceWindowStart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html
        '''
        if isinstance(tags, dict):
            tags = CfnEnvironment.TagMapProperty(**tags)
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if airflow_configuration_options is not None:
            self._values["airflow_configuration_options"] = airflow_configuration_options
        if airflow_version is not None:
            self._values["airflow_version"] = airflow_version
        if dag_s3_path is not None:
            self._values["dag_s3_path"] = dag_s3_path
        if environment_class is not None:
            self._values["environment_class"] = environment_class
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if max_workers is not None:
            self._values["max_workers"] = max_workers
        if min_workers is not None:
            self._values["min_workers"] = min_workers
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if plugins_s3_object_version is not None:
            self._values["plugins_s3_object_version"] = plugins_s3_object_version
        if plugins_s3_path is not None:
            self._values["plugins_s3_path"] = plugins_s3_path
        if requirements_s3_object_version is not None:
            self._values["requirements_s3_object_version"] = requirements_s3_object_version
        if requirements_s3_path is not None:
            self._values["requirements_s3_path"] = requirements_s3_path
        if schedulers is not None:
            self._values["schedulers"] = schedulers
        if source_bucket_arn is not None:
            self._values["source_bucket_arn"] = source_bucket_arn
        if tags is not None:
            self._values["tags"] = tags
        if webserver_access_mode is not None:
            self._values["webserver_access_mode"] = webserver_access_mode
        if weekly_maintenance_window_start is not None:
            self._values["weekly_maintenance_window_start"] = weekly_maintenance_window_start

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::MWAA::Environment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def airflow_configuration_options(self) -> typing.Any:
        '''``AWS::MWAA::Environment.AirflowConfigurationOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowconfigurationoptions
        '''
        result = self._values.get("airflow_configuration_options")
        return typing.cast(typing.Any, result)

    @builtins.property
    def airflow_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.AirflowVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowversion
        '''
        result = self._values.get("airflow_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dag_s3_path(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.DagS3Path``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-dags3path
        '''
        result = self._values.get("dag_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_class(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.EnvironmentClass``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-environmentclass
        '''
        result = self._values.get("environment_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.KmsKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-kmskey
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.LoggingConfigurationProperty]]:
        '''``AWS::MWAA::Environment.LoggingConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.LoggingConfigurationProperty]], result)

    @builtins.property
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MWAA::Environment.MaxWorkers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-maxworkers
        '''
        result = self._values.get("max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MWAA::Environment.MinWorkers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-minworkers
        '''
        result = self._values.get("min_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.NetworkConfigurationProperty]]:
        '''``AWS::MWAA::Environment.NetworkConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.NetworkConfigurationProperty]], result)

    @builtins.property
    def plugins_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.PluginsS3ObjectVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3objectversion
        '''
        result = self._values.get("plugins_s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugins_s3_path(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.PluginsS3Path``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3path
        '''
        result = self._values.get("plugins_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requirements_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.RequirementsS3ObjectVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3objectversion
        '''
        result = self._values.get("requirements_s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requirements_s3_path(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.RequirementsS3Path``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3path
        '''
        result = self._values.get("requirements_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedulers(self) -> typing.Optional[jsii.Number]:
        '''``AWS::MWAA::Environment.Schedulers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-schedulers
        '''
        result = self._values.get("schedulers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.SourceBucketArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-sourcebucketarn
        '''
        result = self._values.get("source_bucket_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[CfnEnvironment.TagMapProperty]:
        '''``AWS::MWAA::Environment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[CfnEnvironment.TagMapProperty], result)

    @builtins.property
    def webserver_access_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.WebserverAccessMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-webserveraccessmode
        '''
        result = self._values.get("webserver_access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weekly_maintenance_window_start(self) -> typing.Optional[builtins.str]:
        '''``AWS::MWAA::Environment.WeeklyMaintenanceWindowStart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-weeklymaintenancewindowstart
        '''
        result = self._values.get("weekly_maintenance_window_start")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()
