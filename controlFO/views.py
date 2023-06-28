from django.http import HttpResponse
from django.shortcuts import render
from .models import Fields
from .forms import FieldsForm
# Create your views here.


def index(request):
    fields = Fields.objects.all()
    return render(request, 'index.html', {'fields': fields})


def form(request):
    if request.method == 'POST':
        form = FieldsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved')
    else:
        form = FieldsForm()
    print (form)
    return render(request, 'form.html', {'form': form})
#render(request, 'index.html')