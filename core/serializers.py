from rest_framework import serializers
from .models import Employee, Attendance
from rest_framework.validators import UniqueTogetherValidator


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Attendance.objects.all(),
                fields=['employee', 'date'],
                message="This employee already has attendance marked for this date."
            )
        ]