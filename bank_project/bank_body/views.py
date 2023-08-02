from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import AccountForm
from .models import Branch


# Create your views here.


def new(request):
    return render(request, 'new.html')


def fill_form(request):
    if request.method == "POST":                        # if this is a POST request we need to process the form data
        form = AccountForm(request.POST)                # create a form instance and populate it with data from the request:
        print(form)
        if form.is_valid():
            print('correct')          # check whether it's valid:
            form.save(commit=False)
            form.save()
            messages.success(request, 'Application Form Submitted Successfully !!!!')
            return redirect('bank_body:success')

    else:
        form = AccountForm()
        print('incorrect')       # if a GET (or any other method) we'll create a blank form
        print(form.errors)      # displays the errors if any during validation

    form = AccountForm()
    return render(request, "form.html", {"form": form})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id)
    return render(request, "branches_dropdown_list_options.html", {'branches': branches})  # modifying the branches at server side

    #return JsonResponse(list(branches.values('id', 'name')), safe=False)     # modifying the branches at client side (javascript)


def success(request):
    return render(request, 'success.html')












# def districts(request, name=None):
#     district_ = District.objects.get(name=name)
#
#     return render(request, 'form.html', {'district_': district_})
#
#
# def branches(request, district_name=None, name=None):
#     reverse('bank_body:district', args=[district_name])
#     branch_ = Branch.objects.get(name=name, district__name=district_name)
#
#     return render(request, 'form.html', {'branch_': branch_})