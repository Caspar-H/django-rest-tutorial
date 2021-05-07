from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from snippets.forms import BookFormset, BirdFormSet
from snippets.models import Book, Bird


def create_book_normal(request):
    template_name = 'formset/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            # once all books are saved, redirect to book list view
            return redirect('book_list')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


class BookList(ListView):
    model = Book
    template_name = 'formset/book_list.html'
    context_object_name = 'book_list'


class BirdListView(ListView):
    model = Bird
    template_name = "formset/bird_list.html"


class BirdAddView(TemplateView):
    template_name = "formset/add_bird.html"

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        formset = BirdFormSet(queryset=Bird.objects.none())
        return self.render_to_response({'form_formset': formset})

    def post(self, *args, **kwargs):
        formset = BirdFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("snippets:bird_list"))

        return self.render_to_response({'form_formset': formset})
