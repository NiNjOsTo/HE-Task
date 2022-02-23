from django.urls import path
from . import views


urlpatterns = [
    # Override urls
    path(
        "all/",
        views.PackagesListView.as_view(),
        name="package-variants",
    ),
    ]