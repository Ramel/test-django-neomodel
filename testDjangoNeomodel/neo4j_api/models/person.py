from django.urls import reverse
from django_neomodel import DjangoNode
from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship,
    UniqueIdProperty
)

class Person(DjangoNode):

    #uid = UniqueIdProperty()
    name        = StringProperty()
    #handle_id     = StringProperty(index = True)
    handle_id     = StringProperty()

    movies   = RelationshipTo('.movie.Movie', 'ACTED_IN')

    persons       = Relationship('.person.Person', None)

    class Meta:
        app_label = 'neo4j_api'
