from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.District)


class BranchAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(models.Branch, BranchAdmin)

admin.site.register(models.AccountType)


class AccountOpeningFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'phone', 'district', 'branch', 'account_type']
    list_editable = ['age', 'district', 'branch', 'account_type']
    list_per_page = 10


admin.site.register(models.AccountOpeningForm, AccountOpeningFormAdmin)