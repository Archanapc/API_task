from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import homeSerializer
from form.models import FormPage

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = FormPage.objects.all()
    serializer_class = homeSerializer

    def perform_create(self, serializer):
        serializer.save()