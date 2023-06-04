from django.contrib.auth import get_user_model
from rest_framework import serializers
from page.models import (
    Specializations,
    Doctors, 
    ServicesCategories,
    Services
)

class SpecializationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specializations
        fields = (
            'id',
            'name',
        )

class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctors
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'contact_number',
            'password',
            'confirm_password',
            'dob',
            'specialization',
            'experience_in_year',
            'gender',
            'profile_picture',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            'status',
            'address1',
            'address2',
            'country',
            'state',
            'city',
            'postal_code',
        )
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['specialization'] = instance.specialization.name

        return response

class ServicesCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicesCategories
        fields = (
            'id',
            'name',
        )
    
class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = (
            'id',
            'name',
            'category',
            'doctors',
            'short_description',
            'icon',
            'status',
        )
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = instance.category.name
        response['doctors'] = instance.doctors.first_name + ' ' + instance.doctors.last_name

        return response

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
        )