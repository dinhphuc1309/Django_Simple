from django.http import HttpResponse
from rest_framework.response import Response

from django.shortcuts import render

from rest_framework import generics

def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")

class LoginView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'login/index.html')

    def post(self, request, *args, **kwargs):
        pass
