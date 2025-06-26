from rest_framework import serializers

from users.models import StudentProfile

class StudentProfileReadSerializer(serializers.ModelSerializer):
    bmi = serializers.FloatField(read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'birth_date', 'bmi']
        read_only_fields = ['id', 'user', 'birth_date', 'bmi']

class StudentProfileReadDetailSerializer(serializers.ModelSerializer):
    bmi = serializers.FloatField(read_only=True)

    class Meta:
        model = StudentProfile
        fields = '__all__'
        read_only_fields = [f.name for f in StudentProfile._meta.fields]

class StudentProfileWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        exclude = ['active', 'created_by']

    def validate(self, data):
        user = data.get('user')
        if not user.is_student:
            raise serializers.ValidationError("O usuário informado não está marcado como aluno.")

        if StudentProfile.objects.filter(user=user, active=True).exists():
            raise serializers.ValidationError("Este usuário já possui um perfil de aluno ativo.")
        
        return data

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if not instance.user.is_student:
            raise serializers.ValidationError("O usuário não está marcado como aluno.")
        
        return super().update(instance, validated_data)

    def delete(self):
        self.instance.active = False
        self.instance.save()
