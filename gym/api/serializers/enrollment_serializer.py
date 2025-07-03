"""
    Serializer and model imports for enrollment

    Django REST Framework imports:
    - serializers: Base module for creating API serializers

    Local application imports:
    - Enrollment: Model containing enrollment data (from gym app)
"""

from rest_framework import serializers

from gym.models import Enrollment

class EnrollmentReadSerializer(serializers.ModelSerializer):
    """ Read Serializer for Enrollment Model """
    student = serializers.StringRelatedField()
    plan = serializers.StringRelatedField()

    class Meta:
        """ Class that defines the serializer metadata """
        model = Enrollment
        fields = ['id', 'student', 'plan', 'start_date', 'end_date', 'status', 'active']
        read_only_fields = ['id', 'student', 'plan', 'start_date', 'end_date', 'status', 'active']

class EnrollmentReadDetailSerializer(serializers.ModelSerializer):
    """ Detailed reading serializer for Enrollment model """
    student = serializers.StringRelatedField()
    plan = serializers.StringRelatedField()
    assigned_by = serializers.StringRelatedField()

    class Meta:
        """ Class that defines the serializer metadata """
        model = Enrollment
        fields = [
            'id', 'student', 'plan', 
            'start_date', 'end_date', 
            'status', 'active', 
            'notes', 
            'assigned_by', 
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'student', 'plan', 
            'start_date', 'end_date', 
            'status', 'active', 
            'notes', 
            'assigned_by', 
            'created_at', 'updated_at'
        ]

class EnrollmentWriteSerializer(serializers.ModelSerializer):
    """ Writing serializer for Enrollment model """
    class Meta:
        """ Class that defines the serializer metadata """
        model = Enrollment
        exclude = ['active', 'created_by', 'end_date']

    def validate(self, attrs):
        student = attrs.get('student')
        plan = attrs.get('plan')

        if Enrollment.objects.filter(student=student, plan=plan, active=True).exists():  # pylint: disable=no-member
            raise serializers.ValidationError(
                "Este aluno já possui uma matrícula ativa neste plano."
            )

        return attrs

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        enrollment = Enrollment(**validated_data)
        enrollment.full_clean()
        enrollment.save()

        return enrollment

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

    def delete(self):
        """ Method that performs the soft-delete of the object """
        self.instance.active = False
        self.instance.save()
