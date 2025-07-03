"""
    Serializer and model imports for instructor profiles.

    Django REST Framework imports:
    - serializers: Base module for creating API serializers

    Local application imports:
    - InstructorProfile: Model containing instructor profile data (from users app)
"""

from rest_framework import serializers

from users.models import InstructorProfile


class InstructorProfileReadSerializer(serializers.ModelSerializer):
    """ Read Serializer for InstructorProfile Model """
    class Meta:
        """ Class that defines the serializer metadata """
        model = InstructorProfile
        fields = [
            'id', 'user', 'specialization', 'experience_years', 'is_available'
        ]
        read_only_fields = ['id', 'user', 'specialization', 'experience_years', 'is_available']

class InstructorProfileReadDetailSerializer(serializers.ModelSerializer):
    """ Detailed reading serializer for InstructorProfile model """
    class Meta:
        """ Class that defines the serializer metadata """
        model = InstructorProfile
        fields = [
            'id', 'user', 
            'specialization', 'experience_years', 'certifications',
            'biography', 
            'active', 'is_available',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'user', 
            'specialization', 'experience_years', 'certifications',
            'biography', 
            'active', 'is_available',
            'created_at', 'updated_at'
        ]

class InstructorProfileWriteSerializer(serializers.ModelSerializer):
    """ Writing serializer for InstructorProfile model """
    class Meta:
        """ Class that defines the serializer metadata """
        model = InstructorProfile
        exclude = ['active', 'created_by']

    def validate(self, attrs):
        user = attrs.get('user')
        if not user.is_instructor:
            raise serializers.ValidationError(
                "O usuário informado não está marcado como instrutor."
            )

        if InstructorProfile.objects.filter(user=user, active=True).exists(): # pylint: disable=no-member
            raise serializers.ValidationError(
                "Este usuário já possui um perfil de instrutor ativo."
            )

        return attrs

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if not instance.user.is_instructor:
            raise serializers.ValidationError("O usuário não está marcado como instrutor.")

        return super().update(instance, validated_data)

    def delete(self):
        """ Method that performs the soft-delete of the object """
        self.instance.active = False
        self.instance.save()
