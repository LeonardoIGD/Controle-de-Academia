from rest_framework import serializers

from gym.models import Plan


class PlanReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'duration_months', 'price', 'modality', 'instructor', 'active']
        read_only_fields = ['id', 'name', 'duration_months', 'price', 'modality', 'instructor', 'active']

class PlanReadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
        read_only_fields = [f.name for f in Plan._meta.fields]

class PlanWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        exclude = ['active', 'created_by']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def delete(self):
        self.instance.active = False
        self.instance.save()
