from django.core.management.base import BaseCommand
from core.models import Employee, Attendance
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = "Seed dummy employees and attendance data"

    def handle(self, *args, **kwargs):
        employees_data = [
            ("EMP001", "Amit Sharma", "amit.sharma@company.com", "Engineering"),
            ("EMP002", "Priya Verma", "priya.verma@company.com", "HR"),
            ("EMP003", "Rahul Mehta", "rahul.mehta@company.com", "Sales"),
            ("EMP004", "Sneha Iyer", "sneha.iyer@company.com", "Marketing"),
            ("EMP005", "Vikram Singh", "vikram.singh@company.com", "Finance"),
        ]

        employees = []
        for emp_id, name, email, dept in employees_data:
            emp, created = Employee.objects.get_or_create(
                employee_id=emp_id,
                defaults={
                    "full_name": name,
                    "email": email,
                    "department": dept,
                }
            )
            employees.append(emp)

        statuses = ["Present", "Absent"]
        today = date.today()

        for emp in employees:
            for i in range(10):  # last 10 days
                att_date = today - timedelta(days=i)
                Attendance.objects.get_or_create(
                    employee=emp,
                    date=att_date,
                    defaults={
                        "status": random.choice(statuses)
                    }
                )

        self.stdout.write(self.style.SUCCESS("Dummy data seeded successfully"))