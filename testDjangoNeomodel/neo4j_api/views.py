from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Person
from .models import Movie


def get_persons(request):

    #return render('neo4j/persons.html', request, {'persons': Person.nodes.all()})
    #output = '{}'.format(Person.nodes.all())
    output = Person.nodes.all()
    return HttpResponse(output)


def persons(request):
    #return render(request, 'neo4j/persons.html', {'persons': Person.nodes.all()})
    #return render(request, {'persons': HttpResponse(Person.nodes.all())})
    return HttpResponse(Person.nodes.all())


class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ['name']


def movie_list(request, template_name='neo4j_api/movie_list.html'):

    movie = Movie.nodes.all()
    data = {}
    data['object_list'] = movie
    return render(request, template_name, data)


def person_list(request, template_name='neo4j_api/person_list.html'):

    person = Person.nodes.all()
    data = {}
    data['object_list'] = person
    return render(request, template_name, data)


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['name']


def person_update(request, handle_id, template_name='neo4j_api/person_form.html'):
    #person = get_object_or_404(Person, uid=uid)
    person = Person.nodes.get_or_none(handle_id=handle_id)
    if person:
        print("person = ", person)
        #name = person.name
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('neo4j_api:person_list')
    return render(request, template_name, {'form':form})

