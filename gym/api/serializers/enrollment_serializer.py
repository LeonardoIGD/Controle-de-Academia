from rest_framework import serializers

from gym.models import Enrollment

class EnrollmentReadSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    plan = serializers.StringRelatedField()

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'plan', 'start_date', 'end_date', 'status', 'active']
        read_only_fields = ['id', 'student', 'plan', 'start_date', 'end_date', 'status', 'active']

class EnrollmentReadDetailSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    plan = serializers.StringRelatedField()
    assigned_by = serializers.StringRelatedField()

    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = [f.name for f in Enrollment._meta.fields]

class EnrollmentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = ['active', 'created_by', 'end_date']

    def validate(self, data):
        student = data.get('student')
        plan = data.get('plan')

        if Enrollment.objects.filter(student=student, plan=plan, active=True).exists():
            raise serializers.ValidationError("Este aluno já possui uma matrícula ativa neste plano.")

        return data

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        enrollment = Enrollment(**validated_data)
        enrollment.full_clean()
        enrollment.save()
        
        return enrollment

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def delete(self):
        self.instance.active = False
        self.instance.save()
