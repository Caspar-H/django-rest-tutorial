from django import forms
from django.forms import formset_factory, ModelForm, modelformset_factory

from snippets.models import Bird


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