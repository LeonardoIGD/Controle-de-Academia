"""
    Serializer and model imports for student profiles.

    Django REST Framework imports:
    - serializers: Base module for creating API serializers

    Local application imports:
    - StudentProfile: Model containing student profile data (from users app)
"""

from rest_framework import serializers

from users.models import StudentProfile

class StudentProfileReadSerializer(serializers.ModelSerializer): # pylint: disable=too-few-public-methods
    """ Read Serializer for StudentProfile Model """

    bmi = serializers.FloatField(read_only=True)

    class Meta:
        """ Class that defines the serializer metadata """
        model = StudentProfile
        fields = ['id', 'user', 'birth_date', 'bmi']
        read_only_fields = ['id', 'user', 'birth_date', 'bmi']

class StudentProfileReadDetailSerializer(serializers.ModelSerializer): # pylint: disable=too-few-public-methods
    """ Detailed reading serializer for StudentProfile model """
    bmi = serializers.FloatField(read_only=True)

    class Meta:
        """ Class that defines the serializer metadata """
        model = StudentProfile
        fields = [
            'id', 'user',
            'height', 'weight',
            'birth_date',
            'health_restrictions', 'fitness_goals',
            'bmi', 'active',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'user',
            'height', 'weight',
            'birth_date',
            'health_restrictions', 'fitness_goals',
            'bmi', 'active',
            'created_at', 'updated_at'
        ]

class StudentProfileWriteSerializer(serializers.ModelSerializer): # pylint: disable=too-few-public-methods
    """ Writing serializer for StudentProfile model """
    class Meta:
        """ Class that defines the serializer metadata """
        model = StudentProfile
        exclude = ['active', 'created_by']

    def validate(self, attrs):
        user = attrs.get('user')
        if not user.is_student:
            raise serializers.ValidationError("O usuário informado não está marcado como aluno.")

        if StudentProfile.objects.filter(user=user, active=True).exists(): # pylint: disable=no-member
            raise serializers.ValidationError("Este usuário já possui um perfil de aluno ativo.")

        return attrs

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if not instance.user.is_student:
            raise serializers.ValidationError("O usuário não está marcado como aluno.")

        return super().update(instance, validated_data)

    def delete(self):
        """ Method that performs the soft-delete of the object """
        self.instance.active = False
        self.instance.save()
