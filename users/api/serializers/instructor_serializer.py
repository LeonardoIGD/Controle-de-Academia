from rest_framework import serializers

from users.models import InstructorProfile


class InstructorProfileReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorProfile
        fields = [
            'id', 'user', 'specialization', 'experience_years', 'is_available'
        ]
        read_only_fields = ['id', 'user', 'specialization', 'experience_years', 'is_available']

class InstructorProfileReadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorProfile
        fields = '__all__'
        read_only_fields = [f.name for f in InstructorProfile._meta.fields]

class InstructorProfileWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorProfile
        exclude = ['active', 'created_by']

    def validate(self, data):
        user = data.get('user')
        if not user.is_instructor:
            raise serializers.ValidationError("O usuário informado não está marcado como instrutor.")

        if InstructorProfile.objects.filter(user=user, active=True).exists():
            raise serializers.ValidationError("Este usuário já possui um perfil de instrutor ativo.")
        
        return data

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if not instance.user.is_instructor:
            raise serializers.ValidationError("O usuário não está marcado como instrutor.")
        
        return super().update(instance, validated_data)

    def delete(self):
        self.instance.active = False
        self.instance.save()

