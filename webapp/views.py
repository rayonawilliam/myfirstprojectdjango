from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Advisor
from . models import bookadvisor
from . models import registeruser
from . serializer import AdvisorSerializer
from . serializer import bookappointment
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import models
from . serializer import userSerializer



# Create your views here.

class Advisorlist(APIView):

    def get(self, request):
        Advisor1=Advisor.objects.all()
        serializer=AdvisorSerializer(Advisor1, many=True)
        return Response(serializer.data)


    def post(self):
        pass


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class=userSerializer

class bookadvisorlist(CreateAPIView):

    def get(self, request):
        bookadvisor1=bookadvisor.objects.all()
        serializer=bookappointment(bookadvisor1, many=True)
        return Response(serializer.data)


    def post(self):
        pass