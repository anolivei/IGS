from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from igs.employee.views import EmployeeViewSet, Employee

router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('igs/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', include(router.urls)),
    path('employee-alphabetic/', Employee.as_view()),
]
