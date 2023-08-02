from .models import District, Branch, AccountType


def district_branch_accounttype(request):
    district = District.objects.all()
    branch = Branch.objects.all()
    account_type = AccountType.objects.all()
    return dict(district=district, branch=branch, account_type=account_type)
