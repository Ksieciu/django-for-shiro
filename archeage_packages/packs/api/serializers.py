from rest_framework import serializers
from ..models import Component, Pack, PackComponent


class ComponentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source='component_name', 
        required=True
    )
    class Meta:
        model = Component
        fields = ['name']


class PackComponentsSerializer(serializers.ModelSerializer):
    component = serializers.SlugRelatedField(
        slug_field='component_name',
        queryset=Component.objects.all(),
    )

    class Meta:
        model = PackComponent
        fields = ['component', 'amount']


class PackSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source='pack_name', 
        required=True
    )
    components = PackComponentsSerializer(
        source='components_for_pack', 
        many=True
    )

    class Meta:
        model = Pack
        fields = ['name', 'components']
