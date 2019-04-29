test for Django Neomodel issue:

https://github.com/neo4j-contrib/neomodel/issues/444

Requirements:
=============

Python 3.6

Run locally
===========

Start your local Neo4j Server (Download & Install), open the Neo4j Browser. Then install the Movies data-set with `:play movies`.

Create a Virtual Environment:

```pew new test-django-neomodel```

Install requirements:

```pip install -r requirements```

Then:

```
export NEO4J_BOLT_URL=bolt://neo4j:password@localhost:7687

cd testDjangoNeomodel

python manage.py install_labels
python manage.py runserver
```

You should be able to go to [here](http://127.0.0.1:8000/neo4j_api/person_list.html)
