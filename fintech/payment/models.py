from django.db import models

# Create your models here.

class Register(models.Model):
    """docstring forRegister."""

    username = models.CharField(max_length = 7)
    first_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length = 100)
    phoneNo = models.CharField(max_length = 10,default="")
    email = models.CharField(max_length=100,default='1234')
    password = models.CharField(max_length = 1000)

    def __str__(self):
        return f'{self.username},{self.phoneNo},{self.first_name}'
