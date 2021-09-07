'''
# AWS::AppIntegrations Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_appintegrations as appintegrations
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
class CfnEventIntegration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appintegrations.CfnEventIntegration",
):
    '''A CloudFormation ``AWS::AppIntegrations::EventIntegration``.

    :cloudformationResource: AWS::AppIntegrations::EventIntegration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        event_bridge_bus: builtins.str,
        event_filter: typing.Union["CfnEventIntegration.EventFilterProperty", aws_cdk.core.IResolvable],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::AppIntegrations::EventIntegration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param event_bridge_bus: ``AWS::AppIntegrations::EventIntegration.EventBridgeBus``.
        :param event_filter: ``AWS::AppIntegrations::EventIntegration.EventFilter``.
        :param name: ``AWS::AppIntegrations::EventIntegration.Name``.
        :param description: ``AWS::AppIntegrations::EventIntegration.Description``.
        :param tags: ``AWS::AppIntegrations::EventIntegration.Tags``.
        '''
        props = CfnEventIntegrationProps(
            event_bridge_bus=event_bridge_bus,
            event_filter=event_filter,
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
    @jsii.member(jsii_name="attrAssociations")
    def attr_associations(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: Associations
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrAssociations"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEventIntegrationArn")
    def attr_event_integration_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: EventIntegrationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventIntegrationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppIntegrations::EventIntegration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventBridgeBus")
    def event_bridge_bus(self) -> builtins.str:
        '''``AWS::AppIntegrations::EventIntegration.EventBridgeBus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventbridgebus
        '''
        return typing.cast(builtins.str, jsii.get(self, "eventBridgeBus"))

    @event_bridge_bus.setter
    def event_bridge_bus(self, value: builtins.str) -> None:
        jsii.set(self, "eventBridgeBus", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventFilter")
    def event_filter(
        self,
    ) -> typing.Union["CfnEventIntegration.EventFilterProperty", aws_cdk.core.IResolvable]:
        '''``AWS::AppIntegrations::EventIntegration.EventFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventfilter
        '''
        return typing.cast(typing.Union["CfnEventIntegration.EventFilterProperty", aws_cdk.core.IResolvable], jsii.get(self, "eventFilter"))

    @event_filter.setter
    def event_filter(
        self,
        value: typing.Union["CfnEventIntegration.EventFilterProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "eventFilter", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::AppIntegrations::EventIntegration.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppIntegrations::EventIntegration.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appintegrations.CfnEventIntegration.EventFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class EventFilterProperty:
        def __init__(self, *, source: builtins.str) -> None:
            '''
            :param source: ``CfnEventIntegration.EventFilterProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "source": source,
            }

        @builtins.property
        def source(self) -> builtins.str:
            '''``CfnEventIntegration.EventFilterProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html#cfn-appintegrations-eventintegration-eventfilter-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appintegrations.CfnEventIntegration.EventIntegrationAssociationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_association_metadata": "clientAssociationMetadata",
            "client_id": "clientId",
            "event_bridge_rule_name": "eventBridgeRuleName",
            "event_integration_association_arn": "eventIntegrationAssociationArn",
            "event_integration_association_id": "eventIntegrationAssociationId",
        },
    )
    class EventIntegrationAssociationProperty:
        def __init__(
            self,
            *,
            client_association_metadata: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEventIntegration.MetadataProperty"]]]] = None,
            client_id: typing.Optional[builtins.str] = None,
            event_bridge_rule_name: typing.Optional[builtins.str] = None,
            event_integration_association_arn: typing.Optional[builtins.str] = None,
            event_integration_association_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param client_association_metadata: ``CfnEventIntegration.EventIntegrationAssociationProperty.ClientAssociationMetadata``.
            :param client_id: ``CfnEventIntegration.EventIntegrationAssociationProperty.ClientId``.
            :param event_bridge_rule_name: ``CfnEventIntegration.EventIntegrationAssociationProperty.EventBridgeRuleName``.
            :param event_integration_association_arn: ``CfnEventIntegration.EventIntegrationAssociationProperty.EventIntegrationAssociationArn``.
            :param event_integration_association_id: ``CfnEventIntegration.EventIntegrationAssociationProperty.EventIntegrationAssociationId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventintegrationassociation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if client_association_metadata is not None:
                self._values["client_association_metadata"] = client_association_metadata
            if client_id is not None:
                self._values["client_id"] = client_id
            if event_bridge_rule_name is not None:
                self._values["event_bridge_rule_name"] = event_bridge_rule_name
            if event_integration_association_arn is not None:
                self._values["event_integration_association_arn"] = event_integration_association_arn
            if event_integration_association_id is not None:
                self._values["event_integration_association_id"] = event_integration_association_id

        @builtins.property
        def client_association_metadata(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEventIntegration.MetadataProperty"]]]]:
            '''``CfnEventIntegration.EventIntegrationAssociationProperty.ClientAssociationMetadata``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventintegrationassociation.html#cfn-appintegrations-eventintegration-eventintegrationassociation-clientassociationmetadata
            '''
            result = self._values.get("client_association_metadata")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEventIntegration.MetadataProperty"]]]], result)

        @builtins.property
        def client_id(self) -> typing.Optional[builtins.str]:
            '''``CfnEventIntegration.EventIntegrationAssociationProperty.ClientId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventintegrationassociation.html#cfn-appintegrations-eventintegration-eventintegrationassociation-clientid
            '''
            result = self._values.get("client_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_bridge_rule_name(self) -> typing.Optional[builtins.str]:
            '''``CfnEventIntegration.EventIntegrationAssociationProperty.EventBridgeRuleName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventintegrationassociation.html#cfn-appintegrations-eventintegration-eventintegrationassociation-eventbridgerulename
            '''
            result = self._values.get("event_bridge_rule_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_integration_association_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnEventIntegration.EventIntegrationAssociationProperty.EventIntegrationAssociationArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventintegrationassociation.html#cfn-appintegrations-eventintegration-eventintegrationassociation-eventintegrationassociationarn
            '''
            result = self._values.get("event_integration_association_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_integration_association_id(self) -> typing.Optional[builtins.str]:
            '''``CfnEventIntegration.EventIntegrationAssociationProperty.EventIntegrationAssociationId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventintegrationassociation.html#cfn-appintegrations-eventintegration-eventintegrationassociation-eventintegrationassociationid
            '''
            result = self._values.get("event_integration_association_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventIntegrationAssociationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appintegrations.CfnEventIntegration.MetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class MetadataProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: ``CfnEventIntegration.MetadataProperty.Key``.
            :param value: ``CfnEventIntegration.MetadataProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-metadata.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnEventIntegration.MetadataProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-metadata.html#cfn-appintegrations-eventintegration-metadata-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnEventIntegration.MetadataProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-metadata.html#cfn-appintegrations-eventintegration-metadata-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appintegrations.CfnEventIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_bridge_bus": "eventBridgeBus",
        "event_filter": "eventFilter",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnEventIntegrationProps:
    def __init__(
        self,
        *,
        event_bridge_bus: builtins.str,
        event_filter: typing.Union[CfnEventIntegration.EventFilterProperty, aws_cdk.core.IResolvable],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppIntegrations::EventIntegration``.

        :param event_bridge_bus: ``AWS::AppIntegrations::EventIntegration.EventBridgeBus``.
        :param event_filter: ``AWS::AppIntegrations::EventIntegration.EventFilter``.
        :param name: ``AWS::AppIntegrations::EventIntegration.Name``.
        :param description: ``AWS::AppIntegrations::EventIntegration.Description``.
        :param tags: ``AWS::AppIntegrations::EventIntegration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "event_bridge_bus": event_bridge_bus,
            "event_filter": event_filter,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def event_bridge_bus(self) -> builtins.str:
        '''``AWS::AppIntegrations::EventIntegration.EventBridgeBus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventbridgebus
        '''
        result = self._values.get("event_bridge_bus")
        assert result is not None, "Required property 'event_bridge_bus' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_filter(
        self,
    ) -> typing.Union[CfnEventIntegration.EventFilterProperty, aws_cdk.core.IResolvable]:
        '''``AWS::AppIntegrations::EventIntegration.EventFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventfilter
        '''
        result = self._values.get("event_filter")
        assert result is not None, "Required property 'event_filter' is missing"
        return typing.cast(typing.Union[CfnEventIntegration.EventFilterProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::AppIntegrations::EventIntegration.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppIntegrations::EventIntegration.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppIntegrations::EventIntegration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEventIntegration",
    "CfnEventIntegrationProps",
]

publication.publish()
