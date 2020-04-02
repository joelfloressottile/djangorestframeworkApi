from django.db import models
from django_countries.fields import CountryField
# Create your models here.


class Operator(models.Model):
    name = models.CharField(max_length=20)
    country = CountryField(blank_label='(select country)')
    SIDES = [
        ('', "choose operator's side"),
        ('ATT', 'Attacker'),
        ('DEF', 'Defender'),
    ]
    side = models.CharField(max_length=3,
                            choices=SIDES,
                            default='',
                            )

    def __str__(self):
        return self.name


class Skin(models.Model):
    name = models.CharField(max_length=20)
    operator = models.ForeignKey(Operator,
                                 default=1,
                                 on_delete=models.SET_DEFAULT,
                                 related_name='skins')


class Gadget(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    operator = models.OneToOneField(Operator,
                                    on_delete=models.SET_DEFAULT,
                                    default=1,
                                    related_name='gadget')

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=20)
    operator = models.ManyToManyField(Operator,
                                      related_name='weapons')

    def operators_that_equip_it(self):
        return ", ".join([o.name for o in self.operator.all()])

    def __str__(self):
        return self.name







