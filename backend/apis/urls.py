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
    StaffsRolesViewSet,
    StaffsViewSet,
    VisitsViewSet
)

router = DefaultRouter()
router.register("users", UserViewSet, basename='users')
router.register('specializations', SpecializationsViewSet, basename='specializations')
router.register('doctors', DoctorsViewSet, basename='doctors')
router.register('services-categories', ServicesCategoriesViewSet, basename='services-categories')
router.register('services', ServicesViewSet, basename='services')
router.register('patients', PatientsViewSet, basename='patients')
router.register('staffs-roles', StaffsRolesViewSet, basename='staffs-roles')
router.register('staffs', StaffsViewSet, basename='staffs')
router.register('visits', VisitsViewSet, basename='visits')

urlpatterns = router.urls