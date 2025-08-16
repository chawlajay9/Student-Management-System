from rest_framework import serializers
from .models import Teacher
from users.serializers import UserSerializer

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'employee_id', 'hire_date']

class TeacherCreateSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'employee_id', 'hire_date']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Teacher.objects.create(user=user, **validated_data)
