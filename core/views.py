from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'delete']


class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        employee_id = self.request.query_params.get('employee_id')
        qs = Attendance.objects.all()
        if employee_id:
            qs = qs.filter(employee__employee_id=employee_id)
        return qs

class DashboardStats(APIView):
    def get(self, request):
        today = now().date()
        total_employees = Employee.objects.count()
        present = Attendance.objects.filter(date=today, status="Present").count()
        absent = Attendance.objects.filter(date=today, status="Absent").count()

        return Response({
            "total_employees": total_employees,
            "present_today": present,
            "absent_today": absent,
        })
def health_check(request):
    return JsonResponse({"status": "ok"})