from django.urls import path

from neo4j_api import views


app_name = 'neo4j_api'


urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('movie_list.html', views.movie_list, name='movie_list'),
    path('person_list.html', views.person_list, name='person_list'),
    path('persons.html', views.persons),
    path('person_edit/<uid>', views.person_update, name='person_edit'),
]
