'''
# AWS::EMRContainers Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_emrcontainers as emrcontainers
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
class CfnVirtualCluster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-emrcontainers.CfnVirtualCluster",
):
    '''A CloudFormation ``AWS::EMRContainers::VirtualCluster``.

    :cloudformationResource: AWS::EMRContainers::VirtualCluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        container_provider: typing.Union["CfnVirtualCluster.ContainerProviderProperty", aws_cdk.core.IResolvable],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRContainers::VirtualCluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param container_provider: ``AWS::EMRContainers::VirtualCluster.ContainerProvider``.
        :param name: ``AWS::EMRContainers::VirtualCluster.Name``.
        :param tags: ``AWS::EMRContainers::VirtualCluster.Tags``.
        '''
        props = CfnVirtualClusterProps(
            container_provider=container_provider, name=name, tags=tags
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
        '''``AWS::EMRContainers::VirtualCluster.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containerProvider")
    def container_provider(
        self,
    ) -> typing.Union["CfnVirtualCluster.ContainerProviderProperty", aws_cdk.core.IResolvable]:
        '''``AWS::EMRContainers::VirtualCluster.ContainerProvider``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-containerprovider
        '''
        return typing.cast(typing.Union["CfnVirtualCluster.ContainerProviderProperty", aws_cdk.core.IResolvable], jsii.get(self, "containerProvider"))

    @container_provider.setter
    def container_provider(
        self,
        value: typing.Union["CfnVirtualCluster.ContainerProviderProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "containerProvider", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::EMRContainers::VirtualCluster.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emrcontainers.CfnVirtualCluster.ContainerInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"eks_info": "eksInfo"},
    )
    class ContainerInfoProperty:
        def __init__(
            self,
            *,
            eks_info: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualCluster.EksInfoProperty"],
        ) -> None:
            '''
            :param eks_info: ``CfnVirtualCluster.ContainerInfoProperty.EksInfo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "eks_info": eks_info,
            }

        @builtins.property
        def eks_info(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualCluster.EksInfoProperty"]:
            '''``CfnVirtualCluster.ContainerInfoProperty.EksInfo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html#cfn-emrcontainers-virtualcluster-containerinfo-eksinfo
            '''
            result = self._values.get("eks_info")
            assert result is not None, "Required property 'eks_info' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualCluster.EksInfoProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emrcontainers.CfnVirtualCluster.ContainerProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "info": "info", "type": "type"},
    )
    class ContainerProviderProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            info: typing.Union[aws_cdk.core.IResolvable, "CfnVirtualCluster.ContainerInfoProperty"],
            type: builtins.str,
        ) -> None:
            '''
            :param id: ``CfnVirtualCluster.ContainerProviderProperty.Id``.
            :param info: ``CfnVirtualCluster.ContainerProviderProperty.Info``.
            :param type: ``CfnVirtualCluster.ContainerProviderProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "id": id,
                "info": info,
                "type": type,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''``CfnVirtualCluster.ContainerProviderProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def info(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnVirtualCluster.ContainerInfoProperty"]:
            '''``CfnVirtualCluster.ContainerProviderProperty.Info``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-info
            '''
            result = self._values.get("info")
            assert result is not None, "Required property 'info' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnVirtualCluster.ContainerInfoProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnVirtualCluster.ContainerProviderProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emrcontainers.CfnVirtualCluster.EksInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace"},
    )
    class EksInfoProperty:
        def __init__(self, *, namespace: builtins.str) -> None:
            '''
            :param namespace: ``CfnVirtualCluster.EksInfoProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "namespace": namespace,
            }

        @builtins.property
        def namespace(self) -> builtins.str:
            '''``CfnVirtualCluster.EksInfoProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html#cfn-emrcontainers-virtualcluster-eksinfo-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-emrcontainers.CfnVirtualClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_provider": "containerProvider",
        "name": "name",
        "tags": "tags",
    },
)
class CfnVirtualClusterProps:
    def __init__(
        self,
        *,
        container_provider: typing.Union[CfnVirtualCluster.ContainerProviderProperty, aws_cdk.core.IResolvable],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EMRContainers::VirtualCluster``.

        :param container_provider: ``AWS::EMRContainers::VirtualCluster.ContainerProvider``.
        :param name: ``AWS::EMRContainers::VirtualCluster.Name``.
        :param tags: ``AWS::EMRContainers::VirtualCluster.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "container_provider": container_provider,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def container_provider(
        self,
    ) -> typing.Union[CfnVirtualCluster.ContainerProviderProperty, aws_cdk.core.IResolvable]:
        '''``AWS::EMRContainers::VirtualCluster.ContainerProvider``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-containerprovider
        '''
        result = self._values.get("container_provider")
        assert result is not None, "Required property 'container_provider' is missing"
        return typing.cast(typing.Union[CfnVirtualCluster.ContainerProviderProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::EMRContainers::VirtualCluster.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::EMRContainers::VirtualCluster.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnVirtualCluster",
    "CfnVirtualClusterProps",
]

publication.publish()
