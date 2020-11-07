from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employer(models.Model):
    WORK_CHOICE = (
        ('painters', 'painters'),
        ('carpenter', 'carpenter'),
        ('handloom worker', 'handloom worker'),
        ('labour', 'labour'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    dateTime = models.DateTimeField(auto_now_add=True)
    requirement_type = models.CharField(
        max_length=100, default='labour', choices=WORK_CHOICE)
    other = models.CharField(max_length=100, default=None, blank=True)
    address = models.TextField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"


class Worker(models.Model):
    WORK_CHOICE = (
        ('painters', 'painters'),
        ('carpenter', 'carpenter'),
        ('handloom worker', 'handloom worker'),
        ('labour', 'labour'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=35)
    slug = models.SlugField()
    adhar = models.CharField(max_length=12, unique=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    dob = models.DateField()
    work = models.CharField(
        max_length=100, default='labour', choices=WORK_CHOICE)
    other = models.CharField(max_length=100, default=None, blank=True)
    is_registered = models.BooleanField(default=None, blank=True)
    is_employed = models.BooleanField(default=None, blank=True)
    works_for = models.ForeignKey(
        Employer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"
