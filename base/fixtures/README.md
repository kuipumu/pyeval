## App Fixtures Folder

Add any initial or sample fixture data to load to this app model.

A fixture is a collection of data that Django knows how to import into a database. The most straightforward way of creating a fixture if you’ve already got some data is to use the manage.py dumpdata command. Or, you can write fixtures by hand; fixtures can be written as JSON, XML documents.

As an example, though, here’s what a fixture for a User model might look like in JSON:

```json

[
  {
    "model": "base.user",
    "pk": 2,
    "fields": {
      "username": "mary",
      "password": "123abcqq##",
      "role_id": 2,
      "status": true
    }
  },
  {
    "model": "base.user",
    "pk": 3,
    "fields": {
      "username": "louis",
      "password": "123abcqq##",
      "role_id": 2,
      "status": false
    }
  }
]

```

Reference: [Django 3.2 - Providing initial data for models](https://docs.djangoproject.com/en/3.2/howto/initial-data/)
