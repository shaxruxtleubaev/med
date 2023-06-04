from django.urls import path, include
from rest_framework.routers import (
    BaseRouter,
    SimpleRouter,
    DefaultRouter,
)
from .views import (
    SpecializationsViewSet,
    DoctorsViewSet,
    ServicesCategoriesViewSet,
    ServicesViewSet,
    PatientsViewSet,
    UserViewSet,
)

router = DefaultRouter()
router.register("users", UserViewSet, basename='users')
router.register('specializations', SpecializationsViewSet, basename='specializations')
router.register('doctors', DoctorsViewSet, basename='doctors')
router.register('services-categories', ServicesCategoriesViewSet, basename='services-categories')
router.register('services', ServicesViewSet, basename='services')
router.register('patients', PatientsViewSet, basename='patients')

urlpatterns = router.urls