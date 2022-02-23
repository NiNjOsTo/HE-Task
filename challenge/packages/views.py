from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PackagesSerializer
from .models import Package
from rest_framework import status
# Create your views here.
class PackagesListView(APIView):
    def get(self, request):
        pkgs=Package.objects.all()
        serializer=PackagesSerializer(pkgs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
   