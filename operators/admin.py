from django.contrib import admin
from .models import Operator, Weapon, Gadget, Skin

# Register your models here.


class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'side', 'country',)


class SkinAdmin(admin.ModelAdmin):
    list_display = ('name', 'operator')


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'operators_that_equip_it')
    # operators is a method from the Weapon class to list display it on the admin site.


class GadgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'operator')

    # As Gadget admin has a unique one to one relation with Operator, then it will only find one Operator related
    # So there's no need to create a function to list display it on the admin site.
    # def get_operator(self, obj):
    # return obj.operator.name
    # get_operator.admin_order_field = 'operator'  # How it will be called from list_display
    # get_operator.short_description = 'Owner Operator'  # How the column in the admin will be named


admin.site.register(Operator, OperatorAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Gadget, GadgetAdmin)
admin.site.register(Skin, SkinAdmin)

