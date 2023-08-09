from django.contrib.auth import get_user_model
from rest_framework import serializers
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

class SpecializationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specializations
        fields = '__all__'

class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctors
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['specialization'] = instance.specialization.name

    #     return response

class ServicesCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicesCategories
        fields = '__all__'
    
class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['category'] = instance.category.name
    #     response['doctors'] = instance.doctors.first_name + ' ' + instance.doctors.last_name

    #     return response

class PatientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patients
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'

class StaffsRolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffsRoles
        fields = '__all__'

class StaffsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staffs
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['role'] = instance.role.name

    #     return response

class VisitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visits
        fields = '__all__'

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['doctor'] = instance.doctor.first_name + ' ' + instance.doctor.last_name
    #     response['patient'] = instance.patient.first_name + ' ' + instance.patient.last_name

    #     return response