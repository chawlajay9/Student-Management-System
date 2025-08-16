from rest_framework import serializers

# Placeholder serializers for courses app
# Add your Course model serializers here when models are created

class CourseSerializer(serializers.Serializer):
    """Placeholder serializer for Course model"""
    pass

# Example structure for when Course model is created:
# 
# from .models import Course
# 
# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'
