from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Account(models.Model):
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
