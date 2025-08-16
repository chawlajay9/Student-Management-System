from rest_framework import serializers

# Placeholder serializers for notifications app
# Add your Notification model serializers here when models are created

class NotificationSerializer(serializers.Serializer):
    """Placeholder serializer for Notification model"""
    pass

# Example structure for when Notification model is created:
# 
# from .models import Notification
# from users.serializers import UserSerializer
# 
# class NotificationSerializer(serializers.ModelSerializer):
#     recipient = UserSerializer(read_only=True)
#     
#     class Meta:
#         model = Notification
#         fields = '__all__'
