from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from page.models import (
    Specializations,
    Doctors, 
    ServicesCategories,
    Services, 
    Patients,
    StaffsRoles,
    Staffs,
    Visits
)
from .serializers import (
    SpecializationsSerializer,
    DoctorsSerializer,
    ServicesCategoriesSerializer,
    ServicesSerializer,
    PatientsSerializer,
    UserSerializer,
    StaffsRolesSerializer,
    StaffsSerializer,
    VisitsSerializer
)

class SpecializationsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Specializations.objects.all()
    serializer_class = SpecializationsSerializer

class DoctorsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer

class ServicesCategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = ServicesCategories.objects.all()
    serializer_class = ServicesCategoriesSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class PatientsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class StaffsRolesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = StaffsRoles.objects.all()
    serializer_class = StaffsRolesSerializer

class StaffsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Staffs.objects.all()
    serializer_class = StaffsSerializer

class VisitsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer