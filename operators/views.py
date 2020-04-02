from django.shortcuts import render
from .models import Operator, Weapon, Gadget, Skin
from .serializers import OperatorSerializer, WeaponSerializer, GadgetSerializer, SkinSerializer
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

# Create your views here.


class OperatorViewSet(viewsets.ModelViewSet):
    serializer_class = OperatorSerializer

    def get_queryset(self):
        queryset = Operator.objects.all()
        weapon_id = self.request.query_params.get('weapon_id', None)
        side = self.request.query_params.get('side', None)
        if weapon_id is not None:
            print(' --- IS NOT NONE --- ')
            queryset = queryset.filter(weapons__id=weapon_id)
        if side is not None:
            print(' --- IS NOT NONE --- ')
            queryset = queryset.filter(side=side)
        return queryset


class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class GadgetViewSet(viewsets.ModelViewSet):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer


class SkinViewSet(viewsets.ModelViewSet):
    queryset = Skin.objects.all()
    serializer_class = SkinSerializer


