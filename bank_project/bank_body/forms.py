from django import forms
from .models import AccountOpeningForm


class DateInput(forms.DateInput):
    input_type = 'date'


class AccountForm(forms.ModelForm):
    # name = forms.CharField(max_length=50)
    # date_of_birth = forms.DateField()
    # age = forms.IntegerField()
    # gender = forms.CharField(max_length=50)
    # phone = forms.IntegerField()
    # mail_id = forms.EmailField(max_length=20)
    # address = forms.CharField(max_length=250, widget=forms.Textarea)
    # district = forms.ModelChoiceField(queryset=District.objects.all())
    # branch = forms.ModelChoiceField(queryset=Branch.objects.all())
    # account_type = forms.ModelChoiceField(queryset=AccountType.objects.all())
    # debit_card = forms.BooleanField(required=False)
    # credit_card = forms.BooleanField(required=False)
    # chequebook = forms.BooleanField(required=False)

    class Meta:
        model = AccountOpeningForm
        fields = ['name', 'date_of_birth', 'age', 'gender', 'phone', 'mail_id', 'address', 'district', 'branch',
                  'account_type', 'debit_card', 'credit_card', 'chequebook']
        widgets = {'date_of_birth': DateInput(), }

