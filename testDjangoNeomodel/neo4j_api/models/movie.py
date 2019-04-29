from django_neomodel import DjangoNode
from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship,
    UniqueIdProperty
)


class Movie(DjangoNode):

    uid = UniqueIdProperty()
    name = StringProperty()
    #handle_id = StringProperty(index = True)

    persons = RelationshipFrom('.person.Person', 'ACTED_IN')

    movies = Relationship('.movie.Movie', None)

    class Meta:
        app_label = 'neo4j_api'


