from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from django.db.models.functions import Lower

from igs.employee.models import Employee
from igs.employee.serializers import EmployeeSerializer

class AllViewSet(viewsets.ModelViewSet):
    """Lists all employees order by id"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Employees(generics.ListAPIView):
    """Lists all employees order by name"""
    queryset = Employee.objects.all().order_by(Lower("name"))
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EmployeesSearch(generics.ListAPIView):
    """Returns the employee data according his/her name or part of the name"""
    def get_queryset(self):
        search = self.kwargs['pk']
        queryset = Employee.objects.filter(nome__contains=search)
        return queryset
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
