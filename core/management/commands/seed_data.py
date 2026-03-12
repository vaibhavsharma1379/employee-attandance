from django.core.management.base import BaseCommand
from core.models import Employee, Attendance,LeaveRequest,Department
from datetime import date, timedelta
import random
class Command(BaseCommand):
    help = "Seed database with dummy data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        LeaveRequest.objects.all().delete()
        Attendance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

        self.stdout.write("Creating departments...")
        departments = []
        dept_data = [
            ("Engineering", "Building A, Floor 3"),
            ("HR", "Building A, Floor 1"),
            ("Design", "Building B, Floor 2"),
            ("QA", "Building A, Floor 2"),
            ("Marketing", "Building C, Floor 1"),
        ]
        for name, location in dept_data:
            dept = Department.objects.create(name=name, location=location)
            departments.append(dept)

        self.stdout.write("Creating employees...")
        employees_data = [
            # (employee_id, full_name, dept_index, role, email, salary, manager_id_ref)
            ("EMP001", "Rahul Sharma",    0, "Manager",   "rahul@company.com",    120000, None),
            ("EMP002", "Priya Patel",     0, "Developer", "priya@company.com",     85000, "EMP001"),
            ("EMP003", "Amit Kumar",      0, "Developer", "amit@company.com",      78000, "EMP001"),
            ("EMP004", "Sneha Reddy",     0, "QA",        "sneha@company.com",     65000, "EMP001"),
            ("EMP005", "Vikram Singh",    1, "Manager",   "vikram@company.com",   110000, None),
            ("EMP006", "Neha Gupta",      1, "HR",        "neha@company.com",      70000, "EMP005"),
            ("EMP007", "Arjun Nair",      2, "Manager",   "arjun@company.com",    105000, None),
            ("EMP008", "Kavita Joshi",    2, "Designer",  "kavita@company.com",    80000, "EMP007"),
            ("EMP009", "Rohan Mehta",     2, "Designer",  "rohan@company.com",     75000, "EMP007"),
            ("EMP010", "Anjali Verma",    3, "Manager",   "anjali@company.com",   100000, None),
            ("EMP011", "Deepak Yadav",    3, "QA",        "deepak@company.com",    60000, "EMP010"),
            ("EMP012", "Pooja Mishra",    3, "QA",        "pooja@company.com",     58000, "EMP010"),
            ("EMP013", "Suresh Iyer",     0, "Developer", "suresh@company.com",    90000, "EMP001"),
            ("EMP014", "Meera Chopra",    4, "Manager",   "meera@company.com",    115000, None),
            ("EMP015", "Karan Malhotra",  4, "Designer",  "karan@company.com",     72000, "EMP014"),
            ("EMP016", "Divya Saxena",    0, "Developer", "divya@company.com",     82000, "EMP001"),
            ("EMP017", "Ravi Tiwari",     1, "HR",        "ravi@company.com",      68000, "EMP005"),
            ("EMP018", "Nisha Agarwal",   0, "QA",        "nisha@company.com",     62000, "EMP001"),
            ("EMP019", "Manish Pandey",   3, "QA",        "manish@company.com",    55000, "EMP010"),
            ("EMP020", "Swati Kulkarni",  2, "Designer",  "swati@company.com",     77000, "EMP007"),
        ]

        # First pass: create all employees without managers
        emp_objects = {}
        for eid, name, dept_idx, role, email, salary, _ in employees_data:
            emp = Employee.objects.create(
                employee_id=eid,
                full_name=name,
                department=departments[dept_idx],
                role=role,
                email=email,
                salary=salary,
            )
            emp_objects[eid] = emp

        # Second pass: assign managers
        for eid, _, _, _, _, _, mgr_id in employees_data:
            if mgr_id:
                emp = emp_objects[eid]
                emp.manager = emp_objects[mgr_id]
                emp.save(update_fields=['manager'])

        self.stdout.write("Creating attendance records (last 60 days)...")
        statuses = ['Present', 'Present', 'Present', 'Present', 'Absent', 'Leave', 'Remote']
        # weighted toward Present

        today = date.today()
        for emp in Employee.objects.all():
            for i in range(60):
                day = today - timedelta(days=i)
                # Skip weekends
                if day.weekday() >= 5:
                    continue
                Attendance.objects.create(
                    employee=emp,
                    date=day,
                    status=random.choice(statuses),
                )

        self.stdout.write("Creating leave requests...")
        leave_types = ['Sick Leave', 'Casual Leave', 'Maternity Leave', 'Paternity Leave', 'Unpaid Leave']
        leave_statuses = ['Pending', 'Approved', 'Approved', 'Rejected']

        managers = Employee.objects.filter(role='Manager')
        non_managers = Employee.objects.exclude(role='Manager')

        for emp in non_managers:
            for _ in range(random.randint(1, 3)):
                start = today - timedelta(days=random.randint(1, 90))
                end = start + timedelta(days=random.randint(1, 5))
                status = random.choice(leave_statuses)
                LeaveRequest.objects.create(
                    employee=emp,
                    leave_type=random.choice(leave_types),
                    start_date=start,
                    end_date=end,
                    reason=f"Leave request by {emp.full_name}",
                    status=status,
                    approved_by=random.choice(managers) if status != 'Pending' else None,
                )

        total_emp = Employee.objects.count()
        total_att = Attendance.objects.count()
        total_leave = LeaveRequest.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f"Done! Created {total_emp} employees, {total_att} attendance records, {total_leave} leave requests"
        ))



