from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from rest_framework.views import APIView

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)

from rest_framework.filters import (SearchFilter, OrderingFilter)

## MODELS ##
from django.contrib.auth.models import User


# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
