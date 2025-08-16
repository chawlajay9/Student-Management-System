from rest_framework import serializers

# Placeholder serializers for reports app
# Add your Report model serializers here when models are created

class ReportSerializer(serializers.Serializer):
    """Placeholder serializer for Report model"""
    pass

# Example structure for when Report model is created:
# 
# from .models import Report
# from students.serializers import StudentListSerializer
# from teachers.serializers import TeacherListSerializer
# 
# class ReportSerializer(serializers.ModelSerializer):
#     generated_by = TeacherListSerializer(read_only=True)
#     
#     class Meta:
#         model = Report
#         fields = '__all__'
