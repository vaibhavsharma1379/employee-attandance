from django.db import models

# Create your models here.
from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    location=models.CharField(max_length=200)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Departments"
        ordering = ['name']


class Employee(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('QA', 'QA'),
        ('HR', 'HR'),
    ]
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    department=models.ForeignKey(Department, on_delete=models.CASCADE,related_name='employee')
    role=models.CharField(max_length=10,choices=ROLE_CHOICES, default='QA')
    manager=models.ForeignKey("self" , on_delete=models.SET_NULL,related_name='subordinates',null=True,blank=True)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.full_name} ({self.employee_id})"

    class Meta:
        ordering = ('employee_id',)
        indexes=[
            models.Index(fields=['email'])
        ]

    def attandance_percentage(self, month=None, year=None):
        qs=self.attandance_records.all()
        if month and year:
            qs=qs.filter(date__month=month, date__year=year)
        total=qs.count()
        if total==0:
            return 0
        present=qs.filter(status='Present').count()
        return (present/total)*100

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
        ('Remote', 'Remote'),
        ('Work From Home', 'Work From Home')
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)


    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.full_name} - {self.date} - {self.status}"


class LeaveRequest(models.Model):
    LEAVE_CHOICES = [
        ('Sick Leave', 'Sick Leave'),
        ('Casual Leave', 'Casual Leave'),
        ('Maternity Leave', 'Maternity Leave'),
        ('Paternity Leave', 'Paternity Leave'),
        ('Unpaid Leave', 'Unpaid Leave')
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_request')
    leave_type = models.CharField(max_length=20, choices=LEAVE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    approved_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leaves')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.full_name} - {self.leave_type} ({self.start_date} to {self.end_date}) - {self.status}"

    @property
    def duration(self):
        return (self.end_date - self.start_date).days + 1