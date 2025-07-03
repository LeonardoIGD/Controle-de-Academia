"""
    Serializer and model imports for plan

    Django REST Framework imports:
    - serializers: Base module for creating API serializers

    Local application imports:
    - Plan: Model containing plan data (from gym app)
"""

from rest_framework import serializers

from gym.models import Plan


class PlanReadSerializer(serializers.ModelSerializer):
    """ Read Serializer for Plan Model """
    class Meta:
        """ Class that defines the serializer metadata """
        model = Plan
        fields = ['id', 'name', 'duration_months', 'price', 'modality', 'instructor', 'active']
        read_only_fields = [
            'id', 
            'name', 
            'duration_months', 'price', 
            'modality', 'instructor', 
            'active'
        ]

class PlanReadDetailSerializer(serializers.ModelSerializer):
    """ Detailed reading serializer for Plan model """
    class Meta:
        """ Class that defines the serializer metadata """
        model = Plan
        fields = [
            'id', 
            'name', 'description', 
            'duration_months', 'price', 
            'modality', 'max_students', 
            'instructor', 
            'active', 
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 
            'name', 'description', 
            'duration_months', 'price', 
            'modality', 'max_students', 
            'instructor', 
            'active', 
            'created_at', 'updated_at'
        ]

class PlanWriteSerializer(serializers.ModelSerializer):
    """ Writing serializer for Plan model """
    class Meta:
        """ Class that defines the serializer metadata """
        model = Plan
        exclude = ['active', 'created_by']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

    def delete(self):
        """ Method that performs the soft-delete of the object """
        self.instance.active = False
        self.instance.save()
