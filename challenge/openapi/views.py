from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from packages.models import Package, Variant
from rest_framework import status
from packages.serializer import PackagesSerializer, VariantsSerializer, VariantsUpdateSerializer

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


# Create Pagination class how many post
class PackagesPagination(PageNumberPagination):
    page_size = 5


class VariantsPagination(PageNumberPagination):
    page_size = 5


class PackagesViewSet(viewsets.ModelViewSet):
    pagination_class = PackagesPagination
    serializer_class = PackagesSerializer
    queryset = Package.objects.all()


class VariantsViewSet(viewsets.ModelViewSet):
    pagination_class = VariantsPagination
    serializer_class = VariantsSerializer
    queryset = Variant.objects.all()

# Get Variant with Pack id


@api_view(['GET', 'PUT'])
def updateVariant(request, id=None):
    try:
        pkgs = Variant.objects.filter(id=id,).all()
        serializer = VariantsUpdateSerializer(pkgs, many=True)
    except Exception as e:
        print("Updating Variant Fetching item Error", e)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

# Get Variant with Pack id


@api_view(['GET'])
def getVariant(request, id=None):
    try:
        pkgs = Variant.objects.filter(package=id,).all()
        serializer = VariantsSerializer(pkgs, many=True)
    except Exception as e:
        print("Fetching Variant with Specific packid Error", e)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

# Fetching Active Packages


@api_view(['GET'])
def activePackages(request):
    try:
        pkgs = Package.objects.filter(is_active=True).all()
        serializer = PackagesSerializer(pkgs, many=True)
    except Exception as e:
        print("Error in Fetching Active Packages", e)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
