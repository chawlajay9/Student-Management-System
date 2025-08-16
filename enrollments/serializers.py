from rest_framework import serializers

# Placeholder serializers for enrollments app
# Add your Enrollment model serializers here when models are created

class EnrollmentSerializer(serializers.Serializer):
    """Placeholder serializer for Enrollment model"""
    pass

# Example structure for when Enrollment model is created:
# 
# from .models import Enrollment
# from students.serializers import StudentListSerializer
# from subjects.serializers import SubjectListSerializer
# 
# class EnrollmentSerializer(serializers.ModelSerializer):
#     student = StudentListSerializer(read_only=True)
#     subject = SubjectListSerializer(read_only=True)
#     
#     class Meta:
#         model = Enrollment
#         fields = '__all__'
