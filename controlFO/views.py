from django.http import HttpResponse
from django.shortcuts import render
from .models import Fields
from .forms import FieldsForm
from django.views.generic import FormView
# Create your views here.


def index(request):
    fields = Fields.objects.all()
    return render(request, 'index.html', {'fields': fields})


def form(request):
    if request.method == 'POST':
        forms = FieldsForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse('Saved')
    else:
        forms = FieldsForm()
    print (forms)
    return render(request, 'form.html', {'form': forms})
#render(request, 'index.html')