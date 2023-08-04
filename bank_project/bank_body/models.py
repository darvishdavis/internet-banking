from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ["name"]

    def get_url(self):
        return reverse('bank_body:district', args=[self.name])


class Branch(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ["name"]

    def get_url(self):
        return reverse('bank_body:branch', args=[self.district.name, self.name])


class AccountType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ["name"]


materials = (('debitcard', 'Debit card'), ('creditcard', 'Credit card'), ('chequebook', 'Cheque book'),)


class AccountOpeningForm(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phone = models.IntegerField()
    mail_id = models.EmailField(max_length=20)
    address = models.TextField(max_length=250)
    district = models.ForeignKey(District, models.CASCADE)
    branch = models.ForeignKey(Branch, models.CASCADE)
    account_type = models.ForeignKey(AccountType, models.CASCADE)
    materials_required = MultiSelectField(choices=materials, min_choices=1, max_choices=3, max_length=20, default='empty')


    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ["name"]



