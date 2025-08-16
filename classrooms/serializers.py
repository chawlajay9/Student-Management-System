from rest_framework import serializers
from .models import ClassRoom


class ClassRoomSerializer(serializers.ModelSerializer):
    """Serializer for ClassRoom model"""
    display_name = serializers.CharField(source='__str__', read_only=True)
    
    class Meta:
        model = ClassRoom
        fields = ['id', 'name', 'section', 'display_name']
        read_only_fields = ['id']
    
    def validate(self, attrs):
        name = attrs.get('name')
        section = attrs.get('section')
        
        # Check for unique combination during creation
        if self.instance is None:  # Creating new instance
            if ClassRoom.objects.filter(name=name, section=section).exists():
                raise serializers.ValidationError("Classroom with this name and section already exists")
        else:  # Updating existing instance
            if ClassRoom.objects.filter(name=name, section=section).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Classroom with this name and section already exists")
        
        return attrs


class ClassRoomListSerializer(serializers.ModelSerializer):
    """Simplified serializer for classroom lists"""
    display_name = serializers.CharField(source='__str__', read_only=True)
    student_count = serializers.SerializerMethodField()
    
    class Meta:
        model = ClassRoom
        fields = ['id', 'name', 'section', 'display_name', 'student_count']
    
    def get_student_count(self, obj):
        return obj.student_set.count() if hasattr(obj, 'student_set') else 0
