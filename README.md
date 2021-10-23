# Python Evaluation

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

This is a Django API evaluation project, this API allows you to list, create and edit users, roles and logs from a Django Rest Framework backend storing data on a PostgreSQL database. It uses django-plaintext-password to store user passwords in plain format, django-eviron to set project settings using enviromental variables, django_filters to filter objects retrived from API, and Django Rest Framework auth_token to generate access token to users.

## Instalation

Clone this repository and get into the project folder:

```bash
git clone https://github.com/kuipumu/pyeval
cd pyeval
```

Create a python virtualenv and install dependencies:

```bash
virtualenv venv
pip install -r requirements.txt  
```

You will need set the appropiate settings in the file project/settings.py, set the correct host, user and database to match your PostgreSQL, SQLite or MySQL database:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}
```

Migrate models to database, load sample fixture data and run Django development server:

```bash
./manage.py migrate
./manage.py loaddata sample  
./manage.py runserver
```

Go to the server address and start using the API.

## API Usage

- API root: http://127.0.0.1:8000/api/
- User Login: http://127.0.0.1:8000/api/login/
- GET users:  http://127.0.0.1:8000/api/users/
- GET roles:  http://127.0.0.1:8000/api/roles/
- GET logs:  http://127.0.0.1:8000/api/users/

You can also import the file postman_collection.json into Postman to get more information about all of the API endpoints and methods.

## Authors

- [@kuipumu](https://www.github.com/kuipumu)

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
