from rest_framework import serializers
from .models import Attendance
from students.serializers import StudentListSerializer


class AttendanceSerializer(serializers.ModelSerializer):
    """Serializer for Attendance model"""
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    student_id = serializers.CharField(source='student.student_id', read_only=True)
    class_name = serializers.CharField(source='student.class_assigned.__str__', read_only=True)
    
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'student_name', 'student_id', 'class_name', 'date', 'status']
        read_only_fields = ['id']
    
    def validate(self, attrs):
        student = attrs.get('student')
        date = attrs.get('date')
        
        # Check for duplicate attendance record
        if self.instance is None:  # Creating new instance
            if Attendance.objects.filter(student=student, date=date).exists():
                raise serializers.ValidationError("Attendance record already exists for this student on this date")
        else:  # Updating existing instance
            if Attendance.objects.filter(student=student, date=date).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Attendance record already exists for this student on this date")
        
        return attrs


class AttendanceDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Attendance model with nested student data"""
    student = StudentListSerializer(read_only=True)
    
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'date', 'status']
        read_only_fields = ['id']


class AttendanceCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating attendance records"""
    
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']


class AttendanceBulkCreateSerializer(serializers.Serializer):
    """Serializer for bulk creating attendance records"""
    date = serializers.DateField()
    attendance_records = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )
    
    def validate_attendance_records(self, value):
        for record in value:
            if 'student_id' not in record or 'status' not in record:
                raise serializers.ValidationError("Each record must have student_id and status")
            if record['status'] not in ['present', 'absent']:
                raise serializers.ValidationError("Status must be either 'present' or 'absent'")
        return value


class AttendanceReportSerializer(serializers.ModelSerializer):
    """Serializer for attendance reports"""
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    student_id = serializers.CharField(source='student.student_id', read_only=True)
    class_name = serializers.CharField(source='student.class_assigned.__str__', read_only=True)
    
    class Meta:
        model = Attendance
        fields = ['student_name', 'student_id', 'class_name', 'date', 'status']
