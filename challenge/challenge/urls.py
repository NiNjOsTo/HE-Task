from django import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from openapi.views import PackagesViewSet, VariantsViewSet


router = DefaultRouter()
router.register("Packages", PackagesViewSet, basename="Packages")
router.register("Variants", VariantsViewSet, basename="Variants")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui',),
    path('openapi/', include('openapi.urls')),
    path("packages/", include('packages.urls')),

    path('', include(router.urls))

]
