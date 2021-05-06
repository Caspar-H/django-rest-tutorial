from django import forms
from django.forms import formset_factory, ModelForm, modelformset_factory

from snippets.models import *


class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )


BookFormset = formset_factory(BookForm, extra=1)

BirdFormSet = modelformset_factory(
    Bird, fields=("common_name", "scientific_name"), extra=1
)

from django.forms import ModelForm
from .models import Comics, Author


class ComicsForm(ModelForm):
    class Meta:
        model = Comics
        fields = [
            "title",
            "author",
            "price",
            "publish",
        ]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "name"
        ]


class PersonForm(forms.ModelForm):
    model_choices = (
        ('country', 'Country'),
        ('city', 'City'),
        ('dogname', 'DogName')
    )

    test_model_field = forms.ChoiceField(choices=model_choices)
    test_instance_field = forms.ChoiceField(choices=[])
    # test_instance_field = forms.ModelChoiceField(queryset=DogName.objects.all())


    class Meta:
        model = Person
        fields = ('name', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
                self.fields['test_instance_field'].queryset = City.objects.all()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
