from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from snippets.forms import PersonForm
from snippets.models import *

from django.apps import apps


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'dropdown_list/person_list.html'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')
    template_name = 'dropdown_list/person_create.html'


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')
    template_name = 'dropdown_list/person_update.html'


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'dropdown_list/city_dropdown_list_options.html', {'cities': cities})


def load_model_type(request):
    test_model_field_value = request.GET.get('test_model_field_value')
    print(test_model_field_value)
    model_name = apps.get_model('snippets', test_model_field_value)
    print(model_name)
    cities = model_name.objects.all()
    print(cities)
    return render(request, 'dropdown_list/city_dropdown_list_options.html', {'cities': cities})

