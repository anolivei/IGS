from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from igs.employee import views

router = routers.DefaultRouter()
router.register('employee', views.AllViewSet, basename='employee')

urlpatterns = [
    path('pikachu/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', include(router.urls)),
    path('alphabetic/', views.Employees.as_view()),
    path('alphabetic/search/<str:pk>/', views.EmployeesSearch.as_view()),
]
