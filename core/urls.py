from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendanceViewSet, DashboardStats,health_check

router = DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('attendance', AttendanceViewSet,basename='attendance')

urlpatterns = [
    path('api/', include(router.urls)),
]
urlpatterns += [
    path("health/", health_check),
    path("api/dashboard/", DashboardStats.as_view()),
]