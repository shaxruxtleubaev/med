from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [

    # Main pages
    path('admin/', admin.site.urls),
    path('adminn/', include('page.urls')),

    # API
    path('api/v1/', include('apis.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc',),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui',)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)