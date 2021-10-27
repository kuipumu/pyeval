"""
Base App API Serializers.
https://www.django-rest-framework.org/api-guide/serializers/
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.serializers import (CharField, ModelSerializer,
                                        SerializerMethodField)

from .models import Log, Role


class RoleSerializer(ModelSerializer):
    """
    Role model serializer.
    https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    """
    class Meta:
        """
        Serializer meta.
        """
        # Set serializer model.
        model = Role
        # Set serializer fields.
        fields = [
            'id',
            'name',
            'level'
        ]

class UserSerializer(ModelSerializer):
    """
    User model serializer.
    https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    """
    # Show any role_id associated to user using pk field.
    password = CharField(
        required=True,
        style={
            'input_type': 'password'
        }
    )
    access_token = SerializerMethodField()

    def create(self, validated_data):
        """
        User serializer create method.
        """
        # Create password using submited validated password data.
        validated_data['password'] = make_password(
            validated_data.get('password')
        )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        User serializer update method.
        """
        # Update password using submited validated password data.
        validated_data['password'] = make_password(
            validated_data.get('password')
        )
        return super().update(instance, validated_data)

    def get_access_token(self, obj):
        """
        Define access_token field method.
        """
        # Get token using user id.
        token = Token.objects.filter(user=obj.id)
        # If token exists return token string.
        if token.exists():
            return str(token.first())
        return None

    class Meta:
        """
        Serializer meta.
        """
        # Set serializer model.
        model = get_user_model()
        # Set serializer fields.
        fields = [
            'id',
            'username',
            'password',
            'role_id',
            'access_token',
            'status'
        ]

class LogSerializer(ModelSerializer):
    """
    Role model serializer.
    https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    """

    class Meta:
        """
        Serializer meta.
        """
        # Set serializer model.
        model = Log
        # Set serializer fields.
        fields = [
            'id',
            'datetime',
            'user_id',
            'action'
        ]
