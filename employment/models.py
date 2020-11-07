from django.db import models

# Create your models here.


class Worker(models.Model):
    WORK_CHOICE = (
        ('painters', 'painters'),
        ('carpenter', 'carpenter'),
        ('handloom worker', 'handloom worker'),
        ('labour', 'labour'),
    )
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    adhar = models.CharField(max_length=12, unique=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    dob = models.DateField()
    work = models.CharField(
        max_length=100, default='labour', choices=WORK_CHOICE)
    other = models.CharField(max_length=100, default=None, blank=True)
    is_registered = models.BooleanField(default=None, blank=True)
    is_employed = models.BooleanField(default=None, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"


class Employer(models.Model):
    WORK_CHOICE = (
        ('painters', 'painters'),
        ('carpenter', 'carpenter'),
        ('handloom worker', 'handloom worker'),
        ('labour', 'labour'),
    )
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
        verbose_name_plural = "Employers "
