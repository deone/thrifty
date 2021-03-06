from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Wallet(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(validators=[phone_regex], max_length=15) # validators should be a list
    balance = models.PositiveSmallIntegerField()
    network = models.CharField(max_length=7)

    def __str__(self):
        return self.phone_number

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'balance': self.balance,
            'network': self.network
        }
