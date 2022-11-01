from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskApi(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes = [IsAuthenticated]
