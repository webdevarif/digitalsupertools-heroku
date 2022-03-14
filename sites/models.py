from email.policy import default
from django.db import models
from accounts.models import *
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.conf import settings

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status_type='public')

class Website(models.Model):
    STATUS_OPTIONS = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    CATEGORIES_OPTIONS = (
        ('uncategory', 'Uncategory'),
        ('portfolio', 'Portfolio'),
        ('blogging', 'Blogging'),
        ('book', 'Book'),
    )
    user        = models.ForeignKey(UserAccount, related_name="Author", null=True, on_delete=models.SET_NULL)
    title       = models.CharField(max_length=50)
    slug        = models.SlugField(max_length=100)
    excerpt     = models.TextField(max_length=150, blank=True, null=True) 
    category    = models.CharField(max_length=15, choices=CATEGORIES_OPTIONS, default='uncategory')
    body        = models.JSONField(blank=True, null=True)
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
