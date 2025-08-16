from rest_framework import serializers
from .models import Student
from users.serializers import UserSerializer
from classrooms.models import ClassRoom


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model"""
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class_assigned_name = serializers.CharField(source='class_assigned.name', read_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'user', 'user_id', 'student_id', 'admission_date', 
                 'class_assigned', 'class_assigned_name', 'section']
        read_only_fields = ['id']
    
    def validate_user_id(self, value):
        from users.models import User
        try:
            user = User.objects.get(id=value, role='student')
        except User.DoesNotExist:
            raise serializers.ValidationError("User with student role not found")
        return value


class StudentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new students"""
    
    class Meta:
        model = Student
        fields = ['user', 'student_id', 'admission_date', 'class_assigned', 'section']
    
    def validate_student_id(self, value):
        if Student.objects.filter(student_id=value).exists():
            raise serializers.ValidationError("Student ID already exists")
        return value


class StudentListSerializer(serializers.ModelSerializer):
    """Simplified serializer for student lists"""
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class_name = serializers.CharField(source='class_assigned.name', read_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'student_id', 'full_name', 'email', 'class_name', 'section', 'admission_date']
