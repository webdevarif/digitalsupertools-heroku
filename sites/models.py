from email.policy import default
from django.db import models
from accounts.models import *
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.conf import settings

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status_type='public')

# Create your models here.
def user_directory_path(instance, filename):
    return 'websites/user_{0}/{1}'.format(instance.username, filename)


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
    logo        = models.FileField(upload_to=user_directory_path, blank=True, null=True, verbose_name='logo')
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

# ====================================#
# START BOOK CATEGORY ================#
# ====================================#
class Book(models.Model):
    STATUS_OPTIONS = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    website     = models.ForeignKey(Website, related_name="website", null=True, on_delete=models.CASCADE)
    user        = models.ForeignKey(UserAccount, related_name="book_author", null=True, on_delete=models.SET_NULL)
    title       = models.CharField(max_length=50)
    thumbnail   = models.FileField(upload_to=user_directory_path, blank=True, null=True, verbose_name='book_thumbnail')
    slug        = models.SlugField(max_length=100)
    excerpt     = models.TextField(max_length=150, blank=True, null=True) 
    body        = models.TextField(blank=True, null=True)
    status      = models.CharField(max_length=7, choices=STATUS_OPTIONS, default='public')
    created_on  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = models.Manager()  # The default manager.
    PublicObjects = ActiveManager()  # The Dahl-specific manager.

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class Bookpage(models.Model):
    STATUS_OPTIONS = (
        ('public', 'Public'),
        ('draft', 'Draft'),
    )
    book        = models.ForeignKey(Book, on_delete=models.CASCADE)
    user        = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title       = models.CharField(max_length=50)
    slug        = models.SlugField(max_length=100)
    excerpt     = models.TextField(max_length=150, blank=True, null=True) 
    body        = models.TextField(blank=True, null=True)
    status      = models.CharField(max_length=7, choices=STATUS_OPTIONS, default='draft')
    views       = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_on  = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on  = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = models.Manager()  # The default manager.
    PublicObjects = ActiveManager()  # The Dahl-specific manager.

    class Meta:
        verbose_name_plural = "Book Page"

    def __str__(self):
        return self.title

# ====================================#
# END BOOK CATEGORY ==================#
# ====================================#