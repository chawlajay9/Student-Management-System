from rest_framework import serializers

# Placeholder serializers for fees app
# Add your Fee model serializers here when models are created

class FeeSerializer(serializers.Serializer):
    """Placeholder serializer for Fee model"""
    pass

# Example structure for when Fee model is created:
# 
# from .models import Fee
# from students.serializers import StudentListSerializer
# 
# class FeeSerializer(serializers.ModelSerializer):
#     student = StudentListSerializer(read_only=True)
#     
#     class Meta:
#         model = Fee
#         fields = '__all__'
