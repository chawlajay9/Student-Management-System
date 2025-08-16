from rest_framework import serializers
from .models import Exam, Mark
from classrooms.serializers import ClassRoomSerializer
from subjects.serializers import SubjectListSerializer
from students.serializers import StudentListSerializer


class ExamSerializer(serializers.ModelSerializer):
    """Serializer for Exam model"""
    class_room_name = serializers.CharField(source='class_room.__str__', read_only=True)
    display_name = serializers.CharField(source='__str__', read_only=True)
    
    class Meta:
        model = Exam
        fields = ['id', 'name', 'class_room', 'class_room_name', 'date', 'display_name']
        read_only_fields = ['id']


class ExamDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Exam model with nested data"""
    class_room = ClassRoomSerializer(read_only=True)
    marks_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Exam
        fields = ['id', 'name', 'class_room', 'date', 'marks_count']
        read_only_fields = ['id']
    
    def get_marks_count(self, obj):
        return obj.mark_set.count() if hasattr(obj, 'mark_set') else 0


class ExamCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating exams"""
    
    class Meta:
        model = Exam
        fields = ['name', 'class_room', 'date']
    
    def validate(self, attrs):
        name = attrs.get('name')
        class_room = attrs.get('class_room')
        date = attrs.get('date')
        
        # Check if exam already exists for this classroom on this date
        if Exam.objects.filter(name=name, class_room=class_room, date=date).exists():
            raise serializers.ValidationError("Exam with this name already exists for this classroom on this date")
        
        return attrs


class MarkSerializer(serializers.ModelSerializer):
    """Serializer for Mark model"""
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    student_id = serializers.CharField(source='student.student_id', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    exam_name = serializers.CharField(source='exam.name', read_only=True)
    
    class Meta:
        model = Mark
        fields = ['id', 'student', 'student_name', 'student_id', 'subject', 'subject_name', 
                 'exam', 'exam_name', 'score']
        read_only_fields = ['id']
    
    def validate(self, attrs):
        student = attrs.get('student')
        subject = attrs.get('subject')
        exam = attrs.get('exam')
        score = attrs.get('score')
        
        # Validate score range
        if score < 0 or score > 100:
            raise serializers.ValidationError("Score must be between 0 and 100")
        
        # Check for duplicate mark record
        if self.instance is None:  # Creating new instance
            if Mark.objects.filter(student=student, subject=subject, exam=exam).exists():
                raise serializers.ValidationError("Mark already exists for this student, subject, and exam")
        else:  # Updating existing instance
            if Mark.objects.filter(student=student, subject=subject, exam=exam).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Mark already exists for this student, subject, and exam")
        
        # Validate that student belongs to the same class as exam
        if student.class_assigned != exam.class_room:
            raise serializers.ValidationError("Student must belong to the same class as the exam")
        
        # Validate that subject belongs to the same class as exam
        if subject.class_room != exam.class_room:
            raise serializers.ValidationError("Subject must belong to the same class as the exam")
        
        return attrs


class MarkDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Mark model with nested data"""
    student = StudentListSerializer(read_only=True)
    subject = SubjectListSerializer(read_only=True)
    exam = ExamSerializer(read_only=True)
    
    class Meta:
        model = Mark
        fields = ['id', 'student', 'subject', 'exam', 'score']
        read_only_fields = ['id']


class MarkCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating marks"""
    
    class Meta:
        model = Mark
        fields = ['student', 'subject', 'exam', 'score']


class MarkBulkCreateSerializer(serializers.Serializer):
    """Serializer for bulk creating marks"""
    exam = serializers.IntegerField()
    subject = serializers.IntegerField()
    marks = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )
    
    def validate_marks(self, value):
        for mark in value:
            if 'student_id' not in mark or 'score' not in mark:
                raise serializers.ValidationError("Each mark must have student_id and score")
            try:
                score = float(mark['score'])
                if score < 0 or score > 100:
                    raise serializers.ValidationError("Score must be between 0 and 100")
            except ValueError:
                raise serializers.ValidationError("Score must be a valid number")
        return value


class StudentMarkReportSerializer(serializers.ModelSerializer):
    """Serializer for student mark reports"""
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    exam_name = serializers.CharField(source='exam.name', read_only=True)
    exam_date = serializers.DateField(source='exam.date', read_only=True)
    
    class Meta:
        model = Mark
        fields = ['subject_name', 'exam_name', 'exam_date', 'score']
