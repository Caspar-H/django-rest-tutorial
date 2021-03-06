from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from snippets.forms import ComicsForm, AuthorForm
from snippets.models import Comics, Author
from django.views.decorators.csrf import csrf_exempt
import json


def ComicsCreate(request):
    form = ComicsForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect("/")
    return render(request, "formset/comics_form.html", {"form": form, })


def AuthorCreatePopup(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        instance = form.save()

        ## Change the value of the "#id_author". This is the element id in the form

        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_author");</script>' % (instance.pk, instance))

    return render(request, "formset/author_form.html", {"form": form})


def AuthorEditPopup(request, pk=None):
    instance = get_object_or_404(Author, pk=pk)
    form = AuthorForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save()

        ## Change the value of the "#id_author". This is the element id in the form

        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_author");</script>' % (instance.pk, instance))

    return render(request, "formset/author_form.html", {"form": form})


@csrf_exempt
def get_author_id(request):
    if request.is_ajax():
        author_name = request.GET['author_name']
        author_id = Author.objects.get(name=author_name).id
        data = {'author_id': author_id, }
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse("/")
