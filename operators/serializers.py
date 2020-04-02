from rest_framework import serializers
from .models import Operator, Weapon, Gadget, Skin


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id', 'name']


class GadgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gadget
        fields = ['id', 'name', 'description']


class SkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skin
        fields = ['id', 'name']


class OperatorSerializer(serializers.ModelSerializer):
    skins = SkinSerializer(many=True, read_only=True)
    weapons = WeaponSerializer(many=True, read_only=True)
    gadget = GadgetSerializer(read_only=True)

    class Meta:
        model = Operator
        fields = ['id', 'name', 'side', 'country', 'skins', 'weapons', 'gadget']


class OperatorWeapon(serializers.ModelSerializer):

    class Meta:
        model = Operator
        fields = ['operators_weapon']