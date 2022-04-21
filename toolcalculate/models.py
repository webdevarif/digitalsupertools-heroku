from email.policy import default
from django.db import models
from accounts.models import *
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.conf import settings

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status_type='public')



# ====================================#
# DOG AGE CALCULATOR ================#
# ====================================#
class DogAgeCalcualtor(models.Model):
    year_num    = models.ForeignKey("DogAgeCalcualtorYear", related_name="year_num", on_delete=models.CASCADE)
    year_size   = models.ForeignKey("DogAgeCalcualtorSize", related_name="year_size", on_delete=models.CASCADE)
    year_result = models.PositiveIntegerField()
    body        = models.TextField(blank=True, null=True)
    created_on  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = models.Manager()  # The default manager.
    PublicObjects = ActiveManager()  # The Dahl-specific manager.

    class Meta:
        verbose_name_plural = "Dog Age Calculator"

    def __str__(self):
        return f"{self.year_num} + {self.year_size} => {self.year_result}"


class DogAgeCalcualtorYear(models.Model):
    year_value  = models.PositiveIntegerField(unique=True)
    year_label  = models.CharField(max_length=50)
    created_on  = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on  = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = models.Manager()  # The default manager.
    PublicObjects = ActiveManager()  # The Dahl-specific manager.

    class Meta:
        verbose_name_plural = "Dog Age Year Number"

    def __str__(self):
        return self.year_label

class DogAgeCalcualtorSize(models.Model):
    size_value  = models.PositiveIntegerField(unique=True)
    size_label  = models.CharField(max_length=50)
    created_on  = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on  = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = models.Manager()  # The default manager.
    PublicObjects = ActiveManager()  # The Dahl-specific manager.

    class Meta:
        verbose_name_plural = "Calculator Dog Size"

    def __str__(self):
        return self.size_label



# ====================================#
# END BOOK CATEGORY ==================#
# ====================================#