from rest_framework import serializers
from .models import Subject
from classrooms.serializers import ClassRoomSerializer
from teachers.serializers import TeacherListSerializer


class SubjectSerializer(serializers.ModelSerializer):
    """Serializer for Subject model"""
    class_room_name = serializers.CharField(source='class_room.__str__', read_only=True)
    teacher_name = serializers.CharField(source='teacher.user.get_full_name', read_only=True)
    display_name = serializers.CharField(source='__str__', read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'name', 'class_room', 'class_room_name', 'teacher', 'teacher_name', 'display_name']
        read_only_fields = ['id']


class SubjectDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Subject model with nested data"""
    class_room = ClassRoomSerializer(read_only=True)
    teacher = TeacherListSerializer(read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'name', 'class_room', 'teacher']
        read_only_fields = ['id']


class SubjectCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating subjects"""
    
    class Meta:
        model = Subject
        fields = ['name', 'class_room', 'teacher']
    
    def validate(self, attrs):
        name = attrs.get('name')
        class_room = attrs.get('class_room')
        
        # Check if subject already exists for this classroom
        if Subject.objects.filter(name=name, class_room=class_room).exists():
            raise serializers.ValidationError("Subject already exists for this classroom")
        
        return attrs


class SubjectListSerializer(serializers.ModelSerializer):
    """Simplified serializer for subject lists"""
    class_room_name = serializers.CharField(source='class_room.__str__', read_only=True)
    teacher_name = serializers.CharField(source='teacher.user.get_full_name', read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'name', 'class_room_name', 'teacher_name']
