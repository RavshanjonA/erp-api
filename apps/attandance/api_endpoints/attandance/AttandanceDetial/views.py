from django.views.generic import DetailView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.attandance.api_endpoints.attandance.AttandanceDetial.serializers import AttandanceDetailSerailizer
from apps.attandance.models import Attandance
from apps.employee.models import Employee


class AttandanceDetail(APIView):
    def get(self,request, pk):
        employee  = get_object_or_404(Employee, pk = pk)
        attandance = Attandance.objects.filter(employee=employee)
        serializer = AttandanceDetailSerailizer(attandance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
