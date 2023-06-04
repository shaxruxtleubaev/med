from rest_framework.routers import SimpleRouter
from .views import (
    SpecializationsViewSet,
    DoctorsViewSet,
    ServicesCategoriesViewSet,
    ServicesViewSet,
    UserViewSet,
)

router = SimpleRouter()
router.register("users", UserViewSet, basename='users')
router.register('specializations', SpecializationsViewSet, basename='specializations')
router.register('doctors', DoctorsViewSet, basename='doctors')
router.register('services-categories', ServicesCategoriesViewSet, basename='services-categories')
router.register('services', ServicesViewSet, basename='services')

urlpatterns = router.urls