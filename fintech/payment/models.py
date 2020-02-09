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
    account = models.CharField(max_length=10,default="")

    def __str__(self):
        return f'{self.username},{self.phoneNo},{self.first_name},{self.account},{self.email}'


class PaymentModel(models.Model):
    username = models.CharField(max_length=7)
    amount = models.CharField(max_length=10,default=0)
    message = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=10)
    date = models.CharField(max_length=10,default="")
    time = models.CharField(max_length=10,default="time")

    def __str__(self):
        return f'{self.username},{self.message},{self.category},{self.amount}'



class RemindModel(models.Model):
    username=models.CharField(max_length=100)
    pay=models.CharField(max_length=100)
    amount=models.DecimalField(max_length=100,default=0.0,decimal_places=4,max_digits=8)
    date= models.CharField(max_length=10,default="")
    paid=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username},{self.pay},{self.amount},{self.date}"



class AssosiateModel(models.Model):
    orguser = models.CharField(max_length=7)
    account_no = models.CharField(max_length=10)
    ass_user = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.orguser},{self.account_no},{self.ass_user}"
