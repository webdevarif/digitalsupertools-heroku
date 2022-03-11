from django.db import models
from accounts.models import *

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status_type='public')


class Website(models.Model):
    STATUS_OPTIONS = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    user        = models.ForeignKey(UserAccount, related_name="Author", null=True, on_delete=models.SET_NULL)
    title       = models.CharField(max_length=50)
    slug        = models.SlugField(max_length=100)
    excerpt     = models.TextField(max_length=150, blank=True, null=True) 
    body        = models.JSONField(blank=True)
    status      = models.CharField(max_length=7, choices=STATUS_OPTIONS, default='public')
    views       = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_on  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = models.Manager()  # The default manager.
    PublicObjects = ActiveManager()  # The Dahl-specific manager.

    class Meta:
        verbose_name_plural = "Website"

    def __str__(self):
        return self.title