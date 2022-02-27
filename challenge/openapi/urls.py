from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Packages", views.PackagesViewSet, basename="Packages")
router.register("Variants", views.VariantsViewSet, basename="Variants")

urlpatterns = [
    # Get Active Packs and has future Dates
    path('Packages/isactive/', views.activePackages),
    # Get Variant with pack id
    path('Variants/packageid/<int:id>', views.getVariant),
    # path('VariantsUpdate/<int:id>',
    #      views.updateVariant.as_view({'post': 'update'})),
    # Update variants title, Description
    path(
        "VariantsUpdate/<int:id>",
        views.updateVariant,
        name="variants",
    ),

    path('', include(router.urls))

]
