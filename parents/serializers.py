from rest_framework import serializers

# Placeholder serializers for parents app
# Add your Parent model serializers here when models are created

class ParentSerializer(serializers.Serializer):
    """Placeholder serializer for Parent model"""
    pass

# Example structure for when Parent model is created:
# 
# from .models import Parent
# from users.serializers import UserSerializer
# from students.serializers import StudentListSerializer
# 
# class ParentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     children = StudentListSerializer(many=True, read_only=True)
#     
#     class Meta:
#         model = Parent
#         fields = '__all__'
