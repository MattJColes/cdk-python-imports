'''
# AWS::Location Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_location as location
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
class CfnGeofenceCollection(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-location.CfnGeofenceCollection",
):
    '''A CloudFormation ``AWS::Location::GeofenceCollection``.

    :cloudformationResource: AWS::Location::GeofenceCollection
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        collection_name: builtins.str,
        pricing_plan: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        pricing_plan_data_source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Location::GeofenceCollection``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param collection_name: ``AWS::Location::GeofenceCollection.CollectionName``.
        :param pricing_plan: ``AWS::Location::GeofenceCollection.PricingPlan``.
        :param description: ``AWS::Location::GeofenceCollection.Description``.
        :param kms_key_id: ``AWS::Location::GeofenceCollection.KmsKeyId``.
        :param pricing_plan_data_source: ``AWS::Location::GeofenceCollection.PricingPlanDataSource``.
        '''
        props = CfnGeofenceCollectionProps(
            collection_name=collection_name,
            pricing_plan=pricing_plan,
            description=description,
            kms_key_id=kms_key_id,
            pricing_plan_data_source=pricing_plan_data_source,
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
    @jsii.member(jsii_name="attrCollectionArn")
    def attr_collection_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: CollectionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollectionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="collectionName")
    def collection_name(self) -> builtins.str:
        '''``AWS::Location::GeofenceCollection.CollectionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-collectionname
        '''
        return typing.cast(builtins.str, jsii.get(self, "collectionName"))

    @collection_name.setter
    def collection_name(self, value: builtins.str) -> None:
        jsii.set(self, "collectionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::GeofenceCollection.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplan
        '''
        return typing.cast(builtins.str, jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: builtins.str) -> None:
        jsii.set(self, "pricingPlan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::GeofenceCollection.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::GeofenceCollection.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pricingPlanDataSource")
    def pricing_plan_data_source(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::GeofenceCollection.PricingPlanDataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplandatasource
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlanDataSource"))

    @pricing_plan_data_source.setter
    def pricing_plan_data_source(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pricingPlanDataSource", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-location.CfnGeofenceCollectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "collection_name": "collectionName",
        "pricing_plan": "pricingPlan",
        "description": "description",
        "kms_key_id": "kmsKeyId",
        "pricing_plan_data_source": "pricingPlanDataSource",
    },
)
class CfnGeofenceCollectionProps:
    def __init__(
        self,
        *,
        collection_name: builtins.str,
        pricing_plan: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        pricing_plan_data_source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Location::GeofenceCollection``.

        :param collection_name: ``AWS::Location::GeofenceCollection.CollectionName``.
        :param pricing_plan: ``AWS::Location::GeofenceCollection.PricingPlan``.
        :param description: ``AWS::Location::GeofenceCollection.Description``.
        :param kms_key_id: ``AWS::Location::GeofenceCollection.KmsKeyId``.
        :param pricing_plan_data_source: ``AWS::Location::GeofenceCollection.PricingPlanDataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "collection_name": collection_name,
            "pricing_plan": pricing_plan,
        }
        if description is not None:
            self._values["description"] = description
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if pricing_plan_data_source is not None:
            self._values["pricing_plan_data_source"] = pricing_plan_data_source

    @builtins.property
    def collection_name(self) -> builtins.str:
        '''``AWS::Location::GeofenceCollection.CollectionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-collectionname
        '''
        result = self._values.get("collection_name")
        assert result is not None, "Required property 'collection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::GeofenceCollection.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplan
        '''
        result = self._values.get("pricing_plan")
        assert result is not None, "Required property 'pricing_plan' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::GeofenceCollection.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::GeofenceCollection.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan_data_source(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::GeofenceCollection.PricingPlanDataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplandatasource
        '''
        result = self._values.get("pricing_plan_data_source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGeofenceCollectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMap(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-location.CfnMap",
):
    '''A CloudFormation ``AWS::Location::Map``.

    :cloudformationResource: AWS::Location::Map
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        configuration: typing.Union["CfnMap.MapConfigurationProperty", aws_cdk.core.IResolvable],
        map_name: builtins.str,
        pricing_plan: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Location::Map``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param configuration: ``AWS::Location::Map.Configuration``.
        :param map_name: ``AWS::Location::Map.MapName``.
        :param pricing_plan: ``AWS::Location::Map.PricingPlan``.
        :param description: ``AWS::Location::Map.Description``.
        '''
        props = CfnMapProps(
            configuration=configuration,
            map_name=map_name,
            pricing_plan=pricing_plan,
            description=description,
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
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDataSource")
    def attr_data_source(self) -> builtins.str:
        '''
        :cloudformationAttribute: DataSource
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataSource"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMapArn")
    def attr_map_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: MapArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMapArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union["CfnMap.MapConfigurationProperty", aws_cdk.core.IResolvable]:
        '''``AWS::Location::Map.Configuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-configuration
        '''
        return typing.cast(typing.Union["CfnMap.MapConfigurationProperty", aws_cdk.core.IResolvable], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union["CfnMap.MapConfigurationProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "configuration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mapName")
    def map_name(self) -> builtins.str:
        '''``AWS::Location::Map.MapName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-mapname
        '''
        return typing.cast(builtins.str, jsii.get(self, "mapName"))

    @map_name.setter
    def map_name(self, value: builtins.str) -> None:
        jsii.set(self, "mapName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::Map.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-pricingplan
        '''
        return typing.cast(builtins.str, jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: builtins.str) -> None:
        jsii.set(self, "pricingPlan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::Map.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-location.CfnMap.MapConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"style": "style"},
    )
    class MapConfigurationProperty:
        def __init__(self, *, style: builtins.str) -> None:
            '''
            :param style: ``CfnMap.MapConfigurationProperty.Style``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "style": style,
            }

        @builtins.property
        def style(self) -> builtins.str:
            '''``CfnMap.MapConfigurationProperty.Style``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html#cfn-location-map-mapconfiguration-style
            '''
            result = self._values.get("style")
            assert result is not None, "Required property 'style' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MapConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-location.CfnMapProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "map_name": "mapName",
        "pricing_plan": "pricingPlan",
        "description": "description",
    },
)
class CfnMapProps:
    def __init__(
        self,
        *,
        configuration: typing.Union[CfnMap.MapConfigurationProperty, aws_cdk.core.IResolvable],
        map_name: builtins.str,
        pricing_plan: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Location::Map``.

        :param configuration: ``AWS::Location::Map.Configuration``.
        :param map_name: ``AWS::Location::Map.MapName``.
        :param pricing_plan: ``AWS::Location::Map.PricingPlan``.
        :param description: ``AWS::Location::Map.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "configuration": configuration,
            "map_name": map_name,
            "pricing_plan": pricing_plan,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[CfnMap.MapConfigurationProperty, aws_cdk.core.IResolvable]:
        '''``AWS::Location::Map.Configuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[CfnMap.MapConfigurationProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def map_name(self) -> builtins.str:
        '''``AWS::Location::Map.MapName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-mapname
        '''
        result = self._values.get("map_name")
        assert result is not None, "Required property 'map_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::Map.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-pricingplan
        '''
        result = self._values.get("pricing_plan")
        assert result is not None, "Required property 'pricing_plan' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::Map.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMapProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPlaceIndex(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-location.CfnPlaceIndex",
):
    '''A CloudFormation ``AWS::Location::PlaceIndex``.

    :cloudformationResource: AWS::Location::PlaceIndex
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        data_source: builtins.str,
        index_name: builtins.str,
        pricing_plan: builtins.str,
        data_source_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPlaceIndex.DataSourceConfigurationProperty"]] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Location::PlaceIndex``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_source: ``AWS::Location::PlaceIndex.DataSource``.
        :param index_name: ``AWS::Location::PlaceIndex.IndexName``.
        :param pricing_plan: ``AWS::Location::PlaceIndex.PricingPlan``.
        :param data_source_configuration: ``AWS::Location::PlaceIndex.DataSourceConfiguration``.
        :param description: ``AWS::Location::PlaceIndex.Description``.
        '''
        props = CfnPlaceIndexProps(
            data_source=data_source,
            index_name=index_name,
            pricing_plan=pricing_plan,
            data_source_configuration=data_source_configuration,
            description=description,
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
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIndexArn")
    def attr_index_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: IndexArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIndexArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        '''``AWS::Location::PlaceIndex.DataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasource
        '''
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        jsii.set(self, "dataSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> builtins.str:
        '''``AWS::Location::PlaceIndex.IndexName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-indexname
        '''
        return typing.cast(builtins.str, jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: builtins.str) -> None:
        jsii.set(self, "indexName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::PlaceIndex.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-pricingplan
        '''
        return typing.cast(builtins.str, jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: builtins.str) -> None:
        jsii.set(self, "pricingPlan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSourceConfiguration")
    def data_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPlaceIndex.DataSourceConfigurationProperty"]]:
        '''``AWS::Location::PlaceIndex.DataSourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasourceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPlaceIndex.DataSourceConfigurationProperty"]], jsii.get(self, "dataSourceConfiguration"))

    @data_source_configuration.setter
    def data_source_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPlaceIndex.DataSourceConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "dataSourceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::PlaceIndex.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-location.CfnPlaceIndex.DataSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"intended_use": "intendedUse"},
    )
    class DataSourceConfigurationProperty:
        def __init__(
            self,
            *,
            intended_use: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param intended_use: ``CfnPlaceIndex.DataSourceConfigurationProperty.IntendedUse``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if intended_use is not None:
                self._values["intended_use"] = intended_use

        @builtins.property
        def intended_use(self) -> typing.Optional[builtins.str]:
            '''``CfnPlaceIndex.DataSourceConfigurationProperty.IntendedUse``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html#cfn-location-placeindex-datasourceconfiguration-intendeduse
            '''
            result = self._values.get("intended_use")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-location.CfnPlaceIndexProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_source": "dataSource",
        "index_name": "indexName",
        "pricing_plan": "pricingPlan",
        "data_source_configuration": "dataSourceConfiguration",
        "description": "description",
    },
)
class CfnPlaceIndexProps:
    def __init__(
        self,
        *,
        data_source: builtins.str,
        index_name: builtins.str,
        pricing_plan: builtins.str,
        data_source_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPlaceIndex.DataSourceConfigurationProperty]] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Location::PlaceIndex``.

        :param data_source: ``AWS::Location::PlaceIndex.DataSource``.
        :param index_name: ``AWS::Location::PlaceIndex.IndexName``.
        :param pricing_plan: ``AWS::Location::PlaceIndex.PricingPlan``.
        :param data_source_configuration: ``AWS::Location::PlaceIndex.DataSourceConfiguration``.
        :param description: ``AWS::Location::PlaceIndex.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_source": data_source,
            "index_name": index_name,
            "pricing_plan": pricing_plan,
        }
        if data_source_configuration is not None:
            self._values["data_source_configuration"] = data_source_configuration
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def data_source(self) -> builtins.str:
        '''``AWS::Location::PlaceIndex.DataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasource
        '''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_name(self) -> builtins.str:
        '''``AWS::Location::PlaceIndex.IndexName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-indexname
        '''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::PlaceIndex.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-pricingplan
        '''
        result = self._values.get("pricing_plan")
        assert result is not None, "Required property 'pricing_plan' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPlaceIndex.DataSourceConfigurationProperty]]:
        '''``AWS::Location::PlaceIndex.DataSourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasourceconfiguration
        '''
        result = self._values.get("data_source_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPlaceIndex.DataSourceConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::PlaceIndex.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlaceIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRouteCalculator(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-location.CfnRouteCalculator",
):
    '''A CloudFormation ``AWS::Location::RouteCalculator``.

    :cloudformationResource: AWS::Location::RouteCalculator
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        calculator_name: builtins.str,
        data_source: builtins.str,
        pricing_plan: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Location::RouteCalculator``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param calculator_name: ``AWS::Location::RouteCalculator.CalculatorName``.
        :param data_source: ``AWS::Location::RouteCalculator.DataSource``.
        :param pricing_plan: ``AWS::Location::RouteCalculator.PricingPlan``.
        :param description: ``AWS::Location::RouteCalculator.Description``.
        '''
        props = CfnRouteCalculatorProps(
            calculator_name=calculator_name,
            data_source=data_source,
            pricing_plan=pricing_plan,
            description=description,
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
    @jsii.member(jsii_name="attrCalculatorArn")
    def attr_calculator_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: CalculatorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCalculatorArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="calculatorName")
    def calculator_name(self) -> builtins.str:
        '''``AWS::Location::RouteCalculator.CalculatorName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-calculatorname
        '''
        return typing.cast(builtins.str, jsii.get(self, "calculatorName"))

    @calculator_name.setter
    def calculator_name(self, value: builtins.str) -> None:
        jsii.set(self, "calculatorName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        '''``AWS::Location::RouteCalculator.DataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-datasource
        '''
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        jsii.set(self, "dataSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::RouteCalculator.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-pricingplan
        '''
        return typing.cast(builtins.str, jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: builtins.str) -> None:
        jsii.set(self, "pricingPlan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::RouteCalculator.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-location.CfnRouteCalculatorProps",
    jsii_struct_bases=[],
    name_mapping={
        "calculator_name": "calculatorName",
        "data_source": "dataSource",
        "pricing_plan": "pricingPlan",
        "description": "description",
    },
)
class CfnRouteCalculatorProps:
    def __init__(
        self,
        *,
        calculator_name: builtins.str,
        data_source: builtins.str,
        pricing_plan: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Location::RouteCalculator``.

        :param calculator_name: ``AWS::Location::RouteCalculator.CalculatorName``.
        :param data_source: ``AWS::Location::RouteCalculator.DataSource``.
        :param pricing_plan: ``AWS::Location::RouteCalculator.PricingPlan``.
        :param description: ``AWS::Location::RouteCalculator.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "calculator_name": calculator_name,
            "data_source": data_source,
            "pricing_plan": pricing_plan,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def calculator_name(self) -> builtins.str:
        '''``AWS::Location::RouteCalculator.CalculatorName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-calculatorname
        '''
        result = self._values.get("calculator_name")
        assert result is not None, "Required property 'calculator_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source(self) -> builtins.str:
        '''``AWS::Location::RouteCalculator.DataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-datasource
        '''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::RouteCalculator.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-pricingplan
        '''
        result = self._values.get("pricing_plan")
        assert result is not None, "Required property 'pricing_plan' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::RouteCalculator.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouteCalculatorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTracker(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-location.CfnTracker",
):
    '''A CloudFormation ``AWS::Location::Tracker``.

    :cloudformationResource: AWS::Location::Tracker
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        pricing_plan: builtins.str,
        tracker_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        pricing_plan_data_source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Location::Tracker``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param pricing_plan: ``AWS::Location::Tracker.PricingPlan``.
        :param tracker_name: ``AWS::Location::Tracker.TrackerName``.
        :param description: ``AWS::Location::Tracker.Description``.
        :param kms_key_id: ``AWS::Location::Tracker.KmsKeyId``.
        :param pricing_plan_data_source: ``AWS::Location::Tracker.PricingPlanDataSource``.
        '''
        props = CfnTrackerProps(
            pricing_plan=pricing_plan,
            tracker_name=tracker_name,
            description=description,
            kms_key_id=kms_key_id,
            pricing_plan_data_source=pricing_plan_data_source,
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
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTrackerArn")
    def attr_tracker_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: TrackerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTrackerArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::Tracker.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplan
        '''
        return typing.cast(builtins.str, jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: builtins.str) -> None:
        jsii.set(self, "pricingPlan", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trackerName")
    def tracker_name(self) -> builtins.str:
        '''``AWS::Location::Tracker.TrackerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-trackername
        '''
        return typing.cast(builtins.str, jsii.get(self, "trackerName"))

    @tracker_name.setter
    def tracker_name(self, value: builtins.str) -> None:
        jsii.set(self, "trackerName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::Tracker.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::Tracker.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pricingPlanDataSource")
    def pricing_plan_data_source(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::Tracker.PricingPlanDataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplandatasource
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlanDataSource"))

    @pricing_plan_data_source.setter
    def pricing_plan_data_source(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pricingPlanDataSource", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTrackerConsumer(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-location.CfnTrackerConsumer",
):
    '''A CloudFormation ``AWS::Location::TrackerConsumer``.

    :cloudformationResource: AWS::Location::TrackerConsumer
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        consumer_arn: builtins.str,
        tracker_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::Location::TrackerConsumer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param consumer_arn: ``AWS::Location::TrackerConsumer.ConsumerArn``.
        :param tracker_name: ``AWS::Location::TrackerConsumer.TrackerName``.
        '''
        props = CfnTrackerConsumerProps(
            consumer_arn=consumer_arn, tracker_name=tracker_name
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
    @jsii.member(jsii_name="consumerArn")
    def consumer_arn(self) -> builtins.str:
        '''``AWS::Location::TrackerConsumer.ConsumerArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-consumerarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "consumerArn"))

    @consumer_arn.setter
    def consumer_arn(self, value: builtins.str) -> None:
        jsii.set(self, "consumerArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trackerName")
    def tracker_name(self) -> builtins.str:
        '''``AWS::Location::TrackerConsumer.TrackerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-trackername
        '''
        return typing.cast(builtins.str, jsii.get(self, "trackerName"))

    @tracker_name.setter
    def tracker_name(self, value: builtins.str) -> None:
        jsii.set(self, "trackerName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-location.CfnTrackerConsumerProps",
    jsii_struct_bases=[],
    name_mapping={"consumer_arn": "consumerArn", "tracker_name": "trackerName"},
)
class CfnTrackerConsumerProps:
    def __init__(
        self,
        *,
        consumer_arn: builtins.str,
        tracker_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::Location::TrackerConsumer``.

        :param consumer_arn: ``AWS::Location::TrackerConsumer.ConsumerArn``.
        :param tracker_name: ``AWS::Location::TrackerConsumer.TrackerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "consumer_arn": consumer_arn,
            "tracker_name": tracker_name,
        }

    @builtins.property
    def consumer_arn(self) -> builtins.str:
        '''``AWS::Location::TrackerConsumer.ConsumerArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-consumerarn
        '''
        result = self._values.get("consumer_arn")
        assert result is not None, "Required property 'consumer_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tracker_name(self) -> builtins.str:
        '''``AWS::Location::TrackerConsumer.TrackerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-trackername
        '''
        result = self._values.get("tracker_name")
        assert result is not None, "Required property 'tracker_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrackerConsumerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-location.CfnTrackerProps",
    jsii_struct_bases=[],
    name_mapping={
        "pricing_plan": "pricingPlan",
        "tracker_name": "trackerName",
        "description": "description",
        "kms_key_id": "kmsKeyId",
        "pricing_plan_data_source": "pricingPlanDataSource",
    },
)
class CfnTrackerProps:
    def __init__(
        self,
        *,
        pricing_plan: builtins.str,
        tracker_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        pricing_plan_data_source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Location::Tracker``.

        :param pricing_plan: ``AWS::Location::Tracker.PricingPlan``.
        :param tracker_name: ``AWS::Location::Tracker.TrackerName``.
        :param description: ``AWS::Location::Tracker.Description``.
        :param kms_key_id: ``AWS::Location::Tracker.KmsKeyId``.
        :param pricing_plan_data_source: ``AWS::Location::Tracker.PricingPlanDataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "pricing_plan": pricing_plan,
            "tracker_name": tracker_name,
        }
        if description is not None:
            self._values["description"] = description
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if pricing_plan_data_source is not None:
            self._values["pricing_plan_data_source"] = pricing_plan_data_source

    @builtins.property
    def pricing_plan(self) -> builtins.str:
        '''``AWS::Location::Tracker.PricingPlan``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplan
        '''
        result = self._values.get("pricing_plan")
        assert result is not None, "Required property 'pricing_plan' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tracker_name(self) -> builtins.str:
        '''``AWS::Location::Tracker.TrackerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-trackername
        '''
        result = self._values.get("tracker_name")
        assert result is not None, "Required property 'tracker_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::Tracker.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::Tracker.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan_data_source(self) -> typing.Optional[builtins.str]:
        '''``AWS::Location::Tracker.PricingPlanDataSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplandatasource
        '''
        result = self._values.get("pricing_plan_data_source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrackerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGeofenceCollection",
    "CfnGeofenceCollectionProps",
    "CfnMap",
    "CfnMapProps",
    "CfnPlaceIndex",
    "CfnPlaceIndexProps",
    "CfnRouteCalculator",
    "CfnRouteCalculatorProps",
    "CfnTracker",
    "CfnTrackerConsumer",
    "CfnTrackerConsumerProps",
    "CfnTrackerProps",
]

publication.publish()
