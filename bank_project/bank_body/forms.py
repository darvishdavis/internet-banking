from django import forms
from .models import AccountOpeningForm, Branch


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass                      # invalid input from the client; ignore and fallback to empty Branch queryset
        # elif self.instance.pk:
        #     self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')

