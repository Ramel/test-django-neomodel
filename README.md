test for Django Neomodel:

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
python manage.py install_labels
python manage.py runserver
```

