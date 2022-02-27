from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import VariantsSerializer
from .models import Variant
# Create your views here.


# class PackagesListView(APIView):
#     def get(self, request):
#         pkgs = Package.objects.all()
#         serializer = PackagesSerializer(pkgs, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


# class VariantsListView(APIView):
#     def get(self, request):
#         pkgs = Variant.objects.all()
#         serializer = VariantsSerializer(pkgs, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


# class VariantDetailView(APIView):
#     def retrieve(self, pk):
#         queryset = Variant.objects.all()
#         variant = get_object_or_404(queryset, pk=pk)
#         serializer = VariantsSerializer(variant)
#         return Response(serializer.data)
#     def get(request, primary_key):
#         try:
#             variant = Variant.objects.get(pk=primary_key)
#         except Variant.DoesNotExist:
#             raise Http404('Variant does not exist')

# def get(self, request, Package=None):
#     if Package:
#         item = Variant.objects.get(Package=Package)
#         serializer = Variant(item)
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
