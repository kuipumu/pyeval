"""
Base App Models.
https://docs.djangoproject.com/en/3.2/topics/db/models/
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models import (CASCADE, PROTECT, BooleanField, CharField,
                              DateTimeField, ForeignKey, Model,
                              PositiveIntegerField)


class Role(Model):
    """
    Role model.
    """
    name = CharField(
        # Set name max length.
        max_length=60,
        # Limit role name to be unique.
        unique=True
    )
    level = PositiveIntegerField()

    def __str__(self):
        # Return name has nicely printable representation rol.
        # https://docs.python.org/3/reference/datamodel.html#object.__str__
        return str(self.name)

class User(AbstractUser):
    """
    User model.
    """
    role_id = ForeignKey(
        # Set foreign key model.
        Role,
        # On user deletion PROTECT delete.
        # https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.PROTECT
        on_delete=PROTECT,
        null=True
    )
    status = BooleanField(null=True)

    def __str__(self):
        # Return username has nicely printable representation user.
        # https://docs.python.org/3/reference/datamodel.html#object.__str__
        return str(self.username)

class Log(Model):
    """
    Log model.
    """
    datetime = DateTimeField()
    user_id = ForeignKey(
        # Set foreign key model.
        get_user_model(),
        # On log deletion CASCADE delete.
        # https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.CASCADE
        on_delete=CASCADE
    )
    action = CharField(
        # Set name max length.
        max_length=255
    )

    def __str__(self):
        # Return id has nicely printable representation log.
        # https://docs.python.org/3/reference/datamodel.html#object.__str__
        return str(self.id)
