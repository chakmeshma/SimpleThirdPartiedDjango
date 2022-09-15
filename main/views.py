from django.shortcuts import render
from .models import Person


# Create your views here.

def index(request):
    person_list = Person.objects.all()
    context = {'person_list': person_list}
    return render(request, 'index.html', context)


def index_filter(request, name_filter):
    person_list = Person.objects.filter(name__contains=name_filter)
    context = {'person_list': person_list}
    return render(request, 'index.html', context)
