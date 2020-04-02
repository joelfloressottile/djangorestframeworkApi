from django.shortcuts import render
from .models import Operator, Weapon, Gadget, Skin
from .serializers import OperatorSerializer, WeaponSerializer, GadgetSerializer, SkinSerializer
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

# Create your views here.


class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class GadgetViewSet(viewsets.ModelViewSet):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer


class SkinViewSet(viewsets.ModelViewSet):
    queryset = Skin.objects.all()
    serializer_class = SkinSerializer


